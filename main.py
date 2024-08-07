import sys
from math import*
from PyQt6 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow

class CalcApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):     
        buttons = {
            "btn_0": "0", "btn_1": "1", "btn_2": "2", "btn_3": "3",
            "btn_4": "4", "btn_5": "5", "btn_6": "6", "btn_7": "7",
            "btn_8": "8", "btn_9": "9", "btn_dot": ".",
            "btn_plus": "+", "btn_minus": "-",
            "btn_multiple": "*", "btn_divide": "/",
            "btn_leftbracket": "(", "btn_rightbracket": ")",
            "btn_0_2": "0", "btn_1_2": "1", "btn_2_2": "2",
            "btn_3_2": "3", "btn_4_2": "4", "btn_5_2": "5",
            "btn_6_2": "6", "btn_7_2": "7", "btn_8_2": "8",
            "btn_9_2": "9", "btn_dot_2": ".",
            "btn_plus_2": "+", "btn_minus_2": "-",
            "btn_multiple_2": "*", "btn_divide_2": "/",
            "btn_leftbracket_2": "(", "btn_rightbracket_2": ")"
        }

        for btn_name, symbol in buttons.items():
            getattr(self.ui, btn_name).clicked.connect(lambda _, s=symbol: self.write_number(s))
        
        self.ui.btn_clear.clicked.connect(self.clear_line_result)
        self.ui.btn_del.clicked.connect(self.del_text)
        self.ui.btn_equal.clicked.connect(self.calculate)
        self.ui.btn_clear_2.clicked.connect(self.clear_line_result)
        self.ui.btn_del_2.clicked.connect(self.del_text)
        self.ui.btn_equal_2.clicked.connect(self.calculate)
        self.ui.btn_equal_3.clicked.connect(self.calculate)

        self.ui.btn_log.clicked.connect(self.log)
        self.ui.btn_sin.clicked.connect(self.sin)
        self.ui.btn_cos.clicked.connect(self.cos)
        self.ui.btn_tan.clicked.connect(self.tan)
        self.ui.btn_exp.clicked.connect(self.exp)
        self.ui.btn_pi.clicked.connect(self.pi)
        self.ui.btn_e.clicked.connect(self.e)
        self.ui.btn_procent.clicked.connect(self.procent)
        self.ui.btn_square.clicked.connect(self.square)
        self.ui.btn_radical.clicked.connect(self.radical)

        self.ui.act_system.triggered.connect(self.system_theme)
        self.ui.act_light.triggered.connect(self.light_theme)
        self.ui.act_dark.triggered.connect(self.dark_theme)
        self.ui.act_on_trans.triggered.connect(self.transparent)
        
        self.ui.actionStandard.triggered.connect(self.switch_to_standard)
        self.ui.actionEngineer.triggered.connect(self.switch_to_engineer)
        self.ui.actionPaper.triggered.connect(self.switch_to_paper)
        
        self.ui.act_info.triggered.connect(self.show_about_message)

        self.ui.line_result.returnPressed.connect(self.calculate)

        self.is_transparent = False

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
            expression =  self.ui.line_result.text()
            res = eval(expression)
            self.ui.line_result.setText(str(res))
            self.ui.textEdit.append(f"{expression} = {res}")
        except:
            self.error()

    # Clear result line
    def clear_line_result(self):
        self.ui.line_result.setText("0")

    # Delete last symbol
    def del_text(self):
        current_text = self.ui.line_result.text()
        new_text = current_text[:-1]
        self.ui.line_result.setText(new_text)

    # Engineer mode operations
    def log(self):
        try:
            res = eval(self.ui.line_result.text())
            self.ui.line_result.setText(str(log(res)))
        except:
            self.error()
    def sin(self):
        try:
            res = eval(self.ui.line_result.text())
            self.ui.line_result.setText(str(sin(res)))
        except:
            self.error()
    def cos(self):
        try:
            res = eval(self.ui.line_result.text())
            self.ui.line_result.setText(str(cos(res)))
        except:
            self.error()
    def tan(self):
        try:
            res = eval(self.ui.line_result.text())
            self.ui.line_result.setText(str(tan(res)))
        except:
            self.error()
    def exp(self):
        try:
            res = eval(self.ui.line_result.text())
            self.ui.line_result.setText(str(exp(res)))
        except:
            self.error()
    def pi(self):
        try:
            if self.ui.line_result.text() == "" or self.ui.line_result.text() == "0":
                self.ui.line_result.setText(str(pi))
            else:
                res = eval(self.ui.line_result.text())
                self.ui.line_result.setText(str(res*pi))
        except:
            self.error()
    def e(self):
        try:
            if self.ui.line_result.text() == "" or self.ui.line_result.text() == "0":
                self.ui.line_result.setText(str(e))
            else:
                res = eval(self.ui.line_result.text())
                self.ui.line_result.setText(str(res*e))
        except:
            self.error()
    def procent(self):
        try:
            res = eval(self.ui.line_result.text())
            self.ui.line_result.setText(str(res/100))
        except:
            self.error()
    def radical(self):
        try:
            res = eval(self.ui.line_result.text())
            if res >= 0:
                self.ui.line_result.setText(str(sqrt(res)))
            else:
                QtWidgets.QMessageBox.warning(self, "Error",
                                    "It is not possible to extract the root from a negative value")
        except:
            self.error()
    def square(self):
        try:
            res = eval(self.ui.line_result.text())
            self.ui.line_result.setText(str(res*res))
        except:
            self.error()
            
    # Error
    def error(self):
        QtWidgets.QMessageBox.warning(self, "Error", "Incorrect expression")

    # Change style
    def change_theme(self, bg_color, text_color):
        self.setStyleSheet(f"background-color: {bg_color}; color: {text_color};")
    def system_theme(self):
        self.change_theme("", "")
    def light_theme(self):
        self.change_theme("white", "black")
    def dark_theme(self):
        self.change_theme("black", "white")
    def transparent(self):
        self.is_transparent = not self.is_transparent
        if self.is_transparent:
            self.setWindowOpacity(0.7)
        else:
            self.setWindowOpacity(1)
        
    # Change mode
    def switch_to_standard(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.textEdit.clear()
    def switch_to_engineer(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.ui.textEdit.clear()
    def switch_to_paper(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        self.ui.line_result.clear()

    # Show window with info about program
    def show_about_message(self):
        QtWidgets.QMessageBox.information(self, "Simple calc",
                                "Calc, writed \non Python and PyQt6.\n(ɔ) limafresh")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = CalcApp()
    application.show()
    sys.exit(app.exec())
