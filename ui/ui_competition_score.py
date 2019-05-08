# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blood.ui'
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
from ui.ui_competition_score_dialog import winWindow
from ui.ui_setting_test import setSettingWindow


class Ui_Form(object):

    updateMsgSignal = pyqtSignal(str)
    stat = utils.mysqlUtil.MysqlUtil()
    gui = QApplication.processEvents

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(1330, 768)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setAcceptDrops(False)
        Form.setStyleSheet("background-color:#fff")


        #顶部导航
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 0, 1230, 40))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget_3")
        self.verticalLayoutWidget.setStyleSheet("QWidget{color:#000}"
                                       "QWidget{background-color:#DD4F43}"
                                       "QWidget{border:2px}"
                                       "QWidget{border-radius:10px}"
                                       "QWidget{padding:2px 4px}")



        #        self.zubie = QtWidgets.QLabel(self.)

        self.changdi = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changdi.setGeometry(QtCore.QRect(0, 5, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        #font.setFamily("Arial Black")
        self.changdi.setFont(font)

        self.changdi.setStyleSheet("color : #000")


        self.changdihao = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changdihao.setGeometry(QtCore.QRect(70, 5, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        #font.setFamily("Arial Black")
        self.changdihao.setFont(font)

        self.changdihao.setStyleSheet("color : #000")

        self.lunci = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lunci.setGeometry(QtCore.QRect(200, 5, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        # font.setFamily("Arial Black")
        self.lunci.setFont(font)
        # self.lunci.setText("1/8")
        self.lunci.setStyleSheet("color : #000")

        self.jibie = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.jibie.setGeometry(QtCore.QRect(350, 5, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        # font.setFamily("Arial Black")
        self.jibie.setFont(font)
        # self.bisaizhuangtai.setText("1/8")
        self.jibie.setStyleSheet("color : #000")

        self.bisaizhuangtai = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.bisaizhuangtai.setGeometry(QtCore.QRect(800, 5, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        # font.setFamily("Arial Black")
        self.bisaizhuangtai.setFont(font)
        # self.bisaizhuangtai.setText("1/8")
        self.bisaizhuangtai.setStyleSheet("color : #000")


        # self.quite = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.quite.setGeometry(QtCore.QRect(180, 15, 300, 30))
        # font = QtGui.QFont()
        # font.setPointSize(25)
        # font.setFamily("Arial Black")
        # self.quite.setFont(font)
        # self.quite.setText("退出")
        # self.quite.setStyleSheet("color : #000")
        # self.verticalLayout_3.addWidget(self.quite)






        #青方比分
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 150, 200, 150))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")


        self.verticalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qingfangzongfen = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.qingfangzongfen.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(70)
        font.setBold(True)
        self.qingfangzongfen.setFont(font)
        self.qingfangzongfen.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangzongfen.setObjectName("qingfangzongfen")
        self.qingfangzongfen.setText("0")
        self.qingfangzongfen.setStyleSheet("QLabel{color:#fff}"
                                       "QLabel{background-color:rgb(0,120,215)}"
                                       "QLabel{border:2px}"
                                       "QLabel{border-radius:10px}"
                                       "QLabel{padding:2px 4px}")
        self.verticalLayout.addWidget(self.qingfangzongfen)


        #青方姓名

        self.horizontalLayoutWidget_1 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_1.setGeometry(QtCore.QRect(300, 90, 200, 50))
        self.horizontalLayoutWidget_1.setObjectName("horizontalLayoutWidget_1")
        self.horizontalLayoutWidget_1.setStyleSheet("backround-color:#000")

        self.verticalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qingfangname = QtWidgets.QLabel(self.horizontalLayoutWidget_1)
        self.qingfangname.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        self.qingfangname.setFont(font)
        self.qingfangname.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangname.setObjectName("qingfangname")
        self.qingfangname.setText("名字名字名字")
        self.qingfangname.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:rgb(0,120,215)}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")
        self.verticalLayout.addWidget(self.qingfangname)

        # 红方比分
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(830, 150, 200, 150))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.verticalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hongfangzongfen = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.hongfangzongfen.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(70)
        font.setBold(True)
        self.hongfangzongfen.setFont(font)
        self.hongfangzongfen.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangzongfen.setObjectName("hongfangzongfen")
        self.hongfangzongfen.setText("0")
        self.hongfangzongfen.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:10px}"
                                 "QLabel{padding:2px 4px}")
        self.verticalLayout.addWidget(self.hongfangzongfen)

        # 红方姓名

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(830, 90, 200, 50))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setStyleSheet("backround-color:#000")

        self.verticalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hongfangname = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.hongfangname.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        self.hongfangname.setFont(font)
        self.hongfangname.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangname.setObjectName("hongfangname")
        self.hongfangname.setText("名字名字名字")
        self.hongfangname.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")
        self.verticalLayout.addWidget(self.hongfangname)




        #青方单位

        self.horizontalLayoutWidget_1 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_1.setGeometry(QtCore.QRect(30, 130, 220, 80))
        self.horizontalLayoutWidget_1.setObjectName("horizontalLayoutWidget_1")
        self.horizontalLayoutWidget_1.setStyleSheet( "border-width: 1px;border-style: solid;border-color: #767475 "
                                                    )

        self.verticalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qingfangdanwei = QtWidgets.QLabel(self.horizontalLayoutWidget_1)
        self.qingfangdanwei.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        self.qingfangdanwei.setFont(font)
        self.qingfangdanwei.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangdanwei.setObjectName("qingfangdanwei")
        self.qingfangdanwei.setText("zwu")
        self.qingfangdanwei.setStyleSheet("QLabel{color:rgb(0,120,215)}"
                                 "QLabel{background-color:#fff}"

                                 #"QLabel{border:2px}"

                                )
        self.verticalLayout.addWidget(self.qingfangdanwei)

        # 青方扣分
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 250, 80, 50))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setStyleSheet("QWidget{color:#000}"
                                                  "QWidget{border:2px}"
                                                  "QWidget{border-radius:10px}"
                                                  "QWidget{padding:2px 4px}")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qingfangkoufen = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.qingfangkoufen.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        self.qingfangkoufen.setFont(font)
        self.qingfangkoufen.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangkoufen.setObjectName("qingfangkoufen")
        self.qingfangkoufen.setText("0")
        self.qingfangkoufen.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:rgb(0,120,215)}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:10px}"
                                 "QLabel{padding:2px 4px}")

        self.verticalLayout.addWidget(self.qingfangkoufen)

        # 扣分
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(120, 220, 50, 30))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()

        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("扣分")
        self.label.setStyleSheet("color:#595B5D")

        self.verticalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.label)


        # # 青方警告
        # self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        # self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 250, 80, 50))
        # self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        # self.horizontalLayoutWidget.setStyleSheet("QWidget{color:#000}"
        #                                           "QWidget{border:2px}"
        #                                           "QWidget{border-radius:10px}"
        #                                           "QWidget{padding:2px 4px}")
        #
        # self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.qingfangjinggao = QtWidgets.QLabel(self.horizontalLayoutWidget)
        # self.qingfangjinggao.setGeometry(QtCore.QRect(0, 0, 0, 0))
        # font = QtGui.QFont()
        # font.setFamily("Arial Black")
        # font.setPointSize(25)
        # font.setBold(True)
        # self.qingfangjinggao.setFont(font)
        # self.qingfangjinggao.setAlignment(QtCore.Qt.AlignCenter)
        # self.qingfangjinggao.setObjectName("qingfangjinggao")
        # self.qingfangjinggao.setText("0")
        # self.qingfangjinggao.setStyleSheet("QLabel{color:#fff}"
        #                          "QLabel{background-color:rgb(0,120,215)}"
        #                          "QLabel{border:2px}"
        #                          "QLabel{border-radius:10px}"
        #                          "QLabel{padding:2px 4px}")
        #
        # self.verticalLayout.addWidget(self.qingfangjinggao)
        #
        # # 警告这两个字
        # self.widget = QtWidgets.QWidget(Form)
        # self.widget.setGeometry(QtCore.QRect(190, 220, 50, 30))
        # self.widget.setObjectName("widget")
        # self.label = QtWidgets.QLabel(self.widget)
        # self.label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        # font = QtGui.QFont()
        #
        # font.setPointSize(15)
        # font.setBold(True)
        # self.label.setFont(font)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        # self.label.setObjectName("label")
        # self.label.setText("警告")
        # self.label.setStyleSheet("color:#595B5D")
        #
        # self.verticalLayout = QtWidgets.QHBoxLayout(self.widget)
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.verticalLayout.addWidget(self.label)



        #红方单位

        self.horizontalLayoutWidget_1 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_1.setGeometry(QtCore.QRect(1080, 130, 220, 80))
        self.horizontalLayoutWidget_1.setObjectName("horizontalLayoutWidget_1")
        self.horizontalLayoutWidget_1.setStyleSheet( "border-width: 1px;border-style: solid;border-color: #767475 "
                                                    )

        self.verticalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hongfangdanwei = QtWidgets.QLabel(self.horizontalLayoutWidget_1)
        self.hongfangdanwei.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        self.hongfangdanwei.setFont(font)
        self.hongfangdanwei.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangdanwei.setObjectName("hongfangdanwei")
        self.hongfangdanwei.setText("zwu")
        self.hongfangdanwei.setStyleSheet("QLabel{color:red}"
                                 "QLabel{background-color:#fff}"

                                 #"QLabel{border:2px}"

                                )
        self.verticalLayout.addWidget(self.hongfangdanwei)

        # 红方扣分
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1140, 250, 80, 50))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setStyleSheet("QWidget{color:#000}"
                                                  "QWidget{border:2px}"
                                                  "QWidget{border-radius:10px}"
                                                  "QWidget{padding:2px 4px}")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hongfangkoufen = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.hongfangkoufen.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        self.hongfangkoufen.setFont(font)
        self.hongfangkoufen.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangkoufen.setObjectName("hongfangkoufen")
        self.hongfangkoufen.setText("0")
        self.hongfangkoufen.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:10px}"
                                 "QLabel{padding:2px 4px}")

        self.verticalLayout.addWidget(self.hongfangkoufen)

        # 扣分这两个字
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(1150, 220, 50, 30))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()

        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("扣分")
        self.label.setStyleSheet("color:#595B5D")

        self.verticalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.label)


        # 红方警告
        # self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        # self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1080, 250, 80, 50))
        # self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        # self.horizontalLayoutWidget.setStyleSheet("QWidget{color:#000}"
        #                                           "QWidget{border:2px}"
        #                                           "QWidget{border-radius:10px}"
        #                                           "QWidget{padding:2px 4px}")
        #
        # self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget)
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.qingfangjinggao = QtWidgets.QLabel(self.horizontalLayoutWidget)
        # self.qingfangjinggao.setGeometry(QtCore.QRect(0, 0, 0, 0))
        # font = QtGui.QFont()
        # font.setFamily("Arial Black")
        # font.setPointSize(25)
        # font.setBold(True)
        # self.qingfangjinggao.setFont(font)
        # self.qingfangjinggao.setAlignment(QtCore.Qt.AlignCenter)
        # self.qingfangjinggao.setObjectName("qingfangjinggao")
        # self.qingfangjinggao.setText("0")
        # self.qingfangjinggao.setStyleSheet("QLabel{color:#fff}"
        #                          "QLabel{background-color:red}"
        #                          "QLabel{border:2px}"
        #                          "QLabel{border-radius:10px}"
        #                          "QLabel{padding:2px 4px}")
        #
        # self.verticalLayout.addWidget(self.qingfangjinggao)

        # 警告
        # self.widget = QtWidgets.QWidget(Form)
        # self.widget.setGeometry(QtCore.QRect(1090, 220, 50, 30))
        # self.widget.setObjectName("widget")
        # self.label = QtWidgets.QLabel(self.widget)
        # self.label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        # font = QtGui.QFont()
        #
        # font.setPointSize(15)
        # font.setBold(True)
        # self.label.setFont(font)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        # self.label.setObjectName("label")
        # self.label.setText("警告")
        # self.label.setStyleSheet("color:#595B5D")
        #
        # self.verticalLayout = QtWidgets.QHBoxLayout(self.widget)
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        # self.verticalLayout.setObjectName("verticalLayout")
        # self.verticalLayout.addWidget(self.label)

        #VS
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(600, 90, 130, 50))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(40)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("VS")
        self.label.setStyleSheet("color:#595B5D")

        self.verticalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.label)




        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(550, 150, 230, 170))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color:#FF9F02")
        self.setgamenum = QtWidgets.QLabel(self.widget)
        self.setgamenum.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)

        self.setgamenum.setFont(font)
        self.setgamenum.setAlignment(QtCore.Qt.AlignCenter)
        self.setgamenum.setObjectName("setgamenum")
        self.gamenum=1
        self.setgamenum.setText("第"+str(self.gamenum)+"局")
        self.setgamenum.setStyleSheet("color:#fff")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 0, 0))


        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label.setText("-----------------------------")
        self.label.setStyleSheet("color:#fff")


         #倒计时
        self.setdaojishi = QtWidgets.QLabel(self.widget)
        self.setdaojishi.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(45)

        self.setdaojishi.setFont(font)
        self.setdaojishi.setAlignment(QtCore.Qt.AlignCenter)
        self.setdaojishi.setObjectName("setdaojishi")
        self.daojishi = 60
        self.setdaojishi.setText(str(datetime.timedelta(seconds=int(self.daojishi)))[2:])
        self.setdaojishi.setStyleSheet("color:#fff")




        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)


        self.verticalLayout.setContentsMargins(10, 0, 0, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.setgamenum)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.setdaojishi)



    #场裁块

        #裁判员和下划线
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 350, 570, 250))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setStyleSheet("border-width: 1px;border-style: solid;border-color: #767475 ;border-radius:10px")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(185, 5, 100,60))

        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Arial Black")

        self.label.setFont(font)
        self.label.setText("裁判员")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(3, 35, 560, 10))

        self.label.setText("---------------------------------------------------------------------------------------------------------------------")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignTop)
        self.label.setObjectName("label")


        #红方这两个字
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(410, 50, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("红方")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")


        #青方这两个字
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(240, 50, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("青方")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:rgb(0,120,215)}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")


        #场裁数

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(40, 80, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("场裁数:")
        self.label.setStyleSheet("border:0px")
        self.changcainum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.changcainum.setGeometry(QtCore.QRect(120, 85, 40, 20))
        self.changcainum.setObjectName("changcainum")
        self.changcainum.setText("3")

        self.changcainum.setFixedWidth(40)
        self.changcainum.setStyleSheet("color:#000 ; border-radius:0px")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(40, 115, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("场裁1:")
        self.label.setStyleSheet("border:0px")
        self.changcai_1_num = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.changcai_1_num.setGeometry(QtCore.QRect(120, 125, 40, 20))
        self.changcai_1_num.setObjectName("changcai_1_num")
        self.changcai_1_num.setText("4")
        self.changcai_1_num.setFixedWidth(40)
        self.changcai_1_num.setStyleSheet("color:#000 ; border-radius:0px")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(40, 150, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("场裁2:")
        self.label.setStyleSheet("border:0px")
        self.changcai_2_num = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.changcai_2_num.setGeometry(QtCore.QRect(120, 160, 40, 20))
        self.changcai_2_num.setObjectName("changcai_2_num")
        self.changcai_2_num.setText("5")
        self.changcai_2_num.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_2_num.setFixedWidth(40)
        self.changcai_2_num.setStyleSheet("color:#000 ; border-radius:0px ; ")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(40, 185, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("场裁3:")
        self.label.setStyleSheet("border:0px")
        self.changcai_3_num = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.changcai_3_num.setGeometry(QtCore.QRect(120, 195, 40, 20))
        self.changcai_3_num.setObjectName("changcai_3_num")
        self.changcai_3_num.setText("6")
        self.changcai_3_num.setFixedWidth(40)
        self.changcai_3_num.setStyleSheet("color:#000 ; border-radius:0px")





        #青方打分器分值
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(190, 85, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("1")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:rgb(0,120,215)}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(225, 85, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("2")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:rgb(0,120,215)}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(260, 85, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("3")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:rgb(0,120,215)}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(295, 85, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("4")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:rgb(0,120,215)}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(330, 85, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("5")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:rgb(0,120,215)}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")


        #红方打分器分值

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(370, 85, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("5")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")


        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(405, 85, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("4")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(440, 85, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("3")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(475, 85, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("2")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(510, 85, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("1")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")


        #一号裁判打分情况
        # 青方打分器分值
        self.changcai_1_qing_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_1_qing_1.setGeometry(QtCore.QRect(190, 120, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_1_qing_1.setFont(font)
        self.changcai_1_qing_1.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_1_qing_1.setObjectName("changcai_1_qing_1")
        self.changcai_1_qing_1.setText("0")
        self.changcai_1_qing_1.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_1_qing_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_1_qing_2.setGeometry(QtCore.QRect(225, 120, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_1_qing_2.setFont(font)
        self.changcai_1_qing_2.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_1_qing_2.setObjectName("changcai_1_qing_2")
        self.changcai_1_qing_2.setText("0")
        self.changcai_1_qing_2.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_1_qing_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_1_qing_3.setGeometry(QtCore.QRect(260, 120, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_1_qing_3.setFont(font)
        self.changcai_1_qing_3.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_1_qing_3.setObjectName("changcai_1_qing_3")
        self.changcai_1_qing_3.setText("0")
        self.changcai_1_qing_3.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_1_qing_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_1_qing_4.setGeometry(QtCore.QRect(295, 120, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_1_qing_4.setFont(font)
        self.changcai_1_qing_4.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_1_qing_4.setObjectName("changcai_1_qing_4")
        self.changcai_1_qing_4.setText("0")
        self.changcai_1_qing_4.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_1_qing_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_1_qing_5.setGeometry(QtCore.QRect(330, 120, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_1_qing_5.setFont(font)
        self.changcai_1_qing_5.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_1_qing_5.setObjectName("changcai_1_qing_5")
        self.changcai_1_qing_5.setText("0")
        self.changcai_1_qing_5.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )


        # 红方打分器分值

        self.changcai_1_hong_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_1_hong_5.setGeometry(QtCore.QRect(370, 120, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_1_hong_5.setFont(font)
        self.changcai_1_hong_5.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_1_hong_5.setObjectName("changcai_1_hong_5")
        self.changcai_1_hong_5.setText("0")
        self.changcai_1_hong_5.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_1_hong_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_1_hong_4.setGeometry(QtCore.QRect(405, 120, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_1_hong_4.setFont(font)
        self.changcai_1_hong_4.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_1_hong_4.setObjectName("changcai_1_hong_4")
        self.changcai_1_hong_4.setText("0")
        self.changcai_1_hong_4.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_1_hong_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_1_hong_3.setGeometry(QtCore.QRect(440, 120, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_1_hong_3.setFont(font)
        self.changcai_1_hong_3.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_1_hong_3.setObjectName("changcai_1_hong_3")
        self.changcai_1_hong_3.setText("0")
        self.changcai_1_hong_3.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )
        self.changcai_1_hong_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_1_hong_2.setGeometry(QtCore.QRect(475, 120, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_1_hong_2.setFont(font)
        self.changcai_1_hong_2.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_1_hong_2.setObjectName("changcai_1_hong_2")
        self.changcai_1_hong_2.setText("0")
        self.changcai_1_hong_2.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_1_hong_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_1_hong_1.setGeometry(QtCore.QRect(510, 120, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_1_hong_1.setFont(font)
        self.changcai_1_hong_1.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_1_hong_1.setObjectName("changcai_1_hong_1")
        self.changcai_1_hong_1.setText("0")
        self.changcai_1_hong_1.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )




        #二号裁判打分情况
        # 青方打分器分值
        self.changcai_2_qing_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_2_qing_1.setGeometry(QtCore.QRect(190, 155, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_2_qing_1.setFont(font)
        self.changcai_2_qing_1.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_2_qing_1.setObjectName("changcai_2_qing_1")
        self.changcai_2_qing_1.setText("0")
        self.changcai_2_qing_1.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_2_qing_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_2_qing_2.setGeometry(QtCore.QRect(225, 155, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_2_qing_2.setFont(font)
        self.changcai_2_qing_2.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_2_qing_2.setObjectName("changcai_2_qing_2")
        self.changcai_2_qing_2.setText("0")
        self.changcai_2_qing_2.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_2_qing_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_2_qing_3.setGeometry(QtCore.QRect(260, 155, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_2_qing_3.setFont(font)
        self.changcai_2_qing_3.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_2_qing_3.setObjectName("changcai_2_qing_3")
        self.changcai_2_qing_3.setText("0")
        self.changcai_2_qing_3.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_2_qing_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_2_qing_4.setGeometry(QtCore.QRect(295, 155, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_2_qing_4.setFont(font)
        self.changcai_2_qing_4.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_2_qing_4.setObjectName("changcai_2_qing_4")
        self.changcai_2_qing_4.setText("0")
        self.changcai_2_qing_4.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_2_qing_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_2_qing_5.setGeometry(QtCore.QRect(330, 155, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_2_qing_5.setFont(font)
        self.changcai_2_qing_5.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_2_qing_5.setObjectName("changcai_2_qing_5")
        self.changcai_2_qing_5.setText("0")
        self.changcai_2_qing_5.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        # 红方打分器分值

        self.changcai_2_hong_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_2_hong_5.setGeometry(QtCore.QRect(370, 155, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_2_hong_5.setFont(font)
        self.changcai_2_hong_5.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_2_hong_5.setObjectName("changcai_2_hong_5")
        self.changcai_2_hong_5.setText("0")
        self.changcai_2_hong_5.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )


        self.changcai_2_hong_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_2_hong_4.setGeometry(QtCore.QRect(405, 155, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_2_hong_4.setFont(font)
        self.changcai_2_hong_4.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_2_hong_4.setObjectName("changcai_2_hong_4")
        self.changcai_2_hong_4.setText("0")
        self.changcai_2_hong_4.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_2_hong_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_2_hong_3.setGeometry(QtCore.QRect(440, 155, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_2_hong_3.setFont(font)
        self.changcai_2_hong_3.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_2_hong_3.setObjectName("changcai_2_hong_3")
        self.changcai_2_hong_3.setText("0")
        self.changcai_2_hong_3.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )
        self.changcai_2_hong_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_2_hong_2.setGeometry(QtCore.QRect(475, 155, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_2_hong_2.setFont(font)
        self.changcai_2_hong_2.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_2_hong_2.setObjectName("changcai_2_hong_2")
        self.changcai_2_hong_2.setText("0")
        self.changcai_2_hong_2.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_2_hong_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_2_hong_1.setGeometry(QtCore.QRect(510, 155, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_2_hong_1.setFont(font)
        self.changcai_2_hong_1.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_2_hong_1.setObjectName("changcai_1_hong_1")
        self.changcai_2_hong_1.setText("0")
        self.changcai_2_hong_1.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        # 三号裁判打分情况
        # 青方打分器分值
        self.changcai_3_qing_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_3_qing_1.setGeometry(QtCore.QRect(190, 190, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_3_qing_1.setFont(font)
        self.changcai_3_qing_1.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_3_qing_1.setObjectName("changcai_3_qing_1")
        self.changcai_3_qing_1.setText("0")
        self.changcai_3_qing_1.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_3_qing_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_3_qing_2.setGeometry(QtCore.QRect(225, 190, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_3_qing_2.setFont(font)
        self.changcai_3_qing_2.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_3_qing_2.setObjectName("changcai_3_qing_2")
        self.changcai_3_qing_2.setText("0")
        self.changcai_3_qing_2.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_3_qing_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_3_qing_3.setGeometry(QtCore.QRect(260, 190, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_3_qing_3.setFont(font)
        self.changcai_3_qing_3.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_3_qing_3.setObjectName("changcai_3_qing_3")
        self.changcai_3_qing_3.setText("0")
        self.changcai_3_qing_3.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_3_qing_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_3_qing_4.setGeometry(QtCore.QRect(295, 190, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_3_qing_4.setFont(font)
        self.changcai_3_qing_4.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_3_qing_4.setObjectName("changcai_3_qing_4")
        self.changcai_3_qing_4.setText("0")
        self.changcai_3_qing_4.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_3_qing_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_3_qing_5.setGeometry(QtCore.QRect(330, 190, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_3_qing_5.setFont(font)
        self.changcai_3_qing_5.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_3_qing_5.setObjectName("changcai_3_qing_5")
        self.changcai_3_qing_5.setText("0")
        self.changcai_3_qing_5.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )


        # 红方打分器分值

        self.changcai_3_hong_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_3_hong_5.setGeometry(QtCore.QRect(370, 190, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_3_hong_5.setFont(font)
        self.changcai_3_hong_5.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_3_hong_5.setObjectName("changcai_3_hong_5")
        self.changcai_3_hong_5.setText("0")
        self.changcai_3_hong_5.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )


        self.changcai_3_hong_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_3_hong_4.setGeometry(QtCore.QRect(405, 190, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_3_hong_4.setFont(font)
        self.changcai_3_hong_4.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_3_hong_4.setObjectName("changcai_3_hong_4")
        self.changcai_3_hong_4.setText("0")
        self.changcai_3_hong_4.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_3_hong_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_3_hong_3.setGeometry(QtCore.QRect(440, 190, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_3_hong_3.setFont(font)
        self.changcai_3_hong_3.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_3_hong_3.setObjectName("changcai_3_hong_3")
        self.changcai_3_hong_3.setText("0")
        self.changcai_3_hong_3.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )
        self.changcai_3_hong_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_3_hong_2.setGeometry(QtCore.QRect(475, 190, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_3_hong_2.setFont(font)
        self.changcai_3_hong_2.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_3_hong_2.setObjectName("changcai_3_hong_2")
        self.changcai_3_hong_2.setText("0")
        self.changcai_3_hong_2.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.changcai_3_hong_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.changcai_3_hong_1.setGeometry(QtCore.QRect(510, 190, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.changcai_3_hong_1.setFont(font)
        self.changcai_3_hong_1.setAlignment(QtCore.Qt.AlignCenter)
        self.changcai_3_hong_1.setObjectName("changcai_3_hong_1")
        self.changcai_3_hong_1.setText("0")
        self.changcai_3_hong_1.setStyleSheet(
            "color:#000 ; border-radius:0px"
        )

        self.dafenqiceshi_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.dafenqiceshi_bt.setGeometry(QtCore.QRect(50, 220, 50, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial Black")

        self.dafenqiceshi_bt.setFont(font)
        self.dafenqiceshi_bt.setStyleSheet("QPushButton{color:#000}"
                                   "QPushButton:hover{color:red}"
                                   "QPushButton{background-color:#FFCD43}"
                                   "QPushButton{border:2px}"
                                   "QPushButton{border-radius:5px}"
                                   "QPushButton{padding:2px 4px}"

                                   )
        self.dafenqiceshi_bt.setObjectName("dafenqiceshi_bt")
        self.dafenqiceshi_bt.setText("测 试")


        #每局比赛扣分和得分记录
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(600, 350, 300, 250))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setStyleSheet("border-width: 1px;border-style: solid;border-color: #767475 ;border-radius:10px")


        #第一局
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(20, 15, 100, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial Black")

        self.label.setFont(font)
        self.label.setText("第一局")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(20, 35, 100, 10))

        self.label.setText("---------------------------------------------------------------------------------")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:rgb(0,120,215)}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:0px}"
                                 "QLabel{padding:2px 4px}")



        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(90, 50, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:0px}"
                                 "QLabel{padding:2px 4px}")




        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(15, 75, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("扣分")
        self.label.setStyleSheet( " color:#000 ; border-width: 0px "
                                 )

        self.qing_game_1_koufen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qing_game_1_koufen.setGeometry(QtCore.QRect(60, 75, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.qing_game_1_koufen.setFont(font)
        self.qing_game_1_koufen.setAlignment(QtCore.Qt.AlignCenter)
        self.qing_game_1_koufen.setObjectName("qing_game_1_koufen")
        self.qing_game_1_koufen.setText("0")
        self.qing_game_1_koufen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "
                                 
                                 )

        self.hong_game_1_koufen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hong_game_1_koufen.setGeometry(QtCore.QRect(90, 75, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.hong_game_1_koufen.setFont(font)
        self.hong_game_1_koufen.setAlignment(QtCore.Qt.AlignCenter)
        self.hong_game_1_koufen.setObjectName("hong_game_1_koufen")
        self.hong_game_1_koufen.setText("0")
        self.hong_game_1_koufen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                             )

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(15, 100, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("得分")
        self.label.setStyleSheet(" color:#000 ; border-width: 0px "
                                 )

        self.qing_game_1_defen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qing_game_1_defen.setGeometry(QtCore.QRect(60, 100, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.qing_game_1_defen.setFont(font)
        self.qing_game_1_defen.setAlignment(QtCore.Qt.AlignCenter)
        self.qing_game_1_defen.setObjectName("qing_game_1_defen")
        self.qing_game_1_defen.setText("0")
        self.qing_game_1_defen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                              )

        self.hong_game_1_defen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hong_game_1_defen.setGeometry(QtCore.QRect(90, 100, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.hong_game_1_defen.setFont(font)
        self.hong_game_1_defen.setAlignment(QtCore.Qt.AlignCenter)
        self.hong_game_1_defen.setObjectName("hong_game_1_koufen")
        self.hong_game_1_defen.setText("0")
        self.hong_game_1_defen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                              )

        # 第二局
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(160, 15, 100, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial Black")

        self.label.setFont(font)
        self.label.setText("第二局")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(160, 35, 100, 10))

        self.label.setText("---------------------------------------------------------------------------------")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(200, 50, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:rgb(0,120,215)}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:0px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(230, 50, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:0px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(155, 75, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("扣分")
        self.label.setStyleSheet(" color:#000 ; border-width: 0px "
                                 )

        self.qing_game_2_koufen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qing_game_2_koufen.setGeometry(QtCore.QRect(200, 75, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.qing_game_2_koufen.setFont(font)
        self.qing_game_2_koufen.setAlignment(QtCore.Qt.AlignCenter)
        self.qing_game_2_koufen.setObjectName("qing_game_2_koufen")
        self.qing_game_2_koufen.setText("0")
        self.qing_game_2_koufen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                              )


        self.hong_game_2_koufen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hong_game_2_koufen.setGeometry(QtCore.QRect(230, 75, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.hong_game_2_koufen.setFont(font)
        self.hong_game_2_koufen.setAlignment(QtCore.Qt.AlignCenter)
        self.hong_game_2_koufen.setObjectName("hong_game_2_koufen")
        self.hong_game_2_koufen.setText("0")
        self.hong_game_2_koufen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                              )

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(155, 100, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("得分")
        self.label.setStyleSheet(" color:#000 ; border-width: 0px "
                                 )

        self.qing_game_2_defen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qing_game_2_defen.setGeometry(QtCore.QRect(200, 100, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.qing_game_2_defen.setFont(font)
        self.qing_game_2_defen.setAlignment(QtCore.Qt.AlignCenter)
        self.qing_game_2_defen.setObjectName("qing_game_2_defen")
        self.qing_game_2_defen.setText("0")
        self.qing_game_2_defen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                             )

        self.hong_game_2_defen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hong_game_2_defen.setGeometry(QtCore.QRect(230, 100, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.hong_game_2_defen.setFont(font)
        self.hong_game_2_defen.setAlignment(QtCore.Qt.AlignCenter)
        self.hong_game_2_defen.setObjectName("hong_game_2_defen")
        self.hong_game_2_defen.setText("0")
        self.hong_game_2_defen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                             )

        # 第三局
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(20, 130, 100, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial Black")

        self.label.setFont(font)
        self.label.setText("第三局")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(20, 150, 100, 10))

        self.label.setText("---------------------------------------------------------------------------------")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(60, 165, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:rgb(0,120,215)}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:0px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(90, 165, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:0px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(15, 190, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("扣分")
        self.label.setStyleSheet(" color:#000 ; border-width: 0px "
                                 )

        self.qing_game_3_koufen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qing_game_3_koufen.setGeometry(QtCore.QRect(60, 190, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.qing_game_3_koufen.setFont(font)
        self.qing_game_3_koufen.setAlignment(QtCore.Qt.AlignCenter)
        self.qing_game_3_koufen.setObjectName("qing_game_3_koufen")
        self.qing_game_3_koufen.setText("0")
        self.qing_game_3_koufen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                              )

        self.hong_game_3_koufen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hong_game_3_koufen.setGeometry(QtCore.QRect(90, 190, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.hong_game_3_koufen.setFont(font)
        self.hong_game_3_koufen.setAlignment(QtCore.Qt.AlignCenter)
        self.hong_game_3_koufen.setObjectName("hong_game_3_koufen")
        self.hong_game_3_koufen.setText("0")
        self.hong_game_3_koufen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                              )

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(15, 215, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("得分")
        self.label.setStyleSheet(" color:#000 ; border-width: 0px "
                                 )

        self.qing_game_3_defen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qing_game_3_defen.setGeometry(QtCore.QRect(60, 215, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.qing_game_3_defen.setFont(font)
        self.qing_game_3_defen.setAlignment(QtCore.Qt.AlignCenter)
        self.qing_game_3_defen.setObjectName("qing_game_3_defen")
        self.qing_game_3_defen.setText("0")
        self.qing_game_3_defen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                             )

        self.hong_game_3_defen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hong_game_3_defen.setGeometry(QtCore.QRect(90, 215, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.hong_game_3_defen.setFont(font)
        self.hong_game_3_defen.setAlignment(QtCore.Qt.AlignCenter)
        self.hong_game_3_defen.setObjectName("hong_game_3_defen")
        self.hong_game_3_defen.setText("0")
        self.hong_game_3_defen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                             )

        # 第四局
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(160, 130, 100, 20))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial Black")

        self.label.setFont(font)
        self.label.setText("第四局")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(160, 150, 100, 10))

        self.label.setText("---------------------------------------------------------------------------------")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(200, 165, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:rgb(0,120,215)}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:0px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(230, 165, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("QLabel{color:#fff}"
                                 "QLabel{background-color:red}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:0px}"
                                 "QLabel{padding:2px 4px}")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(155, 190, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("扣分")
        self.label.setStyleSheet(" color:#000 ; border-width: 0px "
                                 )

        self.qing_game_4_koufen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qing_game_4_koufen.setGeometry(QtCore.QRect(200, 190, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.qing_game_4_koufen.setFont(font)
        self.qing_game_4_koufen.setAlignment(QtCore.Qt.AlignCenter)
        self.qing_game_4_koufen.setObjectName("qing_game_4_koufen")
        self.qing_game_4_koufen.setText("0")
        self.qing_game_4_koufen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                              )

        self.hong_game_4_koufen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hong_game_4_koufen.setGeometry(QtCore.QRect(230, 190, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.hong_game_4_koufen.setFont(font)
        self.hong_game_4_koufen.setAlignment(QtCore.Qt.AlignCenter)
        self.hong_game_4_koufen.setObjectName("hong_game_4_koufen")
        self.hong_game_4_koufen.setText("0")
        self.hong_game_4_koufen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                              )

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(155, 215, 40, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("得分")
        self.label.setStyleSheet(" color:#000 ; border-width: 0px "
                                 )

        self.qing_game_4_defen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qing_game_4_defen.setGeometry(QtCore.QRect(200, 215, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.qing_game_4_defen.setFont(font)
        self.qing_game_4_defen.setAlignment(QtCore.Qt.AlignCenter)
        self.qing_game_4_defen.setObjectName("qing_game_4_defen")
        self.qing_game_4_defen.setText("0")
        self.qing_game_4_defen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                             )

        self.hong_game_4_defen = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hong_game_4_defen.setGeometry(QtCore.QRect(230, 215, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        self.hong_game_4_defen.setFont(font)
        self.hong_game_4_defen.setAlignment(QtCore.Qt.AlignCenter)
        self.hong_game_4_defen.setObjectName("hong_game_4_defen")
        self.hong_game_4_defen.setText("0")
        self.hong_game_4_defen.setStyleSheet(" color:#000 ; border-width: 1px ;border-radius:0px "

                                             )

        # 测试区
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(920, 350, 340, 250))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setStyleSheet(
            "border-width: 1px;border-style: solid;border-color: #767475 ;border-radius:10px")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(50, 5, 200, 70))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial Black")

        self.label.setFont(font)
        self.label.setText("电子护具及打分器测试")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(3, 35, 334, 10))

        self.label.setText(
            "---------------------------------------------------------------------------------------------------------------------")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        # 红方这两个字
        self.honglabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.honglabel.setGeometry(QtCore.QRect(180, 50, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
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


        #设备号
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(250, 50, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("设备号")
        self.label.setStyleSheet("QLabel{color:#000}"
                                     "QLabel{background-color:#fff}"
                                     "QLabel{border:2px}"
                                     "QLabel{border-radius:5px}"
                                     "QLabel{padding:2px 4px}")

        # 青方这两个字
        self.qinglabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qinglabel.setGeometry(QtCore.QRect(50, 50, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
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

        # 设备号
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(115, 50, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("设备号")
        self.label.setStyleSheet("QLabel{color:#000}"
                                 "QLabel{background-color:#fff}"
                                 "QLabel{border:2px}"
                                 "QLabel{border-radius:5px}"
                                 "QLabel{padding:2px 4px}")


        # 头盔这两个字
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(5, 90, 40, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("头盔")
        self.label.setStyleSheet("border:0px")

        # 青方头盔
        self.qingfangtoukui = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qingfangtoukui.setGeometry(QtCore.QRect(75, 85, 30, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.qingfangtoukui.setFont(font)
        self.qingfangtoukui.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangtoukui.setObjectName("qingfangtoukui")
        self.qingfangtoukui.setText("")
        self.qingfangtoukui.setStyleSheet(
            "background-color:#FFE05E;border-color:#FFE05E ;border-radius:15px")

        self.qingtoukuinum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qingtoukuinum.setGeometry(QtCore.QRect(130, 90, 40, 20))
        self.qingtoukuinum.setObjectName("qingtoukuinum")
        self.qingtoukuinum.setText("0")
        self.qingtoukuinum.setAlignment(QtCore.Qt.AlignCenter)
        self.qingtoukuinum.setFixedWidth(40)
        self.qingtoukuinum.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")


        # 红方头盔
        self.hongfangtoukui = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hongfangtoukui.setGeometry(QtCore.QRect(205, 85, 30, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.hongfangtoukui.setFont(font)
        self.hongfangtoukui.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangtoukui.setObjectName("hongfangtoukui")
        self.hongfangtoukui.setText("")
        self.hongfangtoukui.setStyleSheet("background-color:#FFE05E;border-color:#FFE05E ;border-radius:15px")

        self.hongtoukuinum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hongtoukuinum.setGeometry(QtCore.QRect(265, 90, 40, 20))
        self.hongtoukuinum.setObjectName("hongtoukuinum")
        self.hongtoukuinum.setText("0")
        self.hongtoukuinum.setAlignment(QtCore.Qt.AlignCenter)
        self.hongtoukuinum.setFixedWidth(40)
        self.hongtoukuinum.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")



        # 护具这两个字
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(5, 150, 40, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("护具")
        self.label.setStyleSheet("border:0px")

        # 青方护具
        self.qingfanghuju = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qingfanghuju.setGeometry(QtCore.QRect(70, 140, 40, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.qingfanghuju.setFont(font)
        self.qingfanghuju.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfanghuju.setObjectName("qingfanghuju")
        self.qingfanghuju.setText("")
        self.qingfanghuju.setStyleSheet(
            "background-color:#FFE05E;border-color:#FFE05E ;border-radius:0px")

        self.qinghujunum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qinghujunum.setGeometry(QtCore.QRect(130, 150, 40, 20))
        self.qinghujunum.setObjectName("qinghujunum")
        self.qinghujunum.setText("0")
        self.qinghujunum.setAlignment(QtCore.Qt.AlignCenter)
        self.qinghujunum.setFixedWidth(40)
        self.qinghujunum.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")





        # 红方护具
        self.hongfanghuju = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hongfanghuju.setGeometry(QtCore.QRect(203, 140, 40, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.hongfanghuju.setFont(font)
        self.hongfanghuju.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfanghuju.setObjectName("hongfanghuju")
        self.hongfanghuju.setText("")
        self.hongfanghuju.setStyleSheet("background-color:#FFE05E;border-color:#FFE05E ;border-radius:0px")

        self.honghujunum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.honghujunum.setGeometry(QtCore.QRect(265, 150, 40, 20))
        self.honghujunum.setObjectName("honghujunum")
        self.honghujunum.setText("0")
        self.honghujunum.setAlignment(QtCore.Qt.AlignCenter)
        self.honghujunum.setFixedWidth(40)
        self.honghujunum.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")


        # 得分区间
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(40, 220, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("得分区间")
        self.label.setStyleSheet("border:0px")
        self.qingfanghujufirst_lizhi = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qingfanghujufirst_lizhi.setGeometry(QtCore.QRect(120, 220, 40, 20))
        self.qingfanghujufirst_lizhi.setObjectName("hongfanghujufirst_lizhi")
        self.qingfanghujufirst_lizhi.setText("0")
        self.qingfanghujufirst_lizhi.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfanghujufirst_lizhi.setFixedWidth(40)
        self.qingfanghujufirst_lizhi.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")

        # 设备组号
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(160, 220, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("设备组号")
        self.label.setStyleSheet("border:0px")
        self.shebeizunum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.shebeizunum.setGeometry(QtCore.QRect(230, 220, 40, 20))
        self.shebeizunum.setObjectName("shebeizunum")
        self.shebeizunum.setText("0")
        self.shebeizunum.setAlignment(QtCore.Qt.AlignCenter)
        self.shebeizunum.setFixedWidth(40)
        self.shebeizunum.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")



        #底部按钮集
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(25, 620, 1280, 140))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setStyleSheet(
            "border-width: 1px;border-style: solid;border-color: #767475 ;border-radius:10px")


        #青胜
        self.qingsheng_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.qingsheng_bt.setGeometry(QtCore.QRect(20, 10, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.qingsheng_bt.setFont(font)
        self.qingsheng_bt.setStyleSheet("QPushButton{color:#fff}"
                                      "QPushButton:hover{color:red}"
                                      "QPushButton{background-color:#6EBAF8}"
                                      "QPushButton{border:2px}"
                                      "QPushButton{border-radius:5px}"
                                      "QPushButton{padding:2px 4px}"

                                      )
        self.qingsheng_bt.setObjectName("qingsheng_bt")
        self.qingsheng_bt.setText("青 胜")

        #青扣分
        self.qingkoufen_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.qingkoufen_bt.setGeometry(QtCore.QRect(200, 10, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.qingkoufen_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.qingkoufen_bt.setStyleSheet("QPushButton{color:#fff}"
                                        "QPushButton:hover{color:red}"
                                        "QPushButton{background-color:#6EBAF8}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:5px}"
                                        "QPushButton{padding:2px 4px}"

                                        )
        self.qingkoufen_bt.setObjectName("qingkoufen_bt")
        self.qingkoufen_bt.setText("扣分")

        #青方扣分+
        self.qingkoufenjia_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.qingkoufenjia_bt.setGeometry(QtCore.QRect(155, 10, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.qingkoufenjia_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.qingkoufenjia_bt.setStyleSheet("QPushButton{color:#fff}"
                                         "QPushButton:hover{color:red}"
                                         "QPushButton{background-color:#6EBAF8}"
                                         "QPushButton{border:2px}"
                                         "QPushButton{border-radius:5px}"
                                         "QPushButton{padding:2px 4px}"

                                         )
        self.qingkoufenjia_bt.setObjectName("qingkoufenjia_bt")
        self.qingkoufenjia_bt.setText("+")

        #青方扣分-
        self.qingkoufenjian_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.qingkoufenjian_bt.setGeometry(QtCore.QRect(285, 10, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.qingkoufenjian_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.qingkoufenjian_bt.setStyleSheet("QPushButton{color:#fff}"
                                         "QPushButton:hover{color:red}"
                                         "QPushButton{background-color:#6EBAF8}"
                                         "QPushButton{border:2px}"
                                         "QPushButton{border-radius:5px}"
                                         "QPushButton{padding:2px 4px}"

                                         )
        self.qingkoufenjian_bt.setObjectName("qingkoufenjian_bt")
        self.qingkoufenjian_bt.setText("-")


        #青得分
        self.qingdefen_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.qingdefen_bt.setGeometry(QtCore.QRect(100, 70, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.qingdefen_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.qingdefen_bt.setStyleSheet("QPushButton{color:#fff}"
                                        "QPushButton:hover{color:red}"
                                        "QPushButton{background-color:#6EBAF8}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:5px}"
                                        "QPushButton{padding:2px 4px}"

                                        )
        self.qingdefen_bt.setObjectName("qingdefen_bt")
        self.qingdefen_bt.setText("得分")

        #青方得分+
        self.qingdefenjia_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.qingdefenjia_bt.setGeometry(QtCore.QRect(55, 70, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.qingdefenjia_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.qingdefenjia_bt.setStyleSheet("QPushButton{color:#fff}"
                                         "QPushButton:hover{color:red}"
                                         "QPushButton{background-color:#6EBAF8}"
                                         "QPushButton{border:2px}"
                                         "QPushButton{border-radius:5px}"
                                         "QPushButton{padding:2px 4px}"

                                         )
        self.qingdefenjia_bt.setObjectName("qingdefenjia_bt")
        self.qingdefenjia_bt.setText("+")

        #青方得分-
        self.qingdefenjian_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.qingdefenjian_bt.setGeometry(QtCore.QRect(185, 70, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.qingdefenjian_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.qingdefenjian_bt.setStyleSheet("QPushButton{color:#fff}"
                                         "QPushButton:hover{color:red}"
                                         "QPushButton{background-color:#6EBAF8}"
                                         "QPushButton{border:2px}"
                                         "QPushButton{border-radius:5px}"
                                         "QPushButton{padding:2px 4px}"

                                         )
        self.qingdefenjian_bt.setObjectName("qingdefenjian_bt")
        self.qingdefenjian_bt.setText("-")

        #清除
        self.qingchu_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.qingchu_bt.setGeometry(QtCore.QRect(260, 70, 80, 50))
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

        self.bisaipre_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bisaipre_bt.setGeometry(QtCore.QRect(440, 25, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bisaipre_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.bisaipre_bt.setStyleSheet("QPushButton{color:#000}"
                                        "QPushButton:hover{color:red}"
                                        "QPushButton{background-color:#FFE05E}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:5px}"
                                        "QPushButton{padding:2px 4px}"

                                        )
        self.bisaipre_bt.setObjectName("bisaipre_bt")
        self.bisaipre_bt.setText("上一场")

        # 开始
        self.kaishi_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.kaishi_bt.setGeometry(QtCore.QRect(580, 20, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.kaishi_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.kaishi_bt.setStyleSheet("QPushButton{color:#000}"
                                      "QPushButton:hover{color:red}"
                                      "QPushButton{background-color:#FFE05E}"
                                      "QPushButton{border:2px}"
                                      "QPushButton{border-radius:10px}"
                                      "QPushButton{padding:2px 4px}"

                                      )
        self.kaishi_bt.setObjectName("kaishi_bt")
        self.kaishi_bt.setText("开 始")

        # <
        # self.bisaipre_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        # self.bisaipre_bt.setGeometry(QtCore.QRect(550, 25, 40, 40))
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.bisaipre_bt.setFont(font)
        # font.setFamily("Arial Black")
        # font.setBold(True)
        # self.bisaipre_bt.setStyleSheet("QPushButton{color:#000}"
        #                                "QPushButton:hover{color:red}"
        #                                "QPushButton{background-color:#FFE05E}"
        #                                "QPushButton{border:2px}"
        #                                "QPushButton{border-radius:5px}"
        #                                "QPushButton{padding:2px 4px}"
        #
        #                                )
        # self.bisaipre_bt.setObjectName("bisaipre_bt")
        # self.bisaipre_bt.setText("<")

        # >
        self.bisainext_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.bisainext_bt.setGeometry(QtCore.QRect(720, 25, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bisainext_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.bisainext_bt.setStyleSheet("QPushButton{color:#000}"
                                        "QPushButton:hover{color:red}"
                                        "QPushButton{background-color:#FFE05E}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:5px}"
                                        "QPushButton{padding:2px 4px}"

                                        )
        self.bisainext_bt.setObjectName("bisainext_bt")
        self.bisainext_bt.setText("下一场")

        #刷新
        self.shuaxin_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.shuaxin_bt.setGeometry(QtCore.QRect(840, 25, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.shuaxin_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.shuaxin_bt.setStyleSheet("QPushButton{color:#000}"
                                        "QPushButton:hover{color:red}"
                                        "QPushButton{background-color:#FFE05E}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:5px}"
                                        "QPushButton{padding:2px 4px}"

                                        )
        self.shuaxin_bt.setObjectName("shuaxin_bt")
        self.shuaxin_bt.setText("刷新")






        #测试
        self.ceshi_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ceshi_bt.setGeometry(QtCore.QRect(560, 80, 80, 40))
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
        self.ceshi_bt.setText("测 试")

        # 连接
        self.lianjie_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.lianjie_bt.setGeometry(QtCore.QRect(675, 80, 80, 40))
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
        self.lianjie_bt.setText("连 接")

        #更改
        self.genggai_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.genggai_bt.setGeometry(QtCore.QRect(785, 80, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.genggai_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.genggai_bt.setStyleSheet("QPushButton{color:#000}"
                                      "QPushButton:hover{color:red}"
                                      "QPushButton{background-color:#FFE05E}"
                                      "QPushButton{border:2px}"
                                      "QPushButton{border-radius:10px}"
                                      "QPushButton{padding:2px 4px}"

                                      )
        self.genggai_bt.setObjectName("genggai_bt")
        self.genggai_bt.setText("更 改")

        # 设置
        self.shezhi_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.shezhi_bt.setGeometry(QtCore.QRect(450, 80, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.shezhi_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.shezhi_bt.setStyleSheet("QPushButton{color:#000}"
                                    "QPushButton:hover{color:red}"
                                    "QPushButton{background-color:#FFE05E}"
                                    "QPushButton{border:2px}"
                                    "QPushButton{border-radius:10px}"
                                    "QPushButton{padding:2px 4px}"

                                    )
        self.shezhi_bt.setObjectName("shezhi_bt")
        self.shezhi_bt.setText("设 置")



        # 红胜
        self.hongsheng_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hongsheng_bt.setGeometry(QtCore.QRect(1160, 10, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.hongsheng_bt.setFont(font)
        self.hongsheng_bt.setStyleSheet("QPushButton{color:#fff}"
                                        "QPushButton:hover{color:yellow}"
                                        "QPushButton{background-color:#AC1213}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:5px}"
                                        "QPushButton{padding:2px 4px}"

                                        )
        self.hongsheng_bt.setObjectName("hongsheng_bt")
        self.hongsheng_bt.setText("红 胜")

        # 红扣分
        self.hongkoufen_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hongkoufen_bt.setGeometry(QtCore.QRect(1000, 10, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hongkoufen_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.hongkoufen_bt.setStyleSheet("QPushButton{color:#fff}"
                                         "QPushButton:hover{color:yellow}"
                                         "QPushButton{background-color:#AC1213}"
                                         "QPushButton{border:2px}"
                                         "QPushButton{border-radius:5px}"
                                         "QPushButton{padding:2px 4px}"

                                         )
        self.hongkoufen_bt.setObjectName("hongkoufen_bt")
        self.hongkoufen_bt.setText("扣分")

        # 红方扣分+
        self.hongkoufenjia_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hongkoufenjia_bt.setGeometry(QtCore.QRect(1085, 10, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hongkoufenjia_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.hongkoufenjia_bt.setStyleSheet("QPushButton{color:#fff}"
                                            "QPushButton:hover{color:yellow}"
                                            "QPushButton{background-color:#AC1213}"
                                            "QPushButton{border:2px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"

                                            )
        self.hongkoufenjia_bt.setObjectName("hongkoufenjia_bt")
        self.hongkoufenjia_bt.setText("+")

        # 红方扣分-
        self.hongkoufenjian_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hongkoufenjian_bt.setGeometry(QtCore.QRect(955, 10, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hongkoufenjian_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.hongkoufenjian_bt.setStyleSheet("QPushButton{color:#fff}"
                                             "QPushButton:hover{color:yellow}"
                                             "QPushButton{background-color:#AC1213}"
                                             "QPushButton{border:2px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"

                                             )
        self.hongkoufenjian_bt.setObjectName("hongkoufenjian_bt")
        self.hongkoufenjian_bt.setText("-")

        # 红得分
        self.hongdefen_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hongdefen_bt.setGeometry(QtCore.QRect(1100, 70, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hongdefen_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.hongdefen_bt.setStyleSheet("QPushButton{color:#fff}"
                                        "QPushButton:hover{color:yellow}"
                                        "QPushButton{background-color:#AC1213}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:5px}"
                                        "QPushButton{padding:2px 4px}"

                                        )
        self.hongdefen_bt.setObjectName("hongdefen_bt")
        self.hongdefen_bt.setText("得分")

        # 红方得分+
        self.hongdefenjia_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hongdefenjia_bt.setGeometry(QtCore.QRect(1185, 70, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hongdefenjia_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.hongdefenjia_bt.setStyleSheet("QPushButton{color:#fff}"
                                           "QPushButton:hover{color:yellow}"
                                           "QPushButton{background-color:#AC1213}"
                                           "QPushButton{border:2px}"
                                           "QPushButton{border-radius:5px}"
                                           "QPushButton{padding:2px 4px}"

                                           )
        self.hongdefenjia_bt.setObjectName("hongdefenjia_bt")
        self.hongdefenjia_bt.setText("+")

        # 红方得分-
        self.hongdefenjian_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hongdefenjian_bt.setGeometry(QtCore.QRect(1055, 70, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.hongdefenjian_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.hongdefenjian_bt.setStyleSheet("QPushButton{color:#fff}"
                                            "QPushButton:hover{color:yellow}"
                                            "QPushButton{background-color:#AC1213}"
                                            "QPushButton{border:2px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"

                                            )
        self.hongdefenjian_bt.setObjectName("hongdefenjian_bt")
        self.hongdefenjian_bt.setText("-")

        # 计时
        self.jishi_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.jishi_bt.setGeometry(QtCore.QRect(940, 70, 80, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.jishi_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.jishi_bt.setStyleSheet("QPushButton{color:#fff}"
                                      "QPushButton:hover{color:red}"
                                      "QPushButton{background-color:#FE8742}"
                                      "QPushButton{border:2px}"
                                      "QPushButton{border-radius:10px}"
                                      "QPushButton{padding:2px 4px}"

                                      )
        self.jishi_bt.setObjectName("jishi_bt")
        self.jishi_bt.setText("计时")






        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)

        #计时
        self.timer2 = QTimer()
        self.timer2.timeout.connect(self.on_timeout2)

        # 按钮点击事件集

        self.kaishi_bt.clicked.connect(self.start)
        self.shezhi_bt.clicked.connect(self.showsetting)
        # 青方得分+-
        self.qingdefenjia_bt.clicked.connect(self.qingdefenjia)
        self.qingdefenjian_bt.clicked.connect(self.qingdefenjian)
        # 青方扣分+-
        self.qingkoufenjia_bt.clicked.connect(self.qingkoufenjia)
        self.qingkoufenjian_bt.clicked.connect(self.qingkoufenjian)

        # 红方得分+-
        self.hongdefenjia_bt.clicked.connect(self.hongdefenjia)
        self.hongdefenjian_bt.clicked.connect(self.hongdefenjian)
        # 红方扣分+-
        self.hongkoufenjia_bt.clicked.connect(self.hongkoufenjia)
        self.hongkoufenjian_bt.clicked.connect(self.hongkoufenjian)
        #红胜
        self.qingsheng_bt.clicked.connect(self.qingsheng)
        #红败
        self.hongsheng_bt.clicked.connect(self.hongsheng)
        #清除
        self.qingchu_bt.clicked.connect(self.qingchu)

        #刷新
        self.shuaxin_bt.clicked.connect(self.shuaxin)

        self.ceshi_bt.clicked.connect(self.ceshi)

        self.jishi_bt.clicked.connect(self.jishi)

        self.dafenqiceshi_bt.clicked.connect(self.dafenqiceshi)

        self.genggai_bt.clicked.connect(self.genggai)

        self.lianjie_bt.clicked.connect(self.lianjie)
        self.bisainext_bt.clicked.connect(self.bisainext)
        self.bisaipre_bt.clicked.connect(self.bisaipre)
        #判断是暂停还是开始
        self.flag=True
        #判断是否是第一次点击开始
        self.isfirst = True

        #判断是否在倒计时内击打
        self.isfight = False

        self.qinglastscore=0
        self.honglastscore=0

        self.ishujufirst_hong=True
        self.ishujufirst_qing = True

        self.dataFlag2 = False

        #双方踢腿测试
        self.istest=False
        self.isqingfangtestfinsh=False
        self.ishongfangtestfinsh=False
        self.isqingtoutestfinsh = False
        self.ishongtoutestfinsh = False

        self.firstlizhi_qing=0
        self.firstlizhi_hong=0

        self.isdafenqiceshi=True

        self.index=0
        self.issound=True
        self.qingfanghujudefentime=0
        self.hongfanghujudefentime=0
        self.qingfangtoukuidefentime = 0
        self.hongfangtoukuidefentime = 0
        self.hongfanglizhi = ""
        self.qingfanglizhi = ""

        self.isjiashi=False
        self.t1=0

        self.isxiuxi=True
        self.isxiuxinow=False
         # music_path = r'music\yifen.wav'
         # self.sound(music_path)

    def sound(self,path):
        _thread.start_new_thread(playsound, (path,))

    def shuaxin(self):
        QApplication.processEvents()

    def genggai(self):
        sql = "update bisaixinxi set bisaizhuangtai='等待中' ,qingfangdefen='0',hongfangdefen='0',qingfangkoufen='0',hongfangkoufen='0',qingfangdefen1='0',hongfangdefen1='0',qingfangkoufen1='0',hongfangkoufen1='0',qingfangdefen2='0',hongfangdefen2='0',qingfangkoufen2='0',hongfangkoufen2='0',qingfangdefen3='0',hongfangdefen3='0',qingfangkoufen3='0',hongfangkoufen3='0',qingfangdefen4='0',hongfangdefen4='0',qingfangkoufen4='0',hongfangkoufen4='0'  where bisaixuhao=%s" % (

            gl.get_value('bisaixuhao'))
        # print(sql)
        # self.stat.update(sql)
        _thread.start_new_thread(self.stat.update, (sql,))
        self.qingchu()




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
                      "from bisaixinxi where changdi='%s' and changdihao<'%s'  order by changdihao DESC limit 1" % (
                          self.changdi.text(), self.changdihao.text())
                self.yundongyuan = self.stat.fetchone(sql)
                if(self.yundongyuan==None):
                    qw = QtWidgets.QWidget()
                    QMessageBox.warning(qw, '错误', "没有上一场", QMessageBox.Ok)
                else:
                    gl.set_value('changdihao', self.yundongyuan[1])
                    gl.set_value('bisaixuhao', self.yundongyuan[0])
                    gl.set_value('lunci',self.yundongyuan[9])
                    gl.set_value('jibie',self.yundongyuan[6])
                    # print(self.yundongyuan)
                    self.qingfangname.setText(self.yundongyuan[2])
                    self.qingfangdanwei.setText(self.yundongyuan[3])
                    self.hongfangname.setText(self.yundongyuan[4])
                    self.hongfangdanwei.setText(self.yundongyuan[5])
                    self.lunci.setText(self.yundongyuan[9])
                    self.jibie.setText(gl.get_value('jibie'))
                    self.bisaizhuangtai.setText(self.yundongyuan[10])


                    sql = "select hongfangdefen,hongfangkoufen,hongfangdefen1,hongfangkoufen1,hongfangdefen2,hongfangkoufen2,hongfangdefen3,hongfangkoufen3,hongfangdefen4,hongfangkoufen4," \
                          "qingfangdefen,qingfangkoufen,qingfangdefen1,qingfangkoufen1,qingfangdefen2,qingfangkoufen2,qingfangdefen3,qingfangkoufen3,qingfangdefen4,qingfangkoufen4 from bisaixinxi where changdi='%s' and changdihao<'%s'  order by changdihao desc limit 1" % (
                              self.changdi.text(), self.changdihao.text())
                    # print(sql)
                    self.bisaijilu = self.stat.fetchone(sql)
                    # print(self.bisaijilu)
                    for i in self.bisaijilu:
                        if(i==None):
                            print("空")
                    self.changdihao.setText(self.yundongyuan[1])
                    if(self.bisaijilu[0]==None or self.bisaijilu[0]==''):
                        self.hongfangzongfen.setText("0")
                    else:
                        self.hongfangzongfen.setText(self.bisaijilu[0])
                    if(self.bisaijilu[1]==None or self.bisaijilu[1]==''):
                        self.hongfangkoufen.setText("0")
                    else:
                        self.hongfangkoufen.setText(self.bisaijilu[1])
                    if (self.bisaijilu[2] == None or self.bisaijilu[2] ==  ''):
                        self.hong_game_1_defen.setText("0")
                    else:
                        self.hong_game_1_defen.setText(self.bisaijilu[2])
                    if (self.bisaijilu[3] == None or self.bisaijilu[3]== ''):
                        self.hong_game_1_koufen.setText("0")
                    else:
                        self.hong_game_1_koufen.setText(self.bisaijilu[3])
                    if (self.bisaijilu[4] == None or self.bisaijilu[4] == ''):
                        self.hong_game_2_defen.setText("0")
                    else:
                        self.hong_game_2_defen.setText(self.bisaijilu[4])
                    if (self.bisaijilu[5] == None or self.bisaijilu[5] ==  ''):
                        self.hong_game_2_koufen.setText("0")
                    else:
                        self.hong_game_2_koufen.setText(self.bisaijilu[5])
                    if (self.bisaijilu[6] == None or self.bisaijilu[6] == ''):
                        self.hong_game_3_defen.setText("0")
                    else:
                        self.hong_game_3_defen.setText(self.bisaijilu[6])
                    if (self.bisaijilu[7] == None or self.bisaijilu[7] == ''):
                        self.hong_game_3_koufen.setText("0")
                    else:
                        self.hong_game_3_koufen.setText(self.bisaijilu[7])
                    if (self.bisaijilu[8] == None or self.bisaijilu[8] == ''):
                        self.hong_game_4_defen.setText("0")
                    else:
                        self.hong_game_4_defen.setText(self.bisaijilu[8])
                    if (self.bisaijilu[9] == None or self.bisaijilu[9] == ''):
                        self.hong_game_4_koufen.setText("0")
                    else:
                        self.hong_game_4_koufen.setText(self.bisaijilu[9])
                    if (self.bisaijilu[10] == None or self.bisaijilu[10] == '' ):
                        self.qingfangzongfen.setText("0")
                    else:
                        self.qingfangzongfen.setText(self.bisaijilu[10])
                    if (self.bisaijilu[11] ==None or self.bisaijilu[11] ==''):
                        self.qingfangkoufen.setText("0")
                    else:
                        self.qingfangkoufen.setText(self.bisaijilu[11])
                    if (self.bisaijilu[12] == None or self.bisaijilu[12] == ''):
                        self.qing_game_1_defen.setText("0")
                    else:
                        self.qing_game_1_defen.setText(self.bisaijilu[12])
                    if (self.bisaijilu[13] == None or self.bisaijilu[13] ==''):
                        self.qing_game_1_koufen.setText("0")
                    else:
                        self.qing_game_1_koufen.setText(self.bisaijilu[13])
                    if (self.bisaijilu[14] == None or self.bisaijilu[14] ==''):
                        self.qing_game_2_defen.setText("0")
                    else:
                        self.qing_game_2_defen.setText(self.bisaijilu[14])
                    if (self.bisaijilu[15] == None or self.bisaijilu[15] ==''):
                        self.qing_game_2_koufen.setText("0")
                    else:
                        self.qing_game_2_koufen.setText(self.bisaijilu[15])
                    if (self.bisaijilu[16] == None or self.bisaijilu[16] ==''):
                        self.qing_game_3_defen.setText("0")
                    else:
                        self.qing_game_3_defen.setText(self.bisaijilu[16])
                    if (self.bisaijilu[17] == None or self.bisaijilu[17] ==''):
                        self.qing_game_3_koufen.setText("0")
                    else:
                        self.qing_game_3_koufen.setText(self.bisaijilu[17])
                    if (self.bisaijilu[18] == None or self.bisaijilu[18] ==''):
                        self.qing_game_4_defen.setText("0")
                    else:
                        self.qing_game_4_defen.setText(self.bisaijilu[18])
                    if (self.bisaijilu[19] == None or self.bisaijilu[19] ==''):
                        self.qing_game_4_koufen.setText("0")
                    else:
                        self.qing_game_4_koufen.setText(self.bisaijilu[19])


            # else:
            #     qw = QtWidgets.QWidget()
            #     QMessageBox.warning(qw, '错误', "没有上一场", QMessageBox.Ok)

    def bisainext(self):
        # self.li=gl.get_value("changci")
        # if(self.li==[]):
        #     qw = QtWidgets.QWidget()
        #     QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)

            qw = QtWidgets.QWidget()
            reply=QMessageBox.warning(qw, '警告', "确定下一场？", QMessageBox.Yes | QMessageBox.No)
            if(reply==QMessageBox.Yes):
                # if(self.index<len(self.li)):
                #     self.qingchu()
                #     self.index +=1
                #     self.changdihao.setText(self.li[self.index])
                #     gl.set_value('changdihao',self.changdihao.text())
                    self.qingchu()




                    sql = "select bisaixuhao,changdihao,qingfangxinming,qingfangdanwei,hongfangxinming,hongfangdanwei,jibie,qingfangbianhao,hongfangbianhao,bisaizhuangtai,lunci " \
                          "from bisaixinxi where changdi='%s' and changdihao>'%s' and bisaizhuangtai='等待中' order by changdihao ASC LIMIT 1" % (
                    self.changdi.text(), self.changdihao.text())
                    self.yundongyuan = self.stat.fetchone(sql)
                    if(self.yundongyuan == None):
                        qw = QtWidgets.QWidget()
                        QMessageBox.warning(qw, '错误', "该场地比赛已全部结束", QMessageBox.Ok)
                    else:
                        gl.set_value('changdihao',self.yundongyuan[1])
                        gl.set_value('bisaixuhao',self.yundongyuan[0])
                        gl.set_value('lunci',self.yundongyuan[10])
                        gl.set_value('jibie',self.yundongyuan[6])

                        # sql = "update dangqianbisai set changdihao=%s,daojishi=%s,bisaizhuangtai=%s,jishi=%s,dangqianju=%s,bisaixuhao=%s,defenqujian=%s " % (
                        # gl.get_value('changdihao'), self.daojishi, 0, gl.get_value('jishitime'), 0,
                        # gl.get_value('bisaixuhao'),gl.get_value('defenqujian'))
                        # print(sql)

                        # _thread.start_new_thread(self.stat.update, (sql,))


                        #
                        # sql = "DELETE FROM dangqianbisai WHERE id=1"
                        # print(sql)
                        # _thread.start_new_thread(self.stat.delete, (sql,))
                        # time.sleep(1)
                        # # self.stat.delete(sql)
                        #
                        # sql = "insert into dangqianbisai (id,changdihao,daojishi,bisaizhuangtai,jishi,dangqianju,bisaixuhao,defenqujian) values (%s,%s,%s,%s,%s,%s,%s,%s)" % (
                        # 1, gl.get_value('changdihao'), self.daojishi, 0, gl.get_value('jishitime'), 0, gl.get_value('bisaixuhao'),
                        # gl.get_value('defenqujian'))
                        # print(sql)
                        # _thread.start_new_thread(self.stat.insert, (sql,))
                        # print(self.yundongyuan)
                        self.qingfangname.setText(self.yundongyuan[2])
                        self.qingfangdanwei.setText(self.yundongyuan[3])
                        self.hongfangname.setText(self.yundongyuan[4])
                        self.hongfangdanwei.setText(self.yundongyuan[5])
                        self.changdihao.setText(self.yundongyuan[1])
                        self.lunci.setText(self.yundongyuan[10])
                        self.jibie.setText(gl.get_value('jibie'))
                        self.bisaizhuangtai.setText('')




    def lianjie(self):
        if (self.isfirst):
            # 判断是否已经设置比赛信息
            if (gl.get_value('bisaijushu') == None):
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '错误', "请先设置比赛信息", QMessageBox.Ok)

            else:
                # 比赛局数
                self.gamenums = gl.get_value('bisaijushu')
                self.gamenumsnow = int(self.gamenums)
                self.gamenum = int(gl.get_value('dangqianju'))
                # print('当前局')
                # print(self.gamenum)
                self.setgamenum.setText("第" + str(self.gamenum) + "局")
                # 比赛裁判数
                self.caipanshu = self.changcainum.text()
                # 获取比赛局时
                self.daojishi = gl.get_value('jushi')
                self.daojishinow = int(gl.get_value('dangqianshijian'))

                self.jiashijushi = gl.get_value('jiashijushi')
                self.setdaojishi.setText(str(datetime.timedelta(seconds=int(self.daojishinow)))[2:])
                # print(self.daojishi)
                # 比赛休息时间
                self.xiuxitime = gl.get_value('xiuxitime')
                self.xiuxitimenow = int(self.xiuxitime)
                # print(self.xiuxitime)

                # #当前局
                # self.dangqianju=gl.get_value('dangqianju')
                #
                # #当前时间
                # self.dangqianshijian=gl.get_value('dangqianshijian')
                #
                # print(self.dangqianju)
                # print(self.dangqianshijian)

                # 计时时间
                self.jishitime = gl.get_value('jishitime')
                self.jishitimenow = int(self.jishitime)

                # 有效得分
                self.youxiaodefen = int(gl.get_value('youxiaodefen'))
                # 最大分差
                self.maxfencha = int(gl.get_value('zuidafencha'))

                # 得分区间
                self.defenqujian = int(gl.get_value('defenqujian'))

                # 串口
                # self.chuankou = gl.get_value('chuankou')
                # print(self.chuankou)

                # 裁判时差
                self.caipanshicha = int(gl.get_value('caipanshicha'))

                # 组号
                # self.zunum = int(gl.get_value('hujunum'))

                # 设置青方信息
                self.qingfangdanwei.setText(gl.get_value('qingfangdanwei'))
                # print(gl.get_value('qingfangdanwei'))
                self.qingfangname.setText(gl.get_value('qingfangname'))
                # print(gl.get_value('qingfangname'))

                # 设置红方信息
                self.hongfangdanwei.setText(gl.get_value('hongfangdanwei'))
                # print(gl.get_value('hongfangname'))
                # print(gl.get_value('hongfangdanwei'))
                self.hongfangname.setText(gl.get_value('hongfangname'))

                self.qingfanghujufirst_lizhi.setText(str(self.defenqujian))

                # 允许扣分数，超过则对方胜
                self.koufenshu = int(gl.get_value('koufenshu'))
                # 加时赛得分，达到即胜
                self.jiashizuidadefen = int(gl.get_value('jiashizuidadefen'))
                # 加时赛允许扣分数，超过则对方胜
                self.jiashikoufenshu = int(gl.get_value('jiashikoufenshu'))

                self.lunci.setText(gl.get_value('lunci'))

                self.changdi.setText(gl.get_value('changdi'))
                self.changdihao.setText(gl.get_value('changdihao'))
                self.jibie.setText(gl.get_value('jibie'))

                # 设置设备号
                self.qingtoukuinum.setText(gl.get_value('qingtoukuinum'))
                self.hongtoukuinum.setText(gl.get_value('hongtoukuinum'))
                self.qinghujunum.setText(gl.get_value('qinghujunum'))
                self.honghujunum.setText(gl.get_value('honghujunum'))

                #设置设备组号
                self.shebeizunum.setText(gl.get_value('hujuzunum'))

                self.isfirst = False
                self.istest = False
                self.t1 = 0

                sql = "select bisaixuhao,changdihao,qingfangxinming,qingfangdanwei,hongfangxinming,hongfangdanwei,jibie,qingfangbianhao,hongfangbianhao from bisaixinxi where changdi='%s' and changdihao='%s' and bisaizhuangtai='等待中' order by changdihao" % (
                    self.changdi.text(), self.changdihao.text())
                # print(sql)
                self.yundongyuan = self.stat.fetchone(sql)
                # print(self.yundongyuan)

                # 设置青方信息
                self.qingfangdanwei.setText(self.yundongyuan[3])
                self.qingfangname.setText(self.yundongyuan[2])

                # 设置红方信息
                self.hongfangdanwei.setText(self.yundongyuan[5])
                self.hongfangname.setText(self.yundongyuan[4])

                self.qingfanghujufirst_lizhi.setText(str(self.defenqujian))

                self.qingfangtoukuirotatetime = 0
                self.hongfangtoukuirotatetime = 0

                self.twoPointsTimeNowqing=None
                self.twoPointsTimeNowhong=None

                sql = "select id from dangqianbisai where changdi='%s'" % (self.changdi.text())
                if (self.stat.fetchone(sql)):
                    sql = "DELETE FROM dangqianbisai WHERE changdi='%s'" % (self.changdi.text())
                    # print(sql)
                    _thread.start_new_thread(self.stat.delete, (sql,))
                    time.sleep(1)
                    # self.stat.delete(sql)

                sql = "insert into dangqianbisai (id,changdi,changdihao,daojishi,bisaizhuangtai,jishi,dangqianju,bisaixuhao,defenqujian) values (%s,'%s',%s,%s,%s,%s,%s,%s,%s)" % (
                gl.get_value('bisaixuhao'), self.changdi.text(), gl.get_value('changdihao'), self.daojishi, 0,
                gl.get_value('jishitime'), 0, gl.get_value('bisaixuhao'), gl.get_value('defenqujian'))
                print(sql)
                _thread.start_new_thread(self.stat.insert, (sql,))
                self.stat.insert(sql)

                # print(gl.get_value('qinghujunum'))
                # print(gl.get_value('honghujunum'))
                # print(gl.get_value('hongtoukuinum'))
                # print(gl.get_value('qingtoukuinum'))
                try:
                    print('开始连接串口')
                    import serial.tools.list_ports
                    port_list = list(serial.tools.list_ports.comports())
                    if len(port_list) == 0:
                        qw = QtWidgets.QWidget()
                        QMessageBox.warning(qw, '错误', "未找到串口设备", QMessageBox.Ok)
                    else:
                        for i in range(0, len(port_list)):
                            print(str(port_list[i])[:4])

                    x = serial.Serial(str(port_list[0])[:4], "115200")

                    print(x)
                    self.dataFlag = True
                    _thread.start_new_thread(self.getData, (x,))

                    # 测试页面刷新
                    # _thread.start_new_thread(self.getData2,(x,)    )
                    self.lianjie_bt.setText('已连接')
                except:
                    self.isfirst = True
                    qw = QtWidgets.QWidget()
                    QMessageBox.warning(qw, '错误', "连接串口失败，请检查串口号和波特率是否正确", QMessageBox.Ok)






        else:
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "已成功连接串口，不可重复连接", QMessageBox.Ok)
    def dafenqiceshi(self):

        if(self.isdafenqiceshi):
            self.dataFlag2 = True
            self.dafenqiceshi_bt.setText("完 成")
            self.isdafenqiceshi=False
        else:
            self.isdafenqiceshi=True
            self.dafenqiceshi_bt.setText("测 试")
            self.qingfangzongfen.setText("0")
            self.qingfangkoufen.setText("0")
            self.qingfanghujufirst_lizhi.setText("0")

            self.changcai_1_qing_1.setText("0")
            self.changcai_1_qing_2.setText("0")
            self.changcai_1_qing_3.setText("0")
            self.changcai_1_qing_4.setText("0")
            self.changcai_1_qing_5.setText("0")
            self.changcai_2_qing_1.setText("0")
            self.changcai_2_qing_2.setText("0")
            self.changcai_2_qing_3.setText("0")
            self.changcai_2_qing_4.setText("0")
            self.changcai_2_qing_5.setText("0")
            self.changcai_3_qing_1.setText("0")
            self.changcai_3_qing_2.setText("0")
            self.changcai_3_qing_3.setText("0")
            self.changcai_3_qing_4.setText("0")
            self.changcai_3_qing_5.setText("0")

            self.qing_game_1_koufen.setText("0")
            self.qing_game_1_defen.setText("0")

            self.qing_game_2_koufen.setText("0")
            self.qing_game_2_defen.setText("0")

            self.qing_game_3_koufen.setText("0")
            self.qing_game_3_defen.setText("0")

            self.qing_game_4_koufen.setText("0")
            self.qing_game_4_defen.setText("0")

            self.hongfangzongfen.setText("0")
            self.hongfangkoufen.setText("0")

            self.changcai_1_hong_1.setText("0")
            self.changcai_1_hong_2.setText("0")
            self.changcai_1_hong_3.setText("0")
            self.changcai_1_hong_4.setText("0")
            self.changcai_1_hong_5.setText("0")
            self.changcai_2_hong_1.setText("0")
            self.changcai_2_hong_2.setText("0")
            self.changcai_2_hong_3.setText("0")
            self.changcai_2_hong_4.setText("0")
            self.changcai_2_hong_5.setText("0")
            self.changcai_3_hong_1.setText("0")
            self.changcai_3_hong_2.setText("0")
            self.changcai_3_hong_3.setText("0")
            self.changcai_3_hong_4.setText("0")
            self.changcai_3_hong_5.setText("0")

            self.hong_game_1_koufen.setText("0")
            self.hong_game_1_defen.setText("0")

            self.hong_game_2_koufen.setText("0")
            self.hong_game_2_defen.setText("0")

            self.hong_game_3_koufen.setText("0")
            self.hong_game_3_defen.setText("0")

            self.hong_game_4_koufen.setText("0")
            self.hong_game_4_defen.setText("0")
    def jishi(self):

        self.timer.stop()
        self.timer2.start(1000)
        self.setdaojishi.setStyleSheet("color:#fff")
        self.dataFlag2 = False
        self.flag = True
        self.issound=False
        self.kaishi_bt.setText("开 始")

    def qingchu(self):
        self.qingfangzongfen.setText("0")
        self.qingfangkoufen.setText("0")
        self.qingfanghujufirst_lizhi.setText("0")
        self.qingfangname.setText("青方")
        self.qingfangdanwei.setText("青方单位")
        self.changcai_1_qing_1.setText("0")
        self.changcai_1_qing_2.setText("0")
        self.changcai_1_qing_3.setText("0")
        self.changcai_1_qing_4.setText("0")
        self.changcai_1_qing_5.setText("0")
        self.changcai_2_qing_1.setText("0")
        self.changcai_2_qing_2.setText("0")
        self.changcai_2_qing_3.setText("0")
        self.changcai_2_qing_4.setText("0")
        self.changcai_2_qing_5.setText("0")
        self.changcai_3_qing_1.setText("0")
        self.changcai_3_qing_2.setText("0")
        self.changcai_3_qing_3.setText("0")
        self.changcai_3_qing_4.setText("0")
        self.changcai_3_qing_5.setText("0")

        self.qing_game_1_koufen.setText("0")
        self.qing_game_1_defen.setText("0")

        self.qing_game_2_koufen.setText("0")
        self.qing_game_2_defen.setText("0")

        self.qing_game_3_koufen.setText("0")
        self.qing_game_3_defen.setText("0")

        self.qing_game_4_koufen.setText("0")
        self.qing_game_4_defen.setText("0")


        self.hongfangzongfen.setText("0")
        self.hongfangkoufen.setText("0")

        self.hongfangname.setText("红方")
        self.hongfangdanwei.setText("红方单位")
        self.changcai_1_hong_1.setText("0")
        self.changcai_1_hong_2.setText("0")
        self.changcai_1_hong_3.setText("0")
        self.changcai_1_hong_4.setText("0")
        self.changcai_1_hong_5.setText("0")
        self.changcai_2_hong_1.setText("0")
        self.changcai_2_hong_2.setText("0")
        self.changcai_2_hong_3.setText("0")
        self.changcai_2_hong_4.setText("0")
        self.changcai_2_hong_5.setText("0")
        self.changcai_3_hong_1.setText("0")
        self.changcai_3_hong_2.setText("0")
        self.changcai_3_hong_3.setText("0")
        self.changcai_3_hong_4.setText("0")
        self.changcai_3_hong_5.setText("0")

        self.hong_game_1_koufen.setText("0")
        self.hong_game_1_defen.setText("0")

        self.hong_game_2_koufen.setText("0")
        self.hong_game_2_defen.setText("0")

        self.hong_game_3_koufen.setText("0")
        self.hong_game_3_defen.setText("0")

        self.hong_game_4_koufen.setText("0")
        self.hong_game_4_defen.setText("0")
        self.setdaojishi.setStyleSheet("color:#fff")
        self.lianjie_bt.setText('连接')
        # self.changdi.setText('')
        # self.changdihao.setText('')
        self.lunci.setText('')
        self.jibie.setText('')
        self.bisaizhuangtai.setText('')

        self.isfirst = True
        self.qingfanghujudefentime = 0
        self.hongfanghujudefentime = 0
        self.qingfangtoukuidefentime = 0
        self.hongfangtoukuidefentime = 0
        self.hongfanglizhi=""
        self.qingfanglizhi=""

        self.gamenum = 1

        self.setgamenum.setText("第" + str(self.gamenum) + "局")
        self.daojishi = gl.get_value('dangqianshijian')
        self.setdaojishi.setText(str(datetime.timedelta(seconds=int(self.daojishi)))[2:])

        self.timer.stop()
        self.t1=0
        self.flag = True
        self.isfight = False
        self.dataFlag2 = False

        self.ishujufirst_hong = True
        self.ishujufirst_qing = True
        self.issound=True
        self.istest = True
        self.isqingfangtestfinsh = False
        self.isqingfangtestfinsh = False
        self.ceshi_bt.setText('测试')

        self.istest = False
        self.isqingfangtestfinsh = False
        self.ishongfangtestfinsh = False
        self.isqingtoutestfinsh = False
        self.ishongtoutestfinsh = False


        self.isjiashi = False
        self.kaishi_bt.setText("开 始")
        self.qinglabel.setStyleSheet("QLabel{color:#000}"
                                     "QLabel{background-color:#fff}"
                                     "QLabel{border:2px}"
                                     "QLabel{border-radius:5px}"
                                     "QLabel{padding:2px 4px}")

        self.honglabel.setStyleSheet("QLabel{color:#000}"
                                     "QLabel{background-color:#fff}"
                                     "QLabel{border:2px}"
                                     "QLabel{border-radius:5px}"
                                     "QLabel{padding:2px 4px}")

        self.qingfanghuju.setStyleSheet(
            "background-color:#FFE05E;border-color:#FFE05E;border-radius:0px")

        self.hongfanghuju.setStyleSheet("background-color:#FFE05E;border-color:#FFE05E ;border-radius:0px")

        self.hongfangtoukui.setStyleSheet("background-color:#FFE05E;border-color:#FFE05E ;border-radius:15px")

        self.qingfangtoukui.setStyleSheet(
            "background-color:#FFE05E;border-color:#FFE05E ;border-radius:15px")

        # 道馆的每局比赛打完后给他清零，正式比赛一定要注释掉
        # sql = "update bisaixinxi set hongfangdefen=%s,hongfangdefen1=%s,hongfangdefen2=%s,hongfangdefen3=%s,hongfangdefen4=%s,hongfangkoufen=%s,hongfangkoufen1=%s,hongfangkoufen2=%s,hongfangkoufen3=%s,hongfangkoufen4=%s," \
        #       "qingfangdefen=%s,qingfangdefen1=%s,qingfangdefen2=%s,qingfangdefen3=%s,qingfangdefen4=%s,qingfangkoufen=%s,qingfangkoufen1=%s,qingfangkoufen2=%s,qingfangkoufen3=%s,qingfangkoufen4=%s where bisaixuhao=%s" % (
        #           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        #           gl.get_value('bisaixuhao'))
        # # print(sql)
        # _thread.start_new_thread(self.stat.update, (sql,))

    def ceshi(self):
        if(not self.istest):
            self.istest=True
            self.ceshi_bt.setText("取消")

        else:
            self.istest=False

            self.ceshi_bt.setText("测试")


    def qingsheng(self):

        windialog.setWindowTitle("青方获胜")
        gl.set_value('huoshengzhe',"青方")

        gl.set_value('winnername',self.qingfangname.text())

        gl.set_value('winnerbianhao',self.yundongyuan[7])
        gl.set_value('winnerdanwei',self.qingfangdanwei.text())

        sql = "update dangqianbisai set huoshengzhe='%s'  where bisaixuhao = '%s'" % (
            1,
            gl.get_value('bisaixuhao'))
        # print(sql)
        _thread.start_new_thread(self.stat.update, (sql,))
        # self.stat.update(sql)
        self.timer.stop()
        self.timer2.stop()
        self.dataFlag=False
        self.showwin()
    def hongsheng(self):

        windialog.setWindowTitle("红方获胜")
        gl.set_value('huoshengzhe', "红方")

        gl.set_value('winnername',self.hongfangname.text())
        gl.set_value('winnerbianhao', self.yundongyuan[8])
        gl.set_value('winnerdanwei', self.hongfangdanwei.text())
        sql = "update dangqianbisai set huoshengzhe='%s'  where bisaixuhao = '%s'" % (
            0,
            gl.get_value('bisaixuhao'))
        print(sql)
        _thread.start_new_thread(self.stat.update, (sql,))
        # self.stat.update(sql)
        self.timer.stop()
        self.timer2.stop()
        self.dataFlag = False
        self.showwin()

    def fencha(self, qingdefen, hongdefen):
        # 加时得分
        if(self.isjiashi):
            if (hongdefen >= self.jiashizuidadefen):
                self.setgamenum.setText("结束")
                music_path = r'music\jieshu.wav'
                self.sound(music_path)
                self.hongsheng_bt.click()
                self.flag = True
                self.isfight = False
                self.dataFlag2 = False
            if (qingdefen >= self.jiashizuidadefen):
                self.setgamenum.setText("结束")
                music_path = r'music\jieshu.wav'
                self.sound(music_path)
                self.qingsheng_bt.click()
                self.flag = True
                self.isfight = False
                self.dataFlag2 = False
        else:
             #判断是否达到最大分差
            if(abs(qingdefen - hongdefen)>=int(gl.get_value('zuidafencha'))):
                music_path = r'music\jieshu.wav'
                self.sound(music_path)
                if qingdefen>hongdefen:
                    self.qingsheng_bt.click()
                else:
                    self.hongsheng_bt.click()

                self.timer.stop()
                self.istest = False
                self.flag = True
                self.isfight = False
                self.dataFlag2 = False
                self.ishujufirst_qing = True


    def qingdefenjia(self):
        self.qingfangzongfen.setText(str(int(self.qingfangzongfen.text())+1))
        sql = "update bisaixinxi set qingfangdefen=%s where bisaixuhao=%s" % (self.qingfangzongfen.text(),
                                                                              gl.get_value('bisaixuhao'))
        # print(sql)
        _thread.start_new_thread(self.stat.update, (sql,))
        self.fencha(int(self.qingfangzongfen.text()), int(self.hongfangzongfen.text()))
        # self.stat.update(sql)
    def qingdefenjian(self):
        self.qingfangzongfen.setText(str(int(self.qingfangzongfen.text()) - 1))
        sql = "update bisaixinxi set qingfangdefen=%s where bisaixuhao=%s" % (self.qingfangzongfen.text(),
                                                                              gl.get_value('bisaixuhao'))
        # print(sql)
        _thread.start_new_thread(self.stat.update, (sql,))
        # self.stat.update(sql)

    def qingkoufenjia(self):
        self.qingfangkoufen.setText(str(int(self.qingfangkoufen.text())+1))
        self.hongfangzongfen.setText(str(int(self.hongfangzongfen.text()) + 1))


        music_path = r'music\koufen.wav'
        self.sound(music_path)
        sql = "update bisaixinxi set hongfangdefen=%s,qingfangkoufen=%s where bisaixuhao=%s" % (
            self.hongfangzongfen.text(), self.qingfangkoufen.text(),
            gl.get_value('bisaixuhao'))
        # print(sql)
        _thread.start_new_thread(self.stat.update, (sql,))
        # self.stat.update(sql)

        if(self.isjiashi):
            if (int(self.qingfangkoufen.text()) >= self.jiashikoufenshu):
                music_path = r'music\jieshu.wav'
                self.sound(music_path)
                self.timer.stop()
                self.dataFlag = False
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '提示', "青方扣分数已达最大扣分数", QMessageBox.Ok)
        else:
            if(int(self.qingfangkoufen.text())>=self.koufenshu):
                music_path = r'music\jieshu.wav'
                self.sound(music_path)
                self.timer.stop()
                self.dataFlag = False
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '提示', "青方扣分数已达最大扣分数", QMessageBox.Ok)


    def qingkoufenjian(self):
        self.qingfangkoufen.setText(str(int(self.qingfangkoufen.text()) - 1))
        self.hongfangzongfen.setText(str(int(self.hongfangzongfen.text()) - 1))

        sql = "update bisaixinxi set hongfangdefen=%s,qingfangkoufen=%s where bisaixuhao=%s" % (
            self.hongfangzongfen.text(), self.qingfangkoufen.text(),
            gl.get_value('bisaixuhao'))
        # print(sql)
        _thread.start_new_thread(self.stat.update, (sql,))
        # self.stat.update(sql)

    def hongdefenjia(self):
        self.hongfangzongfen.setText(str(int(self.hongfangzongfen.text()) + 1))
        sql = "update bisaixinxi set hongfangdefen=%s where bisaixuhao=%s" % (self.hongfangzongfen.text(),
                                                                              gl.get_value('bisaixuhao'))
        # print(sql)
        _thread.start_new_thread(self.stat.update, (sql,))
        # self.stat.update(sql)
        self.fencha(int(self.qingfangzongfen.text()), int(self.hongfangzongfen.text()))



    def hongdefenjian(self):
        self.hongfangzongfen.setText(str(int(self.hongfangzongfen.text()) - 1))
        sql = "update bisaixinxi set hongfangdefen=%s where bisaixuhao=%s" % (self.hongfangzongfen.text(),
                                                                              gl.get_value('bisaixuhao'))
        # print(sql)
        _thread.start_new_thread(self.stat.update, (sql,))
        # self.stat.update(sql)

    def hongkoufenjia(self):
        self.hongfangkoufen.setText(str(int(self.hongfangkoufen.text()) + 1))
        self.qingfangzongfen.setText(str(int(self.qingfangzongfen.text()) +1))

        music_path = r'music\koufen.wav'
        self.sound(music_path)
        sql = "update bisaixinxi set hongfangkoufen=%s,qingfangdefen=%s where bisaixuhao=%s" % (self.hongfangkoufen.text(),
                                                                                                                 self.qingfangzongfen.text(),
                                                                                                                 gl.get_value('bisaixuhao'))
        # print(sql)
        _thread.start_new_thread(self.stat.update, (sql,))
        # self.stat.update(sql)
        if (self.isjiashi):
            if (int(self.hongfangkoufen.text()) >= self.jiashikoufenshu):
                self.setgamenum.setText("结束")
                music_path = r'music\jieshu.wav'
                self.sound(music_path)
                self.timer.stop()
                self.dataFlag = False
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '提示', "红方扣分数已达最大扣分数", QMessageBox.Ok)
        else:
            if (int(self.hongfangkoufen.text()) >= self.koufenshu):
                self.setgamenum.setText("结束")
                music_path = r'music\jieshu.wav'
                self.sound(music_path)
                self.timer.stop()
                self.dataFlag = False
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '提示', "红方扣分数已达最大扣分数", QMessageBox.Ok)

    def hongkoufenjian(self):
        self.hongfangkoufen.setText(str(int(self.hongfangkoufen.text()) - 1))
        self.qingfangzongfen.setText(str(int(self.qingfangzongfen.text()) - 1))

        sql = "update bisaixinxi set hongfangkoufen=%s,qingfangdefen=%s where bisaixuhao=%s" % (
        self.hongfangkoufen.text(),
        self.qingfangzongfen.text(),
        gl.get_value('bisaixuhao'))
        # print(sql)
        _thread.start_new_thread(self.stat.update, (sql,))
        # self.stat.update(sql)

    def transform_hex_data(self, data):
        return int(data, 16)

    def start(self):
        # if self.serial_port.text() == '' or self.qujian == '' or self.bstime == '':
        #     qw = QtWidgets.QWidget()
        #     QMessageBox.warning(qw, '警告', "串口号和得分区间和比赛时间不能为空", QMessageBox.Ok)
        #     return


        #若是第一次点击开始则获取设置相关参数
        if(self.isfirst):
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '错误', "还未连接串口设备", QMessageBox.Ok)



        else:

            self.jishitime = gl.get_value('jishitime')
            self.jishitimenow = int(self.jishitime)

            if(self.flag):

                if (self.isxiuxinow):
                    self.timer.start(1000)
                    self.isxiuxi = False
                    self.isxiuxinow = False
                    # self.daojishinow=int(self.daojishi)





                if(self.issound):
                    music_path = r'music\kaishi.wav'
                    self.sound(music_path)

                self.xiuxitime = gl.get_value('xiuxitime')
                self.xiuxitimenow = int(self.xiuxitime)
                self.dataFlag2 = True
                self.dataFlag=True

                print(self.gamenum)
                if(self.isjiashi):
                    self.setgamenum.setText("决胜局")
                else:
                    self.setgamenum.setText("第" + str(self.gamenum) + "局")
                self.setdaojishi.setStyleSheet("color:#fff")

                self.kaishi_bt.setText("暂 停")
                # print('开始')
                self.flag = False
                self.isfight=True
                self.timer2.stop()
                self.timer.start(1000)

                    # sql = "update dangqianbisai set changdihao=%s,daojishi=%s,bisaizhuangtai=%s,jishi=%s,dangqianju=%s where id = 1" % (
                    # gl.get_value('changdihao'), self.daojishi, 1, gl.get_value('jishitime'), 0)
                    # print(sql)
                    # self.stat.update(sql)






            else:
                self.timer.stop()
                self.timer2.stop()
                self.flag=True
                self.dataFlag2=False
                self.isfight = False
                self.issound=False
                self.setdaojishi.setStyleSheet("color:#EA2000")
                self.kaishi_bt.setText("开 始")
                sql = "update dangqianbisai set changdihao=%s,daojishi=%s,bisaizhuangtai=%s,jishi=%s,dangqianju=%s,defenqujian=%s where id=%s and changdi='%s'" % (
                    gl.get_value('changdihao'), self.daojishinow, 2, gl.get_value('jishitime'), self.gamenum,gl.get_value('defenqujian'),gl.get_value('bisaixuhao'),self.changdi.text())
                # print(sql)
                _thread.start_new_thread(self.stat.update, (sql,))
                # self.stat.update(sql)




    def my_timeout(self):
        # _thread.start_new_thread(self.my_timeout, ())
        pass


    # 加时得分
    # def jiashidefen(self,qingdefen,hongdefen):
    #
    #     if (hongdefen >= self.jiashizuidadefen):
    #         self.setgamenum.setText("结束")
    #         music_path = r'music\jieshu.wav'
    #         self.sound(music_path)
    #         self.hongsheng_bt.click()
    #         self.flag = True
    #         self.isfight = False
    #         self.dataFlag2 = False
    #     if (qingdefen >= self.jiashizuidadefen):
    #         self.setgamenum.setText("结束")
    #         music_path = r'music\jieshu.wav'
    #         self.sound(music_path)
    #         self.qingsheng_bt.click()
    #         self.flag = True
    #         self.isfight = False
    #         self.dataFlag2 = False

    def on_timeout(self):
        # self.shuaxin()


        if (int(self.daojishinow) > 0):

            self.shuaxin_bt.click()
            if (self.isjiashi):
                if (int(self.hongfangzongfen.text()) >= self.jiashizuidadefen):
                    self.setgamenum.setText("结束")
                    music_path = r'music\jieshu.wav'
                    self.sound(music_path)
                    self.hongsheng_bt.click()
                    self.flag = True
                    self.isfight = False
                    self.dataFlag2 = False
                if(int(self.qingfangzongfen.text()) >= self.jiashizuidadefen):
                    self.setgamenum.setText("结束")
                    music_path = r'music\jieshu.wav'
                    self.sound(music_path)
                    self.qingsheng_bt.click()
                    self.flag = True
                    self.isfight = False
                    self.dataFlag2 = False


                    # self.timer.stop()
                    # self.dataFlag = False
                    # qw = QtWidgets.QWidget()
                    # QMessageBox.warning(qw, '提示', "已达到加时赛最大得分", QMessageBox.Ok)
            print("青方护具护具号", self.qinghujunum.text())
            self.isxiuxi=True

            self.t2 = time.time()
            self.isone = True
            self.isfight = True

            self.daojishinow -= 1
            # print("aaaaaaaaaaaaaa")
            # print(self.daojishinow)

            if (int(self.t2) - int(self.t1) > 1):
                sql = "update dangqianbisai set caipanqing1=0,caipanqing2=0,caipanqing3=0,caipanhong1=0,caipanhong2=0,caipanhong3=0 where bisaixuhao=%s" % gl.get_value(
                    'bisaixuhao')
                _thread.start_new_thread(self.stat.update, (sql,))
                # print(sql)
                # print('大于1秒')
                # self.stat.update(sql)
            if (self.daojishinow == 9):
                music_path = r'music\daoji.wav'
                # _thread.start_new_thread(self.sound, (music_path,))
                self.sound(music_path)
            _thread.start_new_thread( self.setdaojishi.setText, (str(datetime.timedelta(seconds=self.daojishinow))[2:],))
            QApplication.processEvents()
            # self.setdaojishi.setText(str(datetime.timedelta(seconds=self.daojishinow))[2:])
            sql = "update dangqianbisai set changdihao=%s,daojishi=%s,bisaizhuangtai=%s,jishi=%s,dangqianju=%s,defenqujian=%s where id = %s and changdi='%s'" % (
                gl.get_value('changdihao'), self.daojishinow, 1, gl.get_value('jishitime'), self.gamenum,
                gl.get_value('defenqujian'),gl.get_value('bisaixuhao'),self.changdi.text())
            # print(sql)
            _thread.start_new_thread(self.stat.update, (sql,))
            # self.stat.update(sql)
        else:
            if (self.isone):
                music_path = r'music\jieshu.wav'
                self.sound(music_path)
                self.isone = False
            self.kaishi_bt.setText("开 始")
            self.isfight = False
            self.flag = True
            self.dataFlag2 = False

            if (self.gamenum == 1):
                self.qing_game_1_defen.setText(self.qingfangzongfen.text())
                self.qing_game_1_koufen.setText(self.qingfangkoufen.text())
                self.hong_game_1_defen.setText(self.hongfangzongfen.text())
                self.hong_game_1_koufen.setText(self.hongfangkoufen.text())
                sql = "update bisaixinxi set qingfangdefen1=%s,qingfangkoufen1=%s,hongfangdefen1=%s,hongfangkoufen1=%s where bisaixuhao=%s" % (
                    self.qing_game_1_defen.text(), self.qing_game_1_koufen.text(),
                    self.hong_game_1_defen.text(), self.hong_game_1_koufen.text(),
                    gl.get_value('bisaixuhao'))
                # print(sql)
                _thread.start_new_thread(self.stat.update, (sql,))
                # self.stat.update(sql)

            elif (self.gamenum == 2):
                self.qing_game_2_defen.setText(
                    str(int(self.qingfangzongfen.text()) - int(self.qing_game_1_defen.text())))
                self.qing_game_2_koufen.setText(
                    str(int(self.qingfangkoufen.text()) - int(self.qing_game_1_koufen.text())))
                self.hong_game_2_defen.setText(
                    str(int(self.hongfangzongfen.text()) - int(self.hong_game_1_defen.text())))
                self.hong_game_2_koufen.setText(
                    str(int(self.hongfangkoufen.text()) - int(self.hong_game_1_koufen.text())))
                sql = "update bisaixinxi set qingfangdefen2=%s,qingfangkoufen2=%s,hongfangdefen2=%s,hongfangkoufen2=%s where bisaixuhao=%s" % (
                    self.qing_game_2_defen.text(), self.qing_game_2_koufen.text(),
                    self.hong_game_2_defen.text(), self.hong_game_2_koufen.text(),
                    gl.get_value('bisaixuhao'))
                # print(sql)
                _thread.start_new_thread(self.stat.update, (sql,))
                # self.stat.update(sql)
            elif (self.gamenum == 3):
                self.qing_game_3_defen.setText(
                    str(int(self.qingfangzongfen.text()) - int(self.qing_game_1_defen.text()) - int(
                        self.qing_game_2_defen.text())))
                self.qing_game_3_koufen.setText(
                    str(int(self.qingfangkoufen.text()) - int(self.qing_game_1_koufen.text()) - int(
                        self.qing_game_2_koufen.text())))
                self.hong_game_3_defen.setText(
                    str(int(self.hongfangzongfen.text()) - int(self.hong_game_1_defen.text()) - int(
                        self.hong_game_2_defen.text())))
                self.hong_game_3_koufen.setText(
                    str(int(self.hongfangkoufen.text()) - int(self.hong_game_1_koufen.text()) - int(
                        self.hong_game_2_koufen.text())))

                sql = "update bisaixinxi set qingfangdefen3=%s,qingfangkoufen3=%s,hongfangdefen3=%s,hongfangkoufen3=%s where bisaixuhao=%s" % (
                    self.qing_game_3_defen.text(), self.qing_game_3_koufen.text(),
                    self.hong_game_3_defen.text(), self.hong_game_3_koufen.text(),
                    gl.get_value('bisaixuhao'))
                # print(sql)
                _thread.start_new_thread(self.stat.update, (sql,))
                # self.stat.update(sql)


            elif (self.gamenum == 4):
                self.qing_game_4_defen.setText(
                    str(int(self.qingfangzongfen.text()) - int(self.qing_game_1_defen.text()) - int(
                        self.qing_game_2_defen.text()) - int(self.qing_game_3_defen.text())))
                self.qing_game_4_koufen.setText(
                    str(int(self.qingfangkoufen.text()) - int(self.qing_game_1_koufen.text()) - int(
                        self.qing_game_2_koufen.text()) - int(self.qing_game_3_koufen.text())))
                self.hong_game_4_defen.setText(
                    str(int(self.hongfangzongfen.text()) - int(self.hong_game_1_defen.text()) - int(
                        self.hong_game_2_defen.text()) - int(self.hong_game_3_defen.text())))
                self.hong_game_4_koufen.setText(
                    str(int(self.hongfangkoufen.text()) - int(self.hong_game_1_koufen.text()) - int(
                        self.hong_game_2_koufen.text()) - int(self.hong_game_3_koufen.text())))

                sql = "update bisaixinxi set qingfangdefen4=%s,qingfangkoufen4=%s,hongfangdefen4=%s,hongfangkoufen4=%s where bisaixuhao=%s" % (
                    self.qing_game_4_defen.text(), self.qing_game_4_koufen.text(),
                    self.hong_game_4_defen.text(), self.hong_game_4_koufen.text(),
                    gl.get_value('bisaixuhao'))
                # print(sql)
                _thread.start_new_thread(self.stat.update, (sql,))
                # self.stat.update(sql)

            if (self.gamenum <= int(self.gamenums)):
                # print("休息")

                if(self.gamenum==int(self.gamenums) and (int(self.qingfangzongfen.text())-int(self.hongfangzongfen.text())>0 or int(self.hongfangzongfen.text())-int(self.qingfangzongfen.text()))):
                    # if():
                        self.setgamenum.setText("结束")
                        self.timer.stop()
                        self.dataFlag=False
                        self.istest = False
                        self.flag = True
                        self.isfight = False
                        self.dataFlag2 = False
                        self.ishujufirst_qing = True
                else:


                    if (int(self.xiuxitimenow) > 0 and self.isxiuxi):
                        self.isxiuxinow=True
                        self.xiuxitimenow -= 1
                        self.setgamenum.setText("休息时间")
                        _thread.start_new_thread(self.setdaojishi.setText,
                                                 (str(datetime.timedelta(seconds=self.xiuxitimenow))[2:],))

                        sql = "update dangqianbisai set changdihao=%s,daojishi=%s,bisaizhuangtai=%s,jishi=%s,dangqianju=%s where id = %s and changdi='%s'" % (
                            gl.get_value('changdihao'), self.daojishinow, 3, self.xiuxitimenow, self.gamenum,gl.get_value('bisaixuhao'),self.changdi.text())
                        # print(sql)
                        _thread.start_new_thread(self.stat.update, (sql,))
                        # self.stat.update(sql)


                    else:
                        self.daojishinow = int(self.daojishi)

                        self.isone = True
                        self.issound = True
                        # print('当前局' + str(self.gamenum))
                        # print('总局数' + str(self.gamenums))
                        if (self.gamenum == int(self.gamenums)):
                            if (int(self.hongfangzongfen.text()) == int(self.qingfangzongfen.text())):
                                self.isjiashi = True
                                self.setgamenum.setText("决胜局")
                                self.qingfangzongfen.setText("0")
                                self.qingfangkoufen.setText("0")

                                self.changcai_1_qing_1.setText("0")
                                self.changcai_1_qing_2.setText("0")
                                self.changcai_1_qing_3.setText("0")
                                self.changcai_1_qing_4.setText("0")
                                self.changcai_1_qing_5.setText("0")
                                self.changcai_2_qing_1.setText("0")
                                self.changcai_2_qing_2.setText("0")
                                self.changcai_2_qing_3.setText("0")
                                self.changcai_2_qing_4.setText("0")
                                self.changcai_2_qing_5.setText("0")
                                self.changcai_3_qing_1.setText("0")
                                self.changcai_3_qing_2.setText("0")
                                self.changcai_3_qing_3.setText("0")
                                self.changcai_3_qing_4.setText("0")
                                self.changcai_3_qing_5.setText("0")

                                self.qing_game_1_koufen.setText("0")
                                self.qing_game_1_defen.setText("0")

                                self.qing_game_2_koufen.setText("0")
                                self.qing_game_2_defen.setText("0")

                                self.qing_game_3_koufen.setText("0")
                                self.qing_game_3_defen.setText("0")

                                self.qing_game_4_koufen.setText("0")
                                self.qing_game_4_defen.setText("0")

                                self.hongfangzongfen.setText("0")
                                self.hongfangkoufen.setText("0")

                                self.changcai_1_hong_1.setText("0")
                                self.changcai_1_hong_2.setText("0")
                                self.changcai_1_hong_3.setText("0")
                                self.changcai_1_hong_4.setText("0")
                                self.changcai_1_hong_5.setText("0")
                                self.changcai_2_hong_1.setText("0")
                                self.changcai_2_hong_2.setText("0")
                                self.changcai_2_hong_3.setText("0")
                                self.changcai_2_hong_4.setText("0")
                                self.changcai_2_hong_5.setText("0")
                                self.changcai_3_hong_1.setText("0")
                                self.changcai_3_hong_2.setText("0")
                                self.changcai_3_hong_3.setText("0")
                                self.changcai_3_hong_4.setText("0")
                                self.changcai_3_hong_5.setText("0")

                                self.hong_game_1_koufen.setText("0")
                                self.hong_game_1_defen.setText("0")

                                self.hong_game_2_koufen.setText("0")
                                self.hong_game_2_defen.setText("0")

                                self.hong_game_3_koufen.setText("0")
                                self.hong_game_3_defen.setText("0")

                                self.hong_game_4_koufen.setText("0")
                                self.hong_game_4_defen.setText("0")
                                self.setdaojishi.setStyleSheet("color:#fff")
                                self.daojishinow = int(self.jiashijushi)
                                _thread.start_new_thread(self.setdaojishi.setText,
                                                         (str(datetime.timedelta(seconds=self.daojishinow))[2:],))

                                self.timer.stop()
                                sql = "update dangqianbisai set changdihao=%s,daojishi=%s,bisaizhuangtai=%s,jishi=%s,dangqianju=%s where id = %s and changdi='%s'" % (
                                    gl.get_value('changdihao'), self.daojishinow, 5, self.xiuxitime, 5,gl.get_value('bisaixuhao',self.changdi.text()),self.changdi.text())
                                print(sql)
                                _thread.start_new_thread(self.stat.update, (sql,))
                                # self.stat.update(sql)
                            else:
                                self.setgamenum.setText("结束")
                                self.timer.stop()
                        elif (self.gamenum < int(self.gamenums)):
                            self.gamenum += 1
                            self.setgamenum.setText("第" + str(self.gamenum) + "局")
                            self.setdaojishi.setText(str(datetime.timedelta(seconds=int(self.daojishinow)))[2:])
                            self.timer.stop()
                            sql = "update dangqianbisai set changdihao=%s,daojishi=%s,bisaizhuangtai=%s,jishi=%s,dangqianju=%s where id = %s and changdi='%s'" % (
                                gl.get_value('changdihao'), self.daojishinow, 5, self.xiuxitimenow, self.gamenum,gl.get_value('bisaixuhao'),self.changdi.text())
                            # print(sql)
                            _thread.start_new_thread(self.stat.update, (sql,))
                            # self.stat.update(sql)
        QApplication.processEvents()

    def my_timeout2(self):
       pass

    def on_timeout2(self):
        QApplication.processEvents()
        if (int(self.jishitimenow) > 0):
            self.isfight = False
            self.jishitimenow -= 1

            self.setgamenum.setText("计时")
            self.setdaojishi.setText(str(datetime.timedelta(seconds=self.jishitimenow))[2:])
            sql = "update dangqianbisai set changdihao=%s,daojishi=%s,bisaizhuangtai=%s,jishi=%s,dangqianju=%s where id = %s and changdi='%s'" % (
                gl.get_value('changdihao'), self.daojishinow, 4, self.jishitimenow, self.gamenum,gl.get_value('bisaixuhao'),self.changdi.text())
            # print(sql)
            _thread.start_new_thread(self.stat.update, (sql,))
            # self.stat.update(sql)



        else:
            self.jishitimenow = int(self.jishitime)
            self.timer2.stop()
            self.dataFlag2 = False
            self.kaishi_bt.setText("开 始")
            self.isfight = False
            self.flag = True
            self.dataFlag2 = False
            sql = "update dangqianbisai set changdihao=%s,daojishi=%s,bisaizhuangtai=%s,jishi=%s,dangqianju=%s where id = %s and changdi='%s'" % (
                gl.get_value('changdihao'), self.daojishinow, 0, self.jishitimenow, self.gamenum,gl.get_value('bisaixuhao'),self.changdi.text())
            # print(sql)
            _thread.start_new_thread(self.stat.update, (sql,))
            # self.stat.update(sql)

    def showsetting(self):
       seting.show()
       # print(seting.getdata())

    def showwin(self):
        windialog.show()

    # def mysleep(self,sql):
    #     time.sleep(1000)
    #     self.stat.update(sql)


    #保存裁判打2分（旋转）的时间，若0.5秒内运动员电子护具头盔得分则加上这两分，否则不加
    def twoPoinsTime(self,poins):
        if(poins==2):
            return time.time()
        else:
            return None




    def getData(self, x):

        print(x)
        myout = []
        self.index_2 = 0
        firstlizhi = 0
        dafenqi1_qing = 0
        dafenqi2_qing = 0
        dafenqi3_qing = 0
        dafenqi1_hong = 0
        dafenqi2_hong = 0
        dafenqi3_hong = 0
        jishi = 0
        # print(self.dataFlag)

        while self.dataFlag:

            if (self.isfirst):
                print("结束串口进程")
                _thread.exit()

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
                print(myout)
                # s = str(myout[0:])
                s = str(myout)
                #   print(s)
                last = s.replace("b'", "").replace("[", "").replace("']", "").replace(",", "").replace("' ",
                                                                                                          "").replace(
                    "b'_'", '')
                print(last)

                #判断是电子护具(组别 红方 3 青方 2)还是打分器
                group_1 = last[5]
                #判断头盔是否被击打
                is_jida=last[9]

                #判断头盔是否旋转

                is_rotate=last[7]
                print("group_1",group_1)
                #设备组号
                zunum=int(last[2])
                print("组号",zunum)
                print("设置的设备组号",self.shebeizunum.text())
                # print('当前组号---',zunum)
                #设备号
                shebeinum=int(last[4])

                # print(group_1)
                lizhi = (self.transform_hex_data(myout[4]) << 8) + self.transform_hex_data(myout[3])
                # print("力值--", lizhi)
                if(zunum==int(self.shebeizunum.text())):

                    if ((group_1 == "2" or group_1 == "3" or group_1=="7" or group_1=="8") ):
                        self.shuaxin_bt.click()

                        # lizhi = (self.transform_hex_data(myout[4]) << 8) + self.transform_hex_data(myout[3])
                        # print(lizhi)
                        if (group_1 == "2" and shebeinum==int(self.qinghujunum.text())):
                            if (self.ishujufirst_qing):
                                self.firstlizhi_qing = lizhi

                                # print("第一次力值" + str(self.firstlizhi_qing))
                                self.qinglabel.setStyleSheet("QLabel{color:#fff}"
                                                             "QLabel{background-color:rgb(0,120,215)}"
                                                             "QLabel{border:2px}"
                                                             "QLabel{border-radius:5px}"
                                                             "QLabel{padding:2px 4px}")
                                # myout = []
                                self.ishujufirst_qing = False
                        if (group_1 == "3" and shebeinum==int(self.honghujunum.text())):
                            if (self.ishujufirst_hong):
                                self.firstlizhi_hong = lizhi

                                # print("第一次力值" + str(self.firstlizhi_hong))
                                # myout = []
                                self.honglabel.setStyleSheet("QLabel{color:#fff}"
                                                             "QLabel{background-color:red}"
                                                             "QLabel{border:2px}"
                                                             "QLabel{border-radius:5px}"
                                                             "QLabel{padding:2px 4px}")
                                self.ishujufirst_hong = False

                        if (self.istest):
                            if (group_1 == "2" and shebeinum==int(self.qinghujunum.text())):
                                # print("力值" + str(lizhi))

                                self.qingfanghuju.setStyleSheet(
                                    "background-color:rgb(0,120,215);border-color:(0,120,215) ;border-radius:0px")
                                # _thread.start_new_thread(self.qingfanghuju.setStyleSheet, ( "background-color:rgb(0,120,215);border-color:(0,120,215) ;border-radius:0px",))
                                self.isqingfangtestfinsh = True

                            if (group_1 == "3" and shebeinum==int(self.honghujunum.text())):
                                # print("力值" + str(lizhi))
                                self.hongfanghuju.setStyleSheet("background-color:red;border-color:red ;border-radius:0px")
                                # _thread.start_new_thread(self.hongfanghuju.setStyleSheet, (
                                # "background-color:red;border-color:red ;border-radius:0px",))

                                self.ishongfangtestfinsh = True

                            if (group_1 == "7" and shebeinum==int(self.qingtoukuinum.text()) ):
                                self.qingfangtoukui.setStyleSheet(
                                    "background-color:rgb(0,120,215);border-color:(0,120,215) ;border-radius:15px")

                                self.isqingtoutestfinsh = True


                            if (group_1 == "8" and shebeinum==int(self.hongtoukuinum.text())):
                                # print("第一次力值" + str(self.firstlizhi_hong))

                                self.hongfangtoukui.setStyleSheet(
                                    "background-color:red;border-color:red ;border-radius:15px")
                                self.ishongtoutestfinsh=True

                            if (self.isqingfangtestfinsh and self.ishongfangtestfinsh and  self.ishongtoutestfinsh and self.isqingtoutestfinsh):
                                self.istest = False
                                self.ceshi_bt.setText('已测试')
                            self.shuaxin_bt.click()


                    # 正式开始比赛
                    if (self.dataFlag2):
                        self.shuaxin_bt.click()
                        if(group_1=="7" or group_1=="8"):
                            if (group_1 == "7" and shebeinum==int(self.qingtoukuinum.text())):
                                print('青方头盔')
                                self.qingfangtoukuitime = time.time()

                                if (is_rotate == "1"):
                                    self.qingfangtoukuirotatetime = time.time()
                                    print("青方旋转")

                                if ((self.qingfangtoukuitime - self.qingfangtoukuidefentime) > 0.3 and is_jida == "1"):
                                    self.qingfangtoukuidefentime = time.time()
                                    # 记录当前护具得分时间
                                    # lizhixian=self.firstlizhi_qing - (1 * int(self.defenqujian))
                                    # if(lizhi<lizhixian):
                                    #     hongfanglizhi=math.ceil((lizhixian-lizhi)/1)+int(self.defenqujian)
                                    # else:
                                    #     hongfanglizhi = math.ceil((self.firstlizhi_qing - lizhi) / 1)
                                    # print("红方力值",hongfanglizhi)

                                    music_path = r'music\liangfen.wav'
                                    self.sound(music_path)
                                    # print("得2分")

                                    # print(sql)
                                    hongfangdefen = int(self.hongfangzongfen.text()) + 3

                                    if(self.qingfangtoukuitime-self.hongfangtoukuirotatetime<0.3):
                                        hongfangdefen = hongfangdefen+2

                                    if(self.twoPointsTimeNowhong):
                                        if(self.qingfangtoukuitime-self.twoPointsTimeNowhong<0.5):
                                            hongfangdefen = hongfangdefen + 2

                                        self.twoPointsTimeNowhong = None


                                    _thread.start_new_thread(self.hongfangzongfen.setText,
                                                             (str(hongfangdefen),))

                                    sql = "update bisaixinxi set hongfangdefen='%s' where bisaixuhao='%s'" % (
                                        hongfangdefen,
                                        gl.get_value('bisaixuhao'))
                                    _thread.start_new_thread(self.stat.update, (sql,))

                                    if (self.hongfanglizhi == ""):
                                        self.hongfanglizhi = str(40)
                                    else:
                                        self.hongfanglizhi = self.hongfanglizhi + "," + str(40)

                                    # 击打头盔，力值为40
                                    sql = "update dangqianbisai set hongfanglizhi='%s' where bisaixuhao='%s'" % (
                                        self.hongfanglizhi,
                                        gl.get_value('bisaixuhao'))
                                    # print(sql)
                                    _thread.start_new_thread(self.stat.update, (sql,))

                                    # self.hongfangzongfen.setText(str(int(self.hongfangzongfen.text()) + 2))
                                    # self.stat.update(sql)


                                    self.fencha(int(self.qingfangzongfen.text()), hongfangdefen)

                                # print("当力值小于" + str(self.firstlizhi_qing - (30 * int(self.defenqujian))) + "得两分")
                                # print("ID:" + str(lizhi))
                            if (group_1 == "8" and shebeinum==int(self.hongtoukuinum.text())):

                                print('红方头盔')
                                self.hongfangtoukuitime=time.time()

                                if (is_rotate == "1"):
                                    self.hongfangtoukuirotatetime = time.time()
                                    print("红方旋转")

                                if ((self.hongfangtoukuitime - self.hongfangtoukuidefentime) > 0.3 and is_jida == "1"):
                                    self.hongfangtoukuidefentime = time.time()

                                    qingfangdefen = int(self.qingfangzongfen.text()) + 3

                                    if (self.hongfangtoukuitime - self.qingfangtoukuirotatetime < 0.3):
                                        qingfangdefen = qingfangdefen + 2

                                    if (self.twoPointsTimeNowqing):
                                        if (self.hongfangtoukuitime - self.twoPointsTimeNowqing < 0.5):
                                            qingfangdefen = qingfangdefen + 2
                                        self.twoPointsTimeNowqing=None

                                    music_path = r'music\liangfen.wav'
                                    self.sound(music_path)


                                    _thread.start_new_thread(self.qingfangzongfen.setText, (str(qingfangdefen),))


                                    sql = "update bisaixinxi set qingfangdefen=%s where bisaixuhao=%s" % (
                                        qingfangdefen,
                                        gl.get_value('bisaixuhao'))
                                    # print(sql)
                                    _thread.start_new_thread(self.stat.update, (sql,))

                                    if (self.qingfanglizhi == ""):
                                        self.qingfanglizhi = str(40)
                                    else:
                                        self.qingfanglizhi = self.qingfanglizhi + "," + str(40)
                                    # 击打头盔，力值为40
                                    sql = "update dangqianbisai set qingfanglizhi='%s' where bisaixuhao='%s'" % (
                                        self.qingfanglizhi,
                                        gl.get_value('bisaixuhao'))
                                    # print(sql)
                                    _thread.start_new_thread(self.stat.update, (sql,))



                                    # self.qingfangzongfen.setText(str(int(self.qingfangzongfen.text()) + 2))
                                    # self.stat.update(sql)

                                    self.fencha(int(qingfangdefen), int(self.hongfangzongfen.text()))

                                # print("当力值小于" + str(self.firstlizhi_hong - (30 * int(self.defenqujian))) + "得两分")
                                # print("ID:" + str(lizhi))
                            myout = []
                        if (group_1 == "2" or group_1 == "3"):
                            # print("------------------护具-------------------")

                            # print(lizhi)


                            if (group_1 == "2" and shebeinum==int(self.qinghujunum.text())):
                                print(myout)
                                lizhi = (self.transform_hex_data(myout[4]) << 8) + self.transform_hex_data(myout[3])
                                # print("力值--",lizhi)
                                self.qingfanghujutime = time.time()
                                hongfanglizhi = 0
                                if ((self.qingfanghujutime - self.qingfanghujudefentime) > 0.3):
                                    self.qingfanghujudefentime = time.time()



                                    if (lizhi <= 300):
                                        hongfanglizhi = math.floor(lizhi / 10)
                                    else:
                                        hongfanglizhi = 30
                                    print("红方力值",hongfanglizhi)
                                    if(self.hongfanglizhi==""):
                                        self.hongfanglizhi=str(hongfanglizhi)
                                    else:
                                        self.hongfanglizhi = self.hongfanglizhi + "," + str(hongfanglizhi)
                                    sql = "update dangqianbisai set hongfanglizhi='%s' where bisaixuhao='%s'" % (
                                        self.hongfanglizhi,
                                        gl.get_value('bisaixuhao'))
                                    # print(sql)
                                    _thread.start_new_thread(self.stat.update, (sql,))

                                    if(hongfanglizhi>=int(self.defenqujian)):

                                        music_path = r'music\liangfen.wav'
                                        self.sound(music_path)
                                        print("得2分")


                                        # print(sql)
                                        hongfangdefen=int(self.hongfangzongfen.text()) + 2

                                        if (self.qingfanghujutime - self.hongfangtoukuirotatetime < 0.3):
                                            hongfangdefen = hongfangdefen + 2

                                        if (self.twoPointsTimeNowhong):
                                            if (self.qingfanghujutime - self.twoPointsTimeNowhong < 0.5):
                                                hongfangdefen = hongfangdefen + 2

                                            self.twoPointsTimeNowhong = None

                                        _thread.start_new_thread(self.hongfangzongfen.setText,
                                                                 (str(hongfangdefen),))


                                        sql = "update bisaixinxi set hongfangdefen='%s' where bisaixuhao='%s'" % (
                                            hongfangdefen,
                                            gl.get_value('bisaixuhao'))
                                        _thread.start_new_thread(self.stat.update, (sql,))
                                        # self.hongfangzongfen.setText(str(int(self.hongfangzongfen.text()) + 2))
                                        # self.stat.update(sql)


                                    self.fencha(int(self.qingfangzongfen.text()), int(hongfangdefen))

                                # print("当力值小于" + str(self.firstlizhi_qing - (30 * int(self.defenqujian))) + "得两分")
                                # print("ID:" + str(lizhi))
                            if (group_1 == "3" and shebeinum==int(self.honghujunum.text())):
                                print(myout)
                                lizhi = (self.transform_hex_data(myout[4]) << 8) + self.transform_hex_data(myout[3])
                                # print("力值--", lizhi)

                                self.hongfanghujutime = time.time()
                                qingfanglizhi = 0
                                if ((self.hongfanghujutime - self.hongfanghujudefentime) > 0.3):
                                    self.hongfanghujudefentime = time.time()

                                    #记录当前护具得分时间

                                    # lizhixian = self.firstlizhi_hong - (1 * int(self.defenqujian))
                                    # if(lizhi<lizhixian):
                                    #     qingfanglizhi = math.ceil((lizhixian - lizhi) / 1) + int(self.defenqujian)
                                    # else:
                                    #     qingfanglizhi = math.ceil((self.firstlizhi_hong - lizhi) / 1)
                                    # print("青方力值",qingfanglizhi)
                                    # print("红方力值", hongfanglizhi)
                                    if(lizhi<=300):
                                        qingfanglizhi=math.floor(lizhi/10)
                                    else:
                                        qingfanglizhi=30
                                    print("青方力值",qingfanglizhi)

                                    if(self.qingfanglizhi==""):
                                        self.qingfanglizhi=str(qingfanglizhi)
                                    else:
                                        self.qingfanglizhi = self.qingfanglizhi + "," + str(qingfanglizhi)
                                    # print(self.qingfanglizhi,"ggggggggggggggg")
                                    sql = "update dangqianbisai set qingfanglizhi='%s' where bisaixuhao='%s'" % (
                                        self.qingfanglizhi,
                                        gl.get_value('bisaixuhao'))
                                    # print(sql)
                                    _thread.start_new_thread(self.stat.update, (sql,))
                                    # self.stat.update(sql)
                                    # if (lizhi > (firstlizhi - (30 * (int(self.qujian.text()) )))):
                                    #     self.redjd.setText(str(int(self.qujian.text()) + 1))
                                    # elif (lizhi > (firstlizhi - (30 * (int(self.qujian.text()) + 2)))):
                                    #     self.redjd.setText(str(int(self.qujian.text()) + 2))
                                    # elif (lizhi > (firstlizhi - (30 * (int(self.qujian.text()) + 3)))):
                                    #     self.redjd.setText(str(int(self.qujian.text()) + 3))
                                    # elif (lizhi > (firstlizhi - (30 * (int(self.qujian.text()) + 4)))):
                                    #     self.redjd.setText(str(int(self.qujian.text()) + 4))
                                    # elif (lizhi > (firstlizhi - (30 * (int(self.qujian.text()) + 5)))):
                                    #     self.redjd.setText(str(int(self.qujian.text()) + 5))
                                    # elif (lizhi > (firstlizhi - (30 * (int(self.qujian.text()) + 6)))):
                                    #     self.redjd.setText(str(int(self.qujian.text()) + 6))
                                    if(qingfanglizhi>=int(self.defenqujian)):
                                        print("得2分")
                                        qingfangdefen=int(self.qingfangzongfen.text()) + 2
                                        if (self.hongfanghujutime - self.qingfangtoukuirotatetime < 0.3):
                                            qingfangdefen = qingfangdefen + 2

                                        if (self.twoPointsTimeNowqing):
                                            if (self.hongfanghujutime - self.twoPointsTimeNowqing < 0.5):
                                                qingfangdefen = qingfangdefen + 2
                                            self.twoPointsTimeNowqing = None

                                        music_path = r'music\liangfen.wav'
                                        self.sound(music_path)


                                        _thread.start_new_thread( self.qingfangzongfen.setText, (str(qingfangdefen),))



                                        sql = "update bisaixinxi set qingfangdefen=%s where bisaixuhao=%s" % (
                                            qingfangdefen,
                                            gl.get_value('bisaixuhao'))
                                        # print(sql)
                                        _thread.start_new_thread(self.stat.update, (sql,))
                                        # self.qingfangzongfen.setText(str(int(self.qingfangzongfen.text()) + 2))
                                        # self.stat.update(sql)

                                    self.fencha(int(qingfangdefen), int(self.hongfangzongfen.text()))



                                # print("当力值小于" + str(self.firstlizhi_hong - (30 * int(self.defenqujian))) + "得两分")
                                # print("ID:" + str(lizhi))
                            myout = []
                            self.ishujufirst = False
                            self.shuaxin_bt.click()










                        # 进入打分器
                        if (group_1 == self.changcai_1_num.text() or group_1 == self.changcai_2_num.text() or group_1 == self.changcai_3_num.text()):
                            # 组别 红方 3 青方 2
                            group = last[9]
                            # print("组别" + group)
                            value = last[7]
                            self.shuaxin_bt.click()



                            self.index_2 = self.index_2 + 1
                            if (self.index_2 == 1):
                                t = time.time()
                            #      print("3秒计时开始")

                            self.t1 = time.time()
                            if (self.t1 - t > self.caipanshicha):
                                t = time.time()
                                dafenqi1_qing = 0
                                dafenqi2_qing = 0
                                dafenqi3_qing = 0
                                dafenqi1_hong = 0
                                dafenqi2_hong = 0
                                dafenqi3_hong = 0

                                # print("重新开始3秒计时")

                            if(group == "2"):

                                if(group_1 == self.changcai_1_num.text()):
                                    t_changcai_1=time.time()

                                    print("4号打分器打分时间" + str(t_changcai_1 - t))

                                    value = last[7]
                                    print("打分器" + group_1 + "打分：" + value)
                                    dafenqi1_qing = int(value)

                                    if(value == "1"):
                                        self.changcai_1_qing_1.setText(str(int(self.changcai_1_qing_1.text())+1))
                                    if (value == "2"):
                                        self.changcai_1_qing_2.setText(str(int(self.changcai_1_qing_2.text()) + 1))
                                    if (value == "3"):
                                        self.changcai_1_qing_3.setText(str(int(self.changcai_1_qing_3.text()) + 1))
                                    if (value == "4"):
                                        self.changcai_1_qing_4.setText(str(int(self.changcai_1_qing_4.text()) + 1))
                                    if (value == "5"):
                                        self.changcai_1_qing_5.setText(str(int(self.changcai_1_qing_5.text()) + 1))

                                if (group_1 == self.changcai_2_num.text()):
                                    t_changcai_2 = time.time()

                                    print("5号打分器打分时间" + str(t_changcai_2 - t))

                                    value = last[7]
                                    print("打分器" + group_1 + "打分：" + value)

                                    dafenqi2_qing = int(value)

                                    if (value == "1"):
                                        self.changcai_2_qing_1.setText(str(int(self.changcai_2_qing_1.text()) + 1))
                                    if (value == "2"):
                                        self.changcai_2_qing_2.setText(str(int(self.changcai_2_qing_2.text()) + 1))
                                    if (value == "3"):
                                        self.changcai_2_qing_3.setText(str(int(self.changcai_2_qing_3.text()) + 1))
                                    if (value == "4"):
                                        self.changcai_2_qing_4.setText(str(int(self.changcai_2_qing_4.text()) + 1))
                                    if (value == "5"):
                                        self.changcai_2_qing_5.setText(str(int(self.changcai_2_qing_5.text()) + 1))

                                if (group_1 == self.changcai_3_num.text()):
                                    t_changcai_3 = time.time()

                                    print("6号打分器打分时间" + str(t_changcai_3 - t))

                                    value = last[7]
                                    print("打分器" + group_1 + "打分：" + value)

                                    dafenqi3_qing = int(value)

                                    if (value == "1"):
                                        self.changcai_3_qing_1.setText(str(int(self.changcai_3_qing_1.text()) + 1))
                                    if (value == "2"):
                                        self.changcai_3_qing_2.setText(str(int(self.changcai_3_qing_2.text()) + 1))
                                    if (value == "3"):
                                        self.changcai_3_qing_3.setText(str(int(self.changcai_3_qing_3.text()) + 1))
                                    if (value == "4"):
                                        self.changcai_3_qing_4.setText(str(int(self.changcai_3_qing_4.text()) + 1))
                                    if (value == "5"):
                                        self.changcai_3_qing_5.setText(str(int(self.changcai_3_qing_5.text()) + 1))
                                sql = "update dangqianbisai set caipanqing1=%s,caipanqing2=%s,caipanqing3=%s where bisaixuhao=%s" % (
                                    dafenqi1_qing, dafenqi2_qing, dafenqi3_qing,
                                    gl.get_value('bisaixuhao'))
                                # print(sql)
                                _thread.start_new_thread(self.stat.update, (sql,))
                                # self.stat.update(sql)

                                if (self.t1 - t <= self.caipanshicha):

                                    if (not dafenqi1_qing == 0 and dafenqi2_qing == dafenqi1_qing):
                                        print("1----------------------打分器得分------------------" + str(dafenqi1_qing))
                                        if(self.isfight):
                                            self.twoPointsTimeNowqing=self.twoPoinsTime(dafenqi1_qing)
                                            if( self.twoPointsTimeNowqing==None):
                                                fenshu=int(self.qingfangzongfen.text())+dafenqi1_qing
                                                self.qingfangzongfen.setText(str(fenshu))

                                                if(dafenqi1_qing==1):
                                                    music_path = r'music\yifen.wav'
                                                    self.sound(music_path)
                                                elif(dafenqi1_qing==2):
                                                    music_path = r'music\liangfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_qing == 3):
                                                    music_path = r'music\sanfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_qing == 4):
                                                    music_path = r'music\sifen.wav'
                                                    self.sound(music_path)


                                                t = time.time()
                                                sql = "update dangqianbisai set caipanqing1=%s,caipanqing2=%s,caipanqing3=%s where bisaixuhao=%s" % (
                                                    dafenqi1_qing, dafenqi2_qing, dafenqi3_qing,
                                                    gl.get_value('bisaixuhao'))
                                                # print(sql)
                                                _thread.start_new_thread(self.stat.update, (sql,))
                                                # self.stat.update(sql)
                                                dafenqi1_qing = 0
                                                dafenqi2_qing = 0
                                                dafenqi3_qing = 0
                                                self.fencha(fenshu, int(self.hongfangzongfen.text()))





                                    elif (not dafenqi2_qing == 0 and dafenqi3_qing == dafenqi2_qing):
                                        print("2----------------------打分器得分----------------" + str(dafenqi2_qing))
                                        if(self.isfight):
                                            self.twoPointsTimeNowqing = self.twoPoinsTime(dafenqi2_qing)
                                            if (self.twoPointsTimeNowqing == None):
                                                fenshu = int(self.qingfangzongfen.text()) + dafenqi2_qing
                                                self.qingfangzongfen.setText(str(fenshu))



                                                if (dafenqi2_qing == 1):
                                                    music_path = r'music\yifen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi2_qing == 2):
                                                    music_path = r'music\liangfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi2_qing == 3):
                                                    music_path = r'music\sanfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi2_qing == 4):
                                                    music_path = r'music\sifen.wav'
                                                    self.sound(music_path)

                                                t = time.time()
                                                sql = "update dangqianbisai set caipanqing1=%s,caipanqing2=%s,caipanqing3=%s where bisaixuhao=%s" % (
                                                    dafenqi1_qing, dafenqi2_qing, dafenqi3_qing,
                                                    gl.get_value('bisaixuhao'))
                                                # print(sql)
                                                _thread.start_new_thread(self.stat.update, (sql,))
                                                # self.stat.update(sql)
                                                dafenqi1_qing = 0
                                                dafenqi2_qing = 0
                                                dafenqi3_qing = 0
                                                self.fencha(fenshu, int(self.hongfangzongfen.text()))




                                    elif (not dafenqi1_qing == 0 and dafenqi1_qing == dafenqi3_qing):
                                        print("3--------------------打分器得分---------------" + str(dafenqi1_qing))
                                        if(self.isfight):
                                            self.twoPointsTimeNowqing = self.twoPoinsTime(dafenqi1_qing)
                                            if (self.twoPointsTimeNowqing == None):
                                                fenshu = int(self.qingfangzongfen.text()) + dafenqi1_qing
                                                self.qingfangzongfen.setText(str(fenshu))


                                                if (dafenqi1_qing == 1):
                                                    music_path = r'music\yifen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_qing == 2):
                                                    music_path = r'music\liangfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_qing == 3):
                                                    music_path = r'music\sanfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_qing == 4):
                                                    music_path = r'music\sifen.wav'
                                                    self.sound(music_path)

                                                t = time.time()
                                                sql = "update dangqianbisai set caipanqing1=%s,caipanqing2=%s,caipanqing3=%s where bisaixuhao=%s" % (
                                                    dafenqi1_qing, dafenqi2_qing, dafenqi3_qing,
                                                    gl.get_value('bisaixuhao'))
                                                # print(sql)
                                                _thread.start_new_thread(self.stat.update, (sql,))
                                                # self.stat.update(sql)
                                                dafenqi1_qing = 0
                                                dafenqi2_qing = 0
                                                dafenqi3_qing = 0
                                                self.fencha(fenshu, int(self.hongfangzongfen.text()))




                                    elif (not dafenqi1_qing == 0 and dafenqi1_qing == dafenqi2_qing == dafenqi3_qing):
                                        print("4--------------------打分器得分---------------" + str(dafenqi1_qing))
                                        if(self.isfight):
                                            self.twoPointsTimeNowqing = self.twoPoinsTime(dafenqi1_qing)
                                            if (self.twoPointsTimeNowqing == None):
                                                fenshu = int(self.qingfangzongfen.text()) + dafenqi1_qing
                                                self.qingfangzongfen.setText(str(fenshu))


                                                if (dafenqi1_qing == 1):
                                                    music_path = r'music\yifen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_qing == 2):
                                                    music_path = r'music\liangfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_qing == 3):
                                                    music_path = r'music\sanfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_qing == 4):
                                                    music_path = r'music\sifen.wav'
                                                    self.sound(music_path)

                                                t = time.time()
                                                sql = "update dangqianbisai set caipanqing1=%s,caipanqing2=%s,caipanqing3=%s where bisaixuhao=%s" % (
                                                    dafenqi1_qing, dafenqi2_qing, dafenqi3_qing,
                                                    gl.get_value('bisaixuhao'))
                                                # print(sql)
                                                _thread.start_new_thread(self.stat.update, (sql,))
                                                # self.stat.update(sql)
                                                dafenqi1_qing = 0
                                                dafenqi2_qing = 0
                                                dafenqi3_qing = 0
                                                self.fencha(fenshu, int(self.hongfangzongfen.text()))

                                    sql = "update bisaixinxi set qingfangdefen=%s where bisaixuhao=%s" % ( self.qingfangzongfen.text(),
                                        gl.get_value('bisaixuhao'))
                                    print(sql)
                                    _thread.start_new_thread(self.stat.update, (sql,))
                                    # self.stat.update(sql)
                                    # self.fencha(int(self.qingfangzongfen.text()), int(self.hongfangzongfen.text()))




                            if (group == "3"):

                                if (group_1 == self.changcai_1_num.text()):
                                    t_changcai_1 = time.time()

                                    print("4号打分器打分时间" + str(t_changcai_1 - t))

                                    value = last[7]
                                    print("打分器" + group_1 + "打分：" + value)

                                    dafenqi1_hong = int(value)

                                    if (value == "1"):
                                        self.changcai_1_hong_1.setText(str(int(self.changcai_1_hong_1.text()) + 1))
                                    if (value == "2"):
                                        self.changcai_1_hong_2.setText(str(int(self.changcai_1_hong_2.text()) + 1))
                                    if (value == "3"):
                                        self.changcai_1_hong_3.setText(str(int(self.changcai_1_hong_3.text()) + 1))
                                    if (value == "4"):
                                        self.changcai_1_hong_4.setText(str(int(self.changcai_1_hong_4.text()) + 1))
                                    if (value == "5"):
                                        self.changcai_1_hong_5.setText(str(int(self.changcai_1_hong_5.text()) + 1))

                                if (group_1 == self.changcai_2_num.text()):
                                    t_changcai_2 = time.time()

                                    print("4号打分器打分时间" + str(t_changcai_2 - t))

                                    value = last[7]
                                    print("打分器" + group_1 + "打分：" + value)

                                    dafenqi2_hong = int(value)

                                    if (value == "1"):
                                        self.changcai_2_hong_1.setText(str(int(self.changcai_2_hong_1.text()) + 1))
                                    if (value == "2"):
                                        self.changcai_2_hong_2.setText(str(int(self.changcai_2_hong_2.text()) + 1))
                                    if (value == "3"):
                                        self.changcai_2_hong_3.setText(str(int(self.changcai_2_hong_3.text()) + 1))
                                    if (value == "4"):
                                        self.changcai_2_hong_4.setText(str(int(self.changcai_2_hong_4.text()) + 1))
                                    if (value == "5"):
                                        self.changcai_2_hong_5.setText(str(int(self.changcai_2_hong_5.text()) + 1))

                                if (group_1 == self.changcai_3_num.text()):
                                    t_changcai_3 = time.time()

                                    print("4号打分器打分时间" + str(t_changcai_3 - t))

                                    value = last[7]
                                    print("打分器" + group_1 + "打分：" + value)

                                    dafenqi3_hong = int(value)

                                    if (value == "1"):
                                        self.changcai_3_hong_1.setText(str(int(self.changcai_3_hong_1.text()) + 1))
                                    if (value == "2"):
                                        self.changcai_3_hong_2.setText(str(int(self.changcai_3_hong_2.text()) + 1))
                                    if (value == "3"):
                                        self.changcai_3_hong_3.setText(str(int(self.changcai_3_hong_3.text()) + 1))
                                    if (value == "4"):
                                        self.changcai_3_hong_4.setText(str(int(self.changcai_3_hong_4.text()) + 1))
                                    if (value == "5"):
                                        self.changcai_3_hong_5.setText(str(int(self.changcai_3_hong_5.text()) + 1))
                                sql = "update dangqianbisai set caipanhong1=%s,caipanhong2=%s,caipanhong3=%s where bisaixuhao=%s" % (
                                    dafenqi1_hong, dafenqi2_hong, dafenqi3_hong,
                                    gl.get_value('bisaixuhao'))
                                # print(sql)
                                _thread.start_new_thread(self.stat.update, (sql,))
                                # self.stat.update(sql)

                                if (self.t1 - t <= self.caipanshicha):

                                    if (not dafenqi1_hong == 0 and dafenqi2_hong == dafenqi1_hong):
                                        print("1----------------------打分器得分------------------" + str(dafenqi1_hong))
                                        if(self.isfight):
                                            self.twoPointsTimeNowhong = self.twoPoinsTime(dafenqi1_hong)
                                            if (self.twoPointsTimeNowhong == None):
                                                fenshu = int(self.hongfangzongfen.text()) + dafenqi1_hong
                                                self.hongfangzongfen.setText(str(fenshu))


                                                if (dafenqi1_hong == 1):
                                                    print("声音")
                                                    music_path = r'music\yifen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_hong == 2):
                                                    music_path = r'music\liangfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_hong == 3):
                                                    music_path = r'music\sanfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_hong == 4):
                                                    music_path = r'music\sifen.wav'
                                                    self.sound(music_path)

                                                t = time.time()
                                                sql = "update dangqianbisai set caipanhong1=%s,caipanhong2=%s,caipanhong3=%s where bisaixuhao=%s" % (
                                                    dafenqi1_hong, dafenqi2_hong, dafenqi3_hong,
                                                    gl.get_value('bisaixuhao'))
                                                # print(sql)
                                                _thread.start_new_thread(self.stat.update, (sql,))
                                                # self.stat.update(sql)
                                                dafenqi1_hong = 0
                                                dafenqi2_hong = 0
                                                dafenqi3_hong = 0
                                                self.fencha(int(self.qingfangzongfen.text()), fenshu)


                                    elif (not dafenqi2_hong == 0 and dafenqi3_hong == dafenqi2_hong):
                                        print("2----------------------打分器得分----------------" + str(dafenqi2_hong))
                                        if(self.isfight):
                                            self.twoPointsTimeNowhong = self.twoPoinsTime(dafenqi2_hong)
                                            if (self.twoPointsTimeNowhong == None):
                                                fenshu = int(self.hongfangzongfen.text()) + dafenqi2_hong
                                                self.hongfangzongfen.setText(str(fenshu))


                                                if (dafenqi2_hong == 1):
                                                    print("声音")
                                                    music_path = r'music\yifen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi2_hong == 2):
                                                    music_path = r'music\liangfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi2_hong == 3):
                                                    music_path = r'music\sanfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi2_hong == 4):
                                                    music_path = r'music\sifen.wav'
                                                    self.sound(music_path)

                                                t = time.time()
                                                sql = "update dangqianbisai set caipanhong1=%s,caipanhong2=%s,caipanhong3=%s where bisaixuhao=%s" % (
                                                    dafenqi1_hong, dafenqi2_hong, dafenqi3_hong,
                                                    gl.get_value('bisaixuhao'))
                                                # print(sql)
                                                _thread.start_new_thread(self.stat.update, (sql,))
                                                # self.stat.update(sql)
                                                dafenqi1_hong = 0
                                                dafenqi2_hong = 0
                                                dafenqi3_hong = 0
                                                self.fencha(int(self.qingfangzongfen.text()), fenshu)


                                    elif (not dafenqi1_hong == 0 and dafenqi1_hong == dafenqi3_hong):
                                        print("3--------------------打分器得分---------------" + str(dafenqi1_hong))
                                        if(self.isfight):
                                            self.twoPointsTimeNowhong = self.twoPoinsTime(dafenqi1_hong)
                                            if (self.twoPointsTimeNowhong == None):
                                                fenshu = int(self.hongfangzongfen.text()) + dafenqi1_hong
                                                self.hongfangzongfen.setText(str(fenshu))

                                                if (dafenqi1_hong == 1):
                                                    print("声音")
                                                    music_path = r'music\yifen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_hong == 2):
                                                    music_path = r'music\liangfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_hong == 3):
                                                    music_path = r'music\sanfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_hong == 4):
                                                    music_path = r'music\sifen.wav'
                                                    self.sound(music_path)

                                                t = time.time()
                                                sql = "update dangqianbisai set caipanhong1=%s,caipanhong2=%s,caipanhong3=%s where bisaixuhao=%s" % (
                                                    dafenqi1_hong, dafenqi2_hong, dafenqi3_hong,
                                                    gl.get_value('bisaixuhao'))
                                                # print(sql)
                                                _thread.start_new_thread( self.stat.update, (sql,))
                                                # self.stat.update(sql)
                                                dafenqi1_hong = 0
                                                dafenqi2_hong = 0
                                                dafenqi3_hong = 0
                                                self.fencha(int(self.qingfangzongfen.text()), fenshu)



                                    elif (not dafenqi1_hong == 0 and dafenqi1_hong == dafenqi2_hong == dafenqi3_hong):
                                        print("4--------------------打分器得分---------------" + str(dafenqi1_hong))
                                        if(self.isfight):
                                            self.twoPointsTimeNowhong = self.twoPoinsTime(dafenqi1_hong)
                                            if (self.twoPointsTimeNowhong == None):
                                                fenshu = int(self.hongfangzongfen.text()) + dafenqi1_hong
                                                self.hongfangzongfen.setText(str(fenshu))


                                                if (dafenqi1_hong == 1):
                                                    print("声音")
                                                    music_path = r'music\yifen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_hong == 2):
                                                    music_path = r'music\liangfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_hong == 3):
                                                    music_path = r'music\sanfen.wav'
                                                    self.sound(music_path)
                                                elif (dafenqi1_hong == 4):
                                                    music_path = r'music\sifen.wav'
                                                    self.sound(music_path)

                                                t = time.time()
                                                sql = "update dangqianbisai set caipanhong1=%s,caipanhong2=%s,caipanhong3=%s where bisaixuhao=%s" % (
                                                    dafenqi1_hong,dafenqi2_hong,dafenqi3_hong,
                                                    gl.get_value('bisaixuhao'))
                                                # print(sql)
                                                # self.stat.update(sql)
                                                _thread.start_new_thread(self.stat.update, (sql,))
                                                dafenqi1_hong = 0
                                                dafenqi2_hong = 0
                                                dafenqi3_hong = 0
                                                self.fencha(int(self.qingfangzongfen.text()), fenshu)


                                    sql = "update bisaixinxi set hongfangdefen=%s where bisaixuhao=%s" % (
                                    self.hongfangzongfen.text(),
                                    gl.get_value('bisaixuhao'))
                                    # print(sql)
                                    # self.stat.update(sql)
                                    _thread.start_new_thread(self.stat.update, (sql,))
                                    # self.fencha(int(self.qingfangzongfen.text()),int(self.hongfangzongfen.text()))
                                    self.shuaxin_bt.click()
            # QApplication.processEvents()

    def getData2(self,x ):
        print(x)
        myout = []
        self.index_2 = 0
        firstlizhi = 0
        dafenqi1_qing = 0
        dafenqi2_qing = 0
        dafenqi3_qing = 0
        dafenqi1_hong = 0
        dafenqi2_hong = 0
        dafenqi3_hong = 0
        jishi = 0
        y=0
        z=0
        print(self.dataFlag)

        while self.dataFlag:

            if (self.isfirst):
                print("结束串口进程")
                _thread.exit()

            myout = []
            while x.inWaiting() > 0:
                myout.append(binascii.b2a_hex(x.read(1)))
                if(len(myout)==7):
                    break

            if myout != []:
                s = str(myout)
                last = s.replace("b'", "").replace("[", "").replace("']", "").replace(",", "").replace("' ",
                                                                                                       "").replace(
                    "b'_'", '')
                print(last)

                # 判断是电子护具(组别 红方 3 青方 2)还是打分器
                group_1 = last[5]
                lizhi = (self.transform_hex_data(myout[4]) << 8) + self.transform_hex_data(myout[3])
                print("力值",math.floor(lizhi / 10))
                # if(group_1=="2"):
                #
                #
                #     _thread.start_new_thread(self.qingfangzongfen.setText, (str(y),))
                #     y = y + 1
                # if(group_1=="3"):
                #     _thread.start_new_thread(self.hongfangzongfen.setText, (str(z),))
                #     z=z+1


                # time.sleep(0.01)






# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_db.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!












# def showseting():
#     _set.show()
#
# class setDBWindow(QtWidgets.QDialog):
#     def __init__(self):
#         super(setDBWindow,self).__init__()
#         self.new=MyDialog()
#         self.new.setupUi(self)

if __name__ == '__main__':

    # utils.mysqlUtil.MysqlUtil.host = '10.60.144.104'
    # utils.mysqlUtil.MysqlUtil.dbPort = '3306'
    # utils.mysqlUtil.MysqlUtil.username = 'root'
    # utils.mysqlUtil.MysqlUtil.password = '123321'
    # utils.mysqlUtil.MysqlUtil.database = 'sport'

    utils.mysqlUtil.MysqlUtil.host = 'localhost'
    utils.mysqlUtil.MysqlUtil.dbPort = '3306'
    utils.mysqlUtil.MysqlUtil.username = 'root'
    utils.mysqlUtil.MysqlUtil.password = 'lgm123'
    utils.mysqlUtil.MysqlUtil.database = 'sport'
    gl._init()
    app = QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    seting = setSettingWindow()
    windialog=winWindow()

    gl.set_value('seting',seting)
    gl.set_value('windialog',windialog)


    content = Ui_Form()
    content.setupUi(main)

    main.show()
    sys.exit(app.exec_())