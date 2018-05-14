# coding:utf8
import os
import sys
from logging.config import DictConfigurator


# 将当前路径放入PATHONPATH中, 以便能够导入clogtimehandler
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)


class ConcurrentDictConfigurator(DictConfigurator):
    def resolve(self, s):
        """
        Resolve strings to objects using standard import and attribute
        syntax.
        """
        name = s.split('.')
        used = name.pop(0)
        try:
            found = self.importer(used)
            for frag in name:
                used += '.' + frag
                try:
                    found = getattr(found, frag)
                except AttributeError:
                    self.importer(used)
                    found = getattr(found, frag)
            return found
        except ImportError:
            e, tb = sys.exc_info()[1:]
            v = ValueError('Cannot resolve %r: %s' % (s, e))
            v.__cause__, v.__traceback__ = e, tb
            raise v


clogDictConfigClass = ConcurrentDictConfigurator


def clogDictConfig(config):
    """Configure logging using a dictionary."""
    clogDictConfigClass(config).configure()
