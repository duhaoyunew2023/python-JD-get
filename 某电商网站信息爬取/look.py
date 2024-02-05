"""对爬取的数据进行分析"""
from plotly.graph_objs import Bar
import time
from plotly import offline
import pandas as pd

class MakePlot:
    def __init__(self):
        time.sleep(1)
        print('正在进行可视化')
        # 读取数据
        self.data = pd.read_excel('JD data.xlsx',sheet_name=0)

    def make(self):
        """将数据可视化"""
        data = [{
            'type':'bar',
            'x':self.data['店铺'],
            'y':self.data['价格']
        }]
        layout = {
            'title':'IPhone4s京东数据表',
            'xaxis':{'title':'店铺名'},
            'yaxis': {'title':'价格'}
        }
        fig = {'data':data,'layout':layout}
        offline.plot(fig,filename = 'JD4s.html')
        print('转换图表成功')






