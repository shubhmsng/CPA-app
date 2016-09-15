import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setStyleSheet('background-color:#252525')
    frame = QFormLayout()
    img = QLabel()

    img.setPixmap(QPixmap('img.png'))
    img.setStyleSheet('margin-left:10px')
    l = QLabel("Adobe AIR")
    l.setStyleSheet('margin-left: 5px ;font-size: 18px; color: #ffffff; font-family:Tahoma')
    frame.addRow(img, l)

    l1 = QLabel("Update Adobe AIR")
    l1.setStyleSheet('margin-left: 80px ;font-size: 12px; color: #ffffff; font-family:Tahoma;')
    frame.addRow(l1)

    l2 = QLabel("This installer will update Above AIR. \n\nClick update to install this update now.\n\nInstalled: 18.0.0.180\n\n Update: 19.0.0.190\n\n")
    l2.setStyleSheet('margin-left: 80px ;font-size: 10px; color: #ffffff; font-family:"Lucida Console", Monaco, monospace;')
    frame.addRow(l2)

    update = QPushButton('Update')
    cancel = QPushButton('Cancel')
    update.setStyleSheet('background-color: #454545;height:30px ;margin-left: 80px ;font-size: 15px; color: #ffffff; font-family:Arial, Helvetica, sans-serif')
    cancel.setStyleSheet('background-color: #454545;height:30px ;margin-left: 80px ;font-size: 15px; color: #ffffff; font-family:Arial, Helvetica, sans-serif')
    update.setFixedWidth(160)
    cancel.setFixedWidth(160)
    frame.addRow(update, cancel)
    win.setLayout(frame)
    win.setMaximumSize(480, 260)
    win.setMinimumSize(480, 260)
    win.move(250, 100)
    win.setWindowTitle("Adobe AIR Setup")

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
