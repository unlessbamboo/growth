# coding:utf8
"""
测试隐士等待的作用: 等待某一个查找结果的出现, 即某一个元素的加载完成, 如果超时则报错
@Note: 最后一次隐士设置才是最终配置
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')
try:
    print(ctime())
    driver.implicitly_wait(5)
    # 如果为找到该ID, 会睡眠5秒钟, 替换之前的10秒配置
    driver.find_element_by_id('kxgx').send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()
