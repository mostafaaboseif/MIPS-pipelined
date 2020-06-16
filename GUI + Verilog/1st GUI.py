import os
import subprocess
import sys
import time
# import PIL
import math

# from PIL import Image
from subprocess import*
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from random import randint

filename_pc = "pc.txt"
filename_dmem = "dataMem.txt"
filename_rg = "regFile.txt"
check_pc = os.path.join(os.getcwd(),"check_pc")
check_regf = os.path.join(os.getcwd(),"check_regf")
check_dmem = os.path.join(os.getcwd(),"check_dmem")
flags = []
inst = []

pc = []
regfile = []
dmem = []

pc_result = []
regfile_result = []
dmem_result = []

#Appending the correct pc in the pc_result list to be checked with the output one
# with open("check_pc.txt") as g:
#     pc_result.append(g.readlines())
for res_pc in os.listdir(check_pc):
     if res_pc.endswith(".txt"):
         with open(os.path.join(check_pc,res_pc)) as oo:
             pc_result.append(oo.read())
#Appending the correct regfile contents in the pc_result list to be checked with the output one
for res_regf in os.listdir(r'C:\Modeltech_pe_edu_10.4a\examples\check_regf'):
     if res_regf.endswith(".txt"):
         with open(os.path.join(r'C:\Modeltech_pe_edu_10.4a\examples\check_regf',res_regf)) as f:
             regfile_result.append(f.read())
#Appending the correct dataMem contents in the dmem_result list to be checked with the output one
for res_dmem in os.listdir(r'C:\Modeltech_pe_edu_10.4a\examples\check_dmem'):
     if res_dmem.endswith(".txt"):
         with open(os.path.join(r'C:\Modeltech_pe_edu_10.4a\examples\check_dmem',res_dmem)) as d:
             dmem_result.append(d.read())
# class TextEdit (QTextEdit):
#     def init(self,parent = None):
#         QTextEdit.init(self)
#         self.setText("Type your instructions here...")
#     def focucInEvent(self,event):
#         self.clear()
#         QTextEdit.focusInEvent(self,event)

class Start_Window(QMainWindow):

    def __init__(asmbStart):
        super(Start_Window,asmbStart).__init__()
        asmbStart.left = 20 #position from left of screen
        asmbStart.top = 20 #position from top of screen
        asmbStart.title = 'Black Pearl Assembler'
        asmbStart.width = 1270 #width of window
        asmbStart.height = 740 #height of window
        asmbStart.InitWindow()

    def InitWindow(asmbStart):
        asmbStart.setWindowTitle(asmbStart.title)
        asmbStart.setGeometry(asmbStart.top, asmbStart.left, asmbStart.width, asmbStart.height)
        asmbStart.setWindowIcon(QIcon('blackpearl'))
        asmbStart.setIconSize(QSize(10,10))
        asmbStart.setAutoFillBackground(True)
        asmbStart.setFocus()



        p = QLabel('',asmbStart)
        p.setPixmap(QPixmap('semichip.jpg'))
        p.setScaledContents(True)
        asmbStart.setCentralWidget(p)

        lbllogo = QLabel(" ",asmbStart)
        pixmap = QPixmap('faculty logo.png')
        lbllogo.setPixmap(pixmap)
        lbllogo.adjustSize()
        lbllogo.move(20,50)



        #Creating a label
        lbl1 = QLabel("Choose how instructions to be executed", asmbStart)
        font_lbl = QFont()
        font_lbl.setPixelSize(35)
        font_lbl.setFamily("Arial black")
        lbl1.setAutoFillBackground(True)
        lbl1.setAlignment(Qt.AlignCenter)

        w = lbl1.palette()
        w.setColor(lbl1.foregroundRole(), Qt.white)
        w.setColor(lbl1.backgroundRole(),Qt.transparent)
        lbl1.setPalette(w)
        lbl1.setFont(font_lbl)
        lbl1.adjustSize()
        lbl1.move(330,120)

        #Creating a textbox
        asmbStart.textbox = QTextEdit(asmbStart)
        # asmbStart.textbox.setText("Type your instructions here...")
        asmbStart.textbox.move(390, 280)
        asmbStart.textbox.resize(550,180)
        font_tb = QFont()
        font_tb.setPixelSize(20)
        asmbStart.textbox.setFont(font_tb)

        #creating button 1
        asmbStart.button = QPushButton('Assemble now', asmbStart)
        font_btn = QFont()
        font_btn.setPixelSize(20)
        asmbStart.button.setFont(font_btn)
        asmbStart.button.resize(200,50)
        asmbStart.button.clicked.connect(asmbStart.onClick1_assmbNow)
        asmbStart.button.setStyleSheet("background-color: lightblue;border-radius: 15px;")
        asmbStart.button.move(950,300)

        #creating button 2
        asmbStart.button = QPushButton('Auto assembly', asmbStart)
        font_btn = QFont()
        font_btn.setPixelSize(20)
        fp = QPalette()
        fp.setColor(asmbStart.button.foregroundRole(), Qt.black)
        asmbStart.button.setFont(font_btn)
        asmbStart.button.setPalette(fp)
        asmbStart.button.resize(200,50)
        asmbStart.button.move(580,530)
        asmbStart.button.setStyleSheet("background-color: darkCyan;border-radius: 15px;")
        asmbStart.button.clicked.connect(asmbStart.onClick2_automated)




        #Creating a button 3 for educational pipeline software
        asmbStart.button = QPushButton('Educational Pipelined MIPS', asmbStart)
        font_btn = QFont()
        font_btn.setPixelSize(20)
        asmbStart.button.setFont(font_btn)
        asmbStart.button.resize(310,50)
        asmbStart.button.clicked.connect(asmbStart.onClick3_edu)
        asmbStart.button.setStyleSheet("background-color: green;border-radius: 15px;")
        asmbStart.button.move(20,300)


        lbl2 = QLabel("Or", asmbStart)
        lbl2.setFont(font_lbl)
        lbl2.setPalette(w)
        lbl2.move(660,480)
        lbl1.adjustSize()
        asmbStart.show()



    @pyqtSlot()
    def onClick1_assmbNow(asmbStart):
        global started
        textValue = asmbStart.textbox.toPlainText()
        asmbStart.textbox.clear()
        asmbStart.statusBar().showMessage("Assembly Started")
        with open("assemblyCode.txt",'w') as f: #or 'a' if we want to append on the previous content of the file
            f.write(textValue)


        dir = os.getcwd()
        p = os.system('"assembler.exe"') #os.path.join(dir,'assembler.exe')

        os.system(r'cmd /c "cd C:\Modeltech_pe_edu_10.4a\examples & vsim -c -do autoTest.do work.atb_all" ')
        # os.system('cmd /d '+ "E:\Vproject\teamPrj" and'atb_all_isim_beh.exe -tclbatch isim.tcl')

        with open(filename_pc) as p, open(filename_dmem) as d, open(filename_rg) as f:
            if len(pc)==0:
                pc.append(p.read())
                regfile.append(f.read()[176:]+"\r\n")
                dmem.append(d.read()[181:]+"\r\n")
            else:
                pc.clear()
                regfile.clear()
                dmem.clear()
                pc.append(p.read())
                regfile.append(f.read()[176:]+"\r\n")
                dmem.append(d.read()[181:]+"\r\n")


        asmbStart.cams = Start_Dialog()
        asmbStart.cams.show()
        asmbStart.cams.data_changed()
        #asmbStart.close()

    def onClick2_automated(asmbStart):
        QMessageBox.information(asmbStart," ",'Instructions are carried on ',QMessageBox.Ok,QMessageBox.Ok)
        asmbStart.statusBar().showMessage("Assembly Started")
        dirTC = os.path.join(os.getcwd(),"dirTC")


        instruction = []
        for testCase in os.listdir(dirTC):
             if testCase.endswith(".txt"):
                 with open(os.path.join(dirTC,testCase)) as f:
                     instruction.append(f.read())
                     print(len(instruction))
                     asmb = open("assemblyCode.txt","w")
                     asmb.write(instruction[len(instruction)-1])
                     asmb.close()
                     p = os.system('"assembler.exe"')
                     os.system('cmd /c "cd C:\Modeltech_pe_edu_10.4a\examples& vsim -c -do autoTest.do work.atb_all"')


                 with open(filename_pc) as pp, open(filename_dmem) as dd, open(filename_rg) as ff:
                         pc.append(pp.read()) #+"\r\n"
                         regfile.append(ff.read()[176:])
                         dmem.append(dd.read()[181:]) #+"\r\n"

        asmbStart.cams = Start_Dialog()
        asmbStart.cams.show()
        asmbStart.cams.check_results()

    def onClick3_edu(asmbStart):
        # os.system('"C:\Modeltech_pe_edu_10.4a\examples\assembler.exe"')
        #read the file containing the instructions letters
        fh = open('animation.txt')
        for line in fh:
            inst.append(line)
        fh.close()
        asmbStart.edu = Start_Edu()
        #asmbStart.edu.show()
        #asmbStart.close()

xmove=100
ymove=650

class Start_Edu (QMainWindow):
    def __init__(self):
        super(Start_Edu, self).__init__()
        self.left = 20 #position from left of screen
        self.top = 20 #position from top of screen
        self.title = 'Educational Pipelined MIPS'
        self.width = 1270 #width of window
        self.height = 750 #height of window
        self.initUI()

    def initUI(self):
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Background, QtCore.Qt.white)
        self.setPalette(palette)
        self.tboard = Edu(self)
        self.setCentralWidget(self.tboard)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle('Educational Pipelined MIPS')
        self.setWindowIcon(QIcon('blackpearl'))
        self.setAutoFillBackground(False)

        self.show()

class Edu(QFrame):
    Speed = 1000
    counter = 0
    i = 0
    def __init__(self,parent):
        super(Edu, self).__init__(parent)
        self.setMouseTracking(True)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setStyleSheet('background-image: url( MIPS_Architecture_(Pipelined).svg.png); background-repeat: no-repeat ') #background-position: center
        self.setAutoFillBackground(False)
        self.timer_draw = QTimer(self)
        self.timer_draw.timeout.connect(self.drawR)
        self.timer_draw.start(self.Speed)

        self.rec_color = QtCore.Qt.black
        self.draw_r = False

        fedu = QFont()
        fedu.setPixelSize(15)
        fedu.setBold(True)
        pedu = QPalette()
        pedu.setColor(self.backgroundRole(),Qt.blue)
        button = QPushButton('Next Instruction',self)
        button.setFont(fedu)
        button.resize(125,20)
        button.move(1180,300)
        button.clicked.connect(self.increment)

        self.label = QLabel(inst[self.i]+'instruction',self)
        self.label.move(20,50)
        self.label.setFont(fedu)
        self.setPalette(pedu)
        self.label.adjustSize()

        self.drawR()

        self.dial = QDial(self)
        self.dial.move(xmove-50,ymove-50)
        self.dial.setValue(30)
        self.dial.resize(100,100)
        self.dial.setWrapping(True)
        self.dial.setMinimum(0)
        self.dial.setMaximum(360)

    def mouseMoveEvent(self, event):
        x=event.x()
        y=event.y()
        if x<xmove and y<ymove :q=1
        elif x>xmove and y<ymove :q=2
        elif x>xmove and y>ymove :q=3
        elif x<xmove and y>ymove :q=4
        # edu_pip.label.setText('Mouse coords: ( %d : %d )' % (x,y))
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



    def paintEvent(self,event):
        painter1 = QPainter()
        painter2 = QPainter()
        painter22 = QPainter()
        painter31 = QPainter()
        painter32 = QPainter()
        painter41 = QPainter()
        painter42 = QPainter()
        painter5 = QPainter()

        self.pen1 = QtGui.QPen()
        self.pen1.setWidth(3)
        #painter1.drawText()

        if self.counter<7:
            painter1.begin(self)

        if inst[self.i]=='R\n':
            if self.counter > 7 and self.counter<14:
                painter1.end()
                painter2.begin(self)
            elif self.counter > 14 and self.counter<21:
                painter2.end()
                painter32.begin(self)
            elif self.counter > 21 and self.counter<28:
                painter32.end()
                painter5.begin(self)

        elif inst[self.i]=='I\n':
            if self.counter > 7 and self.counter<14:
                painter1.end()
                painter22.begin(self)
            elif self.counter > 14 and self.counter<21:
                painter22.end()
                painter32.begin(self)
            elif self.counter > 21 and self.counter<28:
                painter32.end()
                painter5.begin(self)

        elif inst[self.i]=='LW\n':
            if self.counter > 7 and self.counter<14:
                painter1.end()
                painter22.begin(self)
            elif self.counter > 14 and self.counter<21:
                painter22.end()
                painter32.begin(self)
            elif self.counter > 21 and self.counter<28:
                painter32.end()
                painter42.begin(self)
            elif self.counter > 28 and self.counter<35:
                painter42.end()
                painter5.begin(self)


        elif inst[self.i]=='SW\n':
            if self.counter > 7 and self.counter<14:
                painter1.end()
                painter22.begin(self)
            elif self.counter > 14 and self.counter<21:
                painter22.end()
                painter32.begin(self)
            elif self.counter > 21 and self.counter<28:
                painter32.end()
                painter42.begin(self)

        elif inst[self.i]=='B\n':
            if self.counter > 7 and self.counter<14:
                painter1.end()
                painter22.begin(self)
            elif self.counter > 14 and self.counter<21:
                painter22.end()
                painter31.begin(self)
            elif self.counter > 21 and self.counter<28:
                painter31.end()
                painter41.begin(self)

        elif inst[self.i]=='JR\n':
            if self.counter > 7 and self.counter<14:
                painter1.end()
                painter22.begin(self)
            elif self.counter > 14 and self.counter<21:
                painter22.end()
                painter31.begin(self)
            elif self.counter > 21 and self.counter<28:
                painter31.end()

        elif inst[self.i]=='JAL\n' or inst[0]=='J\n':
            if self.counter > 7 and self.counter<14:
                painter1.end()
                painter41.begin(self)
            elif self.counter > 14 and self.counter<21:
                painter41.end()


        if (self.draw_r==True):
            self.pen1.setColor(QtCore.Qt.cyan)

        else:
            self.pen1.setColor(QtCore.Qt.black)

        points_addr = [
            QPoint(150,150),
            QPoint(195,170),
            QPoint(195,231),
            QPoint(150,255),
            QPoint(148,209),
            QPoint(166,200),
            QPoint(150,195)
            ]
        addr = QPolygon(points_addr)

        points_muxWB = [
            QPoint(1102,424),
            QPoint(1102,501),
            QPoint(1134,487),
            QPoint(1134,441)]
        muxWB = QPolygon(points_muxWB)

        points_mux1 = [
            QPoint(615,403),
            QPoint(646,420),
            QPoint(646,463),
            QPoint(615,478) ]
        mux1 = QPolygon(points_mux1)

        points_mux2 = [
            QPoint(615,494),
            QPoint(646,509),
            QPoint(646,554),
            QPoint(615,568) ]
        mux2 = QPolygon(points_mux2)

        points_mux3 = [
            QPoint(898,184),
            QPoint(930,202),
            QPoint(930,246),
            QPoint(900,262)]
        mux3 = QPolygon(points_mux3)

        points_alu = [
            QPoint(667,418),
            QPoint(667,464),
            QPoint(683,472),
            QPoint(683,501),
            QPoint(666,510),
            QPoint(667,554),
            QPoint(727,524),
            QPoint(727,449) ]
        alu = QPolygon(points_alu)

        #stage 1
        if painter1.isActive():
            painter1.setRenderHint(QtGui.QPainter.Antialiasing)
            painter1.setPen(self.pen1)
            painter1.drawRects(QRect(125,375 , 117, 150),QRect(37,376 , 37, 150))
            painter1.drawPolygon(addr)

        #stage 2
        if painter2.isActive():
            painter2.setRenderHint(QtGui.QPainter.Antialiasing)
            painter2.setPen(self.pen1)
            painter2.drawRect(QRect(395,232 ,90, 142))


        #stage 2 of I instruction
        if painter22.isActive():
            painter22.setRenderHint(QtGui.QPainter.Antialiasing)
            painter22.setPen(self.pen1)
            painter22.drawRect(QRect(395,232 ,90, 142))
            painter22.drawEllipse(397,455,75,112)
        #zero flag
        if painter31.isActive():
            painter31.setRenderHint(QtGui.QPainter.Antialiasing)
            painter31.setPen(self.pen1)
            painter31.drawRect(QRect(630,270,60,45))
            painter31.drawPolygon(alu)

        # muxes and alu
        if painter32.isActive():
            painter32.setRenderHint(QtGui.QPainter.Antialiasing)
            painter32.setPen(self.pen1)
            painter32.drawPolygon(mux1)
            painter32.drawPolygon(mux2)
            painter32.drawPolygon(alu)

        #upper mux
        if painter41.isActive():
            painter41.setRenderHint(QtGui.QPainter.Antialiasing)
            painter41.setPen(self.pen1)
            painter41.drawPolygon(mux3)

        #memory
        if painter42.isActive():
            painter42.setRenderHint(QtGui.QPainter.Antialiasing)
            painter42.setPen(self.pen1)
            painter42.drawRect(QRect(860,448 , 117, 150))

        #mux and reg file
        if painter5.isActive():
            painter5.setRenderHint(QtGui.QPainter.Antialiasing)
            painter5.setPen(self.pen1)
            painter5.drawPolygon(muxWB)
            painter5.drawRect(QRect(397,232 ,90, 142))


    def drawR(self):
        self.draw_r = not self.draw_r
        self.counter+=1
        self.update()
    def increment(self):
        self.counter = 0
        self.i = self.i +1
        if self.i<len(inst):
            self.label.setText(inst[self.i]+'instruction')
        # edu_pip.label.update()
        # edu_pip.layout.update()

        # pen = QtGui.QPen()
        # pen.setWidth(3)
        # pen.setColor(QColor(Qt.black))
        # painter.setPen(pen)
        #
        # brush = QBrush()
        # brush.setColor(QColor(Qt.transparent))
        # print(inst[0])
        # if(inst[0]=='R' and edu_pip.drawr==True):
        #     brush.setColor(QColor(Qt.yellow))
        # brush.setStyle(Qt.SolidPattern)
        # painter.setBrush(brush)
        # painter.drawRects(QRect(125,375 , 117, 150),QRect(397,232 ,90, 142),QRect(860,448 , 117, 150))
        #
        # painter.end()

        #print(edu_pip.rec_color)
        # self.x_apple = np.random.randint(0, math.floor(self.BoardWidth/self.SquareWidth)) * self.SquareWidth
        # self.y_apple = np.random.randint(0, math.floor(self.BoardHeight/self.SquareHeight)) * self.SquareHeight

        #edu_pip.rect = QRect(125,375 , 117, 150)




class Start_Dialog(QMainWindow):

    def __init__(assembler):
        super(Start_Dialog,assembler).__init__()
        assembler.left = 0 #position from left of screen
        assembler.top = 0 #position from top of screen
        assembler.title = 'Black Pearl Assembler'
        assembler.width = 1270 #width of window
        assembler.height = 1000 #height of window
        assembler.content_pc = ""
        assembler.content_dmem = ""
        assembler.content_rg = ""
        assembler.InitWindow()

    def InitWindow(assembler):
        assembler.setWindowTitle(assembler.title)
        assembler.setGeometry(assembler.top, assembler.left, assembler.width, assembler.height)
        assembler.setWindowIcon(QIcon('blackpearl'))
        assembler.setAutoFillBackground(True)
        p = assembler.palette()
        p.setColor(assembler.backgroundRole(), Qt.white) #OR assembler.setStyleSheet("background-color: white;")
        assembler.setPalette(p)


        assembler.layout =  QHBoxLayout(assembler)
        assembler.scrollArea = QScrollArea(assembler)
        assembler.scrollArea.resize(1360,750)
        assembler.scrollArea.setWidgetResizable(True)
        assembler.scrollAreaWidgetContents = QWidget()
        assembler.createGridLayout()


        #-------------------------------------------------------------------------------



    def createGridLayout(assembler):
        assembler.gridLayout = QGridLayout(assembler.scrollAreaWidgetContents)
        assembler.scrollArea.setWidget(assembler.scrollAreaWidgetContents)
        assembler.layout.addWidget(assembler.scrollArea)

        #-----------------------------------------------------------------------
        assembler.comboBox = QComboBox(assembler)
        assembler.comboBox.addItem("Current Case")
        assembler.comboBox.addItem("Test Case 1")
        assembler.comboBox.addItem("Test Case 2")
        assembler.comboBox.addItem("Test Case 3")
        assembler.comboBox.addItem("Test Case 4")
        assembler.comboBox.addItem("Test Case 5")
        assembler.comboBox.addItem("Test Case 6")
        assembler.comboBox.addItem("Test Case 7")
        assembler.comboBox.addItem("Test Case 8")
        assembler.comboBox.addItem("Test Case 9")
        assembler.comboBox.addItem("Test Case 10")

        assembler.comboBox.setStyle(QStyleFactory.create('Plastique'))
        assembler.comboBox.setStyleSheet("background-color: dark white")
        assembler.comboBox.activated[str].connect(assembler.select_change)

        assembler.gridLayout.setRowStretch(2, 1)
        assembler.gridLayout.setRowStretch(1, 0)
        #assembler.gridLayout.setColumnStretch()
        #-----------------------------------------------------------------------

        #Creating a dock widget
        assembler.dock = QDockWidget('Results Check',assembler)
        assembler.dock.setFixedWidth(270)
        assembler.addDockWidget(Qt.TopDockWidgetArea, assembler.dock)#
        assembler.layout_rs = QFormLayout()
        assembler.dock.setFloating(True)
        assembler.dockW = QWidget()

        #-----------------------------------------------------------------------
        #creating a label for Assembled data
        lbl = QLabel("Assembled data: ",assembler)
        lbl.move(500,50)
        font_lbl = QFont()
        flp = QPalette()
        flp.setColor(assembler.foregroundRole(),Qt.blue)
        lbl.setPalette(flp)
        font_lbl.setPixelSize(30)
        font_lbl.setFamily("Magma")
        lbl.setFont(font_lbl)
        lbl.adjustSize()
        lbl.setAlignment(Qt.AlignCenter)

        #-----------------------------------------------------------------------
        #creating a label for PC
        assembler.lbl_pc = QLabel(''+assembler.content_pc,assembler)
        font_pc = QFont()
        font_pc.setPixelSize(20)
        font_pc.setFamily('Magma')
        assembler.lbl_pc.setFont(font_pc)
        assembler.lbl_pc.adjustSize()
        #-----------------------------------------------------------------------
        #creating a label for register file contents
        assembler.lbl_rg =QLabel(''+assembler.content_rg,assembler)
        font_rg = QFont()
        font_rg.setPixelSize(18)
        font_rg.setFamily('Magma')
        assembler.lbl_rg.setFont(font_rg)
        #-----------------------------------------------------------------------
        #creating a label for dmem contents
        assembler.lbl_dmem =QLabel('')
        font_dmem = QFont()
        font_dmem.setPixelSize(18)
        font_dmem.setFamily('Magma')
        assembler.lbl_dmem.setFont(font_dmem)
        #-----------------------------------------------------------------------

        assembler.gridLayout.addWidget(assembler.comboBox,1,1)
        assembler.gridLayout.addWidget(lbl,0,1)
        assembler.gridLayout.addWidget(assembler.lbl_pc,2,0)
        assembler.gridLayout.addWidget(assembler.lbl_rg,2,1)
        assembler.gridLayout.addWidget(assembler.lbl_dmem,2,2)

    @pyqtSlot()
    def data_changed(assembler):
        if len(pc)==1:
            assembler.comboBox.setEnabled(False)
        print(regfile[len(regfile)-1])
        assembler.lbl_pc.setText('The Final PC is:\r\n'+pc[0]+"\r\n")
        assembler.lbl_rg.setText('The contents of the register file are:\r\n'+regfile[0]+"\r\n")
        assembler.lbl_dmem.setText('The contents of data memory are:\r\n'+dmem[0]+"\r\n")

    def check_results(assembler):
        r = QPixmap('right.png').scaled(20,20)
        w = QPixmap('wrong.png').scaled(20,20)

        right1 = QLabel('right',assembler)
        right2 = QLabel('t',assembler)
        right3 = QLabel('',assembler)
        right4 = QLabel('',assembler)
        right5 = QLabel('',assembler)
        right6 = QLabel('',assembler)
        right7 = QLabel('',assembler)
        right8 = QLabel('',assembler)
        right9 = QLabel('',assembler)
        right10 = QLabel('',assembler)
        for m in range(0,len(pc)):
            if((pc[m]==pc_result[m]) and (regfile[m]==regfile_result[m])):
                flags.append('True')
            else:
                flags.append('False')

        if flags[0]=='True':
            assembler.layout_rs.addRow("Case 1",right1)
            right1.setPixmap(r)
        elif flags[0]=='False':
            assembler.layout_rs.addRow("Case 1",right1)
            right1.setPixmap(w)
        if flags[1]=='True':
            assembler.layout_rs.addRow("Case 2",right2)
            right2.setPixmap(r)
        elif flags[1]=='False':
            assembler.layout_rs.addRow("Case 2",right2)
            right2.setPixmap(w)
        if flags[2]=='True':
            assembler.layout_rs.addRow("Case 3",right3)
            right3.setPixmap(r)
        elif flags[2]=='False':
            assembler.layout_rs.addRow("Case 3",right3)
            right3.setPixmap(w)
        if flags[3]=='True':
            assembler.layout_rs.addRow("Case 4",right4)
            right4.setPixmap(r)
        elif flags[3]=='False':
            assembler.layout_rs.addRow("Case 4",right4)
            right4.setPixmap(w)
        if flags[4]=='True':
            assembler.layout_rs.addRow("Case 5",right5)
            right5.setPixmap(r)
        elif flags[4]=='False':
            assembler.layout_rs.addRow("Case 5",right5)
            right5.setPixmap(w)
        if flags[5]=='True':
            assembler.layout_rs.addRow("Case 6",right6)
            right6.setPixmap(r)
        elif flags[5]=='False':
            assembler.layout_rs.addRow("Case 6",right6)
            right6.setPixmap(w)
        if flags[6]=='True':
            assembler.layout_rs.addRow("Case 7",right7)
            right7.setPixmap(r)
        elif flags[6]=='False':
            assembler.layout_rs.addRow("Case 7",right7)
            right7.setPixmap(w)
        if flags[7]=='True':
            assembler.layout_rs.addRow("Case 8",right8)
            right8.setPixmap(r)
        elif flags[7]=='False':
            assembler.layout_rs.addRow("Case 8",right8)
            right8.setPixmap(w)
        if flags[8]=='True':
            assembler.layout_rs.addRow("Case 9",right9)
            right9.setPixmap(r)
        elif flags[8]=='False':
            assembler.layout_rs.addRow("Case 9",right9)
            right9.setPixmap(w)
        if flags[9]=='True':
            assembler.layout_rs.addRow("Case 10",right10)
            right10.setPixmap(r)
        elif flags[9]=='False':
            assembler.layout_rs.addRow("Case 10",right10)
            right10.setPixmap(w)

        assembler.dockW.setLayout(assembler.layout_rs)
        assembler.dock.setWidget(assembler.dockW)
        assembler.gridLayout.addWidget(assembler.dock,2,0)

    def select_change(assembler):
        #select the index of the arrays to be displayed
        for i in range(0,11):
            if i==assembler.comboBox.currentIndex():
                print(assembler.comboBox.currentIndex())

                assembler.lbl_pc.setText('The Final PC is:\r\n'+pc[i-1]+"\r\n")
                assembler.lbl_rg.setText('The contents of the register file are:\r\n'+regfile[i-1]+"\r\n")
                assembler.lbl_dmem.setText('The contents of data memory are:\r\n'+dmem[i-1]+"\r\n")


if __name__ == '__main__':
    App = QApplication(sys.argv)
    ex = Start_Window()
    sys.exit(App.exec())
