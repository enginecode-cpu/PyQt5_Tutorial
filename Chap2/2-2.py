# 박스 레이아웃
# QHBoxLayout, QVBoxLayout은 여러 위젯을 수평으로 정렬하는 레이아웃 클래스이다.

# QHBoxLayout, QVBoxLayout 생성자는 수평, 수직의 박스를 하나 만드는데,
# 다른 레이아웃 박스를 넣을 수도 있고 위젯을 배치할 수도 있다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 두 개의 버튼을 만든다.
        okButton = QPushButton('Ok')
        cancelButton = QPushButton('Cancel')


        hbox = QHBoxLayout() # 수평 박스를 하나 만든다.
        hbox.addStretch(1) # 신축성 있는 빈 공간을 하나 만든다.
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout() # 수직 박스를 하나 만든다.
        vbox.addStretch(3)
        vbox.addLayout(hbox) # 수직 박스 안에 수평 박스를 넣는다.
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle("Box Layout")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())