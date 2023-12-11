import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton
import time

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        #оси выравнивания
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_operation = QHBoxLayout()
        self.hbox_result = QHBoxLayout()
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_operation)
        self.vbox.addLayout(self.hbox_result)
        #виджеты, привязыванные их к соответствующим осям выравнивания
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_plus = QPushButton("+", self)
        self.hbox_operation.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_operation.addWidget(self.b_minus)

        self.b_multiplication = QPushButton("*", self)
        self.hbox_operation.addWidget(self.b_multiplication)

        self.b_division = QPushButton("//", self)
        self.hbox_operation.addWidget(self.b_division)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_point = QPushButton(".", self)
        self.hbox_result.addWidget(self.b_point)

        #События, отвечающие за реакции на нажатия по кнопкам
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiplication.clicked.connect(lambda: self._operation("*"))
        self.b_division.clicked.connect(lambda: self._operation("//"))
        self.b_result.clicked.connect(self._result)
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))

        self.b_point.clicked.connect(lambda: self._point("."))


    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)
    # Уже существующая строка в линии ввода конкатенируется саргументом param и устанавливается как отображаемый в линии вводатекст
    def _operation(self, op):
        try:
            self.num_1 = int(self.input.text()) #Запоминаем первое введенное число в целочисленном типе данных
            self.op = op  # Запоминаем в качестве операции аргумент op
            self.input.setText("")  # Очищаем линию ввода
        except:
            self.input.setText("")

    def _result(self):
        try:
            self.num_2 = int(self.input.text())
            # Запоминаем второе введенное число в целочисленном типе данных
            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))

            if self.op == "-":
                self.input.setText(str(self.num_1 - self.num_2))

            if self.op == "*":
                self.input.setText(str(self.num_1 * self.num_2))

            if self.op == "//":
                self.input.setText(str(self.num_1 // self.num_2))
            #Производим вычисление в зависимости от операции и устанавливаем его в качестве текста в линию ввода
        except:
            self.input.setText("")

    #def pointClicked(self):


app = QApplication(sys.argv)

win = Calculator()
win.show()

sys.exit(app.exec_())