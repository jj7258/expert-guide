from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app=QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(200,200,300,300) #(xpos,ypos,width,height)
    win.setWindowTitle("Hello World")
    
    label=QtWidgets.QLabel(win)
    label.setText("My First Text !!!")
    label.move(50,50) #(xpos,ypos)
    
    win.show()
    sys.exit(app.exec_())
    
window()
    
    

