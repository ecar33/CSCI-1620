from controller import *


def main():
    """
    The entry point of the application.

    This function initializes the QApplication, creates an instance of the Controller
    class (which is the main window of the application), sets its fixed size and window
    title, and finally displays the window. It then enters the application's event loop
    by calling exec_() on the QApplication instance.
    """

    application = QApplication([])
    window = Controller()
    window.setFixedSize(400, 550)
    window.setWindowTitle("Final Project_1")
    window.show()
    application.exec_()


if __name__ == "__main__":
    main()

