# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admissions_Win.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admissions_Win(object):
    def setupUi(self, Admissions_Win):
        Admissions_Win.setObjectName("Admissions_Win")
        Admissions_Win.resize(799, 576)
        Admissions_Win.setWindowIcon(QtGui.QIcon('Icons/admissions_Win_icon.png')) # Attribution: <a href="https://www.flaticon.com/free-icons/write" title="write icons">Write icons created by Freepik - Flaticon</a>

        self.GFrom_Admissions = QtWebEngineWidgets.QWebEngineView(Admissions_Win)
        self.GFrom_Admissions.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.GFrom_Admissions.setUrl(QtCore.QUrl("https://www.google.com/"))
        self.GFrom_Admissions.setZoomFactor(1.0)
        self.GFrom_Admissions.setObjectName("GFrom_Admissions")

        self.retranslateUi(Admissions_Win)
        QtCore.QMetaObject.connectSlotsByName(Admissions_Win)

    def retranslateUi(self, Admissions_Win):
        _translate = QtCore.QCoreApplication.translate
        Admissions_Win.setWindowTitle(_translate("Admissions_Win", "Admissions Data Entry"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admissions_Win = QtWidgets.QDialog()
    ui = Ui_Admissions_Win()
    ui.setupUi(Admissions_Win)
    Admissions_Win.show()
    sys.exit(app.exec_())