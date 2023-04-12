from PyQt5.QtWidgets import *
from view import *
import datetime
import pytz
import time
import threading
import math

QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.ApplicationAttribute.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.clock()
        self.reset_pushButton.clicked.connect(lambda: self.reset())
        self.pushButton_page_1.clicked.connect(self.next_page)
        self.pushButton_page_2.clicked.connect(self.next_page)

        self.add_pushButton.clicked.connect(lambda: self.determine_function())
        self.subtract_pushButton.clicked.connect(lambda: self.determine_function())
        self.multiply_pushButton.clicked.connect(lambda: self.determine_function())
        self.divide_pushButton.clicked.connect(lambda: self.determine_function())

        self.exponent_pushButton.clicked.connect(lambda: self.determine_function())
        self.gcd_pushButton.clicked.connect(lambda: self.determine_function())
        self.modulo_pushButton.clicked.connect(lambda: self.determine_function())
        self.percent_pushButton.clicked.connect(lambda: self.determine_function())

    def reset(self):
        self.stackedWidget_result.setCurrentIndex(0)
        self.lineEdit_first_num.setText('')
        self.lineEdit_second_num.setText('')
        self.lineEdit_first_num.setFocus()

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

    def next_page(self):

        # Get the current index and total number of pages in the QStackedWidget
        current_index = self.stackedWidget_options.currentIndex()
        total_pages = self.stackedWidget_options.count()

        # Increment the index and wrap around if necessary
        next_index = (current_index + 1) % total_pages

        # Set the new index for the QStackedWidget
        self.stackedWidget_options.setCurrentIndex(next_index)

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
            case "Exponent":
                self.exponent()
            case "Percent":
                self.percent()
            case "GCD":
                self.gcd()
            case "Modulo":
                self.modulo()

    def add(self):
        self.stackedWidget_functions.setCurrentIndex(1)
        x = self.lineEdit_first_num.text()
        y = self.lineEdit_second_num.text()

        if self.check_if_num(x, y):
            self.stackedWidget_result.setCurrentIndex(1)
            x = round(float(x), 2)
            y = round(float(y), 2)
            result = x + y
            result_text = f'{x} + {y} = {result}'
            self.label_result.setText(result_text)
        else:
            self.stackedWidget_result.setCurrentIndex(2)

    def subtract(self):
        self.stackedWidget_functions.setCurrentIndex(1)
        x = self.lineEdit_first_num.text()
        y = self.lineEdit_second_num.text()

        if self.check_if_num(x, y):
            self.stackedWidget_result.setCurrentIndex(1)
            x = round(float(x), 2)
            y = round(float(y), 2)
            result = x - y
            result_text = f'{x} - {y} = {result:.2f}'
            self.label_result.setText(result_text)
        else:
            self.stackedWidget_result.setCurrentIndex(2)

    def multiply(self):
        self.stackedWidget_functions.setCurrentIndex(1)
        x = self.lineEdit_first_num.text()
        y = self.lineEdit_second_num.text()

        if self.check_if_num(x, y):
            self.stackedWidget_result.setCurrentIndex(1)
            x = round(float(x), 2)
            y = round(float(y), 2)
            result = x * y
            result_text = f'{x} * {y} = {result:.2f}'
            self.label_result.setText(result_text)
        else:
            self.stackedWidget_result.setCurrentIndex(2)

    def divide(self):
        self.stackedWidget_functions.setCurrentIndex(1)
        x = self.lineEdit_first_num.text()
        y = self.lineEdit_second_num.text()

        if self.check_if_num(x, y) and (float(y) != 0):
            self.stackedWidget_result.setCurrentIndex(1)
            x = round(float(x), 2)
            y = round(float(y), 2)
            result = x / y
            result_text = f'{x} / {y} = {result:.2f}'
            self.label_result.setText(result_text)
        else:
            self.stackedWidget_result.setCurrentIndex(2)

    def exponent(self):
        self.stackedWidget_functions.setCurrentIndex(1)
        x = self.lineEdit_first_num.text()
        y = self.lineEdit_second_num.text()

        if self.check_if_num(x, y):
            self.stackedWidget_result.setCurrentIndex(1)
            x = round(float(x), 2)
            y = math.floor(float(y))
            result = math.pow(x, y)
            result_text = f'{x}^{y} = {result:.2f}'
            self.label_result.setText(result_text)
        else:
            self.stackedWidget_result.setCurrentIndex(2)

    def gcd(self):
        self.stackedWidget_functions.setCurrentIndex(1)
        x = self.lineEdit_first_num.text()
        y = self.lineEdit_second_num.text()

        if self.check_if_num(x, y):
            self.stackedWidget_result.setCurrentIndex(1)
            x = math.floor(float(x))
            y = math.floor(float(y))
            result = math.gcd(x, y)
            result_text = f'GCD of {x} and {y} = {result}'
            self.label_result.setText(result_text)
        else:
            self.stackedWidget_result.setCurrentIndex(2)

    def percent(self):
        self.stackedWidget_functions.setCurrentIndex(1)
        x = self.lineEdit_first_num.text()
        y = self.lineEdit_second_num.text()

        if self.check_if_num(x, y):
            self.stackedWidget_result.setCurrentIndex(1)
            x = round(float(x), 2)
            y = round(float(y), 2)
            result = x * (y / 100)
            result_text = f'{y}% of {x} = {result:.2f}'
            self.label_result.setText(result_text)
        else:
            self.stackedWidget_result.setCurrentIndex(2)

    def modulo(self):
        self.stackedWidget_functions.setCurrentIndex(1)
        x = self.lineEdit_first_num.text()
        y = self.lineEdit_second_num.text()

        if self.check_if_num(x, y):
            self.stackedWidget_result.setCurrentIndex(1)
            x = round(float(x), 2)
            y = round(float(y), 2)
            result = x % y
            result_text = f'{x} % {y} = {result:.2f}'
            self.label_result.setText(result_text)
        else:
            self.stackedWidget_result.setCurrentIndex(2)
