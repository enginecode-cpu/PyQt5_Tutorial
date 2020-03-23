# 그리드 레이아웃
# 이 레이아웃 클래스는 위젯의 공간을 행과 열로 구분한다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QGridLayout을 만들고 어플리케이션 창의 레이아웃으로 설정
        grid = QGridLayout()
        self.setLayout(grid)

        # addWidget() 메서드의 첫번째 파라미터는 추가할 위젯, 두세번째 파라미터는 각각 행과 열 번호를 입력
        grid.addWidget(QLabel("Title:"), 0, 0)
        grid.addWidget(QLabel("Author:"), 1, 0)
        grid.addWidget(QLabel("Review:"), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        self.setWindowTitle("QGridLayout")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())