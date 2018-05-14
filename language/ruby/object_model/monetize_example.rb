# encoding:utf-8
require "monetize"


bargain_price = Monetize.from_numeric(99, "USD")
print bargain_price.format
