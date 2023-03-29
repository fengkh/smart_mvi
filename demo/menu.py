# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setStyleSheet("QLineEdit{\n"
                                 "    border:0px;    \n"
                                 "    margin:10px;\n"
                                 "    margin-left:10px; \n"
                                 "    margin-right:10px;\n"
                                 "    border-bottom: 2px solid #B3B3B3;\n"
                                 "    font-family:\'Microsoft YaHei\';\n"
                                 "    font-size:20px;\n"
                                 "    font-weight:bold;\n"
                                 "    }\n"
                                 "\n"
                                 "QLineEdit:hover{\n"
                                 "    border-bottom: 3px solid #66A3FF;\n"
                                 "    }\n"
                                 "\n"
                                 "QLineEdit:focus{\n"
                                 "    border-bottom: 3px solid #E680BD;\n"
                                 "    }\n"
                                 "\n"
                                 "QWidget#centralwidget{\n"
                                 "    background:white;\n"
                                 "    border-radius:10px;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel{\n"
                                 "    text-align:right;\n"
                                 "    font-family:\'Microsoft YaHei\';\n"
                                 "    font-size:30px;\n"
                                 "    font-weight:bold;\n"
                                 "    }\n"
                                 "\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.close_pushButton = QtWidgets.QPushButton(self.widget)
        self.close_pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_pushButton.sizePolicy().hasHeightForWidth())
        self.close_pushButton.setSizePolicy(sizePolicy)
        self.close_pushButton.setMinimumSize(QtCore.QSize(20, 20))
        self.close_pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.close_pushButton.setStyleSheet("QPushButton\n"
                                            "{\n"
                                            "background:#FF6694;\n"
                                            "border-radius:10px;\n"
                                            "}\n"
                                            "QPushButton:hover\n"
                                            "{\n"
                                            "background:#FF0000;\n"
                                            "}\n"
                                            "\n"
                                            "")
        self.close_pushButton.setText("")
        self.close_pushButton.setObjectName("close_pushButton")
        self.horizontalLayout_3.addWidget(self.close_pushButton)
        self.hidden_pushButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hidden_pushButton.sizePolicy().hasHeightForWidth())
        self.hidden_pushButton.setSizePolicy(sizePolicy)
        self.hidden_pushButton.setMinimumSize(QtCore.QSize(20, 20))
        self.hidden_pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.hidden_pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.hidden_pushButton.setStyleSheet("QPushButton\n"
                                             "{\n"
                                             "background:#FFDF80;\n"
                                             "border-radius:10px;\n"
                                             "}\n"
                                             "QPushButton:hover\n"
                                             "{\n"
                                             "background:#FFC105;\n"
                                             "}\n"
                                             "\n"
                                             "")
        self.hidden_pushButton.setText("")
        self.hidden_pushButton.setObjectName("hidden_pushButton")
        self.horizontalLayout_3.addWidget(self.hidden_pushButton)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.user_lineEdit = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_lineEdit.sizePolicy().hasHeightForWidth())
        self.user_lineEdit.setSizePolicy(sizePolicy)
        self.user_lineEdit.setInputMask("")
        self.user_lineEdit.setText("")
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.gridLayout.addWidget(self.user_lineEdit, 1, 1, 1, 1)
        self.password_lineEdit = QtWidgets.QLineEdit(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_lineEdit.sizePolicy().hasHeightForWidth())
        self.password_lineEdit.setSizePolicy(sizePolicy)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.gridLayout.addWidget(self.password_lineEdit, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.login_pushButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_pushButton.sizePolicy().hasHeightForWidth())
        self.login_pushButton.setSizePolicy(sizePolicy)
        self.login_pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.login_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.login_pushButton.setStyleSheet("QPushButton{\n"
                                            "    border:0px;\n"
                                            "    height:30px;\n"
                                            "    border-radius:15px;\n"
                                            "    font-family:\'Microsoft YaHei\';\n"
                                            "    font-size:20px;\n"
                                            "    color:white;\n"
                                            "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #fbc2eb, stop:1 #a6c1ee);\n"
                                            "    }\n"
                                            "\n"
                                            " QPushButton:hover{\n"
                                            "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ffd2f0, stop:1 #b0cbf8);\n"
                                            " }\n"
                                            " \n"
                                            " QPushButton:pressed{\n"
                                            "     background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e1aad2, stop:1 #92adda);\n"
                                            "     }")
        self.login_pushButton.setFlat(False)
        self.login_pushButton.setObjectName("login_pushButton")
        self.horizontalLayout.addWidget(self.login_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登录程序"))
        self.user_lineEdit.setPlaceholderText(_translate("MainWindow", "用户名"))
        self.password_lineEdit.setPlaceholderText(_translate("MainWindow", "密码"))
        self.label.setText(_translate("MainWindow", "智慧肝脏病理检测系统"))
        self.login_pushButton.setText(_translate("MainWindow", "登录"))