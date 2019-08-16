# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_db.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import _thread
import datetime
import binascii
import math
import sys
import PyQt5.sip
import random
from concurrent.futures import thread
import playsound
from playsound import playsound
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog, QVBoxLayout, QDateTimeEdit, QDialogButtonBox
from PyQt5.QtCore import QObject, pyqtSignal, QTimer, QDateTime
import utils.myglobalvar as gl
import time
#import utils.readCardUtils
import utils.mysqlUtil
# from ui.ui_competition_score_dialog import DateDialog


class Ui_Form(object):
    stat = utils.mysqlUtil.MysqlUtil()


    changdi_index=0
    changdihao_index=0


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setAcceptDrops(False)
        Form.setStyleSheet("background-color:#fff")

        #顶部导航
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 0, 1820, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget_3")
        self.verticalLayoutWidget.setStyleSheet("QWidget{color:#000}"
                                       "QWidget{background-color:#DD4F43}"
                                       "QWidget{border:2px}"
                                       "QWidget{border-radius:10px}"
                                       "QWidget{padding:2px 4px}")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(700, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        #        self.zubie = QtWidgets.QLabel(self.)

        self.setting = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.setting.setGeometry(QtCore.QRect(0, 15, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(20)

        #font.setFamily("Arial Black")
        self.setting.setFont(font)
        self.setting.setText("三检")
        self.setting.setStyleSheet("color : #000")
        self.verticalLayout_3.addWidget(self.setting)






        #运动员块
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(500, 740, 700, 250))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setStyleSheet(
            "border-width: 1px;border-style: solid;border-color: #767475 ;border-radius:10px")

        self.chaxun_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chaxun_bt.setGeometry(QtCore.QRect(10, 20, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chaxun_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.chaxun_bt.setStyleSheet("QPushButton{color:#000}"
                                     "QPushButton:hover{color:red}"
                                     "QPushButton{background-color:#FFE05E}"
                                     "QPushButton{border:2px}"
                                     "QPushButton{border-radius:10px}"
                                     "QPushButton{padding:2px 4px}"

                                     )
        self.chaxun_bt.setObjectName("chaxun_bt")
        self.chaxun_bt.setText("查询")


        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(60, 25, 100, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("场地选择")
        self.label.setStyleSheet("border:0px")

        # <
        self.changdipre_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.changdipre_bt.setGeometry(QtCore.QRect(150, 25, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.changdipre_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.changdipre_bt.setStyleSheet("QPushButton{color:#000}"
                                          "QPushButton:hover{color:red}"
                                          "QPushButton{background-color:#FFE05E}"
                                          "QPushButton{border:2px}"
                                          "QPushButton{border-radius:5px}"
                                          "QPushButton{padding:2px 4px}"

                                          )
        self.changdipre_bt.setObjectName("changdipre_bt")
        self.changdipre_bt.setText("<")



        self.changdi = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.changdi.setGeometry(QtCore.QRect(180, 25, 60, 20))
        self.changdi.setObjectName("changdi")
        self.changdi.setText("")
        self.changdi.setAlignment(QtCore.Qt.AlignCenter)

        self.changdi.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")


        #>
        self.changdinext_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.changdinext_bt.setGeometry(QtCore.QRect(250, 25, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.changdinext_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.changdinext_bt.setStyleSheet("QPushButton{color:#000}"
                                     "QPushButton:hover{color:red}"
                                     "QPushButton{background-color:#FFE05E}"
                                     "QPushButton{border:2px}"
                                     "QPushButton{border-radius:5px}"
                                     "QPushButton{padding:2px 4px}"

                                     )
        self.changdinext_bt.setObjectName("changdinext_bt")
        self.changdinext_bt.setText(">")


        # 场次选择
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(280, 25, 100, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("场次选择")
        self.label.setStyleSheet("border:0px")

        # <
        self.changcipre_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.changcipre_bt.setGeometry(QtCore.QRect(380, 25, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.changcipre_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.changcipre_bt.setStyleSheet("QPushButton{color:#000}"
                                         "QPushButton:hover{color:red}"
                                         "QPushButton{background-color:#FFE05E}"
                                         "QPushButton{border:2px}"
                                         "QPushButton{border-radius:5px}"
                                         "QPushButton{padding:2px 4px}"

                                         )
        self.changcipre_bt.setObjectName("changcipre_bt")
        self.changcipre_bt.setText("<")

        self.changdihao = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.changdihao.setGeometry(QtCore.QRect(410, 25, 120, 20))
        self.changdihao.setObjectName("changdihao")
        self.changdihao.setText("")
        self.changdihao.setAlignment(QtCore.Qt.AlignCenter)

        self.changdihao.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")

        # >
        self.changcinext_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.changcinext_bt.setGeometry(QtCore.QRect(540, 25, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.changcinext_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.changcinext_bt.setStyleSheet("QPushButton{color:#000}"
                                          "QPushButton:hover{color:red}"
                                          "QPushButton{background-color:#FFE05E}"
                                          "QPushButton{border:2px}"
                                          "QPushButton{border-radius:5px}"
                                          "QPushButton{padding:2px 4px}"

                                          )
        self.changcinext_bt.setObjectName("changcinext_bt")
        self.changcinext_bt.setText(">")

        # 串口
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(580, 25, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("串口")
        self.label.setStyleSheet("border:0px")
        self.chuankou = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.chuankou.setGeometry(QtCore.QRect(638, 25, 40, 20))
        self.chuankou.setObjectName("defenqujian")
        self.chuankou.setText("COM5")
        self.chuankou.setAlignment(QtCore.Qt.AlignCenter)
        self.chuankou.setFixedWidth(40)
        self.chuankou.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")

        # 级别
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(280, 50, 100, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("级别")
        self.label.setStyleSheet("border:0px")

        self.jibie = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.jibie.setGeometry(QtCore.QRect(410, 50, 120, 20))
        self.jibie.setObjectName("jibie")
        self.jibie.setText("")
        self.jibie.setAlignment(QtCore.Qt.AlignCenter)

        self.jibie.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")



        # 青方
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(10, 100, 60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("青  方")
        self.label.setStyleSheet("border:0px")

        self.qingfangname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qingfangname.setGeometry(QtCore.QRect(65, 100, 140, 20))
        self.qingfangname.setObjectName("qingfangname")
        self.qingfangname.setText("青方")
        self.qingfangname.setAlignment(QtCore.Qt.AlignCenter)

        self.qingfangname.setStyleSheet("color:#3B3E40 ; border-radius:5px ; background-color:#00A4FF ;border-color:#00A4FF")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(220, 100, 30, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("单位")
        self.label.setStyleSheet("border:0px")

        self.qingfangdanwei = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qingfangdanwei.setGeometry(QtCore.QRect(260, 100, 140, 20))
        self.qingfangdanwei.setObjectName("qingfangdanwei")
        self.qingfangdanwei.setText("zwu")
        self.qingfangdanwei.setAlignment(QtCore.Qt.AlignCenter)

        self.qingfangdanwei.setStyleSheet(
            "color:#3B3E40 ; border-radius:5px ; background-color:#00A4FF ;border-color:#00A4FF")

        # 青方护具组号
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(415, 100, 60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("护具组号")
        self.label.setStyleSheet("border:0px")

        self.qinghujunum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qinghujunum.setGeometry(QtCore.QRect(480, 100, 50, 20))
        self.qinghujunum.setObjectName("qinghujunum")
        self.qinghujunum.setText("0")
        self.qinghujunum.setAlignment(QtCore.Qt.AlignCenter)

        self.qinghujunum.setStyleSheet(
            "color:#3B3E40 ; border-radius:5px ; background-color:#00A4FF ;border-color:#00A4FF")


        # 青方头盔组号

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(540, 100, 60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("头盔组号")
        self.label.setStyleSheet("border:0px")

        self.qingtoukuinum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qingtoukuinum.setGeometry(QtCore.QRect(600, 100, 50, 20))
        self.qingtoukuinum.setObjectName("qingtoukuinum")
        self.qingtoukuinum.setText("0")
        self.qingtoukuinum.setAlignment(QtCore.Qt.AlignCenter)

        self.qingtoukuinum.setStyleSheet(
            "color:#3B3E40 ; border-radius:5px ; background-color:#00A4FF ;border-color:#00A4FF")


        # 红方
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(10, 140, 60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("红  方")
        self.label.setStyleSheet("border:0px")
        self.hongfangname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hongfangname.setGeometry(QtCore.QRect(65, 140, 140, 20))
        self.hongfangname.setObjectName("hongfangname")
        self.hongfangname.setText("红方")
        self.hongfangname.setAlignment(QtCore.Qt.AlignCenter)

        self.hongfangname.setStyleSheet(
            "color:#3B3E40 ; border-radius:5px ; background-color:#E37E6D ;border-color:#E37E6D")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(220, 140, 30, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("单位")
        self.label.setStyleSheet("border:0px")

        self.hongfangdanwei = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hongfangdanwei.setGeometry(QtCore.QRect(260, 140, 140, 20))
        self.hongfangdanwei.setObjectName("hongfangdanwei")
        self.hongfangdanwei.setText("zwu")
        self.hongfangdanwei.setAlignment(QtCore.Qt.AlignCenter)

        self.hongfangdanwei.setStyleSheet(
            "color:#3B3E40 ; border-radius:5px ; background-color:#E37E6D ;border-color:#E37E6D")

        # 红方护具组号
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(415, 140, 60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("护具组号")
        self.label.setStyleSheet("border:0px")

        self.honghujunum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.honghujunum.setGeometry(QtCore.QRect(480, 140, 50, 20))
        self.honghujunum.setObjectName("honghujunum")
        self.honghujunum.setText("0")
        self.honghujunum.setAlignment(QtCore.Qt.AlignCenter)

        self.honghujunum.setStyleSheet(
            "color:#3B3E40 ; border-radius:5px ; background-color:#E37E6D ;border-color:#E37E6D")

        # 红方头盔组号

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(540, 140, 60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("头盔组号")
        self.label.setStyleSheet("border:0px")

        self.hongtoukuinum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hongtoukuinum.setGeometry(QtCore.QRect(600, 140, 50, 20))
        self.hongtoukuinum.setObjectName("hongtoukuinum")
        self.hongtoukuinum.setText("0")
        self.hongtoukuinum.setAlignment(QtCore.Qt.AlignCenter)

        self.hongtoukuinum.setStyleSheet(
            "color:#3B3E40 ; border-radius:5px ; background-color:#E37E6D ;border-color:#E37E6D")

        #测试
        self.ceshi_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ceshi_bt.setGeometry(QtCore.QRect(50, 200, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ceshi_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.ceshi_bt.setStyleSheet("QPushButton{color:#000}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:#FFE05E}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:10px}"
                                  "QPushButton{padding:2px 4px}"

                                  )
        self.ceshi_bt.setObjectName("ceshi_bt")
        self.ceshi_bt.setText("测试")



        #上一场
        self.bre_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bre_bt.setGeometry(QtCore.QRect(180, 200, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bre_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.bre_bt.setStyleSheet("QPushButton{color:#000}"
                                   "QPushButton:hover{color:red}"
                                   "QPushButton{background-color:#FFE05E}"
                                   "QPushButton{border:2px}"
                                   "QPushButton{border-radius:10px}"
                                   "QPushButton{padding:2px 4px}"

                                   )
        self.bre_bt.setObjectName("bre_bt")
        self.bre_bt.setText("上一场")


        # 连接
        self.lianjie_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.lianjie_bt.setGeometry(QtCore.QRect(280, 200, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lianjie_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.lianjie_bt.setStyleSheet("QPushButton{color:#000}"
                                     "QPushButton:hover{color:red}"
                                     "QPushButton{background-color:#FFE05E}"
                                     "QPushButton{border:2px}"
                                     "QPushButton{border-radius:10px}"
                                     "QPushButton{padding:2px 4px}"

                                     )
        self.lianjie_bt.setObjectName("lianjie_bt")
        self.lianjie_bt.setText("连接")


        # 下一场
        self.next_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.next_bt.setGeometry(QtCore.QRect(380, 200, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.next_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.next_bt.setStyleSheet("QPushButton{color:#000}"
                                      "QPushButton:hover{color:red}"
                                      "QPushButton{background-color:#FFE05E}"
                                      "QPushButton{border:2px}"
                                      "QPushButton{border-radius:10px}"
                                      "QPushButton{padding:2px 4px}"

                                      )
        self.next_bt.setObjectName("next_bt")
        self.next_bt.setText("下一场")


        # 检录
        self.jianlu_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.jianlu_bt.setGeometry(QtCore.QRect(510, 200, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.jianlu_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.jianlu_bt.setStyleSheet("QPushButton{color:#000}"
                                   "QPushButton:hover{color:red}"
                                   "QPushButton{background-color:#FFE05E}"
                                   "QPushButton{border:2px}"
                                   "QPushButton{border-radius:10px}"
                                   "QPushButton{padding:2px 4px}"

                                   )
        self.jianlu_bt.setObjectName("jianlu_bt")
        self.jianlu_bt.setText("检录")

        # 清除
        self.qingchu_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.qingchu_bt.setGeometry(QtCore.QRect(620, 200, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.qingchu_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.qingchu_bt.setStyleSheet("QPushButton{color:#fff}"
                                      "QPushButton:hover{color:red}"
                                      "QPushButton{background-color:#FE8742}"
                                      "QPushButton{border:2px}"
                                      "QPushButton{border-radius:10px}"
                                      "QPushButton{padding:2px 4px}"

                                      )
        self.qingchu_bt.setObjectName("qingchu_bt")
        self.qingchu_bt.setText("清除")



        # 测试区
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 100, 1800, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setStyleSheet(
            "border-width: 1px;border-style: solid;border-color: #767475 ;border-radius:10px")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(50, 5, 200, 70))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial Black")

        self.label.setFont(font)
        self.label.setText("电子护具及头盔测试")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(3, 35, 1795, 10))

        self.label.setText(
            "-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        # 红方这两个字
        self.honglabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.honglabel.setGeometry(QtCore.QRect(1050, 50, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        self.honglabel.setFont(font)
        self.honglabel.setAlignment(QtCore.Qt.AlignCenter)
        self.honglabel.setObjectName("honglabel")
        self.honglabel.setText("红方")
        self.honglabel.setStyleSheet("QLabel{color:#000}"
                                     "QLabel{background-color:#fff}"
                                     "QLabel{border:2px}"
                                     "QLabel{border-radius:5px}"
                                     "QLabel{padding:2px 4px}")

        # 青方这两个字
        self.qinglabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qinglabel.setGeometry(QtCore.QRect(350, 50, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        self.qinglabel.setFont(font)
        self.qinglabel.setAlignment(QtCore.Qt.AlignCenter)
        self.qinglabel.setObjectName("qinglabel")
        self.qinglabel.setText("青方")
        self.qinglabel.setStyleSheet("QLabel{color:#000}"
                                     "QLabel{background-color:#fff}"
                                     "QLabel{border:2px}"
                                     "QLabel{border-radius:5px}"
                                     "QLabel{padding:2px 4px}")

        # 头盔这两个字
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(5, 180, 80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("头盔")
        self.label.setStyleSheet("border:0px")

        # 青方头盔
        self.qingfangtoukui = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qingfangtoukui.setGeometry(QtCore.QRect(300, 120, 200, 200))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.qingfangtoukui.setFont(font)
        self.qingfangtoukui.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangtoukui.setObjectName("qingfangtoukui")
        self.qingfangtoukui.setText("")
        self.qingfangtoukui.setStyleSheet(
            "background-color:#000000;border-color:#000000 ;border-radius:100px")

        # 红方头盔
        self.hongfangtoukui = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hongfangtoukui.setGeometry(QtCore.QRect(1000, 120, 200, 200))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.hongfangtoukui.setFont(font)
        self.hongfangtoukui.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangtoukui.setObjectName("hongfangtoukui")
        self.hongfangtoukui.setText("")
        self.hongfangtoukui.setStyleSheet("background-color:#000000;border-color:#000000 ;border-radius:100px")


        # 护具这两个字
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(5, 430, 80, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("护具")
        self.label.setStyleSheet("border:0px")

        # 青方护具
        self.qingfanghuju = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qingfanghuju.setGeometry(QtCore.QRect(200, 350, 400, 150))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.qingfanghuju.setFont(font)
        self.qingfanghuju.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfanghuju.setObjectName("qingfanghuju")
        self.qingfanghuju.setText("")
        self.qingfanghuju.setStyleSheet(
            "background-color:#000000;border-color:#000000 ;border-radius:0px")

        # 红方护具
        self.hongfanghuju = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hongfanghuju.setGeometry(QtCore.QRect(900, 350, 400, 150))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.hongfanghuju.setFont(font)
        self.hongfanghuju.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfanghuju.setObjectName("hongfanghuju")
        self.hongfanghuju.setText("")
        self.hongfanghuju.setStyleSheet("background-color:#000000;border-color:#000000 ;border-radius:0px")







        self.firstchaxun()




        # 按钮事件


        self.changdinext_bt.clicked.connect(self.changdinext)
        self.changdipre_bt.clicked.connect(self.changdipre)
        self.changcinext_bt.clicked.connect(self.changdihaonext)
        self.changcipre_bt.clicked.connect(self.changdihaopre)
        self.chaxun_bt.clicked.connect(self.chaxun)


        self.lianjie_bt.clicked.connect(self.lianjie)
        self.next_bt.clicked.connect(self.bisainext)
        self.bre_bt.clicked.connect(self.bisaipre)
        self.jianlu_bt.clicked.connect(self.jianlu)
        # 清除
        self.qingchu_bt.clicked.connect(self.qingchu)

        self.iskaishi=False


        self.qinghujuchangecolor=False
        self.qingtoukuichangecolor=False
        self.honghujuchangecolor=False
        self.hongtoukuichangecolor=False





    def changeColorOne(self,teamnum,qinghujunum,qingtoukuinum,honghujunum,hongtoukuinum):
        """

        :param teamnum: 判断是青方还是红方 红3 青2
        :param qinghujunum: 青方护具组号
        :param qingtoukuinum: 青方头盔组号
        :param honghujunum: 红方护具组号
        :param hongtoukuinum: 红方头盔组号
        :return:
        """
        # print(teamnum,"teamnum")
        # print(type(qinghujunum))
        # print(type(self.qinghujunum.text()))
        # if(qinghujunum==self.qinghujunum.text()):
        #     print("相等")


        if (teamnum == "2" and qinghujunum==self.qinghujunum.text()):

                self.qingfanghuju.setStyleSheet("background-color:#FFE05E;border-color:#FFE05E ;border-radius:0px")
                myout = []

        if (teamnum == "3" and honghujunum==self.honghujunum.text()):


                # print("第一次力值" + str(self.firstlizhi_hong))
                myout = []
                self.hongfanghuju.setStyleSheet("background-color:#FFE05E;border-color:#FFE05E ;border-radius:0px")

        if (teamnum == "7" and qingtoukuinum == self.qingtoukuinum.text()):
            self.qingfangtoukui.setStyleSheet("background-color:#FFE05E;border-color:#FFE05E ;border-radius:100px")
            myout = []

        if (teamnum == "8" and hongtoukuinum == self.hongtoukuinum.text()):
            # print("第一次力值" + str(self.firstlizhi_hong))
            myout = []
            self.hongfangtoukui.setStyleSheet("background-color:#FFE05E;border-color:#FFE05E ;border-radius:100px")


    def changeColorTwo(self, teamnum, qinghujunum, qingtoukuinum, honghujunum, hongtoukuinum):
        """

        :param teamnum: 判断是青方还是红方 红3 青2
        :param qinghujunum: 青方护具组号
        :param qingtoukuinum: 青方头盔组号
        :param honghujunum: 红方护具组号
        :param hongtoukuinum: 红方头盔组号
        :return:
        """


        if (teamnum == "2" and qinghujunum==self.qinghujunum.text()):

                self.qingfanghuju.setStyleSheet("background-color:#FFE05E;border-color:#FFE05E ;border-radius:0px")
                myout = []

        if (teamnum == "3" and honghujunum==self.honghujunum.text()):


                # print("第一次力值" + str(self.firstlizhi_hong))
                myout = []
                self.hongfanghuju.setStyleSheet("background-color:#FFE05E;border-color:#FFE05E ;border-radius:0px")

        if (teamnum == "7" and qingtoukuinum == self.qingtoukuinum.text()):
            self.qingfangtoukui.setStyleSheet("background-color:#FFE05E;border-color:#FFE05E ;border-radius:15px")
            myout = []

        if (teamnum == "8" and hongtoukuinum == self.hongtoukuinum.text()):
            # print("第一次力值" + str(self.firstlizhi_hong))
            myout = []
            self.hongfangtoukui.setStyleSheet("background-color:#FFE05E;border-color:#FFE05E ;border-radius:15px")


        if (teamnum == "2" and qinghujunum == self.qinghujunum.text()):
            self.qingfanghuju.setStyleSheet(
                "background-color:rgb(0,120,215);border-color:(0,120,215) ;border-radius:0px")
            myout = []

        if (teamnum == "3" and honghujunum == self.honghujunum.text()):
            # print("第一次力值" + str(self.firstlizhi_hong))
            myout = []
            self.hongfanghuju.setStyleSheet("background-color:red;border-color:red ;border-radius:0px")

        if (teamnum == "7" and qingtoukuinum == self.qingtoukuinum.text()):
            self.qingfangtoukui.setStyleSheet(
                "background-color:rgb(0,120,215);border-color:(0,120,215) ;border-radius:15px")
            myout = []

        if (teamnum == "8" and qingtoukuinum == self.qingtoukuinum.text()):
            # print("第一次力值" + str(self.firstlizhi_hong))

            self.hongfangtoukui.setStyleSheet("background-color:red;border-color:red ;border-radius:15px")
            myout = []


    # 显示对话框
    def showMsg(self, msg):
        qw = QtWidgets.QWidget()
        QMessageBox.warning(qw, '消息', msg)

    def jianlu(self):
        try:
            sql ="UPDATE bisaixinxi SET sanjian=1 where changdi='%s' and changdihao='%s'"%(self.changdi.text(),self.changdihao.text())
            print(sql)
            self.stat.update(sql)
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '成功', "检录成功", QMessageBox.Ok)
        except:
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "检录失败", QMessageBox.Ok)

    def chaxun(self):
        # self.li=[]
        if (self.changdihaoresult == ()):
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)
        else:
            # for i in self.changdihaoresult:
            #     self.li.append(i[0])
            # li=str(self.li)
            # li=li.replace('[','(').replace(']',')')
            # sql="select bisaixuhao,changdihao,qingfangxinming,qingfangdanwei,hongfangxinming,hongfangdanwei,jibie,lunci,bisaizhuangtai from bisaixinxi where changdi='%s' and changdihao in %s and bisaizhuangtai='等待中' order by changdihao"%(self.changdi.text(),li)
            # print(sql)
            # self.yundongyuans=self.stat.fetchall(sql)
            sql="select bisaixuhao,changdihao,qingfangxinming,qingfangdanwei,hongfangxinming,hongfangdanwei,jibie,lunci from bisaixinxi where changdi='%s' and changdihao='%s' and bisaizhuangtai='等待中' order by changdihao"%(self.changdi.text(),self.changdihao.text())
            print(sql)
            self.yundongyuan=self.stat.fetchone(sql)
            print(self.yundongyuan)
            if(self.yundongyuan==()):
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)
            else:
                self.iskaishi = True
                # print(self.yundongyuans)
                print(self.yundongyuan)
                self.qingfangname.setText(self.yundongyuan[2])
                self.qingfangdanwei.setText(self.yundongyuan[3])
                self.hongfangname.setText(self.yundongyuan[4])
                self.hongfangdanwei.setText(self.yundongyuan[5])
                self.jibie.setText(self.yundongyuan[6])





    def changdinext(self):
        if(self.changdi.text()==""):
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)
        else:
            self.changdi_index +=1
            if(self.changdi_index<len(self.changdiresults)):
                self.changdi.setText(self.changdiresults[self.changdi_index][0])
            else:
                self.changdi_index=0
                self.changdi.setText(self.changdiresults[self.changdi_index][0])
            sql = "select distinct changdihao from bisaixinxi where changdi='%s' and bisaizhuangtai='等待中' order by changdihao" % self.changdi.text()
            print(sql)
            self.changdihaoresult = self.stat.fetchall(sql)
            if(self.changdihaoresult==()):
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw,'错误',"没有数据",QMessageBox.Ok)
            else:

                self.changdihao_index = 0
                self.changdihao.setText(self.changdihaoresult[self.changdihao_index][0])

    def changdipre(self):
        if (self.changdi.text() == ""):
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)
        else:
            if(self.changdi_index>0):
                self.changdi_index -= 1
                self.changdi.setText(self.changdiresults[self.changdi_index][0])
            else:
                self.changdi_index=len(self.changdiresults)-1
                self.changdi.setText(self.changdiresults[self.changdi_index][0])

            sql = "select distinct changdihao from bisaixinxi where changdi='%s' and bisaizhuangtai='等待中' order by changdihao" % self.changdi.text()
            print(sql)
            self.changdihaoresult = self.stat.fetchall(sql)
            if (self.changdihaoresult == ()):
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)
            else:
                self.changdihao_index=0
                self.changdihao.setText(self.changdihaoresult[self.changdihao_index][0])

    def changdihaonext(self):
        if(self.changdihao.text()==""):
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)
        else:
            self.changdihao_index += 1
            if (self.changdihao_index < len(self.changdihaoresult)):
                self.changdihao.setText(self.changdihaoresult[self.changdihao_index][0])
            else:
                self.changdihao_index = 0
                self.changdihao.setText(self.changdihaoresult[self.changdihao_index][0])

    def changdihaopre(self):
        if (self.changdihao.text() == ""):
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)
        else:
            if (self.changdihao_index > 0):
                self.changdihao_index -= 1
                self.changdihao.setText(self.changdihaoresult[self.changdihao_index][0])

            else:
                self.changdihao_index = len(self.changdihaoresult) - 1
                self.changdihao.setText(self.changdihaoresult[self.changdihao_index][0])

    def firstchaxun(self):
        self.changdiresults=self.stat.fetchall("select distinct changdi from bisaixinxi order by changdi")

        if(self.changdiresults==() ):

            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "当前没有比赛信息", QMessageBox.Ok)
            print(self.changdi.text())
        else:
            self.changdi.setText(self.changdiresults[self.changdi_index][0])
            sql= "select distinct changdihao from bisaixinxi where changdi='%s' and bisaizhuangtai='等待中'  order by changdihao"%self.changdi.text()
            print(sql)

            self.changdihaoresult = self.stat.fetchall(sql)
            if( not self.changdihaoresult==()):
                self.changdihao.setText(self.changdihaoresult[self.changdihao_index][0])

    def bisaipre(self):

        # self.li=gl.get_value("changci")
        # if(self.li==[]):
        #     qw = QtWidgets.QWidget()
        #     QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)
        # else:
        #     if(self.index>0):
        #         self.qingchu()
        #         self.index -=1
        # self.changdihao.setText(self.li[self.index])
        # gl.set_value('changdihao',self.changdihao.text())

        sql = "select bisaixuhao,changdihao,qingfangxinming,qingfangdanwei,hongfangxinming,hongfangdanwei,jibie,qingfangbianhao,hongfangbianhao,lunci,bisaizhuangtai " \
              "from bisaixinxi where changdi='%s' and changdihao<'%s' and bisaizhuangtai='等待中' order by changdihao DESC limit 1" % (
                  self.changdi.text(), self.changdihao.text())
        self.yundongyuan = self.stat.fetchone(sql)
        if (self.yundongyuan == None):
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "没有上一场", QMessageBox.Ok)
        else:
            self.changdihao.setText(self.yundongyuan[1])
            self.qingfangname.setText(self.yundongyuan[2])
            self.qingfangdanwei.setText(self.yundongyuan[3])
            self.hongfangname.setText(self.yundongyuan[4])
            self.hongfangdanwei.setText(self.yundongyuan[5])

            self.jibie.setText(self.yundongyuan[6])




    def bisainext(self):
        # self.li=gl.get_value("changci")
        # if(self.li==[]):
        #     qw = QtWidgets.QWidget()
        #     QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)

        # qw = QtWidgets.QWidget()
        # reply = QMessageBox.warning(qw, '警告', "确定下一场？", QMessageBox.Yes | QMessageBox.No)
        # if (reply == QMessageBox.Yes):
            # if(self.index<len(self.li)):
            #     self.qingchu()
            #     self.index +=1
            #     self.changdihao.setText(self.li[self.index])
            #     gl.set_value('changdihao',self.changdihao.text())


            sql = "select bisaixuhao,changdihao,qingfangxinming,qingfangdanwei,hongfangxinming,hongfangdanwei,jibie,qingfangbianhao,hongfangbianhao,bisaizhuangtai,lunci " \
                  "from bisaixinxi where changdi='%s' and changdihao>'%s' and bisaizhuangtai='等待中' order by changdihao ASC LIMIT 1" % (
                      self.changdi.text(), self.changdihao.text())
            print(sql)
            self.yundongyuan = self.stat.fetchone(sql)
            print(self.yundongyuan)
            if (self.yundongyuan == None):
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '错误', "该场地比赛已全部结束", QMessageBox.Ok)
            else:





                print(self.yundongyuan)
                self.changdihao.setText(self.yundongyuan[1])
                self.qingfangname.setText(self.yundongyuan[2])
                self.qingfangdanwei.setText(self.yundongyuan[3])
                self.hongfangname.setText(self.yundongyuan[4])
                self.hongfangdanwei.setText(self.yundongyuan[5])

                self.jibie.setText(self.yundongyuan[6])

                self.qingchu()


    def insert(self):

        _thread.start_new_thread(self.insert_deta, ())


    def lianjie(self):




            try:
                print('开始连接串口')
                x = serial.Serial(self.chuankou.text(), "115200")
                print(x)
                self.dataFlag = True
                _thread.start_new_thread(self.getData, (x,))
                self.lianjie_bt.setText('已连接')
            except:
                self.isfirst=True
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '错误', "连接串口失败，请检查串口号和波特率是否正确", QMessageBox.Ok)







    def getData(self, x):

        print(x)
        myout = []
        self.index_2 = 0
        y=0
        t=0
        print(self.dataFlag)


        while self.dataFlag:


            myout = []
            while x.inWaiting() > 0:
                myout.append(binascii.b2a_hex(x.read(1)))

                # 仅测试需要，实际须注释
                if (len(myout) == 7):
                    break


            if myout != []:
                # myout = [b'\xAA', b'\x02', b'\x00', b'\x01', b'\xD0', b'\xD1', b'\xD2', b'\x01']

                # print(equipment.calculate_time(myout).sport_time)
                # self.showGrade(equipment.calculate_time(myout).run_num,equipment.calculate_time(myout).sport_time)
                # print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
                # print(myout)
                # s = str(myout[0:])
                t1=time.time()

                s = str(myout)
                #   print(s)
                last = s.replace("b'", "").replace("[", "").replace("']", "").replace(",", "").replace("' ",
                                                                                                       "").replace(
                    "b'_'", '')
                print(last)

                #判断是电子护具(组别 红方 3 青方 2)还是打分器
                group_1 = last[5]
                hujunum=last[4]
                print("group_1",group_1)
                print('护具号---',hujunum)
                # print(group_1)


                if(t1-t>1):
                    if (group_1 == "2" and hujunum == self.qinghujunum.text() and not self.qinghujuchangecolor):
                        QApplication.processEvents()
                        self.qingfanghuju.setStyleSheet(
                            "background-color:#FFE05E;border-color:#FFE05E ;border-radius:0px")
                        self.qinghujuchangecolor = True
                        QApplication.processEvents()
                        myout = []
                        print("改变qh1")
                        t=time.time()

                    elif (group_1 == "3" and hujunum == self.honghujunum.text() and not self.honghujuchangecolor):
                        # print("第一次力值" + str(self.firstlizhi_hong))
                        myout = []
                        QApplication.processEvents()
                        self.hongfanghuju.setStyleSheet(
                            "background-color:#FFE05E;border-color:#FFE05E ;border-radius:0px")
                        self.honghujuchangecolor = True
                        QApplication.processEvents()
                        print("改变hh1")
                        t = time.time()

                    elif (group_1 == "7" and hujunum == self.qingtoukuinum.text() and not self.qingtoukuichangecolor):
                        QApplication.processEvents()
                        self.qingfangtoukui.setStyleSheet(
                            "background-color:#FFE05E;border-color:#FFE05E ;border-radius:15px")
                        myout = []
                        self.qingtoukuichangecolor = True
                        QApplication.processEvents()
                        t = time.time()
                        print("改变qt1")

                    elif (group_1 == "8" and hujunum == self.hongtoukuinum.text() and not self.hongtoukuichangecolor):
                        # print("第一次力值" + str(self.firstlizhi_hong))
                        myout = []
                        QApplication.processEvents()
                        self.hongfangtoukui.setStyleSheet(
                            "background-color:#FFE05E;border-color:#FFE05E ;border-radius:15px")
                        self.hongtoukuichangecolor = True
                        QApplication.processEvents()
                        t = time.time()
                        print("改变ht1")

                    elif (group_1 == "2" and hujunum == self.qinghujunum.text() and self.qinghujuchangecolor):
                        QApplication.processEvents()
                        self.qingfanghuju.setStyleSheet(
                            "background-color:rgb(0,120,215);border-color:(0,120,215) ;border-radius:0px")
                        QApplication.processEvents()
                        myout = []
                        t = time.time()
                        print("改变qh2")

                    elif (group_1 == "3" and hujunum == self.honghujunum.text() and self.honghujuchangecolor):
                        # print("第一次力值" + str(self.firstlizhi_hong))
                        myout = []
                        QApplication.processEvents()
                        self.hongfanghuju.setStyleSheet("background-color:red;border-color:red ;border-radius:0px")
                        QApplication.processEvents()
                        t = time.time()
                        print("改变hh2")

                    elif (group_1 == "7" and hujunum == self.qingtoukuinum.text() and self.qingtoukuichangecolor):
                        QApplication.processEvents()
                        self.qingfangtoukui.setStyleSheet(
                            "background-color:rgb(0,120,215);border-color:(0,120,215) ;border-radius:15px")
                        QApplication.processEvents()
                        myout = []
                        t = time.time()
                        print("改变qt2")

                    elif (group_1 == "8" and hujunum == self.qingtoukuinum.text() and self.hongtoukuichangecolor):
                        # print("第一次力值" + str(self.firstlizhi_hong))
                        QApplication.processEvents()
                        self.hongfangtoukui.setStyleSheet(
                            "background-color:red;border-color:red ;border-radius:15px")
                        QApplication.processEvents()
                        myout = []
                        print("改变ht2")
                        t=time.time()

    def qingchu(self):
        self.hongfanghuju.setStyleSheet("background-color:#000000;border-color:#000000 ;border-radius:0px")
        self.qingfanghuju.setStyleSheet(
            "background-color:#000000;border-color:#000000 ;border-radius:0px")
        self.hongfangtoukui.setStyleSheet("background-color:#000000;border-color:#000000 ;border-radius:15px")
        self.qingfangtoukui.setStyleSheet(
            "background-color:#000000;border-color:#000000 ;border-radius:15px")
        self.qinghujuchangecolor = False
        self.qingtoukuichangecolor = False
        self.honghujuchangecolor = False
        self.hongtoukuichangecolor = False











class setSettingWindow(QtWidgets.QDialog):
    def __init__(self):
        # utils.mysqlUtil.MysqlUtil.host = '10.60.144.104'
        # utils.mysqlUtil.MysqlUtil.dbPort = '3306'
        # utils.mysqlUtil.MysqlUtil.username = 'root'
        # utils.mysqlUtil.MysqlUtil.password = '123321'
        # utils.mysqlUtil.MysqlUtil.database = 'sport'

        super(setSettingWindow,self).__init__()
        self.new=Ui_Form()
        self.new.setupUi(self)



    def getdata(self):

        return self.new.xiuxitime.text()

    def myclose(self):
        QtWidgets.QDialog.hideEvent(self)

if __name__ == '__main__':
    utils.mysqlUtil.MysqlUtil.host = 'localhost'
    utils.mysqlUtil.MysqlUtil.dbPort = '3306'
    utils.mysqlUtil.MysqlUtil.username = 'root'
    utils.mysqlUtil.MysqlUtil.password = 'lgm123'
    utils.mysqlUtil.MysqlUtil.database = 'sport'
    app = QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    content = Ui_Form()
    content.setupUi(main)


    main.show()
    sys.exit(app.exec_())