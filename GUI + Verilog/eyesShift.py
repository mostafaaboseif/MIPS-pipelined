import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QDial,  QGridLayout
import math

xmove=250
ymove=450
xshift1=50
yshift1=50
xshift2=-100
yshift2=-100
X1=xmove-xshift1
Y1=ymove-yshift1
X2=xmove-xshift2
Y2=ymove-yshift2

class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('Mouse Tracker')
        self.label = QLabel(self)
        self.label.resize(200, 40)
        self.label.move(100, 40)
        self.setMouseTracking(True)

        self.laabel = QLabel(self)
        self.laabel.resize(200, 40)
        self.laabel.move(200, 300)

        self.laabel1 = QLabel(self)
        self.laabel1.resize(200, 40)
        self.laabel1.move(300, 100)

        self.dial1 = QDial(self)
        self.dial1.move(X1,Y1)
        self.dial1.resize(100,100)
        self.dial1.setWrapping(True)
        self.dial1.setMinimum(0)
        self.dial1.setMaximum(360)

        self.dial2 = QDial(self)
        self.dial2.move(X2,Y2)
        self.dial2.resize(100,100)
        self.dial2.setWrapping(True)
        self.dial2.setMinimum(0)
        self.dial2.setMaximum(360)

        self.show()

    def mouseMoveEvent(self, event):
        x=event.x()
        y=event.y()
        if x<(X1+xshift1) and y<(Y1+yshift1) :q=1
        elif x>(X1+xshift1) and y<(Y1+yshift1) :q=2
        elif x>(X1+xshift1) and y>(Y1+yshift1) :q=3
        elif x<(X1+xshift1) and y>(Y1+yshift1) :q=4
        self.label.setText('Mouse coords: ( %d : %d )' % (x,y))
        if y != (Y1+yshift1) and x != (X1+xshift1):
            a = math.degrees(math.atan(((Y1+yshift1)-y)/((X1+xshift1) - x)))
            if q == 1: a=a
            elif q == 2: a=180+a
            elif q == 3: a=180+a
            elif q == 4: a=a
        else :
            if x<(X1+xshift1) and y==(Y1+yshift1):a=0
            elif x==(X1+xshift1) and y<(Y1+yshift1):a=90
            elif x>(X1+xshift1) and y==(Y1+yshift1):a=180
            elif x==(X1+xshift1) and y>(Y1+yshift1):a=270

        x=event.x()
        y=event.x()
        q2=0
        b=0
        if x<(X2+xshift2) and y<(Y2+yshift2) :q2=1
        elif x>(X2+xshift2) and y<(Y2+yshift2) :q2=2
        elif x>(X2+xshift2) and y>(Y2+yshift2) :q2=3
        elif x<(X2+xshift2) and y>(Y2+yshift2) :q2=4
        self.label.setText('Mouse coords: ( %d : %d )' % (x,y))
        if (y-150) != (Y2+yshift2) and (x-150) != (X2+xshift2):
            b = math.degrees(math.atan(((Y2+yshift2)-(y-150))/((X2+xshift2) - (x-150))))
            if q2 == 1: b=b
            elif q2 == 2: b=180+b
            elif q2 == 3: b=180+b
            elif q2 == 4: b=b
        else :
            if x<(X2+xshift2) and y==(Y2+yshift2):b=0
            elif x==(X2+xshift2) and y<(Y2+yshift2):b=90
            elif x>(X2+xshift2) and y==(Y2+yshift2):b=180
            elif x==(X2+xshift2) and y>(Y2+yshift2):b=270

        self.dial1.setValue(int(a)+90)
        self.dial2.setValue(int(b)+90)
        self.laabel1.setText(str(a))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MouseTracker()
    sys.exit(app.exec_())
