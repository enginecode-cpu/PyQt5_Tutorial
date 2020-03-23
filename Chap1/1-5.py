# 상태바 만들기

"""
---------------------------------------
Menu bar                              |
---------------------------------------
             Toolbars                 |
---------------------------------|    |
    |     Dock Widgets        |  |    |
    ---------------------------  |    |
    |                         |  |    |
    |     Central Widget      |  |    |
    |                         |  |    |
    ---------------------------  |    |
    |                         |  |    |
    |                         |  |    |
--------------------------------------|
Status Bar                            |
--------------------------------------|

"""

# QStatusBar는 어플리케이션의 상태를 알려주기 위해 하단에 존재하는 위젯

# 상태바의 텍스트를 표시하기 위해서는 showMessage() 메서드를 사용한다.

# 상태바를 사라지게 하기 위해서는 clearMessage() 메서드를 사용하거나
# showMessage() 메서드에 텍스트가 표시되는 시간을 설정할 수 있다.

# 현재 표시되는 메세지 텍스트를 갖고오고 싶을 때는 currentMessage() 메서드를 사용한다.

# QStatusBar 클래스는 상태바에 표시되는 메세지가 바뀔 때 마다 messageChanged() 시그널을 발생

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # statusBar() 메서드를 통해서 상태바를 만든다.
        # showMessage() 메서드를 통해서 상태바에 보여질 메시지를 보여준다.
        self.statusBar().showMessage('Ready')

        self.setWindowTitle("Statusbar")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

