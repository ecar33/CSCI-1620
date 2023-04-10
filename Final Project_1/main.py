from controller import *


def main():
    application = QApplication([])
    window = Controller()
    window.setFixedSize(400, 600)
    window.setWindowTitle("Test 10")
    window.show()
    application.exec_()


if __name__ == "__main__":
    main()

