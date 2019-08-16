# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blood.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import _thread
import datetime
import sys
import random
from PyQt5 import sip
import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
import time
#import utils.readCardUtils
# import utils.pyMysqlUtils



class Ui_Form(object):

    showMsgSignal = pyqtSignal(str)

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(1024, 768)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setAcceptDrops(False)
        Form.setStyleSheet("background-color:#000")


        self.dataFlag = False
        #记录当前为第几局
        self.count=0


        self.verticalLayoutWidget_19 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_19.setGeometry(QtCore.QRect(0, 50, 1024, 30))
        self.verticalLayoutWidget_19.setObjectName("verticalLayoutWidget_19")


        self.verticalLayout_7 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_19)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_19)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Arial Black")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("串口:")
        self.label_2.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.label_2)
        self.serial_port = QtWidgets.QLineEdit(self.verticalLayoutWidget_19)
        self.serial_port.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.serial_port.setObjectName("serial_port")
        self.serial_port.setText("COM5")
        self.serial_port.setFixedWidth(40)
        self.serial_port.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.serial_port)



        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_19)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label_3.setStyleSheet("color:#fff")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Arial Black")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("得分区间:")
        self.verticalLayout_7.addWidget(self.label_3)
        self.qujian = QtWidgets.QLineEdit(self.verticalLayoutWidget_19)
        self.qujian.setFixedWidth(30)
        self.qujian.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.qujian.setObjectName("serial_port")
        self.qujian.setText("2")
        self.qujian.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.qujian)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_19)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Arial Black")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setText("比赛时间:")

        self.label_4.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.label_4)
        self.bstime = QtWidgets.QLineEdit(self.verticalLayoutWidget_19)
        self.bstime.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.bstime.setObjectName("bstime")
        self.bstime.setText("90")
        self.bstime.setFixedWidth(40)
        self.bstime.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.bstime)


        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_19)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Arial Black")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("比赛局:")
        self.label_5.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.label_5)
        self.bsju = QtWidgets.QLineEdit(self.verticalLayoutWidget_19)
        self.bsju.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.bsju.setObjectName("bsju")
        self.bsju.setText("1")
        self.bsju.setFixedWidth(30)
        self.bsju.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.bsju)

        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_19)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Arial Black")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_5")
        self.label_10.setText("分差:")
        self.label_10.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.label_10)
        self.fencha = QtWidgets.QLineEdit(self.verticalLayoutWidget_19)
        self.fencha.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.fencha.setObjectName("bsju")
        self.fencha.setText("8")
        self.fencha.setFixedWidth(30)
        self.fencha.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.fencha)








        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_19)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Arial Black")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("红方单位:")
        self.label_6.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.label_6)
        self.hongfangdanwei = QtWidgets.QLineEdit(self.verticalLayoutWidget_19)
        self.hongfangdanwei.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.hongfangdanwei.setObjectName("hongfangdanwei")
        self.hongfangdanwei.setText("xx小学")
        self.hongfangdanwei.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.hongfangdanwei)

        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_19)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Arial Black")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_7.setText("红方姓名:")
        self.label_7.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.label_7)
        self.hongfangnm = QtWidgets.QLineEdit(self.verticalLayoutWidget_19)
        self.hongfangnm.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.hongfangnm.setObjectName("hongfangnm")
        self.hongfangnm.setText("xxx")
        self.hongfangnm.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.hongfangnm)

        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_19)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Arial Black")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_8.setText("青方单位:")
        self.label_8.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.label_8)
        self.qingfangdanwei = QtWidgets.QLineEdit(self.verticalLayoutWidget_19)
        self.qingfangdanwei.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.qingfangdanwei.setObjectName("qingfangdanwei")
        self.qingfangdanwei.setText("xx小学")
        self.qingfangdanwei.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.qingfangdanwei)

        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_19)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Arial Black")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_9.setText("青方姓名:")
        self.label_9.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.label_9)
        self.qingfangnm = QtWidgets.QLineEdit(self.verticalLayoutWidget_19)
        self.qingfangnm.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.qingfangnm.setObjectName("qingfangnm")
        self.qingfangnm.setText("xxx")
        self.qingfangnm.setStyleSheet("color:#fff")
        self.verticalLayout_7.addWidget(self.qingfangnm)









        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 400, 300, 280))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setStyleSheet("background-color:rgb(0,120,215)")


        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.qingfangscore = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qingfangscore.setGeometry(QtCore.QRect(0, 0, 300, 280))
        #self.qingfangscore.setMaximumSize(QtCore.QSize(300, 250))

        font = QtGui.QFont()
        font.setPointSize(160)
        font.setFamily("Arial Black")
        self.qingfangscore.setFont(font)
        self.qingfangscore.setText("0")
        self.qingfangscore.setStyleSheet(
            "color:#ffffff")
        self.qingfangscore.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangscore.setObjectName("qingfangscore")
        self.verticalLayout.addWidget(self.qingfangscore)

        self.verticalLayoutWidget_16 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_16.setGeometry(QtCore.QRect(0, 685, 470, 50))
        self.verticalLayoutWidget_16.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget_16.setStyleSheet("background-color:rgb(0,120,215)")

        self.qingjd = QtWidgets.QLabel(self.verticalLayoutWidget_16)
        self.qingjd.setGeometry(QtCore.QRect(220, 0, 50, 50))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")

        self.qingjd.setFont(font)
        self.qingjd.setText("7")
        self.qingjd.setStyleSheet(
            "color:#fff"

        )
        self.qingjd.setAlignment(QtCore.Qt.AlignCenter)
        self.qingjd.setObjectName("qingjd")





        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(624, 400, 300, 280))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setStyleSheet(" background-color:#ff0000")

        # self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        # self.verticalLayout_2.setObjectName("verticalLayout_2")


        self.hongfangscore = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.hongfangscore.setGeometry(QtCore.QRect(0, 0, 300, 280))
        #self.qingfangscore.setMaximumSize(QtCore.QSize(300, 250))

        font = QtGui.QFont()
        font.setPointSize(160)
        font.setFamily("Arial Black")
        self.hongfangscore.setFont(font)
        self.hongfangscore.setText("0")
        self.hongfangscore.setStyleSheet(
            "color:#ffffff")
        self.hongfangscore.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangscore.setObjectName("hongfangscore")

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0,0,1024,50))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setStyleSheet(" background-color:#000")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

#        self.zubie = QtWidgets.QLabel(self.)


        self.spacenum = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.spacenum.setGeometry(QtCore.QRect(30,15,30,30))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setFamily("Arial Black")
        self.spacenum.setFont(font)
        self.spacenum.setText("A")
        self.spacenum.setStyleSheet("color : #767475")

        self.num = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.num.setGeometry(QtCore.QRect(100, 15, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setFamily("Arial Black")
        self.num.setFont(font)
        self.num.setText("1")
        self.num.setStyleSheet("color : #767475")

        self.item = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.item.setGeometry(QtCore.QRect(180, 15, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setFamily("Arial Black")
        self.item.setFont(font)
        self.item.setText("男子儿童28KG")
        self.item.setStyleSheet("color : #767475")

        self.turn = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.turn.setGeometry(QtCore.QRect(650, 15, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setFamily("Arial Black")
        self.turn.setFont(font)
        self.turn.setText("1/8")
        self.turn.setStyleSheet("color : #767475")

        self.times = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.times.setGeometry(QtCore.QRect(750, 15, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("Arial Black")
        self.times.setFont(font)
        self.times.setText(time.strftime('%Y-%m-%d %H:%M:%S'))
        self.times.setStyleSheet("color : #767475")








        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(312, 150, 400, 150))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setStyleSheet(" background-color:#000")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.daojishi = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.daojishi.setGeometry(QtCore.QRect(0, 0, 280, 280))
        # self.qingfangscore.setMaximumSize(QtCore.QSize(300, 250))

        font = QtGui.QFont()
        font.setPointSize(70)
        font.setFamily("Arial Black")
        self.daojishi.setFont(font)
        self.daojishi.setText(str(datetime.timedelta(seconds=int(self.bstime.text())))[2:])
        self.daojishi.setStyleSheet(
            "color:#fff"
             )
        self.daojishi.setAlignment(QtCore.Qt.AlignCenter)
        self.daojishi.setObjectName("daojishi")
        self.verticalLayout_4.addWidget(self.daojishi)

        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 80, 300, 300))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setStyleSheet(" background-color:#000")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")




        self.qingfangunit = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.qingfangunit.setGeometry(QtCore.QRect(0, 50, 300, 100))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.qingfangunit.setFont(font)
        self.qingfangunit.setText(self.qingfangdanwei.text())
        self.qingfangunit.setStyleSheet(
            "color:rgb(0,120,215)")
        self.qingfangunit.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangunit.setObjectName("qingfangunit")

        self.qingfangname = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.qingfangname.setGeometry(QtCore.QRect(0, 150, 300, 100))
        # self.qingfangscore.setMaximumSize(QtCore.QSize(300, 250))

        font = QtGui.QFont()
        font.setPointSize(35)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.qingfangname.setFont(font)
        self.qingfangname.setText(self.qingfangnm.text())
        self.qingfangname.setStyleSheet(
            "color:rgb(0,120,215)")
        self.qingfangname.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangname.setObjectName("qingfangname")

        self.verticalLayoutWidget_6 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(704, 80, 300, 300))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setStyleSheet(" background-color:#000")

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.hongfangunit = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.hongfangunit.setGeometry(QtCore.QRect(0, 50, 300, 100))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.hongfangunit.setFont(font)
        self.hongfangunit.setText(self.hongfangdanwei.text())
        self.hongfangunit.setStyleSheet(
            "color:red")
        self.hongfangunit.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangunit.setObjectName("hongfangunit")


        self.hongfangname = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.hongfangname.setGeometry(QtCore.QRect(0,150, 300, 100))
        # self.qingfangscore.setMaximumSize(QtCore.QSize(300, 250))

        font = QtGui.QFont()
        font.setPointSize(35)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.hongfangname.setFont(font)
        self.hongfangname.setText(self.hongfangnm.text())
        self.hongfangname.setStyleSheet(
            "color:red")
        self.hongfangname.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangname.setObjectName("hongfangname")



        self.verticalLayoutWidget_7 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(462, 400, 100, 100))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setStyleSheet(

                                                  "border-width: 2px;border-style: solid;border-color: #767475 "
                                                  )

        self.gamenum = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.gamenum.setGeometry(QtCore.QRect(0, 0, 100, 100))

        font = QtGui.QFont()
        font.setPointSize(60)
        font.setFamily("Arial Black")

        self.gamenum.setFont(font)
        self.gamenum.setStyleSheet(
           "color:#00FE02"


            )
        self.gamenum.setAlignment(QtCore.Qt.AlignCenter)
        self.gamenum.setText("0")
        self.gamenum.setObjectName("gamenum")

        self.verticalLayoutWidget_8 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(405, 500, 40, 40))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setStyleSheet(

            "border-width: 2px;border-style: solid;border-color: #767475 "
        )

        self.qingfangscore_1 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.qingfangscore_1.setGeometry(QtCore.QRect(0, 0, 40, 40))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")

        self.qingfangscore_1.setFont(font)
        self.qingfangscore_1.setText("0")
        self.qingfangscore_1.setStyleSheet(
            "color:rgb(0,120,215)"

        )
        self.qingfangscore_1.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangscore_1.setObjectName("qingfangscore_1")

        self.verticalLayoutWidget_9 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(405, 545, 40, 40))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setStyleSheet(

            "border-width: 2px;border-style: solid;border-color: #767475 "
        )

        self.qingfangscore_2 = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        self.qingfangscore_2.setGeometry(QtCore.QRect(0, 0, 40, 40))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")

        self.qingfangscore_2.setFont(font)
        self.qingfangscore_2.setText("0")
        self.qingfangscore_2.setStyleSheet(
            "color:rgb(0,120,215)"

        )
        self.qingfangscore_2.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangscore_2.setObjectName("qingfangscore_2")

        self.verticalLayoutWidget_10 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(405, 590, 40, 40))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setStyleSheet(

            "border-width: 2px;border-style: solid;border-color: #767475 "
        )

        self.qingfangscore_3 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.qingfangscore_3.setGeometry(QtCore.QRect(0, 0, 40, 40))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")

        self.qingfangscore_3.setFont(font)
        self.qingfangscore_3.setText("0")
        self.qingfangscore_3.setStyleSheet(
            "color:rgb(0,120,215)"

        )
        self.qingfangscore_3.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangscore_3.setObjectName("qingfangscore_3")



        self.verticalLayoutWidget_14 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(400, 640, 112, 40))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayoutWidget_14.setStyleSheet(

            " background-color:rgb(0,120,215)"
        )

        self.qingfangscore_4 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        self.qingfangscore_4.setGeometry(QtCore.QRect(55, 0, 40, 40))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")

        self.qingfangscore_4.setFont(font)
        self.qingfangscore_4.setText("0")
        self.qingfangscore_4.setStyleSheet(
            "color:yellow"

        )
        self.qingfangscore_4.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfangscore_4.setObjectName("qingfangscore_4")



        self.verticalLayoutWidget_11 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(579, 500, 40, 40))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setStyleSheet(

            "border-width: 2px;border-style: solid;border-color: #767475 "
        )

        self.hongfangscore_1 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        self.hongfangscore_1.setGeometry(QtCore.QRect(0, 0, 40, 40))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")

        self.hongfangscore_1.setFont(font)
        self.hongfangscore_1.setText("0")
        self.hongfangscore_1.setStyleSheet(
            "color:red"

        )
        self.hongfangscore_1.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangscore_1.setObjectName("hongfangscore_1")

        self.verticalLayoutWidget_12 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(579, 545, 40, 40))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setStyleSheet(

            "border-width: 2px;border-style: solid;border-color: #767475 "
        )

        self.hongfangscore_2 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.hongfangscore_2.setGeometry(QtCore.QRect(0, 0, 40, 40))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")

        self.hongfangscore_2.setFont(font)
        self.hongfangscore_2.setText("0")
        self.hongfangscore_2.setStyleSheet(
            "color:red"

        )
        self.hongfangscore_2.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangscore_2.setObjectName("hongfangscore_2")

        self.verticalLayoutWidget_13 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(579, 590, 40, 40))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayoutWidget_13.setStyleSheet(

            "border-width: 2px;border-style: solid;border-color: #767475 "
        )

        self.hongfangscore_3 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.hongfangscore_3.setGeometry(QtCore.QRect(0, 0, 40, 40))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")

        self.hongfangscore_3.setFont(font)
        self.hongfangscore_3.setText("0")
        self.hongfangscore_3.setStyleSheet(
            "color:red"

        )
        self.hongfangscore_3.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangscore_3.setObjectName("hongfangscore_3")



        self.verticalLayoutWidget_15 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_15.setGeometry(QtCore.QRect(512, 640, 112, 40))
        self.verticalLayoutWidget_15.setObjectName("verticalLayoutWidget_15")
        self.verticalLayoutWidget_15.setStyleSheet(

            " background-color:red"
        )




        self.hongfangscore_4 = QtWidgets.QLabel(self.verticalLayoutWidget_15)
        self.hongfangscore_4.setGeometry(QtCore.QRect(20, 0, 40, 40))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")

        self.hongfangscore_4.setFont(font)
        self.hongfangscore_4.setText("0")
        self.hongfangscore_4.setStyleSheet(
            "color:yellow"

        )
        self.hongfangscore_4.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfangscore_4.setObjectName("hongfangscore_4")

        self.verticalLayoutWidget_17 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_17.setGeometry(QtCore.QRect(554, 685, 470, 50))
        self.verticalLayoutWidget_17.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget_17.setStyleSheet("background-color:red")


        self.redjd = QtWidgets.QLabel(self.verticalLayoutWidget_17)
        self.redjd.setGeometry(QtCore.QRect(200, 0, 50, 50))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")

        self.redjd.setFont(font)
        self.redjd.setText("0")
        self.redjd.setStyleSheet(
            "color:#fff"

        )
        self.redjd.setAlignment(QtCore.Qt.AlignCenter)
        self.redjd.setObjectName("redjd")



        self.verticalLayoutWidget_18 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_18.setGeometry(QtCore.QRect(470, 685, 84, 50))
        self.verticalLayoutWidget_18.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget_18.setStyleSheet("background-color:black")

        self.force = QtWidgets.QLabel(self.verticalLayoutWidget_18)
        self.force.setGeometry(QtCore.QRect(20, 0, 50, 50))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Black")

        self.force.setFont(font)
        self.force.setText(self.qujian.text())
        self.force.setStyleSheet(
            "color:#fff"

        )
        self.force.setAlignment(QtCore.Qt.AlignCenter)
        self.force.setObjectName("force")









        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 335, 80, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{color:#000000}"
                                       "QPushButton:hover{color:red}"
                                       "QPushButton{background-color:lightgreen}"
                                       "QPushButton{border:2px}"
                                       "QPushButton{border-radius:10px}"
                                       "QPushButton{padding:2px 4px}"


                                      )
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("开始")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 335, 80, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{color:#000000}"
                                      "QPushButton:hover{color:red}"
                                      "QPushButton{background-color:lightgreen}"
                                      "QPushButton{border:2px}"
                                      "QPushButton{border-radius:10px}"
                                      "QPushButton{padding:2px 4px}"

                                      )
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("暂停")

        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)



        self.timer = QTimer()
        self.timer.timeout.connect(self.on_timeout)
        self.timer_2 = QTimer()
        self.timer_2.timeout.connect(self.flush)
        self.timer_2.start(1000)





    def flush(self):

        self.times.setText(time.strftime('%Y-%m-%d %H:%M:%S'))


    def start(self):
        if self.serial_port.text()=='' or self.qujian=='' or self.bstime=='':
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw,'警告',"串口号和得分区间和比赛时间不能为空", QMessageBox.Ok)
            return

        try:

            self.force.setText(self.qujian.text())
            self.hongfangunit.setText(self.hongfangdanwei.text())
            self.hongfangname.setText(self.hongfangnm.text())
            self.qingfangunit.setText(self.qingfangdanwei.text())
            self.qingfangname.setText(self.qingfangnm.text())
            print('开始连接串口')
            x = serial.Serial(self.serial_port.text(), "115200")
            print(x)
            self.dataFlag = True
            _thread.start_new_thread( self.getData, (x, ) )
            self.gamenum.setText(self.bsju.text())
            self.timer.start(1000)
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            # t = Thread(target=self.getData,(x))
            # t.start()

        except:
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw,'错误',"连接串口失败，请检查串口号和波特率是否正确", QMessageBox.Ok)

    def stop(self):
        self.timer.stop()
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.daojishi.setText("暂停")
        self.dataFlag = False

    def jishi(self):
        self.y=3


    def on_timeout(self):
        if(int(self.bstime.text())>0):
            a=int(self.bstime.text())-1
            self.bstime.setText(str(a))
            self.daojishi.setText(str(datetime.timedelta(seconds=int(self.bstime.text())))[2:])
            h = int(self.hongfangscore.text())
            q = int(self.qingfangscore.text())
            c = int(self.fencha.text())
            if ((h - q) >= c):
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '消息', '红方胜', QMessageBox.Ok)
                self.index = 0
                self.index_2 = 0
                self.timer.stop()
                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(False)
                self.dataFlag = False
            elif ((q - h) >= c):
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '消息', '青方胜', QMessageBox.Ok)
                self.index = 0
                self.index_2 = 0
                self.timer.stop()
                self.pushButton.setEnabled(True)
                self.pushButton_2.setEnabled(False)
                self.dataFlag = False

            if(int(self.bstime.text()) == 0):

                self.bstime.setText("90")


                if(self.gamenum.text()=="1"):
                    qw = QtWidgets.QWidget()
                    QMessageBox.warning(qw, '消息', '时间到,第一局结束', QMessageBox.Ok)
                    self.timer.stop()
                    self.pushButton.setEnabled(True)
                    self.pushButton_2.setEnabled(False)
                    self.dataFlag = False

                    self.bsju.setText("2")

                elif(self.gamenum.text()=="2"):
                    qw = QtWidgets.QWidget()
                    QMessageBox.warning(qw, '消息', '时间到,第二局结束', QMessageBox.Ok)
                    self.timer.stop()
                    self.pushButton.setEnabled(True)
                    self.pushButton_2.setEnabled(False)
                    self.dataFlag = False

                    self.bsju.setText("3")

                elif (self.gamenum.text() == "3"):
                    self.timer.stop()
                    self.pushButton.setEnabled(True)
                    self.pushButton_2.setEnabled(False)
                    self.dataFlag = False



                    if ((int(self.hongfangscore.text()) - int(self.qingfangscore.text())) > 0):
                        qw = QtWidgets.QWidget()
                        QMessageBox.warning(qw, '消息', '时间到,红方胜', QMessageBox.Ok)
                    elif ((int(self.hongfangscore.text()) - int(self.qingfangscore.text())) < 0):
                        qw = QtWidgets.QWidget()
                        QMessageBox.warning(qw, '消息', '时间到,青方胜', QMessageBox.Ok)





    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

    def transform_hex_data(self,data):
        return int(data.hex(), 16)
    #
    # def openMyDialog(self):
    #
    #     self.setDBWindow = ui.ui_setting_test.setDBWindow()
    #     self.setDBWindow.show()
    #     my = MyDialog(self)
    #     # 在主窗口中连接信号和槽
    #     my.mySignal.connect(self.getDialogSignal)
    #     my.exec_()

    # def getDialogSignal(self, connect):
    #     print(connect)
    #


      #  self.show()
    def getData(self,x):


        print(x)
        myout = []

        self.index = 0
        self.index_2 = 0
        firstlizhi = 0
        dafenqi4 = 0
        dafenqi5 = 0
        dafenqi6 = 0
        jishi = 0

        while self.dataFlag:

            while x.inWaiting() > 0:
                myout.append(x.read(1))

            if myout != []:
                # myout = [b'\xAA', b'\x02', b'\x00', b'\x01', b'\xD0', b'\xD1', b'\xD2', b'\x01']

                # print(equipment.calculate_time(myout).sport_time)
                # self.showGrade(equipment.calculate_time(myout).run_num,equipment.calculate_time(myout).sport_time)
                print(myout)
               # s = str(myout[0:])
                s=str(myout)
                #   print(s)
                last = s.replace("b'\\x", "").replace("[", "").replace("']", "").replace(",", "").replace("' ",
                                                                                                          "").replace(
                    "b'_'", '')
                #   print(last)
                value = last[8:10] + last[6:8]
                #print(value)
                group_1 = last[3]
                group = last[9]
                print("组别" + group)
                # print("组别" + group_1)
                if (group_1 == "2" or group_1 == "3"):
                    print("------------------护具-------------------")
                    # print(transform_hex_data(myout[3]))
                    # print(transform_hex_data(myout[4]))

                    self.index = self.index + 1
                    print(self.index)

                    lizhi = (self.transform_hex_data(myout[4]) << 8) + self.transform_hex_data(myout[3])
                    print(lizhi)
                    if (self.index == 1):
                        firstlizhi = lizhi
                    print("第一次力值" + str(firstlizhi))
                    print(lizhi)





                    if(group_1 == "2"):
                        if (lizhi < (firstlizhi - (30 * int(self.qujian.text())))):
                                # if(lizhi > (firstlizhi - (30 * (int(self.qujian.text()) + 1)))):
                                #     self.qingjd.setText(str(int(self.qujian.text()) + 1))
                                # elif (lizhi > (firstlizhi - (30 * (int(self.qujian.text()) + 2)))):
                                #     self.qingjd.setText(str(int(self.qujian.text()) + 2))
                                # elif (lizhi > (firstlizhi - (30 * (int(self.qujian.text()) + 3)))):
                                #     self.qingjd.setText(str(int(self.qujian.text()) + 3))
                                # elif (lizhi > (firstlizhi - (30 * (int(self.qujian.text()) + 4)))):
                                #     self.qingjd.setText(str(int(self.qujian.text()) + 4))
                                # elif (lizhi > (firstlizhi - (30 * (int(self.qujian.text()) + 5)))):
                                #     self.qingjd.setText(str(int(self.qujian.text()) + 5))
                                # elif (lizhi > (firstlizhi - (30 * (int(self.qujian.text()) + 6)))):
                                #     self.qingjd.setText(str(int(self.qujian.text()) + 6))

                                print("得2分")
                                self.qingjd.setText("2")
                                self.qingfangscore.setText(str(int(self.qingfangscore.text()) + 2))
                    if(group_1 == "3"):
                        if (lizhi < (firstlizhi - (30 * int(self.qujian.text())))):
                        #if (lizhi > (firstlizhi - (30 * (int(self.qujian.text()) )))):
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
                            self.hongfangscore.setText(str(int(self.hongfangscore.text())+2))
                            print("得2分")
                            self.redjd.setText("2")
                    print("当力值小于" + str(firstlizhi - (30 * int(self.qujian.text()))) + "得两分")
                    print("ID:" + str(lizhi))

                    print(value)

                    now = value
                    myout = []
                # 组别 红方 3 青方 2

                # 进入打分器
                if (group_1 == "4" or group_1 == "5" or group_1 == "6"):
                    self.index_2 = self.index_2 + 1
                    if (self.index_2 == 1):
                        t = time.time()
                    #      print("3秒计时开始")

                    t1 = time.time()
                    if (t1 - t > 1):
                        t = time.time()
                        print("重新开始3秒计时")
                        dafenqi4 = 0
                        dafenqi5 = 0
                        dafenqi6 = 0
                        self.qingfangscore_1.setText(str(dafenqi4))
                        self.qingfangscore_2.setText(str(dafenqi5))
                        self.qingfangscore_3.setText(str(dafenqi6))
                        self.hongfangscore_1.setText(str(dafenqi4))
                        self.hongfangscore_2.setText(str(dafenqi5))
                        self.hongfangscore_3.setText(str(dafenqi6))
                    # print("计时开始"+str(t))
                    if (group_1 == "4"):
                        t4 = time.time()
                        print("4号打分器打分时间" + str(t4 - t))

                        # dafenqi4 = 0
                        # self.qingfangscore_1.setText(str(dafenqi4))
                        # self.hongfangscore_1.setText(str(dafenqi4))
                        #   print("----------打分器-------")

                        value4 = last[7]
                        print("打分器" + group_1 + "打分：" + value4)
                        if (t4 - t < 3):
                            dafenqi4 = int(value4)
                        group = last[9]
                        #    print("组别"+group)
                        myout = []

                    if (group_1 == "5"):
                        t5 = time.time()
                        print("5号打分器打分时间" + str(t5 - t))
                        #   print("----------打分器-------")


                        # dafenqi5 = 0
                        #
                        # self.qingfangscore_2.setText(str(dafenqi5))
                        #
                        # self.hongfangscore_2.setText(str(dafenqi5))


                        value5 = last[7]
                        print("打分器" + group_1 + "打分：" + value5)
                        if (t5 - t < 3):
                            dafenqi5 = int(value5)
                        group = last[9]
                        #   print("组别" + group)
                        myout = []
                    if (group_1 == "6"):
                        t6 = time.time()
                        print("6号打分器打分时间" + str(t6 - t))

                        #  print("----------打分器-------")

                        # time.sleep(4)
                        # dafenqi6 = 0
                        #
                        # self.qingfangscore_3.setText(str(dafenqi6))
                        #
                        # self.hongfangscore_3.setText(str(dafenqi6))

                        value6 = last[7]
                        print("打分器" + group_1 + "打分：" + value6)
                        if (t6 - t < 3):
                            dafenqi6 = int(value6)

                        group = last[9]

                        myout = []
                    #   print("组别" + group)

                    if (t1 - t <= 1):

                        if(group=="2"):
                            self.qingfangscore_1.setText(str(dafenqi4))
                            self.qingfangscore_2.setText(str(dafenqi5))
                            self.qingfangscore_3.setText(str(dafenqi6))
                        if (group == "3"):
                            self.hongfangscore_1.setText(str(dafenqi4))
                            self.hongfangscore_2.setText(str(dafenqi5))
                            self.hongfangscore_3.setText(str(dafenqi6))

                        if (not dafenqi4 == 0 and dafenqi4 == dafenqi5):
                            print("1----------------------打分器得分------------------" + str(dafenqi4))

                            if(group == "3"):
                                self.hongfangscore.setText(str(int(self.hongfangscore.text())+dafenqi4))
                                self.hongfangscore_4.setText(str(int(self.hongfangscore.text()) + dafenqi4))
                            if(group == "2"):
                                self.qingfangscore.setText(str(int(self.qingfangscore.text())+dafenqi4))
                                self.qingfangscore_4.setText(str(int(self.qingfangscore.text()) + dafenqi4))
                            t = time.time()
                            dafenqi4 = 0
                            dafenqi5 = 0
                            dafenqi6 = 0

                            self.qingfangscore_1.setText(str(dafenqi4))
                            self.qingfangscore_2.setText(str(dafenqi5))
                            self.qingfangscore_3.setText(str(dafenqi6))
                            self.hongfangscore_1.setText(str(dafenqi4))
                            self.hongfangscore_2.setText(str(dafenqi5))
                            self.hongfangscore_3.setText(str(dafenqi6))



                        elif (not dafenqi5 == 0 and dafenqi6 == dafenqi5):
                            print("2----------------------打分器得分----------------" + str(dafenqi6))
                            if (group == "3"):
                                self.hongfangscore.setText(str(int(self.hongfangscore.text()) + dafenqi5))
                                self.hongfangscore_4.setText(str(int(self.hongfangscore.text()) + dafenqi5))
                            if (group == "2"):
                                self.qingfangscore.setText(str(int(self.qingfangscore.text()) + dafenqi5))
                                self.qingfangscore_4.setText(str(int(self.qingfangscore.text()) + dafenqi5))

                            t = time.time()
                            dafenqi4 = 0
                            dafenqi5 = 0
                            dafenqi6 = 0

                            self.qingfangscore_1.setText(str(dafenqi4))
                            self.qingfangscore_2.setText(str(dafenqi5))
                            self.qingfangscore_3.setText(str(dafenqi6))
                            self.hongfangscore_1.setText(str(dafenqi4))
                            self.hongfangscore_2.setText(str(dafenqi5))
                            self.hongfangscore_3.setText(str(dafenqi6))


                        elif (not dafenqi4 == 0 and dafenqi4 == dafenqi6):
                            print("3--------------------打分器得分---------------" + str(dafenqi6))
                            if (group == "3"):

                                self.hongfangscore.setText(str(int(self.hongfangscore.text()) + dafenqi4))
                                self.hongfangscore_4.setText(str(int(self.hongfangscore.text()) + dafenqi4))

                            if (group == "2"):

                                self.qingfangscore.setText(str(int(self.qingfangscore.text()) + dafenqi4))
                                self.qingfangscore_4.setText(str(int(self.qingfangscore.text()) + dafenqi4))
                            t = time.time()
                            dafenqi4 = 0
                            dafenqi5 = 0
                            dafenqi6 = 0


                            self.qingfangscore_1.setText(str(dafenqi4))
                            self.qingfangscore_2.setText(str(dafenqi5))
                            self.qingfangscore_3.setText(str(dafenqi6))
                            self.hongfangscore_1.setText(str(dafenqi4))
                            self.hongfangscore_2.setText(str(dafenqi5))
                            self.hongfangscore_3.setText(str(dafenqi6))


                        elif (not dafenqi4 == 0 and dafenqi4 == dafenqi5 == dafenqi6):
                            print("4-------------------打分器得分---------------------" + str(dafenqi6))
                            if (group == "3"):
                                self.hongfangscore.setText(str(int(self.hongfangscore.text()) + dafenqi4))
                                self.hongfangscore_4.setText(str(int(self.hongfangscore.text()) + dafenqi4))


                            if (group == "2"):
                                self.qingfangscore.setText(str(int(self.qingfangscore.text()) + dafenqi4))
                                self.qingfangscore_4.setText(str(int(self.qingfangscore.text()) + dafenqi4))

                            t = time.time()
                            dafenqi4 = 0
                            dafenqi5 = 0
                            dafenqi6 = 0


                            self.qingfangscore_1.setText(str(dafenqi4))
                            self.qingfangscore_2.setText(str(dafenqi5))
                            self.qingfangscore_3.setText(str(dafenqi6))
                            self.hongfangscore_1.setText(str(dafenqi4))
                            self.hongfangscore_2.setText(str(dafenqi5))
                            self.hongfangscore_3.setText(str(dafenqi6))



# def showseting():
#     _set.show()
#
# class setDBWindow(QtWidgets.QDialog):
#     def __init__(self):
#         super(setDBWindow,self).__init__()
#         self.new=MyDialog()
#         self.new.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    content = Ui_Form()
    content.setupUi(main)

    main.show()
    sys.exit(app.exec_())