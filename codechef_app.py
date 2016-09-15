__author__ = 'shubham'
import sys
import urllib.request
from bs4 import BeautifulSoup
from PyQt4.QtGui import *
import os


class Widget(QWidget):
    def __init__(self, parent=None):
        self.p=""
        self.uname=""
        QWidget.__init__(self, parent)
        self.setGeometry(350,120,500,550)

        self.setWindowIcon(QIcon('favicon.ico'))
        self.setWindowTitle("CPC(codechef progress calculator)")
        frame = QFormLayout()
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap('logo.png'))
        frame.addRow(self.logo)
        self.edit = QLineEdit()
        self.handle  = QLabel("Codechef User Name")
        self.handle.setStyleSheet('margin-top:50px; '
                         'color: #66CCFF; '
                         'height:25px;'
                         'font-size: 15px; '
                         'font-family:Arial,Helvetica, sans-serif;'
                         'font-weight:bold'
                         )
        self.edit.setStyleSheet('margin-top:50px;'
                       'color: #6495ed;'
                       'height:30px ;'
                       'margin-left: 5px ;'
                       'font-size: 15px; '
                       'font-weight: bold;'
                       'font-family:Arial, Helvetica, sans-serif;'
                       )
        self.btn = QPushButton('Search')
        self.btn.setStyleSheet(
        'height:38px ;'
        'background:#4682B4;'
        'width:50px;'
        'margin-left: 243px ;'
        'font-size: 15px; '
        'color:#ffffff;'
        'font-family:Arial, Helvetica, sans-serif;'
        )
        self.prt = QPushButton('Print')
        self.prt.setStyleSheet(
        'background:#4682B4;'
        'height:30px ;'
        'width:50px;'
        'font-size: 15px; '
        'color:#ffffff;'
        'font-family:Arial, Helvetica, sans-serif;'
        )
        frame.addRow(self.handle,self.edit)
        frame.addRow(self.prt,self.btn)
        self.btn.clicked.connect(self.search)
        self.prt.clicked.connect(self.prnt)

        self.text = QTextEdit("Click search")
        self.text.setReadOnly(True)
        self.text.setLineWrapMode(QTextEdit.NoWrap)
        self.text.setStyleSheet(
            'background-color:#FFEFD5;'
            'font-size:13px;'
            'font-family:Arial, Helvetica, sans-serif;'
        )
        self.text.setMinimumHeight(350)
        frame.addRow(self.text)
        self.setLayout(frame)

    def search(self):
        self.uname = self.edit.text()
        try:
            url = urllib.request.urlopen("http://codechef.com/users/"+self.uname)
            soup = BeautifulSoup(url.read(), "html.parser")
            table = soup.find(id="problem_stats")
            rows = table.find_all('td')
            d = []
            for i in rows:
                s = str(i)
                s = s.replace("<td>","").replace("</td>","")
                d += [s]
            self.p = ""
            for i in range(9):
                self.p +=d[i]+"\n"+d[9+i]+"\n"
            self.text.setText(self.p)
        except:
            self.text.setText("user not exists")

    def prnt(self):
        try:
            path = "/CPC/"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            self.uname = self.edit.text()
            if(self.uname == ""):
                self.text.setText("Error!!!")
            else:
                file = open(path+self.uname+".txt","w+")
                file.write(self.p)
                file.close()
                self.text.setText("Printed Succsessfully")
        except:
            self.text.setText("Error!!!")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())