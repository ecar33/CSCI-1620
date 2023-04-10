from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_main_window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.button_submit.clicked.connect(lambda: self.submit())
        self.button_clear.clicked.connect(lambda: self.clear())

    def submit(self):

        def validate_input(self, food, drink, dessert):
            try:
                float(food)
                float(drink)
                float(dessert)
                self.stackedWidget_summary.setCurrentIndex(0)
                flag = True
                return flag
            except ValueError:
                self.stackedWidget_summary.setCurrentIndex(1)
                flag = False
                return flag


        def convert_to_float(food, drink, dessert):
            food = float(food)
            drink = float(drink)
            dessert = float(dessert)
            return food, drink, dessert

        def get_entry_data(self):
            food = self.entry_food.text()
            drink = self.entry_drink.text()
            dessert = self.entry_dessert.text()
            return food, drink, dessert

        def compute_food_total(food, drink, dessert):
            return food + drink + dessert

        def determine_tip_rate(self):
            if self.button_tip_10.isChecked():
                return .1
            elif self.button_tip_15.isChecked():
                return .15
            elif self.button_tip_20.isChecked():
                return .2

        def compute_tax(food_total):
            return .1 * food_total

        def compute_tip(food_total, total_tax, tip_rate):
            return (food_total + total_tax) * tip_rate

        def compute_complete_total(food_total, total_tax, total_tip):
            return food_total + total_tax + total_tip

        def convert_to_text(food, drink, dessert, total_tax, total_tip, complete_total):
            food_text = f'${food:.2f}'
            drink_text = f'${drink:.2f}'
            dessert_text = f'${dessert:.2f}'
            tip_text = f'${total_tip:.2f}'
            tax_text = f'${total_tax:.2f}'
            complete_total_text = f'${complete_total:.2f}'
            return food_text, drink_text, dessert_text, tip_text, tax_text, complete_total_text

        def set_text(self, food_text, drink_text, dessert_text, tip_text, tax_text, complete_total_text):
            self.label_food_s.setText(food_text)
            self.label_drink_s.setText(drink_text)
            self.label_dessert_s.setText(dessert_text)
            self.label_tax.setText(tax_text)
            self.label_tip.setText(tip_text)
            self.label_complete.setText(complete_total_text)

        food, drink, dessert = get_entry_data(self)
        flag = validate_input(self, food, drink, dessert)

        if flag:
            food, drink, dessert = convert_to_float(food, drink, dessert)
            food_total = compute_food_total(food, drink, dessert)
            tip_rate = determine_tip_rate(self)
            total_tax = compute_tax(food_total)
            total_tip = compute_tip(food_total, total_tax, tip_rate)
            complete_total = compute_complete_total(food_total, total_tax, total_tip)
            food_text, drink_text, dessert_text, tip_text, tax_text, complete_total_text = convert_to_text(food, drink,
                                                                                                           dessert,
                                                                                                           total_tax,
                                                                                                           total_tip,
                                                                                                           complete_total)
            set_text(self, food_text, drink_text, dessert_text, tip_text, tax_text, complete_total_text)

    def clear(self):
        self.entry_food.setText('')
        self.entry_drink.setText('')
        self.entry_dessert.setText('')
        self.stackedWidget_summary.setCurrentIndex(2)
        self.button_tip_10.setChecked(True)
