import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QFrame, QWidget
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)

        red_btn = QPushButton("Red", self)
        red_btn.setCheckable(True)
        red_btn.move(10, 10)

        red_btn.clicked.connect(self.setColor)

        blue_btn = QPushButton("Blue", self)
        blue_btn.setCheckable(True)
        blue_btn.move(10, 60)

        blue_btn.clicked.connect(self.setColor)

        green_btn = QPushButton("Green", self)
        green_btn.setCheckable(True)
        green_btn.move(10, 110)

        green_btn.clicked.connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %self.col.name())

        self.setWindowTitle("Toggle Button")
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def setColor(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Blue":
            self.col.setBlue(val)
        else:
            self.col.setGreen(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %self.col.name())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
