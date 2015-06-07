__author__ = 'ravindra'
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import infixToPostfix
import postfixEvaluation

class Calculator(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setWindowTitle("Ravindra's Calculator")
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.lcd=QtGui.QLabel()#QtGui.QLCDNumber()

        self.btn0=QtGui.QPushButton("0")
        self.btn1=QtGui.QPushButton("1")
        self.btn2=QtGui.QPushButton("2")
        self.btn3=QtGui.QPushButton("3")
        self.btn4=QtGui.QPushButton("4")
        self.btn5=QtGui.QPushButton("5")
        self.btn6=QtGui.QPushButton("6")
        self.btn7=QtGui.QPushButton("7")
        self.btn8=QtGui.QPushButton("8")
        self.btn9=QtGui.QPushButton("9")

        self.btnDiv=QtGui.QPushButton("/")
        self.btnMul=QtGui.QPushButton("*")
        self.btnPlus=QtGui.QPushButton("+")
        self.btnMin=QtGui.QPushButton("-")
        self.btnMod=QtGui.QPushButton("%")
        self.btnEql=QtGui.QPushButton("=")
        self.btnEql.setShortcut("Enter")
        #self.btnRes=QtGui.QPushButton("1/x")
        self.btnDot=QtGui.QPushButton(".")
        self.btnClr=QtGui.QPushButton("clear")

        self.btn0.setShortcut("0")
        self.btn1.setShortcut("1")
        self.btn2.setShortcut("2")
        self.btn3.setShortcut("3")
        self.btn4.setShortcut("4")
        self.btn5.setShortcut("5")
        self.btn6.setShortcut("6")
        self.btn7.setShortcut("7")
        self.btn8.setShortcut("8")
        self.btn9.setShortcut("9")

        self.btnPlus.setShortcut("+")
        self.btnMin.setShortcut("-")
        self.btnMul.setShortcut("*")
        self.btnDiv.setShortcut("/")
        self.btnMod.setShortcut("%")
        self.btnDot.setShortcut(".")
        self.btnClr.setShortcut("backspace")


        grid=QtGui.QGridLayout()

        grid.addWidget(self.lcd,0,0,1,5)
        grid.addWidget(self.btnClr,2,4)

        grid.addWidget(self.btn7,2,0)
        grid.addWidget(self.btn8,2,1)
        grid.addWidget(self.btn9,2,2)
        grid.addWidget(self.btnDiv,2,3)
        grid.addWidget(self.btnMod,3,4)

        grid.addWidget(self.btn4,3,0)
        grid.addWidget(self.btn5,3,1)
        grid.addWidget(self.btn6,3,2)
        grid.addWidget(self.btnMul,3,3)
        #grid.addWidget(self.btnRes,3,4)

        grid.addWidget(self.btn1,4,0)
        grid.addWidget(self.btn2,4,1)
        grid.addWidget(self.btn3,4,2)
        grid.addWidget(self.btnMin,4,3)
        grid.addWidget(self.btnEql,4,4,2,1)

        grid.addWidget(self.btn0,5,0,1,2)
        grid.addWidget(self.btnDot,5,2)
        grid.addWidget(self.btnPlus,5,3)

        self.setLayout(grid)

        self.btn0.clicked.connect(self.btn0Fun)
        self.btn1.clicked.connect(self.btn1Fun)
        self.btn2.clicked.connect(self.btn2Fun)
        self.btn3.clicked.connect(self.btn3Fun)
        self.btn4.clicked.connect(self.btn4Fun)
        self.btn5.clicked.connect(self.btn5Fun)
        self.btn6.clicked.connect(self.btn6Fun)
        self.btn7.clicked.connect(self.btn7Fun)
        self.btn8.clicked.connect(self.btn8Fun)
        self.btn9.clicked.connect(self.btn9Fun)

        self.btnPlus.clicked.connect(self.btnPlusFun)
        self.btnMin.clicked.connect(self.btnMinFun)
        self.btnMul.clicked.connect(self.btnMulFun)
        self.btnMod.clicked.connect(self.btnModFun)
        self.btnDiv.clicked.connect(self.btnDivFun)
        self.btnDot.clicked.connect(self.btnDotFun)

        self.btnClr.clicked.connect(self.clear)

        self.btnEql.clicked.connect(self.calculate)

        #self.display()


    def display(self):
        #self.lcd.display("*")
        pass
    def clear(self):
        self.str=""
        #self.lcd.display(self.str)
        #self.lcd.clear()
        self.lcd.setText(self.str)


    str = ""
    def btn0Fun(self):
        self.str+="0"
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btn1Fun(self):
        self.str+="1"
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btn2Fun(self):
        self.str+="2"
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btn3Fun(self):
        self.str+="3"
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btn4Fun(self):
        self.str+="4"
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btn5Fun(self):
        self.str+="5"
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btn6Fun(self):
        self.str+="6"
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btn7Fun(self):
        self.str+="7"
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btn8Fun(self):
        self.str+="8"
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btn9Fun(self):
        self.str+="9"
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btnDotFun(self):
        self.str+="."
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btnPlusFun(self):
        self.str+=" + "
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btnMinFun(self):
        self.str+=" - "
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btnMulFun(self):
        self.str+=" * "
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btnDivFun(self):
        self.str+=" / "
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)
    def btnModFun(self):
        self.str+=" % "
        #self.lcd.display(self.str)
        self.lcd.setText(self.str)


    def calculate(self):
        t=infixToPostfix.inToPost(self.str)
        self.str= str(postfixEvaluation.evaluate(t))
        self.lcd.setText(self.str)


app=QtGui.QApplication(sys.argv)
window=Calculator()
window.show()
exit(app.exec_())


