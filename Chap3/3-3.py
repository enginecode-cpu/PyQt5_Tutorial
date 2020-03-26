# QCheckBox

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox("Show title", self)
        cb.move(20, 20)
        cb.toggle() # 체크가 된 상태로
        cb.stateChanged.connect(self.changeTitle)

        self.setWindowTitle("QCheckBox")
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle("QCheckBox")
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
