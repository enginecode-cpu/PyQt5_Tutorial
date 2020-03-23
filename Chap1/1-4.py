# 툴팁 나타내기
# 툴팁은 어떤 위젯의 기능을 설명하는 등의 역할을 하는 말풍선 형태의 도움말

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 툴팁에 사용될 폰트와 폰트 크기 설정
        QToolTip.setFont(QFont('SansSerif', 10))

        # 툴팁을 만들기 위해 setToolTip()이라는 메서드를 사용한다.
        # 그리고 표시될 메시지를 넣는다.
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 버튼을 하나 만들고 툴팁을 설정한다.
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # 버튼의 위치와 크기를 설정한다.
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle("Tooltips")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

