# -*- coding: utf-8 -*-
import sys
from ctypes import *
import ui.ui_run
import sport_login

# 人员检录flag
recordFlag = False
# 检录到的卡号
recordCards = set([])


def clickRecord():
    global recordCards
    global recordFlag
    # 开始读卡
    cardNum = readCard()
    if cardNum != -1:
        recordCards.add(cardNum)
        # 设置人员编号文本
        setRecordText(recordCards)


def setRecordText(cards):
    form = sport_login.loginSelf
    form.bh1.setText(cards[0])
    print(cards)


# 加载dll文件
dll = cdll.LoadLibrary("C:\Windows\System32\dcrf32.dll")
# 初始化设备
icdev = dll.dc_init(100, 115200)
# 读取芯片号
data = create_string_buffer(16)
preData = -1
preSt = -2


def readCard():
    global dll, icdev, data, preData, preSt
    d = create_string_buffer(16)
    st = dll.dc_reset(icdev, 0)

    st = dll.dc_cardstr(icdev, 0x01, byref(data))
    # if preSt != st:
    #   print(preSt, st, preData, bytes.decode(data.value))
    # 如果当前卡号与之前卡号不一样
    if preData != bytes.decode(data.value):
        if st < 0 and preSt != st:
            # error!!!
            return -1
        elif st == 0 and preSt != st:
            # 蜂鸣器
            dll.dc_beep(icdev, 10)
            preData = bytes.decode(data.value)
            return bytes.decode(data.value)
        elif st > 0 and preSt <= 0:
            # 无卡或无法寻到卡!!!
            return -1
    elif preData == bytes.decode(data.value) and st != 0:
        preData = -1
    return -1
    preSt = st
    dll.dc_exit()
