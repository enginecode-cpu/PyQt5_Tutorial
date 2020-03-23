# 스타일 꾸미기

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QLabel 클래스를 이용해서 세 개의 라벨 위젯을 만든다.
        # 라벨의 텍스트는 Red, Blue, Green 으로 한다.
        label_red = QLabel('Red')
        label_blue = QLabel('Blue')
        label_green = QLabel('Green')

        # setStyleSheet() 메서드를 이용해서 글자색을 빨간색(red)으로,
        # 경계선을 실선(solid)으로, 경계선 두께를 2px로,
        # 경계선 색을 #FA8072로, 경계선의 모서리를 3px만큼 둥글게 설정
        label_red.setStyleSheet("color: red;"
                                "border-style: solid;"
                                "border-width: 2px;"
                                "border-color: #FA8072;"
                                "border-radius: 3px"
                                )

        # 라벨의 글자색을 파란색(blue)으로,
        # 배경색을 #87CEFA으로, 경계선을 대쉬 스타일로,
        # 경계선 두께를 3px로, 경계선 색을 #1E90FF으로 설정
        label_blue.setStyleSheet("color: blue;"
                                 "background-color: #87CEFA;"
                                 "border-style: dashed;"
                                 "border-width: 3px;"
                                 "border-color: #1E90FF")

        # 라벨의 글자색을 녹색(green)으로, 배경색을 #7FFFD4로 설정
        label_green.setStyleSheet("color: green;"
                                  "background-color: #7FFFD4")

        vbox = QVBoxLayout()
        vbox.addWidget(label_red)
        vbox.addWidget(label_blue)
        vbox.addWidget(label_green)


        self.setLayout(vbox)

        self.setWindowTitle("StyleSheet")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
