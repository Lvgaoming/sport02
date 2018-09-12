# -*- coding: utf-8 -*-
import sys
# sys.path.append('..')
from PyQt5 import sip
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QMessageBox
from PyQt5 import QtWidgets
import ui.ui_login
import ui.ui_main
import ui.ui_run
import ui.ui_ryjl
import ui.ui_sitUps
import ui.ui_setting_db
# import utils.pyMysqlUtils
import utils.mysqlUtil
import configparser
import shutil

app = QApplication(sys.argv)
# 登录界面


class loginWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.loginUI = ui.ui_login.Ui_MainWindow()
        self.loginUI.setupUi(self)
        # 登录按钮
        self.loginUI.pushButton.clicked.connect(lambda: goLogin(self.loginUI))

# 主界面


class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.mainUi = ui.ui_main.Ui_ChildrenWindow()
        self.ryjlUi = ui.ui_ryjl.Ui_Form()
        self.ywqzUi = ui.ui_sitUps.Ui_Form()
        self.mainUi.setupUi(self)
        # 50米测试按钮
        self.mainUi.pushButton.clicked.connect(goRun)
        self.mainUi.pushButton_2.clicked.connect(ywqz)
        self.mainUi.pushButton_3.clicked.connect(jianlu)
        self.mainUi.pushButton_4.clicked.connect(showDB)

# 跑步界面


class runWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.runUi = ui.ui_run.Ui_Form()
        self.runUi.setupUi(self)

#人员检录页面
class ryjlWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ryjlUi = ui.ui_ryjl.Ui_Form()
        self.ryjlUi.setupUi(self)

#人员检录页面
class ywqzWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ywqzUi = ui.ui_sitUps.Ui_Form()
        self.ywqzUi.setupUi(self)

# 出现50米测试页面


def goRun():
    _run.show()

# 登录方法


def goLogin(loginComponent):
    # print(loginComponent.lineEdit.text())
    # print(loginComponent.lineEdit_2.text())
    stat = utils.mysqlUtil.MysqlUtil()
    sql = "SELECT id,username FROM sys_user WHERE username='%s' AND password='%s'"%(loginComponent.lineEdit.text(),loginComponent.lineEdit_2.text())
    results = stat.fetchone(sql)
    if results==None:
        qw = QtWidgets.QWidget()
        QMessageBox.warning(qw,'错误','用户名或密码错误', QMessageBox.Ok)
    else:
        _main.show()
        _login.hide()


#人员检录

def jianlu():
    _ryjl.show()

#人员检录

def ywqz():
    _ywqz.show()  

#数据库显示
def showDB():
    _showDB.show()



if __name__ == '__main__':
    # loginUI = ui.ui_login.Ui_MainWindow()
    # loginUI.setupUi(widget)
    # loginUI.pushButton.clicked.connect(lambda: goLogin(loginUI))
    #拷贝dll文件
    # shutil.copy('dcrf32.dll', 'C:/Windows/System32')
    #设置配置文件中的密码
    cf = configparser.ConfigParser()
    cf.read("db.ini")
    utils.mysqlUtil.MysqlUtil.host = cf.get("db", "db_host")
    utils.mysqlUtil.MysqlUtil.dbPort = cf.getint("db", "db_port")
    utils.mysqlUtil.MysqlUtil.username = cf.get("db", "db_user")
    utils.mysqlUtil.MysqlUtil.password = cf.get("db", "db_password")
    utils.mysqlUtil.MysqlUtil.database = cf.get("db", "db_database")
    _login = loginWindow()
    _main = mainWindow()
    _run = runWindow()
    _ryjl = ryjlWindow()
    _ywqz = ywqzWindow()
    _showDB = ui.ui_setting_db.setDBWindow()
    _login.show()
    # widget.show()
    sys.exit(app.exec_())
