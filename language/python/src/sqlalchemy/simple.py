""" sqlalchemy core 简单测试 """
from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bamboo:bamboodba@127.0.0.1/sqlalchemy?charset=utf8'
DB_POOL = None


def db_pool():
    return create_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=3600)


def get_conn():
    global DB_POOL
    if not DB_POOL:
        DB_POOL = db_pool()
    return DB_POOL.connect()

    
if __name__ == '__main__':
    pass