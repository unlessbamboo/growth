"""
功能: 极验-滑块验证码

"""
import time
import random
import base64
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image


def get_chrome_browser(proxy_url=None, ua=None, headless=True, timeout=None):
    """ Get Chrome Browser """
    chrome_options = webdriver.ChromeOptions()

    if proxy_url:  # 添加代理
        chrome_options.add_argument('--proxy-server={}'.format(proxy_url))

    if headless:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('user-agent=Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/62.0.3202.94Safari/537.36'),
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.set_page_load_timeout(120 if not timeout else timeout)
    return browser


class Geetest(object):
    def __init__(self):
        self.target_url = 'https://www.geetest.com/demo/slide-bind.html'  # 极验daemon网站
        self.browser = get_chrome_browser(headless=False)

    def visit_index(self):
        """ 访问登录页 """
        self.browser.get(self.target_url)
        # 等待用户名输入框加载完成
        element = WebDriverWait(self.browser, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'username')))
        element.clear()
        element.send_keys('bifeng')
        # 等待密码输入框加载完成
        element = WebDriverWait(self.browser, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'password')))
        element.clear()
        element.send_keys('password123')
        # 等待提交按钮加载完成
        element = WebDriverWait(self.browser, 10, 0.5).until(
            EC.presence_of_element_located((By.ID, 'btn')))
        element.click()
        # 等待滑动验证码出现
        WebDriverWait(self.browser, 10, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_fullbg')))
        return True

    def analog_drag(self):
        # 1. 将已经生成好的画布上的照片保存到本地
        self.save_canvas_img('full.jpg', 'geetest_canvas_fullbg geetest_absolute')  # 原图
        self.save_canvas_img('cut.jpg', 'geetest_canvas_bg geetest_absolute')  # 缺口背景图
        full_image = Image.open('full.jpg')
        cut_image = Image.open('cut.jpg')
        distance = self.get_offset_distance(cut_image, full_image)
        self.start_move(distance)
        import pdb
        pdb.set_trace()
        print('xxxxxxxxxxxxxxxxxxxxxxx')

    def save_canvas_img(self, filename, classname):
        """ 保存画布到本地 """
        js = 'return document.getElementsByClassName("{}")[0].toDataURL("image/png")'.format(classname)
        img = self.browser.execute_script(js)
        base64_data_img = img[img.find(',') + 1:]
        with open(filename, 'wb') as fd:
            fd.write(base64.b64decode(base64_data_img))
        return True

    def get_offset_distance(self, cut_image, full_image):
        """ 根据两个照片计算距离 """
        for x in range(cut_image.width):
            for y in range(cut_image.height):
                cpx = cut_image.getpixel((x, y))  # 得到某个像素点的颜色
                fpx = full_image.getpixel((x, y))
                if not self.is_similar_color(cpx, fpx):  # 如果颜色不想近, 表示这是一个缺口
                    # 保存一下计算出来位置图片，看看是不是缺口部分
                    img = cut_image.crop((x, y, x + 50, y + 50))  # 从图像中提取某个矩形大小的图像
                    img.save("slice.png")
                    return x  # 切片图片和缺口的 Y 坐标肯定相同

    def is_similar_color(self, x_pixel, y_pixel):
        """ 判断颜色是否相近 """
        for i, pixel in enumerate(x_pixel):
            if abs(y_pixel[i] - pixel) > 50:
                return False
        return True

    def start_move(self, distance):
        """ 移动切片 """
        # 获取拖动按钮
        element = self.browser.find_element_by_xpath('//div[@class="geetest_slider_button"]')
        # 种类需要进行微调可能计算出来的位置不准确
        distance -= element.size.get('width') / 2
        distance += 25
        # 按下鼠标左键开始移动(点击鼠标左键, 不松开)
        # 可以使用MouseController工具来记录人工的鼠标操作轨迹
        ActionChains(self.browser).click_and_hold(element).perform()
        time.sleep(0.5)
        while distance > 0:
            if distance > 10:
                # 如果距离大于10，就让他移动快一点
                span = random.randint(5, 8)
            else:
                # 快到缺口了，就移动慢一点
                span = random.randint(2, 3)
            ActionChains(self.browser).move_by_offset(span, 0).perform()  # 从当前位置移动到某个坐标(x, y)
            distance -= span
            time.sleep(random.randint(10, 50) / 100)
        ActionChains(self.browser).move_by_offset(distance, 1).perform()
        ActionChains(self.browser).release(on_element=element).perform()  # 释放鼠标左键

    def login(self):
        try:
            # 1. 获取页面并点击登录
            self.visit_index()
            # 2. 获取极验图片并进行模拟拖动
            self.analog_drag()
        finally:
            self.browser.close()


gettest_obj = Geetest()
gettest_obj.login()
