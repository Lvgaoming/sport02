# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ryjl.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import utils.readCardUtils
import utils.mysqlUtil

class Ui_Form(object):

    lastCardId = ''
    stat = utils.mysqlUtil.MysqlUtil()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 768)
        self.photo = QtWidgets.QLabel(Form)
        self.photo.setGeometry(QtCore.QRect(680, 90, 142, 198))
        self.photo.setText("")
        self.photo.setObjectName("photo")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(110, 70, 351, 461))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setReadOnly(True)
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.xh = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.xh.setFont(font)
        self.xh.setReadOnly(True)
        self.xh.setObjectName("xh")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.xh)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.xb = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.xb.setFont(font)
        self.xb.setReadOnly(True)
        self.xb.setObjectName("xb")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.xb)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.bj = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bj.setFont(font)
        self.bj.setReadOnly(True)
        self.bj.setObjectName("bj")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.bj)
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(610, 380, 301, 151))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(30)
        self.formLayout_2.setObjectName("formLayout_2")
        self.kbh = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kbh.setFont(font)
        self.kbh.setObjectName("kbh")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.kbh)
        self.kbh_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kbh_2.setFont(font)
        self.kbh_2.setReadOnly(True)
        self.kbh_2.setObjectName("kbh_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.kbh_2)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.bdxh = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bdxh.setFont(font)
        self.bdxh.setObjectName("bdxh")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.bdxh)
        
        self.search_btn = QtWidgets.QPushButton(Form)
        self.search_btn.setGeometry(QtCore.QRect(640, 560, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")

        self.bd_btn = QtWidgets.QPushButton(Form)
        self.bd_btn.setGeometry(QtCore.QRect(640, 660, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bd_btn.setFont(font)
        self.bd_btn.setObjectName("bd_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.search_btn.clicked.connect(self.search)
        self.bd_btn.clicked.connect(self.bdCard)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "人员检录"))
        self.label.setText(_translate("Form", "姓名:"))
        self.label_2.setText(_translate("Form", "学号:"))
        self.label_3.setText(_translate("Form", "系别："))
        self.label_4.setText(_translate("Form", "班级："))
        self.kbh.setText(_translate("Form", "卡编号："))
        self.label_6.setText(_translate("Form", "绑定学号："))
        self.search_btn.setText(_translate("Form", "查询"))
        self.bd_btn.setText(_translate("Form", "绑定"))

    def search(self):
        sql = "SELECT name,job_number,subject_number,clazz,card_number FROM user_info WHERE job_number='%s'"%self.bdxh.text()
        results = self.stat.fetchall(sql)
        if results==():
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw,'错误','系统中不存在该工号', QMessageBox.Ok)
        else:
            self.name.setText(results[0][0])
            self.xh.setText(results[0][1])
            self.xb.setText(results[0][2])
            self.bj.setText(results[0][3])
            self.kbh_2.setText(results[0][4])

    def bdCard(self):
        if self.bdxh.text()=='':
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw,'警告','请先输入学号查询', QMessageBox.Ok)
            return
        cardId = utils.readCardUtils.getCardId(self.lastCardId)
        if cardId=='':
            qw = QtWidgets.QWidget()
            QMessageBox.warning(qw,'警告','请先放卡再点击检录', QMessageBox.Ok)
        else:
            self.lastCardId = cardId
            self.kbh_2.setText(cardId)
            sql = "UPDATE user_info SET card_number='%s' WHERE job_number='%s'"%(cardId,self.bdxh.text())
            if self.stat.update(sql)>0:
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw,'消息','绑定成功', QMessageBox.Ok)
            else:
                qw = QtWidgets.QWidget()
                QMessageBox.warning(qw,'消息','绑定失败', QMessageBox.Ok)
