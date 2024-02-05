# https://search.jd.com/Search?keyword=iPhone4&enc=utf-8&wq=iPhone4
import selenium.webdriver as driver
from selenium.webdriver.common.by import By
import time
from lxml import etree
import pandas

class GetData:
    """一手数据获取：前端代码"""
    def __init__(self):
        # 目标网站：京东iPhone4s搜索页面
        self.url = 'https://search.jd.com/Search?keyword=iPhone4&enc=utf-8&wq=iPhone4'
        # 创建浏览器
        self.edge = driver.Edge()
        # 访问指定页面
        self.edge.get(self.url)

    def take(self):
        '对页面进行操作'
        button = self.edge.find_element(By.CLASS_NAME,'weixin-icon')
        button.click()
        # 等待登录
        time.sleep(10)
        # 最终数据:目标页面代码
        self.over_data = self.edge.page_source

class Sift:
    "筛选信息"
    def __init__(self):
        # 创建GetData类获取前端代码
        geter = GetData()   # 创建
        geter.take()    # 操作
        # 最终的前端页面数据
        self.over_data = geter.over_data

    def take(self):
        # 创建xpath解析器
        html = etree.HTML(self.over_data)
        # 获取数据
        self.prices = html.xpath('//*[@id="J_goodsList"]/ul/li[*]/div/div[*]/strong/i/text()')
        self.shop = html.xpath('//*[@id="J_goodsList"]/ul/li[*]/div/div[*]/span/a/text()')
        self.shopping = html.xpath('//*[@id="J_goodsList"]/ul/li[*]/div/div[*]/span/a/@href')

        # 将网站链接手动加上https:
        for i in range(len(self.shopping)):
            data = 'https:'+self.shopping[i]
            self.shopping[i] = data
        print('数据获取成功')
    def sava(self):
        '保存'
        print('保存中...')
        # 创建数据集
        data = {'价格':self.prices,
                '店铺':self.shop,
                '店铺链接':self.shopping
                }
        pd = pandas.DataFrame(data)

        # 写入文件
        pd.to_excel('JD data.xlsx',index = False)
        time.sleep(2)
        print('保存成功')


