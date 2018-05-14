# coding:utf8
"""
1 更改TimedRotatingFileHandler, 使其支持多进程日志写入操作
2 其他功能完全同TimeRotatingFileHandler, 支持按秒/分/时进行切割操作
3 多进程仿照ConcurrentRotatingFileHandler功能
"""
import time
import os
import sys
from random import randint
from logging import Handler, LogRecord
from logging.handlers import TimedRotatingFileHandler
from portalocker import lock, unlock, LOCK_EX

try:
    import codecs
except ImportError:
    codecs = None


__all__ = ["ConcurrentTimeRotatingFileHandler", ]


class NullLogRecord(LogRecord):
    def __init__(self):
        pass

    def __getattr__(self, attr):
        return None


class ConcurrentTimeRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, when='h', interval=1, backupCount=0,
                 encoding=None, delay=False, utc=False):
        super(ConcurrentTimeRotatingFileHandler, self).__init__(
            filename, when, interval, backupCount, encoding, delay, utc)
        self._open_lockfile()
        self._rotateFailed = False

    def _open_lockfile(self):
        # Use 'file.lock' and not 'file.log.lock' (Only handles the normal
        # "*.log" case.)
        if self.baseFilename.endswith(".log"):
            lock_file = self.baseFilename[:-4]
        else:
            lock_file = self.baseFilename
        lock_file += ".lock"
        self.stream_lock = open(lock_file, "w")

    def _open(self, mode=None):
        if mode is None:
            mode = self.mode
        if self.encoding is None:
            stream = open(self.baseFilename, mode)
        else:
            stream = codecs.open(self.baseFilename, mode, self.encoding)
        return stream

    def _close(self):
        if self.stream:
            try:
                if not self.stream.closed:
                    self.stream.flush()
                    self.stream.close()
            finally:
                self.stream = None

    def acquire(self):
        """ Acquire thread and file locks.  Re-opening log for 'degraded' mode.
        """
        Handler.acquire(self)
        if self.stream_lock:
            if self.stream_lock.closed:
                try:
                    self._open_lockfile()
                except Exception:
                    self.handleError(NullLogRecord())
                    self.stream_lock = None
                    return
            lock(self.stream_lock, LOCK_EX)

    def release(self):
        """ Release file and thread locks. If in 'degraded' mode, close the
        stream to reduce contention until the log files can be rotated. """
        try:
            if self._rotateFailed:
                self._close()
        except Exception:
            self.handleError(NullLogRecord())
        finally:
            try:
                if self.stream_lock and not self.stream_lock.closed:
                    unlock(self.stream_lock)
            except Exception:
                self.handleError(NullLogRecord())
            finally:
                Handler.release(self)

    def close(self):
        """
        Close log stream and stream_lock. """
        try:
            self._close()
            if not self.stream_lock.closed:
                self.stream_lock.close()
        finally:
            self.stream_lock = None
            Handler.close(self)

    def _degrade(self, degrade, msg, *args):
        """ Set degrade mode or not.  Ignore msg. """
        self._rotateFailed = degrade
        del msg, args   # avoid pychecker warnings

    def _time_tuple(self, dstNow):
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
            dstThen = timeTuple[-1]
            if dstNow != dstThen:
                if dstNow:
                    addend = 3600
                else:
                    addend = -3600
                timeTuple = time.localtime(t + addend)
        return timeTuple

    def _rollover_at(self, dstNow, currentTime):
        """Get new rollover at"""
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    addend = -3600
                else:           # DST bows out before next rollover, so we need to add an hour
                    addend = 3600
                newRolloverAt += addend
        self.rolloverAt = newRolloverAt

    def doRollover(self):
        """
        Do a rollover
        """
        # 1 Close stream
        self._close()
        try:
            # 2 Clear backup fileanme
            current_time = int(time.time())
            dst_now = time.localtime(current_time)[-1]
            time_tuple = self._time_tuple(dst_now)
            dfn = self.baseFilename + "." + \
                time.strftime(self.suffix, time_tuple)
            if os.path.exists(dfn):
                os.remove(dfn)
            # 3 Rename logfile to tempname
            tmpname = None
            while not tmpname or os.path.exists(tmpname):
                tmpname = "%s.rotate.%08d" % (
                    self.baseFilename, randint(0, 99999999))
            try:
                os.rename(self.baseFilename, tmpname)
            except (IOError, OSError):
                exc_value = sys.exc_info()[1]
                self._degrade(
                    True,
                    "rename failed.  File in use?  exception=%s",
                    exc_value)
                return
            # 4 Delete extract backup filename
            if self.backupCount > 0:
                for s in self.getFilesToDelete():
                    os.remove(s)
            # 5 Rename temp to backup log filename
            os.rename(tmpname, dfn)
            self._degrade(False, "Rotation completed")
        finally:
            # 6 Open new stream
            if not self.delay:
                self.stream = self._open()
            self._rollover_at(dst_now, current_time)

    def shouldRollover(self, record):
        """Deletemine if rollover should occur"""
        del record
        if self.stream is None:
            return False
        if self._shouldRollover():
            # 避免多个进程同时执行rollover操作, 先关闭从而阻止后续进程进行rollover操作
            self._close()
            self.stream = self._open()
            return self._shouldRollover()
        return False

    def _shouldRollover(self):
        t = int(time.time())
        if t >= self.rolloverAt:
            return True
        self._degrade(False, "Rotation done or not needed at this time")
        return False
