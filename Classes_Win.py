# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Classes_Win.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
import Classes



class Ui_Classes(object):
    def setupUi(self, Classes):
        Classes.setObjectName("Classes")
        Classes.resize(1604, 820)
        Classes.setStyleSheet("background-image: url(:/Background/QRC/magicpattern-gradient-1690353787077.jpeg);")
        self.gridLayout = QtWidgets.QGridLayout(Classes)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.KinderGarden = QtWidgets.QPushButton(Classes)
        self.KinderGarden.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.KinderGarden.setFont(font)
        self.KinderGarden.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/QRC/kindergartenIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KinderGarden.setIcon(icon)
        self.KinderGarden.setIconSize(QtCore.QSize(25, 28))
        self.KinderGarden.setObjectName("KinderGarden")
        self.verticalLayout.addWidget(self.KinderGarden)
        self.Class_1 = QtWidgets.QPushButton(Classes)
        self.Class_1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Class_1.setFont(font)
        self.Class_1.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icon/QRC/Class_I_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Class_1.setIcon(icon1)
        self.Class_1.setIconSize(QtCore.QSize(27, 27))
        self.Class_1.setObjectName("Class_1")
        self.Class_1.clicked.connect(lambda: self.load_classwiseTT('Class_1'))
        self.verticalLayout.addWidget(self.Class_1)
        self.Class_2 = QtWidgets.QPushButton(Classes)
        self.Class_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Class_2.setFont(font)
        self.Class_2.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icon/QRC/Class_II_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Class_2.setIcon(icon2)
        self.Class_2.setIconSize(QtCore.QSize(27, 27))
        self.Class_2.setObjectName("Class_2")
        self.Class_2.clicked.connect(lambda: self.load_classwiseTT('Class_2'))
        self.verticalLayout.addWidget(self.Class_2)
        self.Class_3 = QtWidgets.QPushButton(Classes)
        self.Class_3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Class_3.setFont(font)
        self.Class_3.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icon/QRC/Class_III_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Class_3.setIcon(icon3)
        self.Class_3.setIconSize(QtCore.QSize(27, 27))
        self.Class_3.setObjectName("Class_3")
        self.verticalLayout.addWidget(self.Class_3)
        self.Class_4 = QtWidgets.QPushButton(Classes)
        self.Class_4.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Class_4.setFont(font)
        self.Class_4.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icon/QRC/Class_IV_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Class_4.setIcon(icon4)
        self.Class_4.setIconSize(QtCore.QSize(27, 27))
        self.Class_4.setObjectName("Class_4")
        self.verticalLayout.addWidget(self.Class_4)
        self.Class_5 = QtWidgets.QPushButton(Classes)
        self.Class_5.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Class_5.setFont(font)
        self.Class_5.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icon/QRC/Class_V_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Class_5.setIcon(icon5)
        self.Class_5.setIconSize(QtCore.QSize(27, 27))
        self.Class_5.setObjectName("Class_5")
        self.verticalLayout.addWidget(self.Class_5)
        self.Class_6 = QtWidgets.QPushButton(Classes)
        self.Class_6.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Class_6.setFont(font)
        self.Class_6.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icon/QRC/Class_VI_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Class_6.setIcon(icon6)
        self.Class_6.setIconSize(QtCore.QSize(27, 27))
        self.Class_6.setObjectName("Class_6")
        self.verticalLayout.addWidget(self.Class_6)
        self.Class_7 = QtWidgets.QPushButton(Classes)
        self.Class_7.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Class_7.setFont(font)
        self.Class_7.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icon/QRC/Class_VII_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Class_7.setIcon(icon7)
        self.Class_7.setIconSize(QtCore.QSize(27, 27))
        self.Class_7.setObjectName("Class_7")
        self.verticalLayout.addWidget(self.Class_7)
        self.Class_8 = QtWidgets.QPushButton(Classes)
        self.Class_8.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Class_8.setFont(font)
        self.Class_8.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/Icon/QRC/Class_VIII_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Class_8.setIcon(icon8)
        self.Class_8.setIconSize(QtCore.QSize(27, 27))
        self.Class_8.setObjectName("Class_8")
        self.verticalLayout.addWidget(self.Class_8)
        self.Class_9 = QtWidgets.QPushButton(Classes)
        self.Class_9.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Class_9.setFont(font)
        self.Class_9.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Icon/QRC/Class_IX_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Class_9.setIcon(icon9)
        self.Class_9.setIconSize(QtCore.QSize(27, 27))
        self.Class_9.setObjectName("Class_9")
        self.verticalLayout.addWidget(self.Class_9)
        self.Class_10 = QtWidgets.QPushButton(Classes)
        self.Class_10.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Class_10.setFont(font)
        self.Class_10.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Icon/QRC/Class_X_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Class_10.setIcon(icon10)
        self.Class_10.setIconSize(QtCore.QSize(27, 27))
        self.Class_10.setObjectName("Class_10")
        self.verticalLayout.addWidget(self.Class_10)
        self.Class_11 = QtWidgets.QPushButton(Classes)
        self.Class_11.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Class_11.setFont(font)
        self.Class_11.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Icon/QRC/Class_XI_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Class_11.setIcon(icon11)
        self.Class_11.setIconSize(QtCore.QSize(27, 27))
        self.Class_11.setObjectName("Class_11")
        self.verticalLayout.addWidget(self.Class_11)
        self.Class_12 = QtWidgets.QPushButton(Classes)
        self.Class_12.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Class_12.setFont(font)
        self.Class_12.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/Icon/QRC/Class_XII_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Class_12.setIcon(icon12)
        self.Class_12.setIconSize(QtCore.QSize(27, 27))
        self.Class_12.setObjectName("Class_12")
        self.verticalLayout.addWidget(self.Class_12)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 3, -1, -1)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(Classes)
        self.backButton.setMinimumSize(QtCore.QSize(0, 44))
        self.backButton.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Icon/QRC/leftWhite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon13)
        self.backButton.setIconSize(QtCore.QSize(26, 25))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(lambda: self.back_and_home_button('Back'))
        self.backButton.clicked.connect(Classes.close)
        self.horizontalLayout.addWidget(self.backButton)
        self.homeButton = QtWidgets.QPushButton(Classes)
        self.homeButton.setMinimumSize(QtCore.QSize(0, 44))
        self.homeButton.setTabletTracking(False)
        self.homeButton.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"color:white;\n"
"border-width: 2px;\n"
"font:bold 25px;\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 2px solid blue;\n"
"border-style: groove;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"border-color: white;\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"border-style:solid;\n"
"border-width: 2px;\n"
"border-color: rgb(0, 170, 0);\n"
"}\n"
"")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/Icon/QRC/homeIcon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeButton.setIcon(icon14)
        self.homeButton.setIconSize(QtCore.QSize(26, 26))
        self.homeButton.setObjectName("homeButton")
        self.homeButton.clicked.connect(lambda: self.back_and_home_button('Home'))
        self.homeButton.clicked.connect(Classes.close)
        self.horizontalLayout.addWidget(self.homeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.classTimeTable = QtWebEngineWidgets.QWebEngineView(Classes)
        self.classTimeTable.setMinimumSize(QtCore.QSize(1200, 0))
        self.classTimeTable.setUrl(QtCore.QUrl("about:blank"))
        self.classTimeTable.setObjectName("classTimeTable")
        self.classTimeTable.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.classTimeTable.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)

        self.gridLayout.addWidget(self.classTimeTable, 1, 0, 1, 1)
        self.classwiseTT = QtWidgets.QLabel(Classes)
        self.classwiseTT.setMinimumSize(QtCore.QSize(0, 69))
        self.classwiseTT.setMaximumSize(QtCore.QSize(16777215, 129))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.classwiseTT.setFont(font)
        self.classwiseTT.setStyleSheet("QLabel\n"
"{\n"
"background: transparent;\n"
"}")
        self.classwiseTT.setScaledContents(True)
        self.classwiseTT.setAlignment(QtCore.Qt.AlignCenter)
        self.classwiseTT.setObjectName("classwiseTT")
        self.gridLayout.addWidget(self.classwiseTT, 0, 0, 1, 2)

        self.retranslateUi(Classes)
        QtCore.QMetaObject.connectSlotsByName(Classes)

    def retranslateUi(self, Classes):
        _translate = QtCore.QCoreApplication.translate
        Classes.setWindowTitle(_translate("Classes", "Dialog"))
        self.KinderGarden.setText(_translate("Classes", " Kindergarten"))
        self.Class_1.setText(_translate("Classes", " Class I"))
        self.Class_2.setText(_translate("Classes", " Class II"))
        self.Class_3.setText(_translate("Classes", " Class III"))
        self.Class_4.setText(_translate("Classes", " Class IV"))
        self.Class_5.setText(_translate("Classes", " Class V"))
        self.Class_6.setText(_translate("Classes", " Class VI"))
        self.Class_7.setText(_translate("Classes", " Class VII"))
        self.Class_8.setText(_translate("Classes", " Class VIII"))
        self.Class_9.setText(_translate("Classes", " Class IX"))
        self.Class_10.setText(_translate("Classes", " Class X"))
        self.Class_11.setText(_translate("Classes", " Class XI"))
        self.Class_12.setText(_translate("Classes", " Class XII"))
        self.backButton.setText(_translate("Classes", " Back"))
        self.homeButton.setText(_translate("Classes", " Home"))
        self.classwiseTT.setText(_translate("Classes", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff;\">Classwise Time Table</span></p></body></html>"))


    def load_classwiseTT(self,button):
        """
        This function is used to load the class-wise timetable pdf file in the QWebEngineView
        :param button: The button clicked by the user
        :return: None
        """
        if button == 'Class_1':
            file_path = '/PDF/TimeTable/Class_1_Timetable_all_div.pdf'
            self.classTimeTable.setUrl(QtCore.QUrl.fromLocalFile(file_path))
        elif button == 'Class_2':
            file_path = '/PDF/TimeTable/Class_2_Timetable_all_div.pdf'
            self.classTimeTable.setUrl(QtCore.QUrl.fromLocalFile(file_path))
        elif button == 'Class_3':
                pass


    def back_and_home_button(self,button):
        """
        This function is used to navigate to the previous window or the home window
        :param button: The button clicked by the user
        :return: None
        """
        if button == 'Back':
            from Academics_Win import Ui_Academics_Win
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Academics_Win()
            self.ui.setupUi(self.window)
            self.window.show()
        elif button == 'Home':
            from School_Reception import Ui_MainWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Classes = QtWidgets.QDialog()
    ui = Ui_Classes()
    ui.setupUi(Classes)
    Classes.show()
    sys.exit(app.exec_())