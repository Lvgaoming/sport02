# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blood.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import sys
import random

import serial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
#import utils.readCardUtils
# import utils.pyMysqlUtils
import utils.mysqlUtil


class Ui_Form(object):
    stat = utils.mysqlUtil.MysqlUtil()
    showMsgSignal = pyqtSignal(str)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 768)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setAcceptDrops(False)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 70, 352, 332))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        #改变verticalLayoutWidget背景色
        self.verticalLayoutWidget.setStyleSheet("background-color:#ffffff")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.qingfang = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qingfang.setMinimumSize(QtCore.QSize(350, 60))
        self.qingfang.setMaximumSize(QtCore.QSize(350, 60))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setFamily("Arial Red")
        self.qingfang.setFont(font)
        self.qingfang.setStyleSheet(
            "color:rgb(0,120,215)")
        self.qingfang.setAlignment(QtCore.Qt.AlignCenter)
        self.qingfang.setObjectName("qingfang")
        self.verticalLayout.addWidget(self.qingfang)
        self.user_1 = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.user_1.setMinimumSize(QtCore.QSize(350, 60))
        self.user_1.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.user_1.setFont(font)
        self.user_1.setStyleSheet("QProgressBar {\n"
                                  "    border: 2px solid grey;\n"
                                  "    border-radius: 5px;\n"
                                  "    background-color: #FFFFFF;\n"
                                  "}\n"
                                  "QProgressBar::chunk {\n"
                                  "    background-color:rgb(0,120,215);\n"
                                  "    width: 20px;\n"
                                  "}\n"
                                  "QProgressBar {\n"
                                  "    border: 2px solid grey;\n"
                                  "    border-radius: 10px;\n"
                                  "    text-align: center;\n"
                                  "}")
        self.user_1.setMaximum(12)
        self.user_1.setProperty("value", 12)
        self.user_1.setOrientation(QtCore.Qt.Horizontal)
        self.user_1.setObjectName("user_1")
        self.verticalLayout.addWidget(self.user_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_title_a = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name_title_a.setMinimumSize(QtCore.QSize(160, 60))
        self.name_title_a.setMaximumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_title_a.setFont(font)
        self.name_title_a.setAlignment(QtCore.Qt.AlignCenter)
        self.name_title_a.setObjectName("name_title_a")
        self.horizontalLayout.addWidget(self.name_title_a)
        self.name_a = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.name_a.setMinimumSize(QtCore.QSize(160, 60))
        self.name_a.setMaximumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_a.setFont(font)
        self.name_a.setText("")
        self.name_a.setAlignment(QtCore.Qt.AlignCenter)
        self.name_a.setObjectName("name_a")
        self.horizontalLayout.addWidget(self.name_a)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bh_title_a = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.bh_title_a.setMinimumSize(QtCore.QSize(160, 60))
        self.bh_title_a.setMaximumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bh_title_a.setFont(font)
        self.bh_title_a.setAlignment(QtCore.Qt.AlignCenter)
        self.bh_title_a.setObjectName("bh_title_a")
        self.horizontalLayout_2.addWidget(self.bh_title_a)
        self.bh_a = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.bh_a.setMinimumSize(QtCore.QSize(160, 60))
        self.bh_a.setMaximumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bh_a.setFont(font)
        self.bh_a.setText("")
        self.bh_a.setAlignment(QtCore.Qt.AlignCenter)
        self.bh_a.setObjectName("bh_a")
        self.horizontalLayout_2.addWidget(self.bh_a)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.blood_title_a = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.blood_title_a.setMinimumSize(QtCore.QSize(160, 60))
        self.blood_title_a.setMaximumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.blood_title_a.setFont(font)
        self.blood_title_a.setAlignment(QtCore.Qt.AlignCenter)
        self.blood_title_a.setObjectName("blood_title_a")
        self.horizontalLayout_3.addWidget(self.blood_title_a)
        self.blood_a = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.blood_a.setMinimumSize(QtCore.QSize(160, 60))
        self.blood_a.setMaximumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.blood_a.setFont(font)
        self.blood_a.setText("")
        self.blood_a.setAlignment(QtCore.Qt.AlignCenter)
        self.blood_a.setObjectName("blood_a")
        self.horizontalLayout_3.addWidget(self.blood_a)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(590, 70, 352, 332))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayoutWidget_2.setStyleSheet(" background-color:#FFFFFF")
        # self.verticalLayout_2.set
        self.hongfang = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.hongfang.setMinimumSize(QtCore.QSize(350, 60))
        self.hongfang.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.hongfang.setAutoFillBackground(False)

        self.hongfang.setFont(font)
        self.hongfang.setStyleSheet("color:#ff0000"

                                    )
        # palette = QPalette()
        # palette.setColor(QPalette., Qt.red)
        # self.hongfang.setPalette(palette)
        self.hongfang.setAlignment(QtCore.Qt.AlignCenter)
        self.hongfang.setObjectName("hongfang")
        self.verticalLayout_2.addWidget(self.hongfang)
        self.user_2 = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.user_2.setMinimumSize(QtCore.QSize(350, 60))
        self.user_2.setMaximumSize(QtCore.QSize(350, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.user_2.setFont(font)
        self.hongfang.setStyleSheet("color:#ff0000"

                                    )

        self.user_2.setStyleSheet("QProgressBar {\n"
                                  "    border: 2px solid grey;\n"
                                  "    border-radius: 5px;\n"
                                  "    background-color: #FFFFFF;\n"
                                  "}\n"
                                  "QProgressBar::chunk {\n"
                                  "    background-color: #ff0000;\n"
                                  "    width: 20px;\n"
                                  "}\n"
                                  "QProgressBar {\n"
                                  "    border: 2px solid grey;\n"
                                  "    border-radius: 10px;\n"
                                  "    text-align: center;\n"
                                  "}"

                                  )
        self.user_2.setMaximum(12)
        self.user_2.setProperty("value", 12)
        self.user_2.setOrientation(QtCore.Qt.Horizontal)
        self.user_2.setObjectName("user_2")
        self.verticalLayout_2.addWidget(self.user_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.name_title_a_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.name_title_a_2.setMinimumSize(QtCore.QSize(160, 60))
        self.name_title_a_2.setMaximumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_title_a_2.setFont(font)
        self.name_title_a_2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_title_a_2.setObjectName("name_title_a_2")
        self.horizontalLayout_4.addWidget(self.name_title_a_2)
        self.name_b = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.name_b.setMinimumSize(QtCore.QSize(160, 60))
        self.name_b.setMaximumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.name_b.setFont(font)
        self.name_b.setText("")
        self.name_b.setAlignment(QtCore.Qt.AlignCenter)
        self.name_b.setObjectName("name_b")
        self.horizontalLayout_4.addWidget(self.name_b)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bh_title_a_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.bh_title_a_2.setMinimumSize(QtCore.QSize(160, 60))
        self.bh_title_a_2.setMaximumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bh_title_a_2.setFont(font)
        self.bh_title_a_2.setAlignment(QtCore.Qt.AlignCenter)
        self.bh_title_a_2.setObjectName("bh_title_a_2")
        self.horizontalLayout_5.addWidget(self.bh_title_a_2)
        self.bh_b = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.bh_b.setMinimumSize(QtCore.QSize(160, 60))
        self.bh_b.setMaximumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bh_b.setFont(font)
        self.bh_b.setText("")
        self.bh_b.setAlignment(QtCore.Qt.AlignCenter)
        self.bh_b.setObjectName("bh_b")
        self.horizontalLayout_5.addWidget(self.bh_b)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.blood_title_a_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.blood_title_a_2.setMinimumSize(QtCore.QSize(160, 60))
        self.blood_title_a_2.setMaximumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.blood_title_a_2.setFont(font)
        self.blood_title_a_2.setAlignment(QtCore.Qt.AlignCenter)
        self.blood_title_a_2.setObjectName("blood_title_a_2")
        self.horizontalLayout_6.addWidget(self.blood_title_a_2)
        self.blood_b = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.blood_b.setMinimumSize(QtCore.QSize(160, 60))
        self.blood_b.setMaximumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.blood_b.setFont(font)
        self.blood_b.setText("")
        self.blood_b.setAlignment(QtCore.Qt.AlignCenter)
        self.blood_b.setObjectName("blood_b")

        self.horizontalLayout_6.addWidget(self.blood_b)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 500, 180, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 500, 180, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(680, 500, 180, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.qingfang.setText(_translate("Form", "青方"))
        self.user_1.setFormat(_translate("Form", "%v"))
        self.name_title_a.setText(_translate("Form", "姓名："))
        self.bh_title_a.setText(_translate("Form", "人员编号："))
        self.blood_title_a.setText(_translate("Form", "扣血量："))
        self.hongfang.setText(_translate("Form", "红方"))
        self.user_2.setFormat(_translate("Form", "%v"))
        self.name_title_a_2.setText(_translate("Form", "姓名："))
        self.bh_title_a_2.setText(_translate("Form", "人员编号："))
        self.blood_title_a_2.setText(_translate("Form", "扣血量："))
        self.pushButton_2.setText(_translate("Form", "开始比赛"))
        self.pushButton_3.setText(_translate("Form", "青方检录"))
        self.pushButton_4.setText(_translate("From", "红方检录"))

        # self.pushButton.clicked.connect(self.qingfangAttk)
        self.pushButton_2.clicked.connect(self.action)
        self.pushButton_3.clicked.connect(self.qingfangwriteInfo)
        self.pushButton_4.clicked.connect(self.hongfangwriteInfo)

    def qingfangAttk(self):
        now = random.randint(10, 20)
        self.blood_b.setText(str(now))
        new = self.user_2.value() - now
        if (new <= 0):
            self.user_2.setValue(0)
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw, '消息', '青方胜', QMessageBox.Ok)

        else:
            self.user_2.setValue(new)

    def action(self):
        serialPort = "COM5"  # 串口
        baudRate = 115200  # 波特率
        ser = serial.Serial(serialPort, baudRate, timeout=0.1, stopbits=1, bytesize=8)
        print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))
        myout = []

        while 1:
            while ser.inWaiting() > 0:
                myout.append(ser.readline())
            if myout != []:
                # myout = [b'\xAA', b'\x02', b'\x00', b'\x01', b'\xD0', b'\xD1', b'\xD2', b'\x01']
                print(myout)
                s = str(myout[0][1:])
                print(s)
                last = s.replace("b", "").replace("'", "").replace("\\x", "")
                print(last)
                value = last[5]
                print(value)
                group = last[7]
                print(group)
                now = value
                # 组别 红方 3 青方 2
                if (int(group) == 3):
                    self.blood_b.setText(str(now))
                    new = self.user_2.value() - int(now)
                    if (new <= 0):
                        self.user_2.setValue(0)
                        qw = QtWidgets.QWidget()
                        QMessageBox.warning(qw, '消息', '青方胜', QMessageBox.Ok)
                        ser.close()
                        break
                    else:
                        self.user_2.setValue(new)

                if (int(group) == 2):
                    self.blood_a.setText(str(now))
                    new = self.user_1.value() - int(now)
                    if (new <= 0):
                        self.user_1.setValue(0)
                        qw = QtWidgets.QWidget()
                        QMessageBox.warning(qw, '消息', '红方胜', QMessageBox.Ok)
                        ser.close()
                        break
                    else:
                        self.user_1.setValue(new)

                myout = []

    # 青方刷卡检录
    def qingfangwriteInfo(self, cardId):
        # cardId = utils.readCardUtils.getCardId()
        # if cardId=='':
        #     qw = QtWidgets.QWidget()
        #     QMessageBox.warning(qw,'警告','请先放卡再点击检录', QMessageBox.Ok)
        #     return
        results = self.stat.fetchall("select * from user_info where card_number=%s" % cardId)
        # print(results)
        if results == ():
            # qw = QtWidgets.QWidget()
            # QMessageBox.warning(qw,'警告','非本系统卡', QMessageBox.Ok)
            self.showMsgSignal.emit("非本系统卡")
        else:
            self.name_a.setText(results[0][2])
            self.bh_a.setText(results[0][1])

    # 红方刷卡检录
    def hongfangwriteInfo(self, cardId):
        # cardId = utils.readCardUtils.getCardId()
        # if cardId=='':
        #     qw = QtWidgets.QWidget()
        #     QMessageBox.warning(qw,'警告','请先放卡再点击检录', QMessageBox.Ok)
        #     return
        # results = self.stat.fetchall("select * from user_info where card_number=%s"%cardId)
        # # print(results)
        # if results==():
        #     # qw = QtWidgets.QWidget()
        #     # QMessageBox.warning(qw,'警告','非本系统卡', QMessageBox.Ok)
        #     self.showMsgSignal.emit("非本系统卡")
        # else:
        #     self.name_b.setText(results[0][2])
        #     self.bh_b.setText(results[0][1])
        self.name_b.setText("李明林")
        self.bh_b.setText("2016011228")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    content = Ui_Form()
    content.setupUi(main)
    main.show()
    sys.exit(app.exec_())