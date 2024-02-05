import get
import look

class Main:
    def __init__(self):
        # 获取目标数据
        geter = get.Sift()   # 创建get.py文件中的Sift类
        geter.take()
        geter.sava()
        # 进行可视化
        layout = look.MakePlot()
        layout.make()

if __name__ == '__main__':
    Main()

