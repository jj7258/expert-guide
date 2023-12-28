
"""
    Similar process for making an VerticalSlider

"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider, QLabel


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(532, 298)
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 210, 491, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)  # Tick Marks (Above,Below,Both)
        self.horizontalSlider.setTickInterval(2) # Set Tick Interval
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.qty = QtWidgets.QLabel(Dialog)
        self.qty.setGeometry(QtCore.QRect(130, 70, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Sans Serif Collection")
        font.setPointSize(26)
        self.qty.setFont(font)
        self.qty.setAlignment(QtCore.Qt.AlignCenter)
        self.qty.setObjectName("qty")

        # Set Slider Properties
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        #self.horizontalSlider.setValue(10)

        # Calls the slider function
        self.moveSlider()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.qty.setText(_translate("Dialog", "0"))

    def moveSlider(self):
        self.horizontalSlider.valueChanged.connect(self.slide_it)

    def slide_it(self, value):
        self.qty.setText(str(value))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
