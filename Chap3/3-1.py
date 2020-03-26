# QPushButton

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("&Button1", self)
        btn1.setCheckable(True) # 선택을 할 수도 있고 안 할 수도 있다
        btn1.toggle() # 이렇게 되면 선택이 된 채로 나타난다.

        btn2 = QPushButton(self)
        btn2.setText("Button&2")

        btn3 = QPushButton("Button3", self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)

        self.setWindowTitle("QPushButton")
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

