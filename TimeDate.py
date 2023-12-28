#!/usr/bin/python

from PyQt5.QtCore import QDate, QTime, Qt

now = QDate.currentDate()
print(now.toString(Qt.DefaultLocaleLongDate))
time = QTime.currentTime()
print(time.toString(Qt.DefaultLocaleLongDate))