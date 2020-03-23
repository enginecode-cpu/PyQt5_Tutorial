# 창 닫기

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 푸시 버튼을 만든다
        # 첫 번째 파라미터에는 버튼에 표시될 텍스트
        # 두 번재 파라미터에는 버튼이 위치할 부모 위젯
        btn = QPushButton('Quit', self)
        btn.move(100, 150)
        btn.resize(btn.sizeHint())

        # 이벤트 처리
        # 버튼을 클릭하면 'clicked' 시그널이 만들어진다.
        # instance() 메서드는 현재 인스턴스를 반환
        # 'clicked' 시그널은 어플리케이션을 종료하는 'quit' 메서드에 연결된다.
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("Quit Button")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())