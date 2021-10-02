from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QGridLayout
import sys
from functools import partial

EVALUATED = False


def insert_symbol(button):
    if not EVALUATED:
        line_edit_display.setText(line_edit_display.text() + button.text())


def cls():
    global EVALUATED
    EVALUATED = False
    line_edit_display.setText('')


def evaluate():
    global EVALUATED
    if not EVALUATED:
        exp = line_edit_display.text()
        if len(exp) == 0:
            return
        try:
            result = eval(exp)
            line_edit_display.setText(line_edit_display.text() + '=' + str(result))
            EVALUATED = True
        except ZeroDivisionError:
            line_edit_display.setText('تقسیم بر صفر خطا است.')
            EVALUATED = True
        except Exception as e:
            print(e)


app = QApplication(sys.argv)
main_window = QWidget()
main_window.setWindowTitle('UB Calculator')
main_window.setGeometry(500, 500, 400, 400)
main_window.setMinimumWidth(300)
main_window.setMinimumHeight(300)
line_edit_display = QLineEdit()
line_edit_display.setReadOnly(True)
buttons = {'0': {'loc': (3, 0),
                 'btn': QPushButton('0')},
           '1': {'loc': (2, 0),
                 'btn': QPushButton('1')},
           '2': {'loc': (2, 1),
                 'btn': QPushButton('2')},
           '3': {'loc': (2, 2),
                 'btn': QPushButton('3')},
           '4': {'loc': (1, 0),
                 'btn': QPushButton('4')},
           '5': {'loc': (1, 1),
                 'btn': QPushButton('5')},
           '6': {'loc': (1, 2),
                 'btn': QPushButton('6')},
           '7': {'loc': (0, 0),
                 'btn': QPushButton('7')},
           '8': {'loc': (0, 1),
                 'btn': QPushButton('8')},
           '9': {'loc': (0, 2),
                 'btn': QPushButton('9')},
           '/': {'loc': (0, 3),
                 'btn': QPushButton('/')},
           '*': {'loc': (1, 3),
                 'btn': QPushButton('*')},
           '-': {'loc': (2, 3),
                 'btn': QPushButton('-')},
           '+': {'loc': (3, 3),
                 'btn': QPushButton('+')},
           '=': {'loc': (3, 2),
                 'btn': QPushButton('=')},
           'cls': {'loc': (3, 1),
                   'btn': QPushButton('cls')}}

vbox_layout = QVBoxLayout()
grid_layout = QGridLayout()

for symbol, value in buttons.items():
    value['btn'].setFixedSize(50, 50)
    grid_layout.addWidget(value['btn'], value['loc'][0], value['loc'][1])
    if symbol not in ['=', 'cls']:
        value['btn'].clicked.connect(partial(insert_symbol, value['btn']))
buttons['=']['btn'].clicked.connect(evaluate)
buttons['cls']['btn'].clicked.connect(cls)
vbox_layout.addWidget(line_edit_display)
vbox_layout.addLayout(grid_layout)
main_window.setLayout(vbox_layout)
main_window.show()
sys.exit(app.exec_())
