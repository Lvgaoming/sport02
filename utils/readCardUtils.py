# -*- coding: utf-8 -*-
from ctypes import *
import time
# 加载dll文件
dll = cdll.LoadLibrary("dcrf32.dll")
# 初始化设备
icdev = dll.dc_init(100,115200)

def getCardId(lastCardId):
	cardId = create_string_buffer(16)
	dll.dc_cardstr(icdev, 0x01, cardId)
	cardId = bytes.decode(cardId.value)
	if cardId!='' and cardId!=lastCardId:
		# print(cardId.value)
		dll.dc_beep(icdev, 10)
		return cardId
	else:
		return ''

dll.dc_exit()
