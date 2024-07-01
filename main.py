import sys, os
from math import*
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from ui import Ui_MainWindow

class CalcApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.png")))

        buttons = {
            "btn_0": "0", "btn_1": "1", "btn_2": "2", "btn_3": "3",
            "btn_4": "4", "btn_5": "5", "btn_6": "6", "btn_7": "7",
            "btn_8": "8", "btn_9": "9", "btn_leftbracket": "(",
            "btn_rightbracket": ")", "btn_plus": "+", "btn_minus": "-",
            "btn_multiple": "*", "btn_divide": "/", "btn_dot": "."
        }

        for btn_name, symbol in buttons.items():
            getattr(self.ui, btn_name).clicked.connect(lambda _, s=symbol: self.write_number(s))
        
        self.ui.btn_radical.clicked.connect(self.radical)
        self.ui.btn_clear.clicked.connect(self.clear_line_result)
        self.ui.btn_del.clicked.connect(self.del_text)
        self.ui.btn_equal.clicked.connect(self.calculate)
        self.ui.btn_square.clicked.connect(self.square)

        self.ui.act_info.triggered.connect(self.show_about_message)
        self.ui.act_system.triggered.connect(self.system_theme)
        self.ui.act_light.triggered.connect(self.light_theme)
        self.ui.act_dark.triggered.connect(self.dark_theme)
        self.ui.act_on_trans.triggered.connect(self.on_transparent)
        self.ui.act_off_trans.triggered.connect(self.off_transparent)

    # Enter numbers in a line with buttons
    def write_number(self, number):
        if self.ui.line_result.text() == "0":
            self.ui.line_result.setText(number)
        else:
            self.ui.line_result.setText(self.ui.line_result.text() + number)

    # Enter characters in a line with buttons
    def write_symbol(self, symbol):
        self.ui.line_result.setText(self.ui.line_result.text() + symbol)
            
    # Calculate
    def calculate(self):
        try:
            res = eval(self.ui.line_result.text())
            self.ui.line_result.setText(str(res))
        except (SyntaxError, NameError, ZeroDivisionError):
            QMessageBox.warning(self, "Error", "Incorrect expression")

    # Clear result line
    def clear_line_result(self):
        self.ui.line_result.setText("0")

    # Root extraction
    def radical(self):
        try:
            res = eval(self.ui.line_result.text())
            if res >= 0:
                self.ui.line_result.setText(str(sqrt(res)))
            else:
                QMessageBox.warning(self, "Error",
                                    "It is not possible to extract the root from a negative value")
        except (SyntaxError, NameError):
            QMessageBox.warning(self, "Error", "Incorrect expression")

    # Square
    def square(self):
        try:
            res = eval(self.ui.line_result.text())
            self.ui.line_result.setText(str(res*res))
        except (SyntaxError, NameError):
            QMessageBox.warning(self, "Error", "Incorrect expression")

    # Delete last symbol
    def del_text(self):
        current_text = self.ui.line_result.text()
        new_text = current_text[:-1]
        self.ui.line_result.setText(new_text)

    # Show window with info about program
    def show_about_message(self):
        QMessageBox.information(self, "Simple calc",
                                "Calc, writed \non Python and PyQt6.\n(c) limafresh")

    # Change theme
    def change_theme(self, bg_color, text_color):
        self.setStyleSheet(f"background-color: {bg_color}; color: {text_color};")
    def system_theme(self):
        self.change_theme("", "")
    def light_theme(self):
        self.change_theme("white", "black")
    def dark_theme(self):
        self.change_theme("black", "white")

    def on_transparent(self):
        self.setWindowOpacity(0.7)
    def off_transparent(self):
        self.setWindowOpacity(1)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = CalcApp()
    application.show()
    sys.exit(app.exec())
