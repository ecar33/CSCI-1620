from PyQt5.QtWidgets import *
from view import *
import formulas as f

QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_main_window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_clear.clicked.connect(lambda: self.clear())

    def submit(self):
        pass

    def clear(self):
        self.entry_food.setText('')
        self.entry_drink.setText('')
        self.entry_dessert.setText('')
        self.stackedWidget_summary.setCurrentIndex(2)
        self.button_tip_10.setChecked(True)
