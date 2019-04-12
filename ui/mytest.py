# -*- coding: utf-8 -*-
import time
from filecmp import cmp

import serial

def transform_hex_data(data):
    return int(data.hex(), 16)

#重置计时以及打分器分值



# 收发数据
if __name__ == '__main__':




    serialPort = "COM5"  # 串口
    baudRate = 115200  # 波特率
    ser = serial.Serial(serialPort, baudRate,)
    print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))
    myout = []

    index=0
    index_2=0
    firstlizhi=0
    dafenqi4=0
    dafenqi5 = 0
    dafenqi6 = 0
    jishi=0

    while 1:

        while ser.inWaiting() > 0:
          myout.append(ser.read(1))

        if myout != []:
            # myout = [b'\xAA', b'\x02', b'\x00', b'\x01', b'\xD0', b'\xD1', b'\xD2', b'\x01']


            # print(equipment.calculate_time(myout).sport_time)
            # self.showGrade(equipment.calculate_time(myout).run_num,equipment.calculate_time(myout).sport_time)

            s = str(myout[0:])
         #   print(s)
            last = s.replace("b'\\x", "").replace("[", "").replace("']", "").replace(",", "").replace("' ", "").replace(
                "b'_'", '')
         #   print(last)
            value = last[8:10] + last[6:8]
          #  print(value)
            group_1 = last[3]
           # print("组别" + group_1)
            if(group_1=="2" or group_1 == "3"):
                print("------------------护具-------------------")
                # print(transform_hex_data(myout[3]))
                # print(transform_hex_data(myout[4]))

                index = index + 1
                print(index)



                lizhi=(transform_hex_data(myout[4]) << 8) + transform_hex_data(myout[3])
                if (index == 1):
                    firstlizhi=lizhi
                print("第一次力值"+str(firstlizhi))
                print(lizhi)

                if(lizhi<(firstlizhi-(30*int(x)))):
                    print("得2分")
                print("当力值小于"+str(firstlizhi-(30*int(x)))+"得两分")
                print("ID:"+str(lizhi))

                print(value)

                now = value
                myout = []
            # 组别 红方 3 青方 2

            # 进入打分器
            if(group_1=="4" or group_1=="5" or group_1=="6"):
                index_2 = index_2 + 1
                if(index_2 == 1):
                    t=time.time()
              #      print("3秒计时开始")

                t1=time.time()
                if(t1-t>3):
                    t = time.time()
                    #   print("重新开始3秒计时")
                    dafenqi4 = 0
                    dafenqi5 = 0
                    dafenqi6 = 0
               # print("计时开始"+str(t))
                if(group_1=="4" ):
                    t4=time.time()
                    print("4号打分器打分时间"+str(t4-t))
                 #   print("----------打分器-------")

                    value4=last[7]
                    print("打分器"+group_1+"打分："+value4)
                    if(t4-t<3):
                        dafenqi4=int(value4)
                    group = last[9]
                    print("组别"+group)
                    myout = []

                if (group_1 == "5"):
                    t5 = time.time()
                    print("5号打分器打分时间" + str(t5-t))
                 #   print("----------打分器-------")

                    value5 = last[7]
                    print("打分器" + group_1 + "打分：" + value5)
                    if (t5 - t < 3):
                        dafenqi5 = int(value5)
                    group = last[9]
                 #   print("组别" + group)
                    myout = []
                if (group_1 == "6"):
                    t6=time.time()
                    print("6号打分器打分时间" + str(t6-t))
                  #  print("----------打分器-------")

                    value6 = last[7]
                    print("打分器" + group_1 + "打分：" + value6)
                    if (t6 - t < 3):
                        dafenqi6 = int(value6)
                    group = last[9]
                    myout = []
                 #   print("组别" + group)

                if (t1 - t <= 3):
                    if (not dafenqi4 == 0 and dafenqi4 == dafenqi5):
                            print("1----------------------打分器得分------------------" + str(dafenqi4))
                            t=time.time()
                            dafenqi4 = 0
                            dafenqi5 = 0
                            dafenqi6 = 0

                    elif (not dafenqi4 == 0 and dafenqi4 == dafenqi5):
                            print("2----------------------打分器得分----------------" + str(dafenqi6))
                            t=time.time()
                            dafenqi4 = 0
                            dafenqi5 = 0
                            dafenqi6 = 0


                    elif (not dafenqi4 == 0 and dafenqi4 == dafenqi6):
                            print("3--------------------打分器得分---------------" + str(dafenqi6))
                            t=time.time()
                            dafenqi4 = 0
                            dafenqi5 = 0
                            dafenqi6 = 0
                    elif (not dafenqi4 == 0 and dafenqi4 == dafenqi5 == dafenqi6):
                            print("4-------------------打分器得分---------------------" + str(dafenqi6))
                            t=time.time()
                            dafenqi4 = 0
                            dafenqi5 = 0
                            dafenqi6 = 0


