# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutUs_Win.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets


class Ui_aboutUs(object):
    def setupUi(self, aboutUs):
        aboutUs.setObjectName("aboutUs")
        aboutUs.resize(768, 625)
        aboutUs.setWindowIcon(QtGui.QIcon('Icons/aboutUs_Win_icon.png')) # Attribution: <a href="https://www.flaticon.com/free-icons/people" title="people icons">People icons created by Freepik - Flaticon</a>
        self.label = QtWidgets.QLabel(aboutUs)
        self.label.setGeometry(QtCore.QRect(320, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(aboutUs)
        self.layoutWidget.setGeometry(QtCore.QRect(590, 50, 171, 561))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.About = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.About.setFont(font)
        self.About.setObjectName("About")
        self.About.clicked.connect(lambda: self.userResponse('About'))
        self.verticalLayout.addWidget(self.About)
        self.History = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.History.setFont(font)
        self.History.setObjectName("History")
        self.History.clicked.connect(lambda: self.userResponse('History'))
        self.verticalLayout.addWidget(self.History)
        self.VisionMission = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.VisionMission.setFont(font)
        self.VisionMission.setObjectName("VisionMission")
        self.VisionMission.clicked.connect(lambda: self.userResponse('Vision And Mission'))
        self.verticalLayout.addWidget(self.VisionMission)
        self.Principal_msg = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.Principal_msg.setFont(font)
        self.Principal_msg.setObjectName("Principal_msg")
        self.Principal_msg.clicked.connect(lambda: self.userResponse('Principal\'s message'))
        self.verticalLayout.addWidget(self.Principal_msg)
        self.President_msg = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(9)
        self.President_msg.setFont(font)
        self.President_msg.setObjectName("President_msg")
        self.President_msg.clicked.connect(lambda: self.userResponse('President\'s message'))
        self.verticalLayout.addWidget(self.President_msg)
        self.schoolInfo = QtWebEngineWidgets.QWebEngineView(aboutUs)
        self.schoolInfo.setGeometry(QtCore.QRect(10, 50, 571, 561))
        self.schoolInfo.setUrl(QtCore.QUrl("about:blank"))
        self.schoolInfo.setObjectName("schoolInfo")

        self.retranslateUi(aboutUs)
        QtCore.QMetaObject.connectSlotsByName(aboutUs)

    def retranslateUi(self, aboutUs):
        _translate = QtCore.QCoreApplication.translate
        aboutUs.setWindowTitle(_translate("aboutUs", "About Us"))
        self.label.setText(_translate("aboutUs", "About Us"))
        self.About.setText(_translate("aboutUs", "About"))
        self.History.setText(_translate("aboutUs", "History"))
        self.VisionMission.setText(_translate("aboutUs", "Vision And Mission"))
        self.Principal_msg.setText(_translate("aboutUs", "Principal\'s message"))
        self.President_msg.setText(_translate("aboutUs", "President\'s message"))

    def userResponse(self, button):
        if button == 'About':
            print('About button pressed')
            self.schoolInfo.setHtml("about:blank")
        elif button == 'History':
            print('History button pressed')
            self.schoolInfo.setHtml("about:blank")
        elif button == 'Vision And Mission':
            print('Vision And Mission button pressed')
            self.schoolInfo.setHtml("about:blank")
        elif button == 'Principal\'s message':
            print('Principal\'s pressed')
            self.schoolInfo.setHtml("about:blank")
        elif button == 'President\'s message':
            print('President\'s button pressed')
            self.schoolInfo.setHtml("about:blank")
        else:
            pass




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutUs = QtWidgets.QDialog()
    ui = Ui_aboutUs()
    ui.setupUi(aboutUs)
    aboutUs.show()
    sys.exit(app.exec_())
