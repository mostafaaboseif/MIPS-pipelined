import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QDial,  QGridLayout
import math

xmove=100
ymove=650
class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('Mouse Tracker')
        self.label = QLabel(self)
        self.label.resize(200, 40)
        self.label.move(100, 40)

        self.laabel = QLabel(self)
        self.laabel.resize(200, 40)
        self.laabel.move(200, 300)

        self.laabel1 = QLabel(self)
        self.laabel1.resize(200, 40)
        self.laabel1.move(300, 100)

        self.dial = QDial(self)
        self.dial.move(xmove-50,ymove-50)
        self.dial.setValue(30)
        self.dial.resize(100,100)
        self.dial.setWrapping(True)
        self.dial.setMinimum(0)
        self.dial.setMaximum(360)
        self.show()

    def mouseMoveEvent(self, event):
        x=event.x()
        y=event.y()
        if x<xmove and y<ymove :q=1
        elif x>xmove and y<ymove :q=2
        elif x>xmove and y>ymove :q=3
        elif x<xmove and y>ymove :q=4
        self.label.setText('Mouse coords: ( %d : %d )' % (x,y))
        if y != ymove and x != xmove:
            a = math.degrees(math.atan((ymove-event.y())/(xmove - event.x())))
            if q == 1: a=a
            elif q == 2: a=180+a
            elif q == 3: a=180+a
            elif q == 4: a=a
        else :
            if x<xmove and y==ymove:a=0
            elif x==xmove and y<ymove:a=90
            elif x>xmove and y==ymove:a=180
            elif x==xmove and y>ymove:a=270

        self.dial.setValue(int(a)+90)
        self.laabel1.setText(str(a))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MouseTracker()
    sys.exit(app.exec_())
