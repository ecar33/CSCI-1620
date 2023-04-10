from PyQt5.QtWidgets import *
from view import *
import datetime
import pytz
import time
import threading

QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.clock()
        self.reset_pushButton.clicked.connect(lambda: self.reset())

        self.add_pushButton.clicked.connect(lambda: self.determine_function())
        self.subtract_pushButton.clicked.connect(lambda: self.determine_function())
        self.multiply_pushButton.clicked.connect(lambda: self.determine_function())
        self.divide_pushButton.clicked.connect(lambda: self.determine_function())

    def reset(self):
        match self.stackedWidget_functions.currentIndex():
            case 1:
                self.lineEdit_first_num.setText("")
                self.lineEdit_second_num.setText("")
                self.stackedWidget_result.setCurrentIndex(0)
                self.label_result.setText("")

    def clock(self):
        # create a function to get the current time in central timezone
        def get_central_time():
            # get the current time in UTC timezone
            local_time = datetime.datetime.now()

            # convert UTC time to central timezone
            central_tz = pytz.timezone('America/Chicago')
            central_time = local_time.astimezone(central_tz)

            return central_time

        # create a function to continuously update the time
        def update_time():
            while True:
                # get the current time in central timezone
                current_time = get_central_time()

                # create a string to display the current time
                time_string = current_time.strftime('%Y-%m-%d %H:%M:%S %Z')

                # update the date/time label
                self.label_datetime.setText(time_string)

                # wait for one second before updating the time again
                time.sleep(1)

        # create a new thread to run the update_time() function in the background
        time_thread = threading.Thread(target=update_time)
        time_thread.daemon = True
        time_thread.start()


    def check_if_num(self, *args):
            try:
                for num in args:
                    float(num)
                return True
            except ValueError:
                return False
    def determine_function(self):
        chosen_function = self.sender().text()
        match chosen_function:
            case "Add":
                self.add()
            case "Subtract":
                self.subtract()
            case "Multiply":
                self.multiply()
            case "Divide":
                self.divide()

    def add(self):
        self.stackedWidget_functions.setCurrentIndex(1)
        x = self.lineEdit_first_num.text()
        y = self.lineEdit_second_num.text()

        if self.check_if_num(x,y):
            self.stackedWidget_result.setCurrentIndex(1)
            result = float(x) + float(y)
            result = f'{result:.2f}'
            self.label_result.setText(result)
        else:
            self.stackedWidget_result.setCurrentIndex(2)

    def subtract(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass