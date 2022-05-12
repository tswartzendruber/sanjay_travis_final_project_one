from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor
from view import Ui_MainWindow
from module import *


class Controller(QWidget, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.main_text.setReadOnly(True)

        self.status = False
        self.central_frame.setDisabled(True)

        self.button_on_off.clicked.connect(lambda: self.on_off())

        self.button_1.clicked.connect(lambda: self.function_one())
        self.button_2.clicked.connect(lambda: self.function_two())
        self.button_3.clicked.connect(lambda: self.function_three())
        self.button_clear.clicked.connect(lambda: self.function_clear())

        self.button_zero.clicked.connect(lambda: self.button0())
        self.button_one.clicked.connect(lambda: self.button1())
        self.button_two.clicked.connect(lambda: self.button2())
        self.button_three.clicked.connect(lambda: self.button3())
        self.button_four.clicked.connect(lambda: self.button4())
        self.button_five.clicked.connect(lambda: self.button5())
        self.button_six.clicked.connect(lambda: self.button6())
        self.button_seven.clicked.connect(lambda: self.button7())
        self.button_eight.clicked.connect(lambda: self.button8())
        self.button_nine.clicked.connect(lambda: self.button9())
        self.button_caret.clicked.connect(lambda: self.caret_button())

        self.function1 = True
        self.function2 = True
        self.function3 = True

    def on_off(self):
        if self.status is False:
            # enable everything
            self.central_frame.setEnabled(True)
            self.status = True
        elif self.status is True:
            # disable everything
            self.function_clear()
            self.central_frame.setDisabled(True)
            self.status = False

    def function_one(self):
        try:
            self.function1 = int(self.main_text.toPlainText())
            output_one = str(one(self.function1))
            self.main_text.append(output_one)
        except ValueError:
            self.main_text.setTextColor(QColor('red'))
            self.main_text.setText('ERROR: Invalid Input')
            self.main_text.setTextColor(QColor('white'))
        except RecursionError:
            self.main_text.setTextColor(QColor('red'))
            self.main_text.setText('OVERFLOW')
            self.main_text.setTextColor(QColor('white'))
        finally:
            # disable buttons
            self.disable_buttons()

    def function_two(self):
        try:
            self.function2 = self.main_text.toPlainText()
            numbers = self.function2.split('^')
            if len(numbers) == 2:
                output_two = str(two(int(numbers[0]), int(numbers[1])))
                self.main_text.append(output_two)
            elif len(numbers) < 2:
                self.main_text.setTextColor(QColor('red'))
                self.main_text.setText('ERROR: Two Numbers Needed')
                self.main_text.setTextColor(QColor('white'))
            else:
                self.main_text.setTextColor(QColor('red'))
                self.main_text.setText('ERROR: Too Many Numbers')
                self.main_text.setTextColor(QColor('white'))
        except ValueError:
            self.main_text.setTextColor(QColor('red'))
            self.main_text.setText('ERROR: Invalid Input')
            self.main_text.setTextColor(QColor('white'))
        except RecursionError:
            self.main_text.setTextColor(QColor('red'))
            self.main_text.setText('OVERFLOW')
            self.main_text.setTextColor(QColor('white'))
        except IndexError:
            self.main_text.setTextColor(QColor('red'))
            self.main_text.setText('ERROR: Invalid Input')
            self.main_text.setTextColor(QColor('white'))
        finally:
            # disable buttons
            self.disable_buttons()

    def function_three(self):
        try:
            self.function3 = int(self.main_text.toPlainText())
            output_three = three(self.function3)
            self.main_text.append(output_three)
        except ValueError:
            self.main_text.setTextColor(QColor('red'))
            self.main_text.setText('ERROR: Invalid Input')
            self.main_text.setTextColor(QColor('white'))
        except RecursionError:
            self.main_text.setTextColor(QColor('red'))
            self.main_text.setText('OVERFLOW')
            self.main_text.setTextColor(QColor('white'))
        finally:
            # disable buttons
            self.disable_buttons()

    def function_clear(self):
        self.main_text.clear()
        # enable buttons
        self.enable_buttons()
        self.main_text.setTextColor(QColor('black'))

    def button0(self):
        self.main_text.insertPlainText('0')

    def button1(self):
        self.main_text.insertPlainText('1')

    def button2(self):
        self.main_text.insertPlainText('2')

    def button3(self):
        self.main_text.insertPlainText('3')

    def button4(self):
        self.main_text.insertPlainText('4')

    def button5(self):
        self.main_text.insertPlainText('5')

    def button6(self):
        self.main_text.insertPlainText('6')

    def button7(self):
        self.main_text.insertPlainText('7')

    def button8(self):
        self.main_text.insertPlainText('8')

    def button9(self):
        self.main_text.insertPlainText('9')

    def caret_button(self):
        self.main_text.insertPlainText('^')

    def disable_buttons(self):
        self.button_zero.setDisabled(True)
        self.button_one.setDisabled(True)
        self.button_two.setDisabled(True)
        self.button_three.setDisabled(True)
        self.button_four.setDisabled(True)
        self.button_five.setDisabled(True)
        self.button_six.setDisabled(True)
        self.button_seven.setDisabled(True)
        self.button_eight.setDisabled(True)
        self.button_nine.setDisabled(True)
        self.button_caret.setDisabled(True)
        self.button_1.setDisabled(True)
        self.button_2.setDisabled(True)
        self.button_3.setDisabled(True)

    def enable_buttons(self):
        self.button_zero.setEnabled(True)
        self.button_one.setEnabled(True)
        self.button_two.setEnabled(True)
        self.button_three.setEnabled(True)
        self.button_four.setEnabled(True)
        self.button_five.setEnabled(True)
        self.button_six.setEnabled(True)
        self.button_seven.setEnabled(True)
        self.button_eight.setEnabled(True)
        self.button_nine.setEnabled(True)
        self.button_caret.setEnabled(True)
        self.button_1.setEnabled(True)
        self.button_2.setEnabled(True)
        self.button_3.setEnabled(True)
