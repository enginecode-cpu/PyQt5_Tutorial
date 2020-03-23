# 메뉴바 만들기

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 아이콘을 갖는 하나의 동작을 만든다.
        # 그리고 이에 대해서 단축키를 정의한다.
        # 어떤 역할을 하는지 상태바에 출력하도록 하기 위해서 setStatusTip()을 사용
        exitAction = QAction(QIcon('exit.png'), "Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")

        # 이 동작을 선택했을 때, 생성된 시그널(triggered)이
        # QApplication 위젯의 quit() 메서드에 연결되고 어플리케이션 종료시킨다.
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        # menuBar() 메서드는 메뉴바를 생성한다.
        # 이어서 File 메뉴를 하나 만들고, 거기에 exitAction 동작을 추가한다.
        # '&'는 간편하게 단축키를 생성한다. 'Alt + F's
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu("&File")
        filemenu.addAction(exitAction)

        self.setWindowTitle("Menubar")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
