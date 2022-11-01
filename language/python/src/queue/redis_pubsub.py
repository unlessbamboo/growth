""" 测试redis的发布和订阅模式 """
import sys
import getopt
import time
import redis


def usage():
    """usage"""
    usage_doc = """消息的发布和订阅
    Usage:
        python redis_pubsub.py -option -m [MODULES] -s M -d N

    Options:
        -h or --help
        --action
            动作, sub-订阅, pub-发布

    For more info visit http://www.unlessbamboo.top/"""
    print(usage_doc)


def get_cli_options(argv):
    """get_cli_options:get command options

    :param argv:
    """
    short_opt = ""
    long_opt = ["action="]
    try:
        opts, args = getopt.getopt(argv[1:], short_opt, long_opt)
    except getopt.GetoptError as msg:
        print("Occur error, msg:{0}".format(msg))
        usage()
        sys.exit(1)
    if not opts:
        usage()
        sys.exit(1)
    return opts[0][1]


class RedisHelper:
    """
    RedisHelper
    """
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1', port=6379)
        self.chan_sub = 'channel1'
        self.chan_pub = 'channel1'

    def publish(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_pub)
        pub.parse_response()
        return pub


def sub_channel():
    obj = RedisHelper()
    redis_sub = obj.subscribe()
    print('-开始订阅并等待消息-')
    while True:
        msg = redis_sub.parse_response()
        if not msg:
            continue
        print(msg[2].decode('utf8'))


def pub_msg():
    """ 将当前时间戳作为消息发布出去 """
    obj = RedisHelper()
    curtime = time.ctime()
    obj.publish(f'hello, {curtime}')


if __name__ == '__main__':
    """ 测试命令
    1. 启动订阅(阻塞等待): python redis_pubsub.py --action=sub
    2. 推送消息: python redis_pubsub.py --action=pub
    """
    action = get_cli_options(sys.argv)
    if action == 'sub':
        sub_channel()
    else:
        pub_msg()
