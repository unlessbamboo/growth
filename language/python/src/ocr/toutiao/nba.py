"""
利用selenium爬取今日头条(ajax异步加载)
"""
import time
import pymongo
from selenium import webdriver
from bs4 import BeautifulSoup as BS


class Toutiao(object):
    def __init__(self):
        self.db_client = None
        self.db_conn = None
        self.browser = None

    def get_chrome(self):
        chrome_options = webdriver.ChromeOptions()  # 创建ChromeOptions对象
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36')
        #  chrome_options.add_argument('--headless')  # 添加headless参数, 无界面模式

        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def close_chrome(self):
        try:
            if self.browser:
                self.browser.close()
        except Exception:
            pass

    def get_article_links(self):
        """
        拿到每篇文章的链接
        :return:
        """
        self.browser.get('https://www.toutiao.com/ch/nba/')
        # 设置隐式等待，最多等待10s
        self.browser.implicitly_wait(5)
        # 模拟鼠标拖动
        for x in range(5):
            js = "var q=document.documentElement.scrollTop=" + str(x * 700)
            self.browser.execute_script(js)
            time.sleep(2)
        time.sleep(5)
        # 链接数组
        soup = BS(self.browser.page_source, 'lxml')
        groups = soup.find_all(class_='link')
        return ['https://www.toutiao.com' + group.attrs['href'] for group in groups]

    def get_article_news(self, links):
        """
        获取每篇新闻
        :param links: 链接列表
        :return:
        """
        for link in links:
            self.browser.get(link)
            html = self.browser.page_source
            soup = BS(html, 'lxml')
            sources = []
            content = ''
            if soup.find(class_='article-sub'):
                for each in soup.find(class_='article-sub'):
                    if each.string.strip():
                        sources.append(each.string.strip())
                for each in soup.find(class_='article-content').find(name='p'):
                    if each.string:
                        content = ''.join(each.string)
                yield {
                    'tittle': soup.find(class_='article-title').string,
                    'source': sources[0],
                    'datetime': sources[1],
                    'content': content
                }

    def save_db(self, new):
        """
        保存到mongodb数据库
        :param new: 新闻
        :return:
        """
        if not self.db_client:
            self.db_client = pymongo.MongoClient('127.0.0.1')
            self.db_conn = self.db_client['news']
        collection = 'nba'
        self.db_conn[collection].insert(dict(new))

    def close_db(self):
        """ 关闭数据库连接 """
        try:
            if self.db_client:
                self.db_client.close()
        except Exception:
            pass

    def run(self):
        try:
            # 初始化
            self.get_chrome()
            # 获取当前主题下所有文章链接
            article_links = self.get_article_links()
            print('*********获取所有文章连接完毕, 总的链接数据:{} ***********'.format(len(article_links)))
            # 开始下载新闻
            article_news = self.get_article_news(article_links)
            for article_new in article_news:
                print(article_new)
        finally:
            self.close_db()
            self.close_chrome()
            print('=================end=================')


if __name__ == '__main__':
    toutiao = Toutiao()
    toutiao.run()
