# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_db.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QObject,pyqtSignal
import pymysql
import sys
import utils.mysqlUtil

class Ui_Form(QObject):

    showMsgSignal = pyqtSignal(str)

    # def __init__(self):
        # self.url_info.setText(utils.mysqlUtil.MysqlUtil.host)
        # self.username_info.setText(utils.mysqlUtil.MysqlUtil.username)
        # self.password_info.setText(utils.mysqlUtil.MysqlUtil.password)
        # self.database_info.setText(utils.mysqlUtil.MysqlUtil.database)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 20, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 100, 260, 128))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(100, 25))
        self.label_2.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.url_info = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.url_info.setMinimumSize(QtCore.QSize(150, 25))
        self.url_info.setMaximumSize(QtCore.QSize(150, 25))
        self.url_info.setObjectName("url_info")
        self.horizontalLayout.addWidget(self.url_info)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 25))
        self.label_3.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.username_info = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.username_info.setMinimumSize(QtCore.QSize(150, 25))
        self.username_info.setMaximumSize(QtCore.QSize(150, 25))
        self.username_info.setObjectName("username_info")
        self.horizontalLayout_2.addWidget(self.username_info)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(100, 25))
        self.label_4.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.password_info = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password_info.setMinimumSize(QtCore.QSize(150, 25))
        self.password_info.setMaximumSize(QtCore.QSize(150, 25))
        self.password_info.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_info.setObjectName("password_info")
        self.horizontalLayout_3.addWidget(self.password_info)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(100, 25))
        self.label_5.setMaximumSize(QtCore.QSize(100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.database_info = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.database_info.setMinimumSize(QtCore.QSize(150, 25))
        self.database_info.setMaximumSize(QtCore.QSize(150, 25))
        self.database_info.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.database_info.setObjectName("database_info")
        self.horizontalLayout_4.addWidget(self.database_info)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 240, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.label.raise_()
        self.label_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.pushButton.raise_()

        self.pushButton.clicked.connect(self.connectDB)
        self.showMsgSignal.connect(self.showMsg)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "数据库连接配置"))
        self.label_2.setText(_translate("Form", "数据库地址："))
        self.label_3.setText(_translate("Form", "用  户  名："))
        self.label_4.setText(_translate("Form", "密      码："))
        self.label_5.setText(_translate("Form", "数据库名称："))
        self.pushButton.setText(_translate("Form", "连接"))
        self.url_info.setText(utils.mysqlUtil.MysqlUtil.host)
        self.username_info.setText(utils.mysqlUtil.MysqlUtil.username)
        self.password_info.setText(utils.mysqlUtil.MysqlUtil.password)
        self.database_info.setText(utils.mysqlUtil.MysqlUtil.database)

    #显示对话框
    def showMsg(self,msg):
        qw = QtWidgets.QWidget()
        QMessageBox.warning(qw,'消息',msg)

    def connectDB(self):
        utils.mysqlUtil.MysqlUtil.host = self.url_info.text()
        utils.mysqlUtil.MysqlUtil.username = self.username_info.text()
        utils.mysqlUtil.MysqlUtil.password = self.password_info.text()
        utils.mysqlUtil.MysqlUtil.database = self.database_info.text()
        try:
            db = pymysql.connect(utils.mysqlUtil.MysqlUtil.host,utils.mysqlUtil.MysqlUtil.username,utils.mysqlUtil.MysqlUtil.password,utils.mysqlUtil.MysqlUtil.database,charset='utf8')
            if db!=None:
                self.showMsgSignal.emit("连接成功")
        except:
            self.showMsgSignal.emit("连接失败，请检查数据库连接信息或数据库服务器是否宕机")

class setDBWindow(QtWidgets.QDialog):
    def __init__(self):
        super(setDBWindow,self).__init__()
        self.new=Ui_Form()
        self.new.setupUi(self)