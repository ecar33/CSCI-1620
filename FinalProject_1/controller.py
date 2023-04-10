from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        #self.button_submit.clicked.connect(lambda: self.submit())
        #self.button_clear.clicked.connect(lambda: self.clear())

    def submit(self):
        pass

    def clear(self):
        pass