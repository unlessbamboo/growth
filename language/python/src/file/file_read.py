#!/usr/bin/python
# coding:utf-8
import os
import sys
import time
import traceback
import logging


info_logger = logging.getLogger('info')


def catch_exception(func, *args, **kw):
    def func(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception as msg:
            traceList = traceback.extract_tb(sys.exc_info()[2])
            for (file, lineno, funcname, text) in traceList:
                info_logger.error("Occur error, func:%s,lineno:%s, msg:%s" % (funcname, lineno, msg))
            return None
    return func


@catch_exception
def find_unexist(filename):
    """
    Read file from fd, and file was remove at any one time.
    """
    fd = open(filename, "r")
    fino = os.stat(filename).st_ino
    while True:
        try:
            tempio = os.stat(filename).st_ino
            if fino != tempio:
                fd.close()
                fd = open(filename, 'r')
            print fd.readline()
            time.sleep(5)
        except (IOError, OSError) as msg:
            print 'IOerror, msg:%s' % msg
            time.sleep(2)


def read_file_with_iter(filename):
    """
    Iteration a file
    """
    with open(filename, 'r') as f:
        for line in f:
            print line


if __name__ == '__main__':
    """main"""
    # find_unexist('./test.log')
    read_file_with_iter('./boot.log')
