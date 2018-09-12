# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'run.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QObject,pyqtSignal
# sys.path.append('C:/Users/admin/Desktop/sport')
import utils.readCardUtils
# import utils.pyMysqlUtils
import utils.mysqlUtil
import serial
import uuid
import time
import _thread
# from threading import Thread
# from utils.readCardUtils import *


class Ui_Form(QObject):

    nowPerson=0
    allPerson=0
    dataFlag = False
    readCardFlag = False
    showMsgSignal = pyqtSignal(str)
    lastCardId = ''
    stat = utils.mysqlUtil.MysqlUtil()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 768)
        Form.setWhatsThis("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 1011, 54))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(240, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(50, 20))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.serial_port = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.serial_port.setMaximumSize(QtCore.QSize(60, 16777215))
        self.serial_port.setObjectName("serial_port")
        self.horizontalLayout_2.addWidget(self.serial_port)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(50, 20))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.baud_rate = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.baud_rate.setMaximumSize(QtCore.QSize(60, 16777215))
        self.baud_rate.setObjectName("baud_rate")
        self.horizontalLayout_3.addWidget(self.baud_rate)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 1011, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sb_title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sb_title.setMinimumSize(QtCore.QSize(200, 40))
        self.sb_title.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sb_title.setFont(font)
        self.sb_title.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_title.setObjectName("sb_title")
        self.horizontalLayout_4.addWidget(self.sb_title)
        self.bh_title_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.bh_title_1.setMinimumSize(QtCore.QSize(200, 40))
        self.bh_title_1.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bh_title_1.setFont(font)
        self.bh_title_1.setAlignment(QtCore.Qt.AlignCenter)
        self.bh_title_1.setObjectName("bh_title_1")
        self.horizontalLayout_4.addWidget(self.bh_title_1)
        self.xm_title_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.xm_title_1.setMinimumSize(QtCore.QSize(200, 40))
        self.xm_title_1.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.xm_title_1.setFont(font)
        self.xm_title_1.setAlignment(QtCore.Qt.AlignCenter)
        self.xm_title_1.setObjectName("xm_title_1")
        self.horizontalLayout_4.addWidget(self.xm_title_1)
        self.cj_title_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cj_title_1.setMinimumSize(QtCore.QSize(200, 40))
        self.cj_title_1.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cj_title_1.setFont(font)
        self.cj_title_1.setAlignment(QtCore.Qt.AlignCenter)
        self.cj_title_1.setObjectName("cj_title_1")
        self.horizontalLayout_4.addWidget(self.cj_title_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sb_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sb_1.setMinimumSize(QtCore.QSize(200, 40))
        self.sb_1.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sb_1.setFont(font)
        self.sb_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_1.setObjectName("sb_1")
        self.horizontalLayout_5.addWidget(self.sb_1)
        self.bh_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.bh_1.setMinimumSize(QtCore.QSize(200, 30))
        self.bh_1.setMaximumSize(QtCore.QSize(130, 16777215))
        self.bh_1.setReadOnly(True)
        self.bh_1.setObjectName("bh_1")
        self.horizontalLayout_5.addWidget(self.bh_1)
        self.mc_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mc_1.setMinimumSize(QtCore.QSize(200, 40))
        self.mc_1.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mc_1.setFont(font)
        self.mc_1.setText("")
        self.mc_1.setAlignment(QtCore.Qt.AlignCenter)
        self.mc_1.setObjectName("mc_1")
        self.horizontalLayout_5.addWidget(self.mc_1)
        self.cj_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cj_1.setMinimumSize(QtCore.QSize(200, 40))
        self.cj_1.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cj_1.setFont(font)
        self.cj_1.setText("")
        self.cj_1.setAlignment(QtCore.Qt.AlignCenter)
        self.cj_1.setObjectName("cj_1")
        self.horizontalLayout_5.addWidget(self.cj_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sb_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sb_2.setMinimumSize(QtCore.QSize(200, 40))
        self.sb_2.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sb_2.setFont(font)
        self.sb_2.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_2.setObjectName("sb_2")
        self.horizontalLayout_6.addWidget(self.sb_2)
        self.bh_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.bh_2.setMinimumSize(QtCore.QSize(200, 30))
        self.bh_2.setMaximumSize(QtCore.QSize(130, 16777215))
        self.bh_2.setReadOnly(True)
        self.bh_2.setObjectName("bh_2")
        self.horizontalLayout_6.addWidget(self.bh_2)
        self.mc_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mc_2.setMinimumSize(QtCore.QSize(200, 40))
        self.mc_2.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mc_2.setFont(font)
        self.mc_2.setText("")
        self.mc_2.setAlignment(QtCore.Qt.AlignCenter)
        self.mc_2.setObjectName("mc_2")
        self.horizontalLayout_6.addWidget(self.mc_2)
        self.cj_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cj_2.setMinimumSize(QtCore.QSize(200, 40))
        self.cj_2.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cj_2.setFont(font)
        self.cj_2.setText("")
        self.cj_2.setAlignment(QtCore.Qt.AlignCenter)
        self.cj_2.setObjectName("cj_2")
        self.horizontalLayout_6.addWidget(self.cj_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sb_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sb_3.setMinimumSize(QtCore.QSize(200, 40))
        self.sb_3.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sb_3.setFont(font)
        self.sb_3.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_3.setObjectName("sb_3")
        self.horizontalLayout_7.addWidget(self.sb_3)
        self.bh_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.bh_3.setMinimumSize(QtCore.QSize(200, 30))
        self.bh_3.setMaximumSize(QtCore.QSize(130, 16777215))
        self.bh_3.setReadOnly(True)
        self.bh_3.setObjectName("bh_3")
        self.horizontalLayout_7.addWidget(self.bh_3)
        self.mc_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mc_3.setMinimumSize(QtCore.QSize(200, 40))
        self.mc_3.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mc_3.setFont(font)
        self.mc_3.setText("")
        self.mc_3.setAlignment(QtCore.Qt.AlignCenter)
        self.mc_3.setObjectName("mc_3")
        self.horizontalLayout_7.addWidget(self.mc_3)
        self.cj_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cj_3.setMinimumSize(QtCore.QSize(200, 40))
        self.cj_3.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cj_3.setFont(font)
        self.cj_3.setText("")
        self.cj_3.setAlignment(QtCore.Qt.AlignCenter)
        self.cj_3.setObjectName("cj_3")
        self.horizontalLayout_7.addWidget(self.cj_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.sb_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sb_4.setMinimumSize(QtCore.QSize(200, 40))
        self.sb_4.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sb_4.setFont(font)
        self.sb_4.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_4.setObjectName("sb_4")
        self.horizontalLayout_8.addWidget(self.sb_4)
        self.bh_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.bh_4.setMinimumSize(QtCore.QSize(200, 30))
        self.bh_4.setMaximumSize(QtCore.QSize(130, 16777215))
        self.bh_4.setReadOnly(True)
        self.bh_4.setObjectName("bh_4")
        self.horizontalLayout_8.addWidget(self.bh_4)
        self.mc_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mc_4.setMinimumSize(QtCore.QSize(200, 40))
        self.mc_4.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mc_4.setFont(font)
        self.mc_4.setText("")
        self.mc_4.setAlignment(QtCore.Qt.AlignCenter)
        self.mc_4.setObjectName("mc_4")
        self.horizontalLayout_8.addWidget(self.mc_4)
        self.cj_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cj_4.setMinimumSize(QtCore.QSize(200, 40))
        self.cj_4.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cj_4.setFont(font)
        self.cj_4.setText("")
        self.cj_4.setAlignment(QtCore.Qt.AlignCenter)
        self.cj_4.setObjectName("cj_4")
        self.horizontalLayout_8.addWidget(self.cj_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.sb_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sb_5.setMinimumSize(QtCore.QSize(200, 40))
        self.sb_5.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sb_5.setFont(font)
        self.sb_5.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_5.setObjectName("sb_5")
        self.horizontalLayout_9.addWidget(self.sb_5)
        self.bh_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.bh_5.setMinimumSize(QtCore.QSize(200, 30))
        self.bh_5.setMaximumSize(QtCore.QSize(130, 16777215))
        self.bh_5.setReadOnly(True)
        self.bh_5.setObjectName("bh_5")
        self.horizontalLayout_9.addWidget(self.bh_5)
        self.mc_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mc_5.setMinimumSize(QtCore.QSize(200, 40))
        self.mc_5.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mc_5.setFont(font)
        self.mc_5.setText("")
        self.mc_5.setAlignment(QtCore.Qt.AlignCenter)
        self.mc_5.setObjectName("mc_5")
        self.horizontalLayout_9.addWidget(self.mc_5)
        self.cj_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cj_5.setMinimumSize(QtCore.QSize(200, 40))
        self.cj_5.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cj_5.setFont(font)
        self.cj_5.setText("")
        self.cj_5.setAlignment(QtCore.Qt.AlignCenter)
        self.cj_5.setObjectName("cj_5")
        self.horizontalLayout_9.addWidget(self.cj_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.sb_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sb_6.setMinimumSize(QtCore.QSize(200, 40))
        self.sb_6.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sb_6.setFont(font)
        self.sb_6.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_6.setObjectName("sb_6")
        self.horizontalLayout_10.addWidget(self.sb_6)
        self.bh_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.bh_6.setMinimumSize(QtCore.QSize(200, 30))
        self.bh_6.setMaximumSize(QtCore.QSize(130, 16777215))
        self.bh_6.setReadOnly(True)
        self.bh_6.setObjectName("bh_6")
        self.horizontalLayout_10.addWidget(self.bh_6)
        self.mc_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mc_6.setMinimumSize(QtCore.QSize(200, 40))
        self.mc_6.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mc_6.setFont(font)
        self.mc_6.setText("")
        self.mc_6.setAlignment(QtCore.Qt.AlignCenter)
        self.mc_6.setObjectName("mc_6")
        self.horizontalLayout_10.addWidget(self.mc_6)
        self.cj_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cj_6.setMinimumSize(QtCore.QSize(200, 40))
        self.cj_6.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cj_6.setFont(font)
        self.cj_6.setText("")
        self.cj_6.setAlignment(QtCore.Qt.AlignCenter)
        self.cj_6.setObjectName("cj_6")
        self.horizontalLayout_10.addWidget(self.cj_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.sb_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sb_7.setMinimumSize(QtCore.QSize(200, 40))
        self.sb_7.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sb_7.setFont(font)
        self.sb_7.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_7.setObjectName("sb_7")
        self.horizontalLayout_11.addWidget(self.sb_7)
        self.bh_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.bh_7.setMinimumSize(QtCore.QSize(200, 30))
        self.bh_7.setMaximumSize(QtCore.QSize(130, 16777215))
        self.bh_7.setReadOnly(True)
        self.bh_7.setObjectName("bh_7")
        self.horizontalLayout_11.addWidget(self.bh_7)
        self.mc_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mc_7.setMinimumSize(QtCore.QSize(200, 40))
        self.mc_7.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mc_7.setFont(font)
        self.mc_7.setText("")
        self.mc_7.setAlignment(QtCore.Qt.AlignCenter)
        self.mc_7.setObjectName("mc_7")
        self.horizontalLayout_11.addWidget(self.mc_7)
        self.cj_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cj_7.setMinimumSize(QtCore.QSize(200, 40))
        self.cj_7.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cj_7.setFont(font)
        self.cj_7.setText("")
        self.cj_7.setAlignment(QtCore.Qt.AlignCenter)
        self.cj_7.setObjectName("cj_7")
        self.horizontalLayout_11.addWidget(self.cj_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.sb_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.sb_8.setMinimumSize(QtCore.QSize(200, 40))
        self.sb_8.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sb_8.setFont(font)
        self.sb_8.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_8.setObjectName("sb_8")
        self.horizontalLayout_12.addWidget(self.sb_8)
        self.bh_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.bh_8.setMinimumSize(QtCore.QSize(200, 30))
        self.bh_8.setMaximumSize(QtCore.QSize(130, 16777215))
        self.bh_8.setReadOnly(True)
        self.bh_8.setObjectName("bh_8")
        self.horizontalLayout_12.addWidget(self.bh_8)
        self.mc_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.mc_8.setMinimumSize(QtCore.QSize(200, 40))
        self.mc_8.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.mc_8.setFont(font)
        self.mc_8.setText("")
        self.mc_8.setAlignment(QtCore.Qt.AlignCenter)
        self.mc_8.setObjectName("mc_8")
        self.horizontalLayout_12.addWidget(self.mc_8)
        self.cj_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cj_8.setMinimumSize(QtCore.QSize(200, 40))
        self.cj_8.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cj_8.setFont(font)
        self.cj_8.setText("")
        self.cj_8.setAlignment(QtCore.Qt.AlignCenter)
        self.cj_8.setObjectName("cj_8")
        self.horizontalLayout_12.addWidget(self.cj_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.passNumber = QtWidgets.QLineEdit(Form)
        self.passNumber.setGeometry(QtCore.QRect(260, 100, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.passNumber.setFont(font)
        self.passNumber.setText("")
        self.passNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.passNumber.setObjectName("passNumber")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 100, 100, 40))
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.max_device = QtWidgets.QLineEdit(Form)
        self.max_device.setGeometry(QtCore.QRect(620, 100, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.max_device.setFont(font)
        self.max_device.setAlignment(QtCore.Qt.AlignCenter)
        self.max_device.setObjectName("max_device")
        self.max_device_title = QtWidgets.QLabel(Form)
        self.max_device_title.setGeometry(QtCore.QRect(500, 100, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.max_device_title.setFont(font)
        self.max_device_title.setObjectName("max_device_title")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.bhList = [self.bh_1,self.bh_2,self.bh_3,self.bh_4,self.bh_5,self.bh_6,self.bh_7,self.bh_8]
        self.mcList = [self.mc_1,self.mc_2,self.mc_3,self.mc_4,self.mc_5,self.mc_6,self.mc_7,self.mc_8]
        self.cjList = [self.cj_1,self.cj_2,self.cj_3,self.cj_4,self.cj_5,self.cj_6,self.cj_7,self.cj_8]
        self.userIds = ['','','','','','','','']

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "50米测试"))
        self.label_2.setText(_translate("Form", "串  口："))
        self.label_3.setText(_translate("Form", "波特率："))
        self.pushButton.setText(_translate("Form", "开始检录"))
        self.pushButton_6.setText(_translate("Form", "停止检录"))
        self.pushButton_5.setText(_translate("Form", "下一个"))
        self.pushButton_2.setText(_translate("Form", "开始接收数据"))
        self.pushButton_3.setText(_translate("Form", "停止接收数据"))
        self.pushButton_4.setText(_translate("Form", "清零"))
        self.sb_title.setText(_translate("Form", "设备"))
        self.bh_title_1.setText(_translate("Form", "人员编号"))
        self.xm_title_1.setText(_translate("Form", "姓名"))
        self.cj_title_1.setText(_translate("Form", "成  绩"))
        self.sb_1.setText(_translate("Form", "设备1："))
        self.sb_2.setText(_translate("Form", "设备2："))
        self.sb_3.setText(_translate("Form", "设备3："))
        self.sb_4.setText(_translate("Form", "设备4："))
        self.sb_5.setText(_translate("Form", "设备5："))
        self.sb_6.setText(_translate("Form", "设备6："))
        self.sb_7.setText(_translate("Form", "设备7："))
        self.sb_8.setText(_translate("Form", "设备8："))
        self.pushButton_7.setText(_translate("Form", "过号"))
        self.max_device.setText(_translate("Form", "0"))
        self.max_device_title.setText(_translate("Form", "可用设备数："))

        self.pushButton.clicked.connect(self.runReadCard)
        self.pushButton_5.clicked.connect(self.nextPerson)
        self.pushButton_6.clicked.connect(self.stopReadCard)
        self.pushButton_2.clicked.connect(self.startRun)
        self.pushButton_3.clicked.connect(self.stopData)
        self.pushButton_4.clicked.connect(self.clearText)
        self.pushButton_7.clicked.connect(self.passPersion)

        self.showMsgSignal.connect(self.showMsg)

    # def readPerson(self):
    #     if(self.nowPerson>=8):
    #         qw = QtWidgets.QWidget()
    #         QMessageBox.warning(qw,'警告','单次最多检录8人', QMessageBox.Ok)
    #     else:
    #         self.writeInfo()

    def runReadCard(self):
        self.lastCardId = ''
        _thread.start_new_thread(self.readCard,())

    def readCard(self):
        self.readCardFlag = True
        self.pushButton.setEnabled(False)
        self.pushButton.setText("正在检录")
        while self.readCardFlag:
            cardId = utils.readCardUtils.getCardId(self.lastCardId)
            if cardId!='':
                self.lastCardId = cardId
                _thread.start_new_thread( self.writeInfo, (cardId, ) )

    #停止检录
    def stopReadCard(self):
        self.readCardFlag = False
        self.pushButton.setEnabled(True)
        self.pushButton.setText("开始检录")

    #显示对话框
    def showMsg(self,msg):
        qw = QtWidgets.QWidget()
        QMessageBox.warning(qw,'消息',msg)

    #刷卡检录
    def writeInfo(self,cardId):
        # if cardId=='':
        #     qw = QtWidgets.QWidget()
        #     QMessageBox.warning(qw,'警告','请先放卡再点击检录', QMessageBox.Ok)
        #     return
        results = self.stat.fetchall("select * from user_info where card_number=%s"%cardId)
        # print(results)
        if results==():
            # qw = QtWidgets.QWidget()
            # QMessageBox.warning(qw,'警告','非本系统卡', QMessageBox.Ok)
            self.showMsgSignal.emit("非本系统卡")
        else:
            sql = "INSERT INTO run_check(id,job_number,name,user_id,create_time) VALUES('%s','%s','%s','%s','%s')"%(uuid.uuid1(),results[0][4],results[0][1],results[0][0],time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            if self.stat.insert(sql)>0:
                # qw = QtWidgets.QWidget()
                # QMessageBox.warning(qw,'消息',results[0][1]+" "+results[0][4]+" 检录成功", QMessageBox.Ok)
                self.showMsgSignal.emit(results[0][1]+" "+results[0][4]+" 检录成功")
            else:
                # qw = QtWidgets.QWidget()
                # QMessageBox.warning(qw,'错误',"检录失败", QMessageBox.Ok)
                self.showMsgSignal.emit("检录失败")
            # bh.setText(results[0][4])
            # mc.setText(results[0][1])
            # self.userIds.append(results[0][0])
            # self.nowPerson+=1
            # self.allPerson+=1

    def startRun(self):
        if self.serial_port.text()=='' or self.baud_rate.text()=='':
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw,'警告',"串口号和波特率不能为空", QMessageBox.Ok)
            return
        try:
            x = serial.Serial(self.serial_port.text(), self.baud_rate.text())
            self.dataFlag = True
            self.pushButton_3.setEnabled(True)
            _thread.start_new_thread( self.getData, (x, ) )
            # t = Thread(target=self.getData,(x))
            # t.start()
        except:
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw,'错误',"连接串口失败，请检查串口号和波特率是否正确", QMessageBox.Ok)
# [b'\xaa', b'\x02', b'\x01', b'\x02']

    def stopData(self):
        self.dataFlag = False

    #计时
    def getData(self,x):
        self.pushButton_2.setText('接收数据中')
        self.pushButton_2.setEnabled(False)
        myout = []
        while self.dataFlag:
            while x.inWaiting() > 0:
                myout.append(x.read(1))
            if myout != []:
                # print(equipment.calculate_time(myout).run_num)
                # print(equipment.calculate_time(myout).sport_time)
                if self.bhList[self.calculate_time(myout).run_num-1].text()=="":
                    continue
                self.cjList[self.calculate_time(myout).run_num-1].setText(str(self.calculate_time(myout).sport_time))
                self.uploadGrade(self.calculate_time(myout).run_num-1)
                # print(equipment.calculate_time(myout).sport_time)
                # self.showGrade(equipment.calculate_time(myout).run_num,equipment.calculate_time(myout).sport_time)
                myout = []
        self.pushButton_2.setText('开始接收数据')
        self.pushButton_2.setEnabled(True)

    def nextPerson(self):
        if self.allPerson>=int(self.max_device.text()):
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw,'警告','单次最多检录'+self.max_device.text()+'人', QMessageBox.Ok)
            return
        sql = "SELECT id,job_number,name,user_id FROM run_check ORDER BY create_time LIMIT 1"
        results = self.stat.fetchall(sql)
        if results==():
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw,'警告','无检录人员', QMessageBox.Ok)
            return
        for index,userId in enumerate(self.userIds):
            if(self.userIds[index]==""):
                self.userIds[index] = results[0][3]
                self.bhList[index].setText(results[0][1]) 
                self.mcList[index].setText(results[0][2])
                self.allPerson+=1
                break
        sql = "DELETE FROM run_check WHERE id='%s'"%results[0][0]
        self.stat.delete(sql)

    #上传成绩
    def uploadGrade(self,uploadNo):
        sql = "INSERT INTO run_result(id,grade,user_id,create_time) VALUES('%s','%s','%s','%s')"%(uuid.uuid1(),self.cjList[uploadNo].text(),self.userIds[uploadNo],time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            # print(sql)
        if self.stat.insert(sql)<=0:
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw,'消息',"设备"+(int(self.cjList[uploadNo])+1)+"上传失败", QMessageBox.Ok)
        self.bhList[uploadNo].setText("")
        self.mcList[uploadNo].setText("")
        self.cjList[uploadNo].setText("")
        self.userIds[uploadNo]=""
        self.allPerson-=1

    #过号
    def passPersion(self):
        if(self.passNumber.text()==''):
            self.showMsgSignal.emit("该设备无测试人员")
            return
        passNum = int(self.passNumber.text())
        if(passNum<1 or passNum>8):
            self.showMsgSignal.emit("请输入1-8的设备号")
        else:
            self.bhList[passNum-1].setText("")
            self.mcList[passNum-1].setText("")
            self.cjList[passNum-1].setText("")
            self.userIds[passNum-1]=""
            self.allPerson-=1

    #清理数据
    def clearText(self):
        for i in range(8):
            self.bhList[i].setText('')
            self.mcList[i].setText('')
            self.cjList[i].setText('')
            self.userIds[i] = ''
            self.nowPerson=0
            self.allPerson=0

        # 转换byte数据为16进制数据
    def transform_hex_data(self,data):
        return int(data.hex(), 16)

    # 计算时间
    def calculate_time(self,out):
        # print(transform_hex_data(out[4]) << 8)
        # print(transform_hex_data(out[5]))
        sport_time = (self.transform_hex_data(out[4]) << 8) + self.transform_hex_data(out[5])
        real_time = sport_time / 100
        result_bean = result(self.transform_hex_data(out[1]), real_time)
        # print(result_bean.to_string())
        return result_bean

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