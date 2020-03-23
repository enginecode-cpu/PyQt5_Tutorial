# 메뉴바 만들기

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Save
        saveAction = QAction(QIcon('save.png'), 'Save', self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("Save Application")

        self.statusBar()

        self.toolbar = self.addToolBar("Save")
        self.toolbar.addAction(saveAction)

        # Print
        printAction = QAction(QIcon('print.png'), 'Print', self)
        printAction.setShortcut("Ctrl+P")
        printAction.setStatusTip("Print Application")
        self.statusBar()

        self.toolbar = self.addToolBar("Save")
        self.toolbar.addAction(printAction)

        # Edit
        editAction = QAction(QIcon('edit.png'), 'Edit', self)
        editAction.setShortcut("Ctrl+E")
        editAction.setStatusTip("Edit Application")

        self.statusBar()

        self.toolbar = self.addToolBar("Edit")
        self.toolbar.addAction(editAction)

        # Exit
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(exitAction)


        self.setWindowTitle("Toolbar")
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
