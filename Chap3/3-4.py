# QCheckBox

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox("Show Title", self) # Show Title 이라는 체크 박스를 하나 만든다.
        cb.move(20, 20)
        cb.toggle() # default가 체크가 해제된 상태로 나타나서 바꿔주기 위해서 사용한다.
        cb.stateChanged.connect(self.changeTitle) # 체크 박스의 상태가 바뀔 때 발생하는 시그널을 changeTitle과 연결한다.

        self.setWindowTitle("QCheckBox")
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle("QCheckBox")
        else:
            self.setWindowTitle(" ")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
