import sys
from PyQt4 import QtGui, QtCore

fname=sys.argv[1]

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap(fname)

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(350, 160)
        self.setWindowTitle(fname)
        self.show()        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
