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
    """
        A class used to control the Calculator GUI.

        This class provides methods for handling user input, performing calculations,
        and updating the UI. See individual method docstrings for more information.

    """
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
        """
        Resets the input fields and the result display.
        """

        self.stackedWidget_result.setCurrentIndex(0)
        self.lineEdit_first_num.setText('')
        self.lineEdit_second_num.setText('')
        self.lineEdit_first_num.setFocus()

    def clock(self):
        """
        Starts a clock that displays the current time in the central timezone.
        """

        # create a function to get the current time in central timezone
        def get_central_time():
            """
            Gets the current time in central timezone.

            Returns
            -------
            central_time : datetime
                The current time in the 'America/Chicago' timezone.
            """
            local_time = datetime.datetime.now()

            # convert UTC time to central timezone
            central_tz = pytz.timezone('America/Chicago')
            central_time = local_time.astimezone(central_tz)

            return central_time

        # create a function to continuously update the time
        def update_time():
            """
            Continuously updates the time every second.
            """
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
        """
            Checks if all arguments can be converted to a float.

            Parameters
            ----------
            *args : Variable length argument list.
                The arguments to be checked.

            Returns
            -------
            bool
                True if all arguments can be converted to a float, False otherwise.
        """
        try:
            for num in args:
                float(num)
            return True
        except ValueError:
            return False

    def next_page(self):
        """
            Changes the displayed page in the QStackedWidget to the next one.

            It gets the current index and total number of pages in the QStackedWidget,
            increments the index and wraps around if necessary, then sets the new index
            for the QStackedWidget.
        """

        # Get the current index and total number of pages in the QStackedWidget
        current_index = self.stackedWidget_options.currentIndex()
        total_pages = self.stackedWidget_options.count()

        # Increment the index and wrap around if necessary
        next_index = (current_index + 1) % total_pages

        # Set the new index for the QStackedWidget
        self.stackedWidget_options.setCurrentIndex(next_index)

    def determine_function(self):
        """
        Determines the mathematical operation to be performed based on the button pressed.
        """

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
        """
        Performs an addition operation on the numbers entered by the user.

        It takes the numbers from the input fields, verifies if they are valid numbers,
        performs the addition, and displays the result in the QStackedWidget. If the inputs
        are not valid numbers, it switches to the error page in the QStackedWidget.
        """

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
        """
        Performs a subtraction operation on the numbers entered by the user.

        It takes the numbers from the input fields, verifies if they are valid numbers,
        performs the subtraction, and displays the result in the QStackedWidget. If the inputs
        are not valid numbers, it switches to the error page in the QStackedWidget.
        """

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
        """
        Performs a multiplication operation on the numbers entered by the user.

        It takes the numbers from the input fields, verifies if they are valid numbers,
        performs the multiplication, and displays the result in the QStackedWidget. If the inputs
        are not valid numbers, it switches to the error page in the QStackedWidget.
        """

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
        """
        Performs a division operation on the numbers entered by the user.

        It takes the numbers from the input fields, verifies if they are valid numbers and
        the divisor is not zero, performs the division, and displays the result in the
        QStackedWidget. If the inputs are not valid numbers or the divisor is zero, it
        switches to the error page in the QStackedWidget.
        """

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
        """
        Performs an exponentiation operation on the numbers entered by the user.

        It takes the numbers from the input fields, verifies if they are valid numbers,
        performs the exponentiation (raising the first number to the power of the second),
        and displays the result in the QStackedWidget. If the inputs are not valid numbers,
        it switches to the error page in the QStackedWidget.
        """

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
        """
        Calculates the Greatest Common Divisor (GCD) of the two numbers entered by the user.

        It takes the numbers from the input fields, verifies if they are valid numbers,
        calculates the GCD, and displays the result in the QStackedWidget. If the inputs
        are not valid numbers, it switches to the error page in the QStackedWidget.
        """

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
        """
        Calculates the percentage of the first number entered by the user relative to the second number.

        It takes the numbers from the input fields, verifies if they are valid numbers,
        calculates the percentage, and displays the result in the QStackedWidget. If the inputs
        are not valid numbers, it switches to the error page in the QStackedWidget.
        """

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
        """
        Performs a modulo operation on the numbers entered by the user.

        It takes the numbers from the input fields, verifies if they are valid numbers,
        performs the modulo operation (calculating the remainder of the division of the first
        number by the second), and displays the result in the QStackedWidget. If the inputs
        are not valid numbers, it switches to the error page in the QStackedWidget.
        """

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
