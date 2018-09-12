# -*- coding: utf-8 -*-
import serial
import result
import threading
import time

# x = serial.Serial('COM4', 38400)


# i=0
def fasong():
    while True:
        # print("wocao")
        myinput = input('shuru>')
        myinput = myinput.encode(encoding="utf-8")
        # print("you input "+myinput)
        # time.sleep(1)
        x.write(myinput)


# 转换byte数据为16进制数据
def transform_hex_data(data):
    return int(data.hex(), 16)


# 计算时间
def calculate_time(out):
    # print(transform_hex_data(out[4]) << 8)
    # print(transform_hex_data(out[5]))
    sport_time = (transform_hex_data(out[4]) << 8) + transform_hex_data(out[5])
    real_time = sport_time / 100
    result_bean = result.result(transform_hex_data(out[1]), real_time)
    # print(result_bean.to_string())
    return result_bean


        # myout=x.read(14)
    # myout="lll"
    # time.sleep(1)


# if __name__ == '__main__':
    # print(0x91 << 8)
    # jieshou()
    # t1 = threading.Thread(target=jieshou, name="jieshou")
    # t2 = threading.Thread(target=fasong, name="fasong")
    # t2.start()
    # t1.start()
