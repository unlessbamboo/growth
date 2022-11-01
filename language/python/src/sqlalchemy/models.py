""" 表定义 """
from sqlalchemy import (
    Table, Column, Integer, Numeric, String, ForeignKey, MetaData)


metadata = MetaData()
# 1. Core方式定义表
cookies = Table(
    'cookies', metadata,
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unit_cost', Numeric(12, 2)),
)
