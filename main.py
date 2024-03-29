from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QPushButton
from functions import *
from functools import partial

settings = []
with open('SetSituation/settings.txt', 'r') as file:
    for line in file:
        settings.append(line)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1089, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rez1 = QtWidgets.QWidget(self.centralwidget)
        self.rez1.setGeometry(QtCore.QRect(100, 230, 61, 101))
        self.rez1.setStyleSheet("border-radius: 30px;\n"
                                "background-color: rgb(255, 255, 0);")
        self.rez1.setObjectName("rez1")
        self.body_1 = QtWidgets.QWidget(self.rez1)
        self.body_1.setGeometry(QtCore.QRect(0, 20, 61, 61))
        self.body_1.setStyleSheet("background-color: rgb(255, 255, 0);\n"
                                  "border: 1px solid black;\n"
                                  "border-radius: 0;")
        self.body_1.setObjectName("body_1")
        self.label = QtWidgets.QLabel(self.body_1)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("margin-left:5%;\n"
                                 "border: 0px;")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 30, 20, 211))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(70, 170, 16, 201))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(80, 160, 51, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(80, 360, 111, 16))
        self.line_4.setStyleSheet("")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(130, 150, 71, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(190, 160, 20, 251))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(180, 350, 20, 21))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(190, 340, 21, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(200, 350, 20, 21))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(210, 360, 161, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(310, 150, 71, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(380, 350, 20, 21))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(360, 350, 20, 21))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(370, 160, 20, 251))
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(250, 170, 16, 201))
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(260, 160, 51, 20))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(390, 360, 161, 16))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setGeometry(QtCore.QRect(300, 30, 20, 211))
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setGeometry(QtCore.QRect(370, 340, 21, 20))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(490, 150, 71, 16))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_22 = QtWidgets.QFrame(self.centralwidget)
        self.line_22.setGeometry(QtCore.QRect(560, 350, 20, 21))
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.mCl3_2_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl3_2_icon.setGeometry(QtCore.QRect(520, 140, 21, 31))
        self.mCl3_2_icon.setStyleSheet("border: 20px solid transparent; \n"
                                       "background-color: rgb(0, 255, 0);\n"
                                       "border-bottom: 20px solid green;")
        self.mCl3_2_icon.setObjectName("mCl3_2_icon")
        self.line_23 = QtWidgets.QFrame(self.centralwidget)
        self.line_23.setGeometry(QtCore.QRect(540, 350, 20, 21))
        self.line_23.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.Background = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1091, 651))
        self.Background.setObjectName("Background")
        self.mCl3_1_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl3_1_icon.setGeometry(QtCore.QRect(480, 190, 21, 31))
        self.mCl3_1_icon.setStyleSheet("border: 20px solid transparent; \n"
                                       "background-color: rgb(0, 255, 0);\n"
                                       "border-bottom: 20px solid green;")
        self.mCl3_1_icon.setObjectName("mCl3_1_icon")
        self.line_24 = QtWidgets.QFrame(self.centralwidget)
        self.line_24.setGeometry(QtCore.QRect(550, 160, 20, 251))
        self.line_24.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.line_25 = QtWidgets.QFrame(self.centralwidget)
        self.line_25.setGeometry(QtCore.QRect(430, 170, 16, 201))
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.line_26 = QtWidgets.QFrame(self.centralwidget)
        self.line_26.setGeometry(QtCore.QRect(440, 160, 51, 20))
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.line_27 = QtWidgets.QFrame(self.centralwidget)
        self.line_27.setGeometry(QtCore.QRect(570, 370, 118, 3))
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.line_28 = QtWidgets.QFrame(self.centralwidget)
        self.line_28.setGeometry(QtCore.QRect(480, 30, 20, 211))
        self.line_28.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.line_29 = QtWidgets.QFrame(self.centralwidget)
        self.line_29.setGeometry(QtCore.QRect(550, 340, 21, 20))
        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.line_21 = QtWidgets.QFrame(self.centralwidget)
        self.line_21.setGeometry(QtCore.QRect(110, 400, 641, 16))
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_30 = QtWidgets.QFrame(self.centralwidget)
        self.line_30.setGeometry(QtCore.QRect(10, 20, 721, 16))
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.mCl3_4_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl3_4_icon.setGeometry(QtCore.QRect(480, 40, 21, 31))
        self.mCl3_4_icon.setStyleSheet("border: 20px solid transparent; \n"
                                       "background-color: rgb(0, 255, 0);\n"
                                       "border-bottom: 20px solid green;")
        self.mCl3_4_icon.setObjectName("mCl3_4_icon")
        self.rez2 = QtWidgets.QWidget(self.centralwidget)
        self.rez2.setGeometry(QtCore.QRect(280, 230, 61, 101))
        self.rez2.setStyleSheet("border-radius: 30px;\n"
                                "background-color: rgb(255, 255, 0);")
        self.rez2.setObjectName("rez2")
        self.body_2 = QtWidgets.QWidget(self.rez2)
        self.body_2.setGeometry(QtCore.QRect(0, 20, 61, 61))
        self.body_2.setStyleSheet("background-color: rgb(255, 255, 0);\n"
                                  "border: 1px solid black;\n"
                                  "border-radius: 0;")
        self.body_2.setObjectName("body_2")
        self.label_2 = QtWidgets.QLabel(self.body_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("margin-left:5%;\n"
                                   "border: 0px;")
        self.label_2.setObjectName("label_2")
        self.rez3 = QtWidgets.QWidget(self.centralwidget)
        self.rez3.setGeometry(QtCore.QRect(460, 230, 61, 101))
        self.rez3.setStyleSheet("border-radius: 30px;\n"
                                "background-color: rgb(255, 255, 0);")
        self.rez3.setObjectName("rez3")
        self.body_3 = QtWidgets.QWidget(self.rez3)
        self.body_3.setGeometry(QtCore.QRect(0, 20, 61, 61))
        self.body_3.setStyleSheet("background-color: rgb(255, 255, 0);\n"
                                  "border: 1px solid black;\n"
                                  "border-radius: 0;")
        self.body_3.setObjectName("body_3")
        self.label_3 = QtWidgets.QLabel(self.body_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("margin-left:5%;\n"
                                   "border: 0px;")
        self.label_3.setObjectName("label_3")
        self.mCl3_3_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl3_3_icon.setGeometry(QtCore.QRect(480, 110, 21, 31))
        self.mCl3_3_icon.setStyleSheet("border: 20px solid transparent; \n"
                                       "background-color: rgb(0, 255, 0);\n"
                                       "border-bottom: 20px solid green;")
        self.mCl3_3_icon.setObjectName("mCl3_3_icon")
        self.mCl3_1 = QtWidgets.QPushButton(self.centralwidget)
        self.mCl3_1.setGeometry(QtCore.QRect(510, 190, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl3_1.setFont(font)
        self.mCl3_1.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl3_1.setObjectName("mCl3_1")
        self.mCl3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.mCl3_2.setGeometry(QtCore.QRect(550, 130, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl3_2.setFont(font)
        self.mCl3_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl3_2.setObjectName("mCl3_2")
        self.mCl3_3 = QtWidgets.QPushButton(self.centralwidget)
        self.mCl3_3.setGeometry(QtCore.QRect(450, 110, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl3_3.setFont(font)
        self.mCl3_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl3_3.setObjectName("mCl3_3")
        self.mCl3_4 = QtWidgets.QPushButton(self.centralwidget)
        self.mCl3_4.setGeometry(QtCore.QRect(510, 50, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl3_4.setFont(font)
        self.mCl3_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl3_4.setObjectName("mCl3_4")
        self.mCl2_1_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl2_1_icon.setGeometry(QtCore.QRect(300, 190, 21, 31))
        self.mCl2_1_icon.setStyleSheet("border: 20px solid transparent; \n"
                                       "background-color: rgb(0, 255, 0);\n"
                                       "border-bottom: 20px solid green;")
        self.mCl2_1_icon.setObjectName("mCl2_1_icon")
        self.mCl2_3 = QtWidgets.QPushButton(self.centralwidget)
        self.mCl2_3.setGeometry(QtCore.QRect(270, 110, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl2_3.setFont(font)
        self.mCl2_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl2_3.setObjectName("mCl2_3")
        self.mCl2_2_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl2_2_icon.setGeometry(QtCore.QRect(340, 140, 21, 31))
        self.mCl2_2_icon.setStyleSheet("border: 20px solid transparent; \n"
                                       "background-color: rgb(0, 255, 0);\n"
                                       "border-bottom: 20px solid green;")
        self.mCl2_2_icon.setObjectName("mCl2_2_icon")
        self.mCl2_4_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl2_4_icon.setGeometry(QtCore.QRect(300, 40, 21, 31))
        self.mCl2_4_icon.setStyleSheet("border: 20px solid transparent; \n"
                                       "background-color: rgb(0, 255, 0);\n"
                                       "border-bottom: 20px solid green;")
        self.mCl2_4_icon.setObjectName("mCl2_4_icon")
        self.mCl2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.mCl2_2.setGeometry(QtCore.QRect(370, 130, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl2_2.setFont(font)
        self.mCl2_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl2_2.setObjectName("mCl2_2")
        self.mCl2_3_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl2_3_icon.setGeometry(QtCore.QRect(300, 110, 21, 31))
        self.mCl2_3_icon.setStyleSheet("border: 20px solid transparent; \n"
                                       "background-color: rgb(0, 255, 0);\n"
                                       "border-bottom: 20px solid green;")
        self.mCl2_3_icon.setObjectName("mCl2_3_icon")
        self.mCl2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.mCl2_1.setGeometry(QtCore.QRect(330, 190, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl2_1.setFont(font)
        self.mCl2_1.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl2_1.setObjectName("mCl2_1")
        self.mCl2_4 = QtWidgets.QPushButton(self.centralwidget)
        self.mCl2_4.setGeometry(QtCore.QRect(330, 50, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl2_4.setFont(font)
        self.mCl2_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl2_4.setObjectName("mCl2_4")
        self.mCl1_1_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl1_1_icon.setGeometry(QtCore.QRect(120, 190, 21, 31))
        self.mCl1_1_icon.setStyleSheet("border: 20px solid transparent; \n"
                                       "background-color: rgb(0, 255, 0);\n"
                                       "border-bottom: 20px solid green;")
        self.mCl1_1_icon.setObjectName("mCl1_1_icon")
        self.mCl1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.mCl1_3.setGeometry(QtCore.QRect(90, 110, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl1_3.setFont(font)
        self.mCl1_3.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl1_3.setObjectName("mCl1_3")
        self.mCl1_2_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl1_2_icon.setGeometry(QtCore.QRect(160, 140, 21, 31))
        self.mCl1_2_icon.setStyleSheet("border: 20px solid transparent; \n"
                                       "background-color: rgb(0, 255, 0);\n"
                                       "border-bottom: 20px solid green;")
        self.mCl1_2_icon.setObjectName("mCl1_2_icon")
        self.mCl1_4_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl1_4_icon.setGeometry(QtCore.QRect(120, 40, 21, 31))
        self.mCl1_4_icon.setStyleSheet("border: 20px solid transparent; \n"
                                       "background-color: rgb(0, 255, 0);\n"
                                       "border-bottom: 20px solid green;")
        self.mCl1_4_icon.setObjectName("mCl1_4_icon")
        self.mCl1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.mCl1_2.setGeometry(QtCore.QRect(190, 130, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl1_2.setFont(font)
        self.mCl1_2.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl1_2.setObjectName("mCl1_2")
        self.mCl1_3_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl1_3_icon.setGeometry(QtCore.QRect(120, 110, 21, 31))
        self.mCl1_3_icon.setStyleSheet("border: 20px solid transparent; \n"
                                       "background-color: rgb(0, 255, 0);\n"
                                       "border-bottom: 20px solid green;")
        self.mCl1_3_icon.setObjectName("mCl1_3_icon")
        self.mCl1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.mCl1_1.setGeometry(QtCore.QRect(150, 190, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl1_1.setFont(font)
        self.mCl1_1.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl1_1.setObjectName("mCl1_1")
        self.mCl1_4 = QtWidgets.QPushButton(self.centralwidget)
        self.mCl1_4.setGeometry(QtCore.QRect(150, 50, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl1_4.setFont(font)
        self.mCl1_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl1_4.setObjectName("mCl1_4")
        self.Sensor1_icon = QtWidgets.QWidget(self.centralwidget)
        self.Sensor1_icon.setGeometry(QtCore.QRect(120, 80, 21, 21))
        self.Sensor1_icon.setStyleSheet("\n"
                                        "background-color: rgb(170, 85, 255);\n"
                                        "border-bottom: 10px solid #623193;")
        self.Sensor1_icon.setObjectName("Sensor1_icon")
        self.Sensor1_pBut = QtWidgets.QPushButton(self.centralwidget)
        self.Sensor1_pBut.setGeometry(QtCore.QRect(90, 70, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Sensor1_pBut.setFont(font)
        self.Sensor1_pBut.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Sensor1_pBut.setObjectName("Sensor1_pBut")
        self.Sensor2_pBut = QtWidgets.QPushButton(self.centralwidget)
        self.Sensor2_pBut.setGeometry(QtCore.QRect(270, 70, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Sensor2_pBut.setFont(font)
        self.Sensor2_pBut.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Sensor2_pBut.setObjectName("Sensor2_pBut")
        self.Sensor2_icon = QtWidgets.QWidget(self.centralwidget)
        self.Sensor2_icon.setGeometry(QtCore.QRect(300, 80, 21, 21))
        self.Sensor2_icon.setStyleSheet("\n"
                                        "background-color: rgb(170, 85, 255);\n"
                                        "border-bottom: 10px solid #623193;")
        self.Sensor2_icon.setObjectName("Sensor2_icon")
        self.Sensor3_pBut = QtWidgets.QPushButton(self.centralwidget)
        self.Sensor3_pBut.setGeometry(QtCore.QRect(450, 70, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Sensor3_pBut.setFont(font)
        self.Sensor3_pBut.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Sensor3_pBut.setObjectName("Sensor3_pBut")
        self.Sensor3_icon = QtWidgets.QWidget(self.centralwidget)
        self.Sensor3_icon.setGeometry(QtCore.QRect(480, 80, 21, 21))
        self.Sensor3_icon.setStyleSheet("\n"
                                        "background-color: rgb(170, 85, 255);\n"
                                        "border-bottom: 10px solid #623193;")
        self.Sensor3_icon.setObjectName("Sensor3_icon")
        self.mCl_flushing_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl_flushing_icon.setGeometry(QtCore.QRect(630, 350, 21, 31))
        self.mCl_flushing_icon.setStyleSheet("border: 20px solid transparent; \n"
                                             "background-color: rgb(0, 255, 0);\n"
                                             "border-bottom: 20px solid green;")
        self.mCl_flushing_icon.setObjectName("mCl_flushing_icon")
        self.mCl_flushing = QtWidgets.QPushButton(self.centralwidget)
        self.mCl_flushing.setGeometry(QtCore.QRect(660, 340, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl_flushing.setFont(font)
        self.mCl_flushing.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl_flushing.setObjectName("mCl_flushing")
        self.mCl_suction_icon = QtWidgets.QWidget(self.centralwidget)
        self.mCl_suction_icon.setGeometry(QtCore.QRect(690, 390, 21, 31))
        self.mCl_suction_icon.setStyleSheet("border: 20px solid transparent; \n"
                                            "background-color: rgb(0, 255, 0);\n"
                                            "border-bottom: 20px solid green;")
        self.mCl_suction_icon.setObjectName("mCl_suction_icon")
        self.mCl_suction = QtWidgets.QPushButton(self.centralwidget)
        self.mCl_suction.setGeometry(QtCore.QRect(720, 370, 23, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mCl_suction.setFont(font)
        self.mCl_suction.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.mCl_suction.setObjectName("mCl_suction")
        self.Barrel_1 = QtWidgets.QLabel(self.centralwidget)
        self.Barrel_1.setGeometry(QtCore.QRect(40, 460, 81, 16))
        self.Barrel_1.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                    "color: rgb(255, 255, 0);")
        self.Barrel_1.setObjectName("Barrel_1")
        self.Barrel_2 = QtWidgets.QLabel(self.centralwidget)
        self.Barrel_2.setGeometry(QtCore.QRect(250, 460, 81, 16))
        self.Barrel_2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                    "color: rgb(255, 255, 0);")
        self.Barrel_2.setObjectName("Barrel_2")
        self.Barrel_3 = QtWidgets.QLabel(self.centralwidget)
        self.Barrel_3.setGeometry(QtCore.QRect(450, 460, 81, 16))
        self.Barrel_3.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                    "color: rgb(255, 255, 0);")
        self.Barrel_3.setObjectName("Barrel_3")
        self.Status_label1 = QtWidgets.QLabel(self.centralwidget)
        self.Status_label1.setGeometry(QtCore.QRect(10, 500, 81, 16))
        self.Status_label1.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                         "color: rgb(170, 255, 255);")
        self.Status_label1.setObjectName("Status_label1")
        self.Status_label2 = QtWidgets.QLabel(self.centralwidget)
        self.Status_label2.setGeometry(QtCore.QRect(210, 500, 81, 16))
        self.Status_label2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                         "color: rgb(170, 255, 255);")
        self.Status_label2.setObjectName("Status_label2")
        self.Status_label3 = QtWidgets.QLabel(self.centralwidget)
        self.Status_label3.setGeometry(QtCore.QRect(410, 500, 81, 16))
        self.Status_label3.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                         "color: rgb(170, 255, 255);")
        self.Status_label3.setObjectName("Status_label3")
        self.Status_B1 = QtWidgets.QLabel(self.centralwidget)
        self.Status_B1.setGeometry(QtCore.QRect(80, 500, 101, 16))
        self.Status_B1.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                     "color: rgb(255, 255, 255);")
        self.Status_B1.setObjectName("Status_B1")
        self.Status_B2 = QtWidgets.QLabel(self.centralwidget)
        self.Status_B2.setGeometry(QtCore.QRect(280, 500, 101, 16))
        self.Status_B2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                     "color: rgb(255, 255, 255);")
        self.Status_B2.setObjectName("Status_B2")
        self.Status_B3 = QtWidgets.QLabel(self.centralwidget)
        self.Status_B3.setGeometry(QtCore.QRect(480, 500, 101, 16))
        self.Status_B3.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                     "color: rgb(255, 255, 255);")
        self.Status_B3.setObjectName("Status_B3")
        self.Status_label2_2 = QtWidgets.QLabel(self.centralwidget)
        self.Status_label2_2.setGeometry(QtCore.QRect(210, 530, 81, 16))
        self.Status_label2_2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                           "color: rgb(170, 255, 255);")
        self.Status_label2_2.setObjectName("Status_label2_2")
        self.Status_label1_2 = QtWidgets.QLabel(self.centralwidget)
        self.Status_label1_2.setGeometry(QtCore.QRect(10, 530, 81, 16))
        self.Status_label1_2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                           "color: rgb(170, 255, 255);")
        self.Status_label1_2.setObjectName("Status_label1_2")
        self.Volume_B3 = QtWidgets.QLabel(self.centralwidget)
        self.Volume_B3.setGeometry(QtCore.QRect(490, 530, 101, 16))
        self.Volume_B3.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                     "color: rgb(255, 255, 255);")
        self.Volume_B3.setObjectName("Volume_B3")
        self.Volume_B1 = QtWidgets.QLabel(self.centralwidget)
        self.Volume_B1.setGeometry(QtCore.QRect(90, 530, 101, 16))
        self.Volume_B1.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                     "color: rgb(255, 255, 255);")
        self.Volume_B1.setObjectName("Volume_B1")
        self.Volume_B2 = QtWidgets.QLabel(self.centralwidget)
        self.Volume_B2.setGeometry(QtCore.QRect(290, 530, 101, 16))
        self.Volume_B2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                     "color: rgb(255, 255, 255);")
        self.Volume_B2.setObjectName("Volume_B2")
        self.Status_label3_2 = QtWidgets.QLabel(self.centralwidget)
        self.Status_label3_2.setGeometry(QtCore.QRect(410, 530, 81, 16))
        self.Status_label3_2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                           "color: rgb(170, 255, 255);")
        self.Status_label3_2.setObjectName("Status_label3_2")
        self.Status_label2_3 = QtWidgets.QLabel(self.centralwidget)
        self.Status_label2_3.setGeometry(QtCore.QRect(210, 560, 81, 16))
        self.Status_label2_3.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                           "color: rgb(170, 255, 255);")
        self.Status_label2_3.setObjectName("Status_label2_3")
        self.Status_label3_3 = QtWidgets.QLabel(self.centralwidget)
        self.Status_label3_3.setGeometry(QtCore.QRect(410, 560, 81, 16))
        self.Status_label3_3.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                           "color: rgb(170, 255, 255);")
        self.Status_label3_3.setObjectName("Status_label3_3")
        self.Temp_B1 = QtWidgets.QLabel(self.centralwidget)
        self.Temp_B1.setGeometry(QtCore.QRect(90, 560, 101, 16))
        self.Temp_B1.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                   "color: rgb(255, 255, 255);")
        self.Temp_B1.setObjectName("Temp_B1")
        self.Status_label1_3 = QtWidgets.QLabel(self.centralwidget)
        self.Status_label1_3.setGeometry(QtCore.QRect(10, 560, 81, 16))
        self.Status_label1_3.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                           "color: rgb(170, 255, 255);")
        self.Status_label1_3.setObjectName("Status_label1_3")
        self.Temp_B2 = QtWidgets.QLabel(self.centralwidget)
        self.Temp_B2.setGeometry(QtCore.QRect(290, 560, 101, 16))
        self.Temp_B2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                   "color: rgb(255, 255, 255);")
        self.Temp_B2.setObjectName("Temp_B2")
        self.Temp_B3 = QtWidgets.QLabel(self.centralwidget)
        self.Temp_B3.setGeometry(QtCore.QRect(490, 560, 101, 16))
        self.Temp_B3.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                   "color: rgb(255, 255, 255);")
        self.Temp_B3.setObjectName("Temp_B3")
        self.Status_label1_4 = QtWidgets.QLabel(self.centralwidget)
        self.Status_label1_4.setGeometry(QtCore.QRect(10, 590, 81, 16))
        self.Status_label1_4.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                           "color: rgb(170, 255, 255);")
        self.Status_label1_4.setObjectName("Status_label1_4")
        self.Pressure_B2 = QtWidgets.QLabel(self.centralwidget)
        self.Pressure_B2.setGeometry(QtCore.QRect(300, 590, 101, 16))
        self.Pressure_B2.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                       "color: rgb(255, 255, 255);")
        self.Pressure_B2.setObjectName("Pressure_B2")
        self.Status_label3_4 = QtWidgets.QLabel(self.centralwidget)
        self.Status_label3_4.setGeometry(QtCore.QRect(410, 590, 81, 16))
        self.Status_label3_4.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                           "color: rgb(170, 255, 255);")
        self.Status_label3_4.setObjectName("Status_label3_4")
        self.Status_label2_4 = QtWidgets.QLabel(self.centralwidget)
        self.Status_label2_4.setGeometry(QtCore.QRect(210, 590, 81, 16))
        self.Status_label2_4.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                           "color: rgb(170, 255, 255);")
        self.Status_label2_4.setObjectName("Status_label2_4")
        self.Pressure_B1 = QtWidgets.QLabel(self.centralwidget)
        self.Pressure_B1.setGeometry(QtCore.QRect(100, 590, 101, 16))
        self.Pressure_B1.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                       "color: rgb(255, 255, 255);")
        self.Pressure_B1.setObjectName("Pressure_B1")
        self.Pressure_B3 = QtWidgets.QLabel(self.centralwidget)
        self.Pressure_B3.setGeometry(QtCore.QRect(500, 590, 101, 16))
        self.Pressure_B3.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                       "color: rgb(255, 255, 255);")
        self.Pressure_B3.setObjectName("Pressure_B3")
        self.mCl1_1_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl1_1_label.setGeometry(QtCore.QRect(830, 20, 71, 21))
        self.mCl1_1_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                        "font: 87 11pt \"Arial Black\";")
        self.mCl1_1_label.setObjectName("mCl1_1_label")
        self.mCl1_1_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl1_1_status.setGeometry(QtCore.QRect(910, 20, 71, 21))
        self.mCl1_1_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.mCl1_1_status.setObjectName("mCl1_1_status")
        self.mCl1_2_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl1_2_status.setGeometry(QtCore.QRect(910, 50, 71, 21))
        self.mCl1_2_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.mCl1_2_status.setObjectName("mCl1_2_status")
        self.mCl1_2_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl1_2_label.setGeometry(QtCore.QRect(830, 50, 71, 21))
        self.mCl1_2_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                        "font: 87 11pt \"Arial Black\";")
        self.mCl1_2_label.setObjectName("mCl1_2_label")
        self.mCl1_3_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl1_3_status.setGeometry(QtCore.QRect(910, 80, 71, 21))
        self.mCl1_3_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.mCl1_3_status.setObjectName("mCl1_3_status")
        self.mCl1_3_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl1_3_label.setGeometry(QtCore.QRect(830, 80, 71, 21))
        self.mCl1_3_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                        "font: 87 11pt \"Arial Black\";")
        self.mCl1_3_label.setObjectName("mCl1_3_label")
        self.mCl1_4_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl1_4_status.setGeometry(QtCore.QRect(910, 110, 71, 21))
        self.mCl1_4_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.mCl1_4_status.setObjectName("mCl1_4_status")
        self.mCl1_4_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl1_4_label.setGeometry(QtCore.QRect(830, 110, 71, 21))
        self.mCl1_4_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                        "font: 87 11pt \"Arial Black\";")
        self.mCl1_4_label.setObjectName("mCl1_4_label")
        self.mCl2_1_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl2_1_status.setGeometry(QtCore.QRect(910, 140, 71, 21))
        self.mCl2_1_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.mCl2_1_status.setObjectName("mCl2_1_status")
        self.mCl2_1_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl2_1_label.setGeometry(QtCore.QRect(830, 140, 71, 21))
        self.mCl2_1_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                        "font: 87 11pt \"Arial Black\";")
        self.mCl2_1_label.setObjectName("mCl2_1_label")
        self.mCl2_2_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl2_2_status.setGeometry(QtCore.QRect(910, 170, 71, 21))
        self.mCl2_2_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.mCl2_2_status.setObjectName("mCl2_2_status")
        self.mCl2_2_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl2_2_label.setGeometry(QtCore.QRect(830, 170, 71, 21))
        self.mCl2_2_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                        "font: 87 11pt \"Arial Black\";")
        self.mCl2_2_label.setObjectName("mCl2_2_label")
        self.mCl2_3_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl2_3_status.setGeometry(QtCore.QRect(910, 200, 71, 21))
        self.mCl2_3_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.mCl2_3_status.setObjectName("mCl2_3_status")
        self.mCl2_3_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl2_3_label.setGeometry(QtCore.QRect(830, 200, 71, 21))
        self.mCl2_3_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                        "font: 87 11pt \"Arial Black\";")
        self.mCl2_3_label.setObjectName("mCl2_3_label")
        self.mCl2_4_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl2_4_status.setGeometry(QtCore.QRect(910, 230, 71, 21))
        self.mCl2_4_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.mCl2_4_status.setObjectName("mCl2_4_status")
        self.mCl2_4_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl2_4_label.setGeometry(QtCore.QRect(830, 230, 71, 21))
        self.mCl2_4_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                        "font: 87 11pt \"Arial Black\";")
        self.mCl2_4_label.setObjectName("mCl2_4_label")
        self.mCl3_1_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl3_1_status.setGeometry(QtCore.QRect(910, 260, 71, 21))
        self.mCl3_1_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.mCl3_1_status.setObjectName("mCl3_1_status")
        self.mCl3_1_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl3_1_label.setGeometry(QtCore.QRect(830, 260, 71, 21))
        self.mCl3_1_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                        "font: 87 11pt \"Arial Black\";")
        self.mCl3_1_label.setObjectName("mCl3_1_label")
        self.mCl3_2_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl3_2_status.setGeometry(QtCore.QRect(910, 290, 71, 21))
        self.mCl3_2_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.mCl3_2_status.setObjectName("mCl3_2_status")
        self.mCl3_2_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl3_2_label.setGeometry(QtCore.QRect(830, 290, 71, 21))
        self.mCl3_2_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                        "font: 87 11pt \"Arial Black\";")
        self.mCl3_2_label.setObjectName("mCl3_2_label")
        self.mCl3_3_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl3_3_status.setGeometry(QtCore.QRect(910, 320, 71, 21))
        self.mCl3_3_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.mCl3_3_status.setObjectName("mCl3_3_status")
        self.mCl3_3_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl3_3_label.setGeometry(QtCore.QRect(830, 320, 71, 21))
        self.mCl3_3_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                        "font: 87 11pt \"Arial Black\";")
        self.mCl3_3_label.setObjectName("mCl3_3_label")
        self.mCl3_4_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl3_4_status.setGeometry(QtCore.QRect(910, 350, 71, 21))
        self.mCl3_4_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.mCl3_4_status.setObjectName("mCl3_4_status")
        self.mCl3_4_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl3_4_label.setGeometry(QtCore.QRect(830, 350, 71, 21))
        self.mCl3_4_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                        "font: 87 11pt \"Arial Black\";")
        self.mCl3_4_label.setObjectName("mCl3_4_label")
        self.mCl_flushing_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl_flushing_label.setGeometry(QtCore.QRect(830, 380, 121, 21))
        self.mCl_flushing_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                              "font: 87 11pt \"Arial Black\";")
        self.mCl_flushing_label.setObjectName("mCl_flushing_label")
        self.mCl_flushing_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl_flushing_status.setGeometry(QtCore.QRect(970, 380, 71, 21))
        self.mCl_flushing_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                               "font: 87 11pt \"Arial Black\";")
        self.mCl_flushing_status.setObjectName("mCl_flushing_status")
        self.mCl_suction_label = QtWidgets.QLabel(self.centralwidget)
        self.mCl_suction_label.setGeometry(QtCore.QRect(830, 410, 121, 21))
        self.mCl_suction_label.setStyleSheet("color: rgb(124, 255, 229);\n"
                                             "font: 87 11pt \"Arial Black\";")
        self.mCl_suction_label.setObjectName("mCl_suction_label")
        self.mCl_suction_status = QtWidgets.QLabel(self.centralwidget)
        self.mCl_suction_status.setGeometry(QtCore.QRect(970, 410, 71, 21))
        self.mCl_suction_status.setStyleSheet("color: rgb(124, 255, 229);\n"
                                              "font: 87 11pt \"Arial Black\";")
        self.mCl_suction_status.setObjectName("mCl_suction_status")
        self.Sensor1_label = QtWidgets.QLabel(self.centralwidget)
        self.Sensor1_label.setGeometry(QtCore.QRect(680, 490, 61, 21))
        self.Sensor1_label.setStyleSheet("color: rgb(170, 0, 255);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.Sensor1_label.setObjectName("Sensor1_label")
        self.Sensor2_label = QtWidgets.QLabel(self.centralwidget)
        self.Sensor2_label.setGeometry(QtCore.QRect(680, 520, 61, 21))
        self.Sensor2_label.setStyleSheet("color: rgb(170, 0, 255);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.Sensor2_label.setObjectName("Sensor2_label")
        self.Sensor3_label = QtWidgets.QLabel(self.centralwidget)
        self.Sensor3_label.setGeometry(QtCore.QRect(680, 550, 61, 21))
        self.Sensor3_label.setStyleSheet("color: rgb(170, 0, 255);\n"
                                         "font: 87 11pt \"Arial Black\";")
        self.Sensor3_label.setObjectName("Sensor3_label")
        self.Sensor1_Status = QtWidgets.QLabel(self.centralwidget)
        self.Sensor1_Status.setGeometry(QtCore.QRect(750, 490, 121, 21))
        self.Sensor1_Status.setStyleSheet("color: rgb(170, 0, 255);\n"
                                          "font: 87 11pt \"Arial Black\";")
        self.Sensor1_Status.setObjectName("Sensor1_Status")
        self.Sensor3_Status = QtWidgets.QLabel(self.centralwidget)
        self.Sensor3_Status.setGeometry(QtCore.QRect(750, 550, 121, 21))
        self.Sensor3_Status.setStyleSheet("color: rgb(170, 0, 255);\n"
                                          "font: 87 11pt \"Arial Black\";")
        self.Sensor3_Status.setObjectName("Sensor3_Status")
        self.Sensor2_Status = QtWidgets.QLabel(self.centralwidget)
        self.Sensor2_Status.setGeometry(QtCore.QRect(750, 520, 121, 21))
        self.Sensor2_Status.setStyleSheet("color: rgb(170, 0, 255);\n"
                                          "font: 87 11pt \"Arial Black\";")
        self.Sensor2_Status.setObjectName("Sensor2_Status")
        self.Background.raise_()
        self.line.raise_()
        self.rez1.raise_()
        self.line_28.raise_()
        self.line_19.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.line_8.raise_()
        self.line_9.raise_()
        self.line_10.raise_()
        self.line_11.raise_()
        self.line_13.raise_()
        self.line_14.raise_()
        self.line_15.raise_()
        self.line_16.raise_()
        self.line_17.raise_()
        self.line_18.raise_()
        self.line_20.raise_()
        self.line_12.raise_()
        self.line_22.raise_()
        self.mCl3_2_icon.raise_()
        self.line_23.raise_()
        self.mCl3_1_icon.raise_()
        self.line_24.raise_()
        self.line_25.raise_()
        self.line_26.raise_()
        self.line_27.raise_()
        self.line_29.raise_()
        self.line_21.raise_()
        self.line_30.raise_()
        self.mCl3_4_icon.raise_()
        self.rez2.raise_()
        self.rez3.raise_()
        self.mCl3_3_icon.raise_()
        self.mCl3_1.raise_()
        self.mCl3_2.raise_()
        self.mCl3_3.raise_()
        self.mCl3_4.raise_()
        self.mCl2_1_icon.raise_()
        self.mCl2_3.raise_()
        self.mCl2_2_icon.raise_()
        self.mCl2_4_icon.raise_()
        self.mCl2_2.raise_()
        self.mCl2_3_icon.raise_()
        self.mCl2_1.raise_()
        self.mCl2_4.raise_()
        self.mCl1_1_icon.raise_()
        self.mCl1_3.raise_()
        self.mCl1_2_icon.raise_()
        self.mCl1_4_icon.raise_()
        self.mCl1_2.raise_()
        self.mCl1_3_icon.raise_()
        self.mCl1_1.raise_()
        self.mCl1_4.raise_()
        self.Sensor1_icon.raise_()
        self.Sensor1_pBut.raise_()
        self.Sensor2_pBut.raise_()
        self.Sensor2_icon.raise_()
        self.Sensor3_pBut.raise_()
        self.Sensor3_icon.raise_()
        self.mCl_flushing_icon.raise_()
        self.mCl_flushing.raise_()
        self.mCl_suction_icon.raise_()
        self.mCl_suction.raise_()
        self.Barrel_1.raise_()
        self.Barrel_2.raise_()
        self.Barrel_3.raise_()
        self.Status_label1.raise_()
        self.Status_label2.raise_()
        self.Status_label3.raise_()
        self.Status_B1.raise_()
        self.Status_B2.raise_()
        self.Status_B3.raise_()
        self.Status_label2_2.raise_()
        self.Status_label1_2.raise_()
        self.Volume_B3.raise_()
        self.Volume_B1.raise_()
        self.Volume_B2.raise_()
        self.Status_label3_2.raise_()
        self.Status_label2_3.raise_()
        self.Status_label3_3.raise_()
        self.Temp_B1.raise_()
        self.Status_label1_3.raise_()
        self.Temp_B2.raise_()
        self.Temp_B3.raise_()
        self.Status_label1_4.raise_()
        self.Pressure_B2.raise_()
        self.Status_label3_4.raise_()
        self.Status_label2_4.raise_()
        self.Pressure_B1.raise_()
        self.Pressure_B3.raise_()
        self.mCl1_1_label.raise_()
        self.mCl1_1_status.raise_()
        self.mCl1_2_status.raise_()
        self.mCl1_2_label.raise_()
        self.mCl1_3_status.raise_()
        self.mCl1_3_label.raise_()
        self.mCl1_4_status.raise_()
        self.mCl1_4_label.raise_()
        self.mCl2_1_status.raise_()
        self.mCl2_1_label.raise_()
        self.mCl2_2_status.raise_()
        self.mCl2_2_label.raise_()
        self.mCl2_3_status.raise_()
        self.mCl2_3_label.raise_()
        self.mCl2_4_status.raise_()
        self.mCl2_4_label.raise_()
        self.mCl3_1_status.raise_()
        self.mCl3_1_label.raise_()
        self.mCl3_2_status.raise_()
        self.mCl3_2_label.raise_()
        self.mCl3_3_status.raise_()
        self.mCl3_3_label.raise_()
        self.mCl3_4_status.raise_()
        self.mCl3_4_label.raise_()
        self.mCl_flushing_label.raise_()
        self.mCl_flushing_status.raise_()
        self.mCl_suction_label.raise_()
        self.mCl_suction_status.raise_()
        self.Sensor1_label.raise_()
        self.Sensor2_label.raise_()
        self.Sensor3_label.raise_()
        self.Sensor1_Status.raise_()
        self.Sensor3_Status.raise_()
        self.Sensor2_Status.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Psuc = 10
        self.Pflush = 506
        self.PsucBf = 0
        self.PflushBf = 0
        self.PressureSensors = [self.Psuc, self.Pflush, self.PsucBf, self.PflushBf]



        self.barrels = [self.rez1, self.rez2, self.rez3]
        self.barrelsStatusLabel = [self.Status_B1, self.Status_B2, self.Status_B3]
        self.barrelsVolume = [self.Volume_B1, self.Volume_B2, self.Volume_B3]
        self.barrelsTemp = [self.Temp_B1, self.Temp_B2, self.Temp_B3]
        self.barrelsPressure = [self.Pressure_B1, self.Pressure_B2, self.Pressure_B3]
        self.barrelsStatus = []

        self.mSensors = [self.Sensor1_pBut, self.Sensor2_pBut, self.Sensor3_pBut]
        self.mSensorsIcons = []
        self.MSensStatusLabels = []
        self.mSensorsNames = []
        self.MSensStatus = []

        for el in self.mSensors:
            exec(f"self.mSensorsIcons.append(self.{el.objectName()[:-5]}_icon)")
            exec(f"self.MSensStatusLabels.append(self.{el.objectName()[:-5]}_Status.objectName())")
            exec(f"self.mSensorsNames.append(self.{el.objectName()}.objectName())")



        self.buttons = [self.mCl1_1, self.mCl1_2, self.mCl1_3,
                        self.mCl1_4, self.mCl2_1, self.mCl2_2,
                        self.mCl2_3, self.mCl2_4, self.mCl3_1,
                        self.mCl3_2, self.mCl3_3, self.mCl3_4,
                        self.mCl_flushing, self.mCl_suction]

        self.buttonsNames = []
        self.status = []
        self.icons = []

        for el in self.buttons:
            exec(f"self.icons.append(self.{el.objectName()}_icon)")
            exec(f"self.status.append(self.{el.objectName()}_status.objectName())")
            exec(f"self.buttonsNames.append(self.{el.objectName()}.objectName())")

        self.switchesStatus = []

        self.setValues()

        self.Section1Sens = dict(zip(self.mSensorsNames, self.MSensStatus))

        self.Section1switches = dict(zip(self.buttonsNames, self.switchesStatus))

        self.setPressure()

        self.rendering()

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "3"))
        self.mCl3_1.setText(_translate("MainWindow", "У"))
        self.mCl3_2.setText(_translate("MainWindow", "У"))
        self.mCl3_3.setText(_translate("MainWindow", "У"))
        self.mCl3_4.setText(_translate("MainWindow", "У"))
        self.mCl2_3.setText(_translate("MainWindow", "У"))
        self.mCl2_2.setText(_translate("MainWindow", "У"))
        self.mCl2_1.setText(_translate("MainWindow", "У"))
        self.mCl2_4.setText(_translate("MainWindow", "У"))
        self.mCl1_3.setText(_translate("MainWindow", "У"))
        self.mCl1_2.setText(_translate("MainWindow", "У"))
        self.mCl1_1.setText(_translate("MainWindow", "У"))
        self.mCl1_4.setText(_translate("MainWindow", "У"))
        self.Sensor1_pBut.setText(_translate("MainWindow", "m"))
        self.Sensor2_pBut.setText(_translate("MainWindow", "m"))
        self.Sensor3_pBut.setText(_translate("MainWindow", "m"))
        self.mCl_flushing.setText(_translate("MainWindow", "У"))
        self.mCl_suction.setText(_translate("MainWindow", "У"))
        self.Barrel_1.setText(_translate("MainWindow", "Barrel 1"))
        self.Barrel_2.setText(_translate("MainWindow", "Barrel 2"))
        self.Barrel_3.setText(_translate("MainWindow", "Barrel 3"))
        self.Status_label1.setText(_translate("MainWindow", "Status:"))
        self.Status_label2.setText(_translate("MainWindow", "Status:"))
        self.Status_label3.setText(_translate("MainWindow", "Status:"))
        self.Status_B1.setText(_translate("MainWindow", "загрузка..."))
        self.Status_B2.setText(_translate("MainWindow", "загрузка..."))
        self.Status_B3.setText(_translate("MainWindow", "загрузка..."))
        self.Status_label2_2.setText(_translate("MainWindow", "Volume:"))
        self.Status_label1_2.setText(_translate("MainWindow", "Volume:"))
        self.Volume_B3.setText(_translate("MainWindow", "загрузка..."))
        self.Volume_B1.setText(_translate("MainWindow", "загрузка..."))
        self.Volume_B2.setText(_translate("MainWindow", "загрузка..."))
        self.Status_label3_2.setText(_translate("MainWindow", "Volume:"))
        self.Status_label2_3.setText(_translate("MainWindow", "Temp:"))
        self.Status_label3_3.setText(_translate("MainWindow", "Temp:"))
        self.Temp_B1.setText(_translate("MainWindow", "..."))
        self.Status_label1_3.setText(_translate("MainWindow", "Temp:"))
        self.Temp_B2.setText(_translate("MainWindow", "..."))
        self.Temp_B3.setText(_translate("MainWindow", "..."))
        self.Status_label1_4.setText(_translate("MainWindow", "Pressure:"))
        self.Pressure_B2.setText(_translate("MainWindow", "..."))
        self.Status_label3_4.setText(_translate("MainWindow", "Pressure:"))
        self.Status_label2_4.setText(_translate("MainWindow", "Pressure:"))
        self.Pressure_B1.setText(_translate("MainWindow", "..."))
        self.Pressure_B3.setText(_translate("MainWindow", "..."))
        self.mCl1_1_label.setText(_translate("MainWindow", "mCl1_1: "))
        self.mCl1_1_status.setText(_translate("MainWindow", "..."))
        self.mCl1_2_status.setText(_translate("MainWindow", "..."))
        self.mCl1_2_label.setText(_translate("MainWindow", "mCl1_2: "))
        self.mCl1_3_status.setText(_translate("MainWindow", "..."))
        self.mCl1_3_label.setText(_translate("MainWindow", "mCl1_3: "))
        self.mCl1_4_status.setText(_translate("MainWindow", "..."))
        self.mCl1_4_label.setText(_translate("MainWindow", "mCl1_4: "))
        self.mCl2_1_status.setText(_translate("MainWindow", "..."))
        self.mCl2_1_label.setText(_translate("MainWindow", "mCl2_1: "))
        self.mCl2_2_status.setText(_translate("MainWindow", "..."))
        self.mCl2_2_label.setText(_translate("MainWindow", "mCl2_2: "))
        self.mCl2_3_status.setText(_translate("MainWindow", "..."))
        self.mCl2_3_label.setText(_translate("MainWindow", "mCl2_3: "))
        self.mCl2_4_status.setText(_translate("MainWindow", "..."))
        self.mCl2_4_label.setText(_translate("MainWindow", "mCl2_4: "))
        self.mCl3_1_status.setText(_translate("MainWindow", "..."))
        self.mCl3_1_label.setText(_translate("MainWindow", "mCl3_1: "))
        self.mCl3_2_status.setText(_translate("MainWindow", "..."))
        self.mCl3_2_label.setText(_translate("MainWindow", "mCl3_2: "))
        self.mCl3_3_status.setText(_translate("MainWindow", "..."))
        self.mCl3_3_label.setText(_translate("MainWindow", "mCl3_3: "))
        self.mCl3_4_status.setText(_translate("MainWindow", "..."))
        self.mCl3_4_label.setText(_translate("MainWindow", "mCl3_4: "))
        self.mCl_flushing_label.setText(_translate("MainWindow", "mCl_flushing: "))
        self.mCl_flushing_status.setText(_translate("MainWindow", "..."))
        self.mCl_suction_label.setText(_translate("MainWindow", "mCl_suction: "))
        self.mCl_suction_status.setText(_translate("MainWindow", "..."))
        self.Sensor1_label.setText(_translate("MainWindow", "Sens1: "))
        self.Sensor2_label.setText(_translate("MainWindow", "Sens2: "))
        self.Sensor3_label.setText(_translate("MainWindow", "Sens3: "))
        self.Sensor1_Status.setText(_translate("MainWindow", "..."))
        self.Sensor3_Status.setText(_translate("MainWindow", "..."))
        self.Sensor2_Status.setText(_translate("MainWindow", "..."))

    def setValues(self):
        self.switchesStatus = list(map(int, settings[0].split()))
        self.barrelsStatus = list(map(int, settings[1].split()))
        self.MSensStatus = list(map(int, settings[2].split()))

        self.Sensor1 = MSens(0, True)
        self.Sensor2 = MSens(1, True)
        self.Sensor3 = MSens(2, True)

        self.Bar1 = Barrel(self.barrelsStatus[0], 4, 0, 0, 0)
        self.Bar2 = Barrel(self.barrelsStatus[1], 4, 0, 0, 1)
        self.Bar3 = Barrel(self.barrelsStatus[2], 4, 0, 0, 2)
        self.Bar =[self.Bar1, self.Bar2, self.Bar3]

    def setPressure(self):
        if list(self.Section1switches.values())[-1] == 0: self.PsucBf = 0
        else: self.PsucBf = 10

        if list(self.Section1switches.values())[-2] == 0: self.PflushBf = 0
        else: self.PflushBf = 506

        self.PressureSensors = [self.Psuc, self.Pflush, self.PsucBf, self.PflushBf]
        print(self.PressureSensors)
        print(list(self.Section1switches.values()))


    def rendering(self):
        f = -1
        for i in range(1, 4):
            for j in range(1, 5):
                f += 1
                el = str(self.Section1switches.get(self.buttonsNames[f]))
                exec(f"self.mCl{i}_{j}_status.setText('{el}')")
                icon = self.icons[f]
                if int(el) == 0:
                    self.set_red(icon)
                else:
                    self.set_green(icon)
        del (f)

        self.mCl_suction_status.setText(str(self.Section1switches.get(self.mCl_suction.objectName())))
        if int(self.Section1switches.get(self.mCl_suction.objectName())) == 0:
            self.set_red(self.mCl_suction_icon)
        else:
            self.set_green(self.mCl_suction_icon)
        self.mCl_flushing_status.setText(str(self.Section1switches.get(self.mCl_flushing.objectName())))
        if int(self.Section1switches.get(self.mCl_flushing.objectName())) == 0:
            self.set_red(self.mCl_flushing_icon)
        else:
            self.set_green(self.mCl_flushing_icon)

        for i in range(len(self.mSensors)):
            el = str(self.Section1Sens.get(self.mSensorsNames[i]))
            exec(f"self.{self.MSensStatusLabels[i]}.setText('{el}')")
            icon = self.mSensorsIcons[i]
            if int(el) == 0:
                self.set_grey(icon)
            else:
                self.set_purple(icon)

        self.BarrelRender()

    def BarrelRender(self):
        self.barrelsStatus.clear()
        val = list(self.Section1switches.values())
        for i in range(0, 9, 4):
            if (int(val[0 + i]) + int(val[2 + i]) + int(val[3 + i])) == 3:
                self.barrelsStatus.append(1)
            else:
                self.barrelsStatus.append(0)
        for i in range(len(self.barrelsStatus)):
            if self.barrelsStatus[i] != 1:
                self.barrelsStatusLabel[i].setText("Отключен")
                self.barrelsStatusLabel[i].setStyleSheet('font: 87 12pt "Arial Black";'
                                                         'color: #ff0000;')
                self.Bar[i].set_vallue_barrel(0,101)
            else:
                self.barrelsStatusLabel[i].setText("Активен")
                self.barrelsStatusLabel[i].setStyleSheet('font: 87 12pt "Arial Black";'
                                                         'color: #00ff00;')
                self.Bar[i].set_vallue_barrel(55,1300)
            info = self.Bar[i].get_info_barrel()
            self.barrelsVolume[i].setText(str(info[1]) +" м^3")
            self.barrelsPressure[i].setText(str(info[3]) +" кПа")
            self.barrelsTemp[i].setText(str(info[2]) +" \"C")

    def dialog(self, dict, name, obj, icon):
        confirmation = QMessageBox()
        confirmation.setWindowTitle("Подтверждение")
        confirmation.setText("Изменить положение переключателя?")
        confirmation.addButton(QPushButton("Переключить"), QMessageBox.YesRole)
        confirmation.addButton(QPushButton("Отмена"), QMessageBox.RejectRole)

        ret = confirmation.exec()

        if ret == 0: self.mCl_click(dict, name, obj, icon)

    def dialog_Sens(self, dict, name, obj, icon):
        confirmation = QMessageBox()
        confirmation.setWindowTitle("Подтверждение")
        if dict[name] == 1:
            confirmation.setText("Отключить датчик аварийной защиты?")
        else:
            confirmation.setText("Включить датчик аварийной защиты?")
        confirmation.addButton(QPushButton("Подтверждаю"), QMessageBox.YesRole)
        confirmation.addButton(QPushButton("Отмена"), QMessageBox.RejectRole)

        ret = confirmation.exec()

        if ret == 0: self.mSens_click(dict, name, obj, icon)

    def mCl_click(self, dict, name, obj, icon):
        if dict[name] == 0:
            dict[name] = 1
            self.set_green(icon)
        else:
            dict[name] = 0
            self.set_red(icon)
        exec(f"self.{obj}.setText('{str(dict.get(name))}')")
        self.BarrelRender()
        self.setPressure()


    def mSens_click(self, dict, name, obj, icon):
        if dict[name] == 0:
            dict[name] = 1
            self.set_purple(icon)
        else:
            dict[name] = 0
            self.set_grey(icon)
        exec(f"self.{obj}.setText('{str(dict.get(name))}')")
        self.BarrelRender()
        self.setPressure()

    def set_green(self, icon):
        icon.setStyleSheet('border: 20px solid transparent;'
                           'background-color: rgb(0, 255, 0);'
                           'border-bottom: 20px solid green;')

    def set_red(self, icon):
        icon.setStyleSheet('border: 20px solid transparent;'
                           'background-color: rgb(255, 0, 0);'
                           'border-bottom: 20px solid rgb(155, 0, 0);')

    def set_purple(self, icon):
        icon.setStyleSheet('background-color: rgb(170, 85, 255);'
                           'border-bottom: 10px solid #623193;')

    def set_grey(self, icon):
        icon.setStyleSheet('background-color: rgb(171, 171, 171);'
                           'border-bottom: 10px solid #717171;')

    def add_functions(self):

        for i in range(len(self.buttons)):
            self.buttons[i].clicked.connect(
                partial(self.dialog, self.Section1switches, name=self.buttonsNames[i], obj=self.status[i],
                        icon=self.icons[i]))

        for i in range(len(self.mSensors)):
            self.mSensors[i].clicked.connect(
                partial(self.dialog_Sens, self.Section1Sens, name=self.mSensorsNames[i],
                        obj=self.MSensStatusLabels[i], icon=self.mSensorsIcons[i]))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
