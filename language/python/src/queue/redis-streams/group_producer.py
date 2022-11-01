""" 消费者组 """
from os import environ
from uuid import uuid4
from time import sleep
from redis import Redis


GROUP_NAME = 'bambooGroup'
STREAM_KEY = 'STREAM-TEST-BAMBOO'  # stream消息队列名
MAX_MESSAGES = int(environ.get("MESSAGES", "100"))


def connect_to_redis():
    """ 创建redis连接实例 """
    hostname = environ.get("REDIS_HOSTNAME", "localhost")
    port = environ.get("REDIS_PORT", 6379)

    r = Redis(hostname, port, retry_on_timeout=True)
    return r


def create_xgroup(rds, stream, group_name):
    """ 创建消费者组: xgroup create ${STREAM_KEY} bambooGroup 0 """
    try:
        rsp = rds.xinfo_groups(stream)
        for item in rsp:
            if group_name == item['name'].decode('utf8'):
                print(f'xgroup:{group_name}已存在, 无需再次创建')
                return
    except Exception as msg:
        pass

    group = rds.xgroup_create(stream, group_name, '0-0', mkstream=True)
    if not group:
        raise Exception(f'创建消费者组:{group_name}异常')
    return group


def send_data(rds, stream_key):
    count = 0
    while count < MAX_MESSAGES:
        try:
            data = {
                "producer": 'xgroup',
                "some_id": uuid4().hex,  # Just some random data
                "count": count,
            }
            resp = rds.xadd(stream_key, data)
            print(f'推送消息:{resp}')
            count += 1

        except ConnectionError as e:
            print("ERROR REDIS CONNECTION: {}".format(e))
        sleep(0.5)


if __name__ == "__main__":
    connection = connect_to_redis()
    create_xgroup(connection, STREAM_KEY, GROUP_NAME)
    send_data(connection, STREAM_KEY)
