# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admissions_Win.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
import Admissions



class Ui_Admissions_Win(object):
    def setupUi(self, Admissions_Win):
        Admissions_Win.setObjectName("Admissions_Win")
        Admissions_Win.resize(1600, 820)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Admissions_Win.sizePolicy().hasHeightForWidth())
        Admissions_Win.setSizePolicy(sizePolicy)
        Admissions_Win.setMinimumSize(QtCore.QSize(1600, 820))
        Admissions_Win.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Admissions_Win.setStyleSheet("background-image: url(:/Background/magicpattern-gradient-1690353787077.jpeg);")
        self.gridLayout = QtWidgets.QGridLayout(Admissions_Win)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(24)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.AdmissionsForm = QtWebEngineWidgets.QWebEngineView(Admissions_Win)
        self.AdmissionsForm.setMinimumSize(QtCore.QSize(0, 0))
        self.AdmissionsForm.setMaximumSize(QtCore.QSize(1600, 800))
        self.AdmissionsForm.setMouseTracking(False)
        self.AdmissionsForm.setTabletTracking(False)
        self.AdmissionsForm.setUrl(QtCore.QUrl("https://surveyheart.com/form/5fd84e07bc3e84028078a8a6"))
        self.AdmissionsForm.setZoomFactor(1.0)
        self.AdmissionsForm.setObjectName("AdmissionsForm")
        self.gridLayout.addWidget(self.AdmissionsForm, 1, 0, 1, 2)
        self.HomeButton = QtWidgets.QPushButton(Admissions_Win)
        self.HomeButton.setMinimumSize(QtCore.QSize(0, 65))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.HomeButton.setFont(font)
        self.HomeButton.setStyleSheet("QPushButton{\n"
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
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/homeIcon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeButton.setIcon(icon)
        self.HomeButton.setIconSize(QtCore.QSize(35, 35))
        self.HomeButton.setObjectName("HomeButton")
        self.HomeButton.clicked.connect(lambda: self.userButtonresponse('Home Button'))
        self.HomeButton.clicked.connect(Admissions_Win.close)
        self.gridLayout.addWidget(self.HomeButton, 2, 1, 1, 1)
        self.BackButton = QtWidgets.QPushButton(Admissions_Win)
        self.BackButton.setMinimumSize(QtCore.QSize(0, 65))
        self.BackButton.setStyleSheet("QPushButton{\n"
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
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icon/leftWhite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon1)
        self.BackButton.setIconSize(QtCore.QSize(30, 30))
        self.BackButton.setObjectName("BackButton")
        self.BackButton.clicked.connect(lambda: self.userButtonresponse('Back Button'))
        self.BackButton.clicked.connect(Admissions_Win.close)
        self.gridLayout.addWidget(self.BackButton, 2, 0, 1, 1)

        self.retranslateUi(Admissions_Win)
        QtCore.QMetaObject.connectSlotsByName(Admissions_Win)

    def retranslateUi(self, Admissions_Win):
        _translate = QtCore.QCoreApplication.translate
        Admissions_Win.setWindowTitle(_translate("Admissions_Win", "Dialog"))
        self.HomeButton.setText(_translate("Admissions_Win", " Home"))
        self.BackButton.setText(_translate("Admissions_Win", "Back"))

    def userButtonresponse(self,button):
        """

        :param button:
        :return:
        """
        if button == 'Back Button':
            from Academics_Win import Ui_Academics_Win
            self.window = QtWidgets.QDialog()
            self.ui = Ui_Academics_Win()
            self.ui.setupUi(self.window)
            self.window.show()
            print('Admission_Win: Back button pressed')
        elif button == 'Home Button':
            from School_Reception import Ui_MainWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            print('Admission_Win: Home button pressed')
        else:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admissions_Win = QtWidgets.QDialog()
    ui = Ui_Admissions_Win()
    ui.setupUi(Admissions_Win)
    Admissions_Win.show()
    sys.exit(app.exec_())