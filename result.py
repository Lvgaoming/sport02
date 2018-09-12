# 串口数据集
class result:
    # 运动时间
    sport_time = 0
    # 跑道编号
    run_num = 0

    # 定义构造方法
    def __init__(self, run_num, sport_time):
        self.sport_time = sport_time
        self.run_num = run_num

    def to_string(self):
        print("第%d跑道用时%.2f" % (self.run_num, self.sport_time))
