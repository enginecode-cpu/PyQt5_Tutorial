# QLabel

# 텍스트 또는 이미지 라벨을 만들 때 쓰인다. 사용자와 어떤 상호작용을 제공하지는 않다

# 라벨은 기본적으로 수평 방향으로는 왼쪽, 수직 방향으로는 가운데 정렬이지만
# setAlignment() 메서드를 통해 조절할 수 있다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        label1 = QLabel("First Label", self)
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel("Second Label", self)
        label2.setAlignment(Qt.AlignVCenter)

        font1 = label1.font()
        font1.setPointSize(20)

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)

        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle("QLabel")
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
