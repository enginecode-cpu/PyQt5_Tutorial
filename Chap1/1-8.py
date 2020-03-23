#  창을 가운데로

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Centering")
        self.resize(500, 300)
        self.center()
        self.show()

    # 창이 화면에 가운데 위치하게 된다.
    def center(self):
        # 창의 위치와 크기 정보를 가져온다.
        qr = self.frameGeometry()

        # 창의 화면의 위치를 화면의 중심의 위치로 이동한다.
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        # 현재 창을, 화면의 중심으로 이동했던 직사각형 (qr)의 위치로 이동시킨다.
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())