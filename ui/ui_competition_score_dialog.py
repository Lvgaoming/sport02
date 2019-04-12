# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_db.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtCore import QObject, pyqtSignal, QCoreApplication
import pymysql
import sys
import utils.myglobalvar as gl

import utils.mysqlUtil

class Ui_Form(object):
    stat = utils.mysqlUtil.MysqlUtil()
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(1000, 100)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setAcceptDrops(False)

        Form.setStyleSheet("background-color:#fff")

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1000, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # self.verticalLayoutWidget.setStyleSheet(
        #     "border-width: 1px;border-style: solid;border-color: #767475 ;border-radius:10px")

        self.ptf_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ptf_bt.setGeometry(QtCore.QRect(20, 35, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.ptf_bt.setFont(font)
        self.ptf_bt.setStyleSheet("QPushButton{color:#fff}"
                                        "QPushButton:hover{color:red}"
                                        "QPushButton{background-color:#FFCD43}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:5px}"
                                        "QPushButton{padding:2px 4px}"

                                        )
        self.ptf_bt.setObjectName("ptf_bt")
        self.ptf_bt.setText("PTF")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("比分胜")
        self.label.setStyleSheet("border:0px")

        self.ptg_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ptg_bt.setGeometry(QtCore.QRect(100, 35, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.ptg_bt.setFont(font)
        self.ptg_bt.setStyleSheet("QPushButton{color:#fff}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:#FFCD43}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:5px}"
                                  "QPushButton{padding:2px 4px}"

                                  )
        self.ptg_bt.setObjectName("ptg_bt")
        self.ptg_bt.setText("PTG")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(85, 70, 80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("分差优势胜")
        self.label.setStyleSheet("border:0px")

        self.sdp_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sdp_bt.setGeometry(QtCore.QRect(180, 35, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.sdp_bt.setFont(font)
        self.sdp_bt.setStyleSheet("QPushButton{color:#fff}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:#FFCD43}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:5px}"
                                  "QPushButton{padding:2px 4px}"

                                  )
        self.sdp_bt.setObjectName("sdp_bt")
        self.sdp_bt.setText("SDP")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(165, 70, 80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("加时得分胜")
        self.label.setStyleSheet("border:0px")

        self.sup_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sup_bt.setGeometry(QtCore.QRect(260, 35, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.sup_bt.setFont(font)
        self.sup_bt.setStyleSheet("QPushButton{color:#fff}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:#FFCD43}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:5px}"
                                  "QPushButton{padding:2px 4px}"

                                  )
        self.sup_bt.setObjectName("sup_bt")
        self.sup_bt.setText("SUP")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(245, 70, 80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("优势判定胜")
        self.label.setStyleSheet("border:0px")

        self.rsc_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.rsc_bt.setGeometry(QtCore.QRect(340, 35, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.rsc_bt.setFont(font)
        self.rsc_bt.setStyleSheet("QPushButton{color:#fff}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:#FFCD43}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:5px}"
                                  "QPushButton{padding:2px 4px}"

                                  )
        self.rsc_bt.setObjectName("rsc_bt")
        self.rsc_bt.setText("RSC")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(325, 70, 80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("终止比赛胜")
        self.label.setStyleSheet("border:0px")

        self.pun_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pun_bt.setGeometry(QtCore.QRect(420, 35, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.pun_bt.setFont(font)
        self.pun_bt.setStyleSheet("QPushButton{color:#fff}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:#FFCD43}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:5px}"
                                  "QPushButton{padding:2px 4px}"

                                  )
        self.pun_bt.setObjectName("pun_bt")
        self.pun_bt.setText("PUN")


        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(420, 70, 50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("犯规胜")
        self.label.setStyleSheet("border:0px")

        self.ko_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ko_bt.setGeometry(QtCore.QRect(500, 35, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.ko_bt.setFont(font)
        self.ko_bt.setStyleSheet("QPushButton{color:#fff}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:#FFCD43}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:5px}"
                                  "QPushButton{padding:2px 4px}"

                                  )
        self.ko_bt.setObjectName("ko_bt")
        self.ko_bt.setText("K.O")


        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(500, 70, 50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("击倒胜")
        self.label.setStyleSheet("border:0px")

        self.wdr_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.wdr_bt.setGeometry(QtCore.QRect(580, 35, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.wdr_bt.setFont(font)
        self.wdr_bt.setStyleSheet("QPushButton{color:#fff}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:#FFCD43}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:5px}"
                                  "QPushButton{padding:2px 4px}"

                                  )
        self.wdr_bt.setObjectName("wdr_bt")
        self.wdr_bt.setText("WDR")


        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(580, 70, 50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("弃权胜")
        self.label.setStyleSheet("border:0px")

        self.dsq_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.dsq_bt.setGeometry(QtCore.QRect(660, 35, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.dsq_bt.setFont(font)
        self.dsq_bt.setStyleSheet("QPushButton{color:#fff}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:#FFCD43}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:5px}"
                                  "QPushButton{padding:2px 4px}"

                                  )
        self.dsq_bt.setObjectName("dsq_bt")
        self.dsq_bt.setText("DSQ")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(660, 70, 50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("失格胜")
        self.label.setStyleSheet("border:0px")

        self.wiw_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.wiw_bt.setGeometry(QtCore.QRect(740, 35, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.wiw_bt.setFont(font)
        self.wiw_bt.setStyleSheet("QPushButton{color:#fff}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:#FFCD43}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:5px}"
                                  "QPushButton{padding:2px 4px}"

                                  )
        self.wiw_bt.setObjectName("wiw_bt")
        self.wiw_bt.setText("WIW")


        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(740, 70, 50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("体重胜")
        self.label.setStyleSheet("border:0px")


        self.draw_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.draw_bt.setGeometry(QtCore.QRect(820, 35, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.draw_bt.setFont(font)
        self.draw_bt.setStyleSheet("QPushButton{color:#fff}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:#FFCD43}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:5px}"
                                  "QPushButton{padding:2px 4px}"

                                  )
        self.draw_bt.setObjectName("draw_bt")
        self.draw_bt.setText("DRAW")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setGeometry(QtCore.QRect(820, 70, 50, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("平局结束")
        self.label.setStyleSheet("border:0px")

        self.qx_bt = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.qx_bt.setGeometry(QtCore.QRect(920, 30, 60, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Arial Black")
        font.setBold(True)
        self.qx_bt.setFont(font)
        self.qx_bt.setStyleSheet("QPushButton{color:#fff}"
                                   "QPushButton:hover{color:red}"
                                   "QPushButton{background-color:#3C3F41}"
                                   "QPushButton{border:2px}"
                                   "QPushButton{border-radius:5px}"
                                   "QPushButton{padding:2px 4px}"

                                   )
        self.qx_bt.setObjectName("qx_bt")
        self.qx_bt.setText("取 消")

        self.qx_bt.clicked.connect(self.qx)

        self.ptf_bt.clicked.connect(self.ptf)
        self.ptg_bt.clicked.connect(self.ptg)
        self.sdp_bt.clicked.connect(self.sdp)
        self.sup_bt.clicked.connect(self.sup)

        self.rsc_bt.clicked.connect(self.rsc)
        self.pun_bt.clicked.connect(self.pun)
        self.ko_bt.clicked.connect(self.ko)
        self.wdr_bt.clicked.connect(self.wdr)
        self.dsq_bt.clicked.connect(self.dsq)
        self.wiw_bt.clicked.connect(self.wiw)
        self.draw_bt.clicked.connect(self.draw)



    def ptf(self):
        gl.set_value('winway',"PTF")
        self.updateDB()
        gl.get_value('windialog').close()

    def ptg(self):
        gl.set_value('winway', "PTG")
        self.updateDB()
        gl.get_value('windialog').close()

    def sdp(self):
        gl.set_value('winway', "SDP")
        self.updateDB()
        gl.get_value('windialog').close()

    def sup(self):
        gl.set_value('winway', "SUP")
        self.updateDB()
        gl.get_value('windialog').close()

    def rsc(self):
        gl.set_value('winway', "RSC")
        self.updateDB()
        gl.get_value('windialog').close()

    def pun(self):
        gl.set_value('winway', "PUN")
        self.updateDB()
        gl.get_value('windialog').close()


    def ko(self):
        gl.set_value('winway', "K.O")
        self.updateDB()
        gl.get_value('windialog').close()

    def wdr(self):
        gl.set_value('winway', "WDR")
        self.updateDB()
        gl.get_value('windialog').close()

    def dsq(self):
        gl.set_value('winway', "DSQ")
        self.updateDB()
        gl.get_value('windialog').close()

    def wiw(self):
        gl.set_value('winway', "WIW")
        self.updateDB()
        gl.get_value('windialog').close()

    def draw(self):
        gl.set_value('winway', "DRAW")
        self.updateDB()
        gl.get_value('windialog').close()



    def qx(self):
        gl.get_value('windialog').close()


    def updateDB(self):
        s=gl.get_value('changdi')+gl.get_value('changdihao')+'胜者'
        sql = "update bisaixinxi set huoshengzhe='%s' ,bisaizhuangtai='已结束',huoshengfangshi='%s' where bisaixuhao = '%s'" % ( gl.get_value('huoshengzhe'),
            gl.get_value('winway'),gl.get_value('bisaixuhao'))
        print(sql)
        self.stat.update(sql)
        sql = "update bisaixinxi set hongfangxinming='%s',hongfangbianhao='%s',hongfangdanwei='%s' where hongfangxinming = '%s'" % (gl.get_value('winnername'),
                        gl.get_value('winnerbianhao'),gl.get_value('winnerdanwei'),s)
        print(sql)
        self.stat.update(sql)
        sql = "update bisaixinxi set qingfangxinming='%s',qingfangbianhao='%s',qingfangdanwei='%s' where qingfangxinming = '%s'" % (
               gl.get_value('winnername'),
               gl.get_value('winnerbianhao'), gl.get_value('winnerdanwei'),s)
        print(sql)
        self.stat.update(sql)



class winWindow(QtWidgets.QDialog):
    def __init__(self):
        super(winWindow,self).__init__()
        self.new=Ui_Form()
        self.new.setupUi(self)




if __name__ == '__main__':
    # utils.mysqlUtil.MysqlUtil.host = '10.60.144.104'
    # utils.mysqlUtil.MysqlUtil.dbPort = '3306'
    # utils.mysqlUtil.MysqlUtil.username = 'root'
    # utils.mysqlUtil.MysqlUtil.password = '123321'
    # utils.mysqlUtil.MysqlUtil.database = 'sport'

    app = QApplication(sys.argv)
    main = QtWidgets.QMainWindow()
    content = Ui_Form()
    content.setupUi(main)

    main.show()
    sys.exit(app.exec_())