# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_db.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import _thread
import time

import win32ui
import xlrd
import xlwt
from PyQt5 import Qt

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QProgressDialog, QWidget
from PyQt5.QtCore import QObject, pyqtSignal, QCoreApplication
import pymysql
import sys


import utils.myglobalvar as gl

import utils.mysqlUtil

class Ui_Form(QWidget):
    stat = utils.mysqlUtil.MysqlUtil()

    showMsgSignal = pyqtSignal(str)
    showMsgSignal2 = pyqtSignal(int)
    changdi_index=0
    changdihao_index=0

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

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(500, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        #        self.zubie = QtWidgets.QLabel(self.)

        self.setting = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.setting.setGeometry(QtCore.QRect(0, 15, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        #font.setFamily("Arial Black")
        self.setting.setFont(font)
        self.setting.setText("竞赛设置")
        self.setting.setStyleSheet("color : #000")
        self.verticalLayout_3.addWidget(self.setting)






        #运动员块
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 600, 200))
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

        self.changci = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.changci.setGeometry(QtCore.QRect(410, 25, 120, 20))
        self.changci.setObjectName("changci")
        self.changci.setText("")
        self.changci.setAlignment(QtCore.Qt.AlignCenter)

        self.changci.setStyleSheet(
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

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(415, 120, 60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("护具组号")
        self.label.setStyleSheet("border:0px")

        self.hujuzunum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hujuzunum.setGeometry(QtCore.QRect(480, 120, 50, 20))
        self.hujuzunum.setObjectName("hujuzunum")
        self.hujuzunum.setText("2")
        self.hujuzunum.setAlignment(QtCore.Qt.AlignCenter)

        self.hujuzunum.setStyleSheet(
            "color:#3B3E40 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")

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



        # 比赛设置
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 350, 400, 400))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setStyleSheet(
            "border-width: 1px;border-style: solid;border-color: #767475 ;border-radius:10px")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(40, 5, 100, 60))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Arial Black")

        self.label.setFont(font)
        self.label.setText("比赛设置")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(3, 35, 394, 10))

        self.label.setText(
            "---------------------------------------------------------------------------------------------------------------------")
        self.label.setStyleSheet(
            " color:#000 ; border-width: 0px "

        )
        self.label.setAlignment(QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        # 局时间
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("局  时")
        self.label.setStyleSheet("border:0px")
        self.jushi = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.jushi.setGeometry(QtCore.QRect(65, 60, 40, 20))
        self.jushi.setObjectName("jushi")
        self.jushi.setText("120")
        self.jushi.setAlignment(QtCore.Qt.AlignCenter)
        self.jushi.setFixedWidth(40)
        self.jushi.setStyleSheet("color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(105, 60, 20, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("秒")
        self.label.setStyleSheet("border:0px")

        # 加时局时
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(135, 60, 60, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("加时局时")
        self.label.setStyleSheet("border:0px")
        self.jiashijushi = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.jiashijushi.setGeometry(QtCore.QRect(200, 60, 40, 20))
        self.jiashijushi.setObjectName("jiashijushi")
        self.jiashijushi.setText("60")
        self.jiashijushi.setAlignment(QtCore.Qt.AlignCenter)
        self.jiashijushi.setFixedWidth(40)
        self.jiashijushi.setStyleSheet("color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(245, 60, 20, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("秒")
        self.label.setStyleSheet("border:0px")
        # 加时赛最大得分
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(155, 90, 100, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("加时赛最大得分")
        self.label.setStyleSheet("border:0px")
        self.jiashizuidadefen = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.jiashizuidadefen.setGeometry(QtCore.QRect(260, 90, 40, 20))
        self.jiashizuidadefen.setObjectName("jiashizuidadefen")
        self.jiashizuidadefen.setText("2")
        self.jiashizuidadefen.setAlignment(QtCore.Qt.AlignCenter)
        self.jiashizuidadefen.setFixedWidth(40)
        self.jiashizuidadefen.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(300, 90, 20, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("分")
        self.label.setStyleSheet("border:0px")

        # 加时扣分数
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(155, 120, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("加时扣分")
        self.label.setStyleSheet("border:0px")
        self.jiashikoufenshu = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.jiashikoufenshu.setGeometry(QtCore.QRect(235, 120, 40, 20))
        self.jiashikoufenshu.setObjectName("jiashikoufenshu")
        self.jiashikoufenshu.setText("2")
        self.jiashikoufenshu.setAlignment(QtCore.Qt.AlignCenter)
        self.jiashikoufenshu.setFixedWidth(40)
        self.jiashikoufenshu.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")

        # 当前局
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(155, 150, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("当前局")
        self.label.setStyleSheet("border:0px")
        self.dangqianju = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.dangqianju.setGeometry(QtCore.QRect(235, 150, 40, 20))
        self.dangqianju.setObjectName("dangqianju")
        self.dangqianju.setText("1")
        self.dangqianju.setAlignment(QtCore.Qt.AlignCenter)
        self.dangqianju.setFixedWidth(40)
        self.dangqianju.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")

        # 当前时间
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(155, 180, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("当前时间")
        self.label.setStyleSheet("border:0px")
        self.dangqianshijian = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.dangqianshijian.setGeometry(QtCore.QRect(235, 180, 40, 20))
        self.dangqianshijian.setObjectName("dangqianshijian")
        self.dangqianshijian.setText("120")
        self.dangqianshijian.setAlignment(QtCore.Qt.AlignCenter)
        self.dangqianshijian.setFixedWidth(40)
        self.dangqianshijian.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(285, 180, 20, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("秒")
        self.label.setStyleSheet("border:0px")


        #
        #青方护具设备号
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(155, 210, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("青方护具号")
        self.label.setStyleSheet("border:0px")
        self.qinghujunum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qinghujunum.setGeometry(QtCore.QRect(235, 210, 40, 20))
        self.qinghujunum.setObjectName("qinghujunum")
        self.qinghujunum.setText("0")
        self.qinghujunum.setAlignment(QtCore.Qt.AlignCenter)
        self.qinghujunum.setFixedWidth(40)
        self.qinghujunum.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")

        # 红护具设备号
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(155, 240, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("红方护具号")
        self.label.setStyleSheet("border:0px")
        self.honghujunum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.honghujunum.setGeometry(QtCore.QRect(235, 240, 40, 20))
        self.honghujunum.setObjectName("honghujunum")
        self.honghujunum.setText("0")
        self.honghujunum.setAlignment(QtCore.Qt.AlignCenter)
        self.honghujunum.setFixedWidth(40)
        self.honghujunum.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")

        # 青方头盔设备号
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(155, 270, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("青方头盔号")
        self.label.setStyleSheet("border:0px")
        self.qingtoukuinum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.qingtoukuinum.setGeometry(QtCore.QRect(235, 270, 40, 20))
        self.qingtoukuinum.setObjectName("qingtoukuinum")
        self.qingtoukuinum.setText("0")
        self.qingtoukuinum.setAlignment(QtCore.Qt.AlignCenter)
        self.qingtoukuinum.setFixedWidth(40)
        self.qingtoukuinum.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")

        # 红头盔设备号
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(155, 300, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("红方头盔号")
        self.label.setStyleSheet("border:0px")
        self.hongtoukuinum = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.hongtoukuinum.setGeometry(QtCore.QRect(235, 300, 40, 20))
        self.hongtoukuinum.setObjectName("hongtoukuinum")
        self.hongtoukuinum.setText("0")
        self.hongtoukuinum.setAlignment(QtCore.Qt.AlignCenter)
        self.hongtoukuinum.setFixedWidth(40)
        self.hongtoukuinum.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")



        # 休息时间
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(10, 90, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("休息时间")
        self.label.setStyleSheet("border:0px")
        self.xiuxitime = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.xiuxitime.setGeometry(QtCore.QRect(88, 90, 40, 20))
        self.xiuxitime.setObjectName("xiuxitime")
        self.xiuxitime.setText("60")
        self.xiuxitime.setAlignment(QtCore.Qt.AlignCenter)
        self.xiuxitime.setFixedWidth(40)
        self.xiuxitime.setStyleSheet("color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(128, 90, 20, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("秒")
        self.label.setStyleSheet("border:0px")

        # 计时时间
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(10, 120, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("计时时间")
        self.label.setStyleSheet("border:0px")
        self.jishitime = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.jishitime.setGeometry(QtCore.QRect(88, 120, 40, 20))
        self.jishitime.setObjectName("jishitime")
        self.jishitime.setText("60")
        self.jishitime.setAlignment(QtCore.Qt.AlignCenter)
        self.jishitime.setFixedWidth(40)
        self.jishitime.setStyleSheet("color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(128, 120, 20, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("秒")
        self.label.setStyleSheet("border:0px")

        # 比赛局数
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(10, 150, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("比赛局数")
        self.label.setStyleSheet("border:0px")
        self.bisaijushu = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.bisaijushu.setGeometry(QtCore.QRect(88, 150, 40, 20))
        self.bisaijushu.setObjectName("bisaijushu")
        self.bisaijushu.setText("2")
        self.bisaijushu.setAlignment(QtCore.Qt.AlignCenter)
        self.bisaijushu.setFixedWidth(40)
        self.bisaijushu.setStyleSheet("color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(128, 150, 20, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("局")
        self.label.setStyleSheet("border:0px")




        # 有效得分
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(10, 180, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("有效得分")
        self.label.setStyleSheet("border:0px")
        self.youxiaodefen = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.youxiaodefen.setGeometry(QtCore.QRect(88, 180, 40, 20))
        self.youxiaodefen.setObjectName("youxiaodefen")
        self.youxiaodefen.setText("2")
        self.youxiaodefen.setAlignment(QtCore.Qt.AlignCenter)
        self.youxiaodefen.setFixedWidth(40)
        self.youxiaodefen.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(128, 180, 20, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("分")
        self.label.setStyleSheet("border:0px")

        # 最大分差
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(10, 210, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("最大分差")
        self.label.setStyleSheet("border:0px")
        self.zuidafencha = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.zuidafencha.setGeometry(QtCore.QRect(88, 210, 40, 20))
        self.zuidafencha.setObjectName("zuidafencha")
        self.zuidafencha.setText("20")
        self.zuidafencha.setAlignment(QtCore.Qt.AlignCenter)
        self.zuidafencha.setFixedWidth(40)
        self.zuidafencha.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(128, 210, 20, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("分")
        self.label.setStyleSheet("border:0px")

        # 裁判时差
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(10, 240, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("裁判时差")
        self.label.setStyleSheet("border:0px")
        self.caipanshicha = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.caipanshicha.setGeometry(QtCore.QRect(88, 240, 40, 20))
        self.caipanshicha.setObjectName("caipanshicha")
        self.caipanshicha.setText("1")
        self.caipanshicha.setAlignment(QtCore.Qt.AlignCenter)
        self.caipanshicha.setFixedWidth(40)
        self.caipanshicha.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(128, 240, 20, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("秒")
        self.label.setStyleSheet("border:0px")

        # 得分区间
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(10, 270, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("得分区间")
        self.label.setStyleSheet("border:0px")
        self.defenqujian = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.defenqujian.setGeometry(QtCore.QRect(88, 270, 40, 20))
        self.defenqujian.setObjectName("defenqujian")
        self.defenqujian.setText("3")
        self.defenqujian.setAlignment(QtCore.Qt.AlignCenter)
        self.defenqujian.setFixedWidth(40)
        self.defenqujian.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")

        #串口
        # self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        # self.label.setGeometry(QtCore.QRect(10, 300, 80, 20))
        # font = QtGui.QFont()
        # font.setFamily("微软雅黑")
        # font.setPointSize(10)
        # self.label.setFont(font)
        # self.label.setAlignment(QtCore.Qt.AlignCenter)
        # self.label.setObjectName("label")
        # self.label.setText("串口")
        # self.label.setStyleSheet("border:0px")
        # self.chuankou = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        # self.chuankou.setGeometry(QtCore.QRect(88, 300, 40, 20))
        # self.chuankou.setObjectName("defenqujian")
        # self.chuankou.setText("COM5")
        # self.chuankou.setAlignment(QtCore.Qt.AlignCenter)
        # self.chuankou.setFixedWidth(40)
        # self.chuankou.setStyleSheet(
        #     "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")
         # 扣分数
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(10, 300, 80, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("扣分个数")
        self.label.setStyleSheet("border:0px")
        self.koufenshu = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.koufenshu.setGeometry(QtCore.QRect(88, 300, 40, 20))
        self.koufenshu.setObjectName("koufenshu")
        self.koufenshu.setText("10")
        self.koufenshu.setAlignment(QtCore.Qt.AlignCenter)
        self.koufenshu.setFixedWidth(40)
        self.koufenshu.setStyleSheet(
            "color:#000 ; border-radius:5px ; background-color:#FFE05E ;border-color:#FFE05E")



        # 按钮块
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(450, 530, 600, 200))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setStyleSheet(
            "border-width: 1px;border-style: solid;border-color: #767475 ;border-radius:10px")

        self.kaishi_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.kaishi_bt.setGeometry(QtCore.QRect(250, 20, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.kaishi_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.kaishi_bt.setStyleSheet("QPushButton{color:#000}"
                                     "QPushButton:hover{color:red}"
                                     "QPushButton{background-color:#21DB95}"
                                     "QPushButton{border:2px}"
                                     "QPushButton{border-radius:10px}"
                                     "QPushButton{padding:2px 4px}"

                                     )
        self.kaishi_bt.setObjectName("kaishi_bt")
        self.kaishi_bt.setText("开始比赛")



        self.daochu_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.daochu_bt.setGeometry(QtCore.QRect(150, 80, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.daochu_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.daochu_bt.setStyleSheet("QPushButton{color:#000}"
                                     "QPushButton:hover{color:red}"
                                     "QPushButton{background-color:#21DB95}"
                                     "QPushButton{border:2px}"
                                     "QPushButton{border-radius:10px}"
                                     "QPushButton{padding:2px 4px}"

                                     )
        self.daochu_bt.setObjectName("daochu_bt")
        self.daochu_bt.setText("导出")

        self.daoru_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.daoru_bt.setGeometry(QtCore.QRect(350, 80, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.daoru_bt.setFont(font)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.daoru_bt.setStyleSheet("QPushButton{color:#000}"
                                     "QPushButton:hover{color:red}"
                                     "QPushButton{background-color:#21DB95}"
                                     "QPushButton{border:2px}"
                                     "QPushButton{border-radius:10px}"
                                     "QPushButton{padding:2px 4px}"

                                     )
        self.daoru_bt.setObjectName("daoru_bt")
        self.daoru_bt.setText("导入")

        self.firstchaxun()




        # 按钮事件
        self.kaishi_bt.clicked.connect(self.setdata)

        self.changdinext_bt.clicked.connect(self.changdinext)
        self.changdipre_bt.clicked.connect(self.changdipre)
        self.changcinext_bt.clicked.connect(self.changdihaonext)
        self.changcipre_bt.clicked.connect(self.changdihaopre)
        self.chaxun_bt.clicked.connect(self.chaxun)
        self.daochu_bt.clicked.connect(self.export)
        self.daoru_bt.clicked.connect(self.insert)
        self.showMsgSignal.connect(self.showMsg)

        self.iskaishi=False


    def setdata(self):
        if (self.iskaishi):


            gl.set_value('jushi', self.jushi.text())
            gl.set_value('xiuxitime', self.xiuxitime.text())
            gl.set_value('jishitime',self.jishitime.text())
            gl.set_value('bisaijushu',self.bisaijushu.text())
            gl.set_value('youxiaodefen',self.youxiaodefen.text())
            gl.set_value('zuidafencha',self.zuidafencha.text())
            gl.set_value('caipanshicha',self.caipanshicha.text())
            gl.set_value('qingfangname',self.qingfangname.text())
            gl.set_value('qingfangdanwei',self.qingfangdanwei.text())

            gl.set_value('hongfangname',self.hongfangname.text())
            gl.set_value('hongfangdanwei',self.hongfangdanwei.text())

            gl.set_value('defenqujian',self.defenqujian.text())
            # gl.set_value('chuankou',self.chuankou.text())
            # gl.set_value('changci',self.li)
            gl.set_value('changdi',self.changdi.text())
            gl.set_value('jiashijushi',self.jiashijushi.text())

            gl.set_value('jibie',self.jibie.text())
            gl.set_value('changdihao',self.yundongyuan[1])
            gl.set_value('bisaixuhao',self.yundongyuan[0])
            gl.set_value('koufenshu',self.koufenshu.text())
            gl.set_value('jiashizuidadefen',self.jiashizuidadefen.text())
            gl.set_value('jiashikoufenshu',self.jiashikoufenshu.text())
            #设备组号
            gl.set_value('hujuzunum',self.hujuzunum.text())

            gl.set_value('dangqianju',self.dangqianju.text())

            gl.set_value('dangqianshijian',self.dangqianshijian.text())
            # 青方红方护具头盔设备号
            gl.set_value('qinghujunum',self.qinghujunum.text())
            gl.set_value('honghujunum', self.honghujunum.text())
            gl.set_value('qingtoukuinum', self.qingtoukuinum.text())
            gl.set_value('hongtoukuinum',self.hongtoukuinum.text())


            print(self.dangqianju.text())
            print(self.dangqianshijian.text())
            print("qqqqqqqq")
            gl.get_value('seting').close()

        else:
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "未查询数据库", QMessageBox.Ok)

    # 显示对话框
    def showMsg(self, msg):
        qw = QtWidgets.QWidget()
        QMessageBox.warning(qw, '消息', msg)

    def chaxun(self):
        # self.li=[]
        # print(self.changdihaoresult)
        if (self.changdiresults == () or self.changdiresults==None):
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "没有数据,请导入比赛数据！！", QMessageBox.Ok)
        else:
            # for i in self.changdihaoresult:
            #     self.li.append(i[0])
            # li=str(self.li)
            # li=li.replace('[','(').replace(']',')')
            # sql="select bisaixuhao,changdihao,qingfangxinming,qingfangdanwei,hongfangxinming,hongfangdanwei,jibie,lunci,bisaizhuangtai from bisaixinxi where changdi='%s' and changdihao in %s and bisaizhuangtai='等待中' order by changdihao"%(self.changdi.text(),li)
            # print(sql)
            # self.yundongyuans=self.stat.fetchall(sql)
            sql="select bisaixuhao,changdihao,qingfangxinming,qingfangdanwei,hongfangxinming,hongfangdanwei,jibie,lunci from bisaixinxi where changdi='%s' and changdihao='%s' and bisaizhuangtai='等待中' order by changdihao"%(self.changdi.text(),self.changci.text())
            print(sql)
            self.yundongyuan=self.stat.fetchone(sql)
            print(self.yundongyuan)
            if(self.yundongyuan==()):
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw, '错误', "没有数据,请导入比赛数据！！", QMessageBox.Ok)
            else:
                self.iskaishi = True
                # print(self.yundongyuans)
                print(self.yundongyuan)
                self.qingfangname.setText(self.yundongyuan[2])
                self.qingfangdanwei.setText(self.yundongyuan[3])
                self.hongfangname.setText(self.yundongyuan[4])
                self.hongfangdanwei.setText(self.yundongyuan[5])
                self.jibie.setText(self.yundongyuan[6])
                gl.set_value('lunci',self.yundongyuan[7])




    def changdinext(self):
        if(self.changdi.text()==""):
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "没有数据,请导入比赛数据！！", QMessageBox.Ok)
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
                QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)
            else:

                self.changdihao_index = 0
                self.changci.setText(self.changdihaoresult[self.changdihao_index][0])

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
                self.changci.setText(self.changdihaoresult[self.changdihao_index][0])

    def changdihaonext(self):
        if(self.changci.text()==""):
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)
        else:
            self.changdihao_index += 1
            if (self.changdihao_index < len(self.changdihaoresult)):
                self.changci.setText(self.changdihaoresult[self.changdihao_index][0])

            else:
                self.changdihao_index = 0
                self.changci.setText(self.changdihaoresult[self.changdihao_index][0])

    def changdihaopre(self):
        if (self.changci.text() == ""):
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "没有数据", QMessageBox.Ok)
        else:
            if (self.changdihao_index > 0):
                self.changdihao_index -= 1
                self.changci.setText(self.changdihaoresult[self.changdihao_index][0])

            else:
                self.changdihao_index = len(self.changdihaoresult) - 1
                self.changci.setText(self.changdihaoresult[self.changdihao_index][0])

    def firstchaxun(self):
        self.changdiresults=self.stat.fetchall("select distinct changdi from bisaixinxi order by changdi")

        if(self.changdiresults==() ):
            # self.showMsgSignal.emit("没有数据")
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "当前没有比赛信息", QMessageBox.Ok)
            print(self.changdi.text())
        else:
            self.changdi.setText(self.changdiresults[self.changdi_index][0])
            sql= "select distinct changdihao from bisaixinxi where changdi='%s' and bisaizhuangtai='等待中'  order by changdihao"%self.changdi.text()
            print(sql)

            self.changdihaoresult = self.stat.fetchall(sql)
            if( not self.changdihaoresult==()):
                self.changci.setText(self.changdihaoresult[self.changdihao_index][0])

    def export(self,):
        table_name="bisaixinxi"
        output_path="比赛信息.xls"
        self._cursor = self.stat.getConnect().cursor()
        print(self._cursor)
        count = self._cursor.execute('select * from ' + table_name)
        # print(self._cursor.lastrowid)
        print(count)
        # 重置游标的位置
        self._cursor.scroll(0, mode='absolute')
        # 搜取所有结果
        results = self._cursor.fetchall()
        # print(results)

        # 获取MYSQL里面的数据字段名称
        fields = self._cursor.description
        # print(fields)
        workbook = xlwt.Workbook()

        # 注意: 在add_sheet时, 置参数cell_overwrite_ok=True, 可以覆盖原单元格中数据。
        # cell_overwrite_ok默认为False, 覆盖的话, 会抛出异常.
        sheet = workbook.add_sheet('table_' + table_name, cell_overwrite_ok=True)

        # 写上字段信息
        for field in range(0, len(fields)):
            sheet.write(0, field, fields[field][0])
            # print( fields[field][0])

        # 获取并写入数据段信息
        row = 1
        col = 0
        for row in range(1, len(results) + 1):
            for col in range(0, len(fields)):
                # print("row",row)
                # print("col",col)
                sheet.write(row, col, u'%s' % results[row - 1][col])
                # print(results[row - 1][col])

        workbook.save(output_path)
        qw = QtWidgets.QWidget()
        QMessageBox.warning(qw, '成功', "导出成功", QMessageBox.Ok)

    def open_excel(self,filename):
        try:
            book = xlrd.open_workbook(filename)  # 文件名，把文件与py文件放在同一目录下
            print('打开文件')
        except:
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "打开文件失败", QMessageBox.Ok)
        try:
            # sheet = book.sheet_by_name("table_bisaixinxi")  # execl里面的worksheet1
            sheet = book.sheets()[0]
            print('打开作业簿')
            return sheet
        except:
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '错误', "打开文件失败2", QMessageBox.Ok)

    def insert_deta(self,filename):
        self.showMsgSignal.emit("导入中......")
        sheet = self.open_excel(filename)

        self.row_num = sheet.nrows
        self.value=[]

        if (len(sheet.row_values(1)) != 39):
            self.showMsgSignal.emit("excel表字段与数据库不符，请重新导入")


#         progress = QProgressDialog(self)
#         progress.setWindowTitle("请稍等")
#         progress.setLabelText("正在操作...")
#         progress.setCancelButtonText("取消")
#         """
# 如果任务的预期持续时间小于minimumDuration，则对话框根本不会出现。这样可以防止弹出对话框，快速完成任务。对于预期超过minimumDuration的任务，对话框将在minimumDuration时间之后或任何进度设置后立即弹出。如果设置为0，则只要设置任何进度，将始终显示对话框。 默认值为4000毫秒,即4秒。
#         """
#         # progress.setMinimumDuration(5)  # 此属性保留对话框出现之前必须通过的时间。
#         """
# 此属性保留由模态小部件阻止的窗口。
# 这个属性只对Windows有意义。 模态小部件防止其他窗口中的小部件获取输入。 该属性的值控制在窗口小部件可见时阻止哪些窗口。 窗口可见时更改此属性无效; 您必须首先hide（）小部件，然后再次show（）。
# 默认情况下，此属性为Qt.NonModal。
#        """
#
#         # progress.setWindowModality(Qt.WindowModal)
#         """
# 由上面我们知道：使用setMinimum() 和setMaximum() 或构造函数来设置操作中的“steps”数量，并在操作进行时调用setValue()。setRange(0,num)就是设置其最小和最大值，这里最小值0，最大值num，num是根据输入框中的数字确定的。
#  """
#         progress.setRange(0, row_num)
        else:
            for i in range(1, self.row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
                print(i)
                row_data = sheet.row_values(i)
                self.value = []
                for j in row_data:
                    if(j=="None"):
                        j=''
                    self.value.append(j)
                    # self.value = (row_data[0], row_data[1], row_data[2], row_data[3],row_data[4], row_data[5], row_data[6], row_data[7],row_data[8], row_data[9], row_data[10], row_data[11],row_data[12], row_data[13], row_data[14], row_data[15],row_data[16], row_data[17], row_data[18], row_data[19],row_data[20], row_data[21], row_data[22], row_data[23],row_data[24], row_data[25], row_data[26], row_data[27],row_data[28], row_data[29], row_data[30], row_data[31],row_data[32], row_data[33], row_data[34], row_data[35],row_data[36])
                # print(i)
                self.value=tuple(self.value)
                # print(self.value[0])

                sql="SELECT bisaixuhao from bisaixinxi where bisaixuhao='%s'"%self.value[0]
                # print(sql)
                result=self.stat.fetchone(sql)
                # print(result,"99999999999999999")
                if(result==None):
                    sql = "INSERT INTO bisaixinxi(bisaixuhao,zonglunci,lunci,changdi,changdihao,jibie,riqi,qingfangbianhao,qingfangxinming,qingfangdanwei,hongfangbianhao,hongfangxinming,hongfangdanwei,bisaizhuangtai,huoshengzhe,huoshengfangshi,qingfangdefen,hongfangdefen,qingfangkoufen,hongfangkoufen,qingfangdefen1,hongfangdefen1,qingfangkoufen1,hongfangkoufen1,qingfangdefen2,hongfangdefen2,qingfangkoufen2,hongfangkoufen2,qingfangdefen3,hongfangdefen3,qingfangkoufen3,hongfangkoufen3,qingfangdefen4,hongfangdefen4,qingfangkoufen4,hongfangkoufen4,yijian,erjian,sanjian)VALUES" + str(
                        self.value)
                    self.stat.insert(sql)
                    # print(sql)
                else:
                    sql="DELETE FROM bisaixinxi WHERE bisaixuhao=%s"%self.value[0]
                    self.stat.delete(sql)
                    sql = "INSERT INTO bisaixinxi(bisaixuhao,zonglunci,lunci,changdi,changdihao,jibie,riqi,qingfangbianhao,qingfangxinming,qingfangdanwei,hongfangbianhao,hongfangxinming,hongfangdanwei,bisaizhuangtai,huoshengzhe,huoshengfangshi,qingfangdefen,hongfangdefen,qingfangkoufen,hongfangkoufen,qingfangdefen1,hongfangdefen1,qingfangkoufen1,hongfangkoufen1,qingfangdefen2,hongfangdefen2,qingfangkoufen2,hongfangkoufen2,qingfangdefen3,hongfangdefen3,qingfangkoufen3,hongfangkoufen3,qingfangdefen4,hongfangdefen4,qingfangkoufen4,hongfangkoufen4,yijian,erjian,sanjian)VALUES" + str(
                        self.value)
                    self.stat.insert(sql)

            self.showMsgSignal.emit("导入成功")
            self.firstchaxun()


    def insert(self):

        dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
        dlg.SetOFNInitialDir('C:/')  # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()
        filename=""


        filename = dlg.GetPathName()  # 获取选择的文件名称
        print(filename)

        if(filename!=None and filename!=""):
            _thread.start_new_thread(self.insert_deta, (filename,))






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
    # utils.mysqlUtil.MysqlUtil.host = 'localhost'
    # utils.mysqlUtil.MysqlUtil.dbPort = '3306'
    # utils.mysqlUtil.MysqlUtil.username = 'root'
    # utils.mysqlUtil.MysqlUtil.password = 'lgm123'
    # utils.mysqlUtil.MysqlUtil.database = 'sport'
    app = QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    content = Ui_Form()
    content.setupUi(main)


    main.show()
    sys.exit(app.exec_())