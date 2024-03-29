#!/usr/bin/python
# coding:utf-8
from basepackage.baselog import globalLog
import os
import sys
import atexit
import time
from signal import SIGTERM

# set root directory
package_path = os.getcwd() + '/../'
sys.path.append(package_path)


class Daemon(object):
    """
    A generic daemon class.

    Usage: subclass the Daemon class and override the run() method
    """

    def __init__(self, pidfile, stdin='/dev/null',
                 stdout='/dev/null', stderr='/dev/null'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def daemonize(self):
        """
        do the UNIX double-fork magic, see Stevens' "Advanced
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        """
        # do first fork
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            globalLog.getError().log(
                globalLog.ERROR, "fork #1 failed: %d (%s)\n" %
                (e.errno, e.strerror))
            sys.exit(1)

        # decouple from parent environment
        os.chdir("/")
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            globalLog.getError().log(
                globalLog.ERROR, "fork #2 failed: %d (%s)\n" %
                (e.errno, e.strerror))
            sys.exit(1)

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = file(self.stdin, 'r')
        so = file(self.stdout, 'a+')
        se = file(self.stderr, 'a+', 0)
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        # registrem destructor function
        atexit.register(self.delpid)
        # write pidfile
        try:
            fd = open(self.pidfile, 'w+')
            fd.write('%s\n' % (str(os.getpid())))
            fd.close()
        except IOError as msg:
            globalLog.getError().log(globalLog.ERROR, "%s:open pidfile failed." % msg)
            sys.exit(1)

    def delpid(self):
        '''destructor function'''
        os.remove(self.pidfile)

    def start(self):
        """
        Start the daemon
        """
        # Check for a pidfile to see if the daemon already runs
        try:
            pf = file(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        # existed daemon process, quit
        if pid:
            message = "pidfile %s already exist. Daemon already running?\n"
            globalLog.getError().log(globalLog.ERROR, message % self.pidfile)
            sys.exit(1)

        # Start the daemon
        self.daemonize()
        # run
        self.run()

    def stop(self):
        """
        Stop the daemon
        """
        # Get the pid from the pidfile
        try:
            pf = file(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None

        if not pid:
            message = "pidfile %s does not exist. Daemon not running?\n"
            globalLog.getError().log(globalLog.ERROR, message % self.pidfile)
            return  # not an error in a restart

        # Try killing the daemon process
        try:
            while True:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                globalLog.getError().log(globalLog.ERROR, 'Daemon stop:%s' % err)
                sys.exit(1)

    def restart(self):
        """
        Restart the daemon
        """
        self.stop()
        self.start()

    def run(self):
        """
        You should override this method when you subclass Daemon.
        It will be called after the process has been
        daemonized by start() or restart().
        """
        pass
