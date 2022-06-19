# Из библиотеки PyQt5 импортируем модули
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication
# Импортируем данные из kr.py 
from kr import Ui_MainWindow
# Импортируем модули из библиотек Python
import sys
import math
import numpy
from functools import reduce


# Сервисные команды
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_5.clicked.connect(
            self.author_program)  # Нажатие на кнопку для вывода автора программы в диалоговом окне
        self.ui.exitButton.clicked.connect(
            self.exit)  # Нажатие на кнопку для выхода из программы с подтверждением о выходе в диалоговом окне
        self.ui.comboBox_2.currentIndexChanged.connect(
            self.max_min)  # Нажатие на комбобокс для вывода положительных и отрицательных чисел массива
        self.ui.comboBox.currentIndexChanged.connect(
            self.criteria)  # Нажатие на комбобокс для рассчета критериев массива
        self.ui.comboBox_1.currentIndexChanged.connect(
            self.task1)  # Рассчет и вывод первого массива y(x) и x c применением комбобокса A
        self.ui.comboBox_3.currentIndexChanged.connect(
            self.task2)  # Рассчет и вывод второго массива y(x) и x c применением комбобокса A
        self.ui.comboBox_4.currentIndexChanged.connect(
            self.task3)  # Рассчет и вывод третьего массива y(x) и x c применением комбобокса A

    # Функция рассчета и вывода первого массива y(x) и x c применением комбобокса A
    def task1(self, value):
        s = 0.5
        x_min = -3
        x_max = 3.5
        if value == 0:
            aa = 2

            def a(x):
                return (x + aa) ** 0.5

            xlist = numpy.arange(x_min, x_max, s)
            ylist = [round(a(x), 2) for x in xlist]

        if value == 1:
            aa = -1

            def b(x):
                return (x + aa) ** 0.5

            xlist = numpy.arange(x_min, x_max, s)
            ylist = [round(b(x), 2) for x in xlist]

        if value == 2:
            aa = 5

            def c(x):
                return math.sqrt(x + aa)

            xlist = numpy.arange(x_min, x_max, s)
            ylist = [round(c(x), 2) for x in xlist]

        self.ui.textEdit_1.setText('\n'.join(str(value) for value in xlist))
        self.ui.textEdit_2.setText('\n'.join(str(value) for value in ylist))

    # Функция рассчета и вывода второго массива y(x) и x c применением комбобокса A
    def task2(self, value):
        s = 0.5
        x_min = -3
        x_max = 3.5
        if value == 0:
            aa = 2

            def a(x):
                return (x ** 3 - aa) / 10

            xlist = numpy.arange(x_min, x_max, s)
            ylist = [round(a(x), 2) for x in xlist]

        if value == 1:
            aa = -1

            def b(x):
                return (x ** 3 - aa) / 10

            xlist = numpy.arange(x_min, x_max, s)
            ylist = [round(b(x), 2) for x in xlist]

        if value == 2:
            aa = 5

            def c(x):
                return (x ** 3 - aa) / 10

            xlist = numpy.arange(x_min, x_max, s)
            ylist = [round(c(x), 2) for x in xlist]

        self.ui.textEdit_3.setText('\n'.join(str(value) for value in xlist))
        self.ui.textEdit_4.setText('\n'.join(str(value) for value in ylist))

    # Функция рассчета и вывода третьего массива y(x) и x c применением комбобокса A
    def task3(self, value):
        s = 0.5
        x_min = -3
        x_max = 3.5
        if value == 0:
            aa = 2

            def a(x):
                return math.cos(x) ** 2 + aa

            xlist = numpy.arange(x_min, x_max, s)
            ylist = [round(a(x), 2) for x in xlist]

        if value == 1:
            aa = -1

            def b(x):
                return math.cos(x) ** 2 + aa

            xlist = numpy.arange(x_min, x_max, s)
            ylist = [round(b(x), 2) for x in xlist]

        if value == 2:
            aa = 5

            def c(x):
                return math.cos(x) ** 2 + aa

            xlist = numpy.arange(x_min, x_max, s)
            ylist = [round(c(x), 2) for x in xlist]

        self.ui.textEdit_5.setText('\n'.join(str(value) for value in xlist))
        self.ui.textEdit_6.setText('\n'.join(str(value) for value in ylist))

    # Функция для рассчета критериев массива
    def criteria(self, value):
        s = 0.5
        x_min = -3
        x_max = 3.5
        xlist = numpy.arange(x_min, x_max, s)
        if value == 0:
            dialog = QMessageBox()
            dialog.setWindowTitle("Максимальный элемент массива")
            dialog.setText(str(max(xlist)))
            dialog.exec()

        if value == 1:
            dialog = QMessageBox()
            dialog.setWindowTitle("Минимальный элемент массива")
            dialog.setText(str(min(xlist)))
            dialog.exec()
        if value == 2:
            dialog = QMessageBox()
            dialog.setWindowTitle("Сумма всех элементов массива")
            dialog.setText(str(sum(xlist)))
            dialog.exec()
        if value == 3:
            dialog = QMessageBox()
            dialog.setWindowTitle("Произведение всех элементов массива")
            dialog.setText(str(reduce(lambda x, y: x * y, xlist)))
            dialog.exec()
        if value == 4:
            dialog = QMessageBox()
            dialog.setWindowTitle("Сумма всех отритцательных элементов массива")
            dialog.setText(str(sum([x for x in xlist if x < 0])))
            dialog.exec()
        if value == 5:
            dialog = QMessageBox()
            dialog.setWindowTitle("Произведение всех отритцательных элементов массива")
            dialog.setText(str(reduce(lambda x, y: x * y, filter(lambda x: x < 0, xlist))))
            dialog.exec()
        if value == 6:
            dialog = QMessageBox()
            dialog.setWindowTitle("Сумма всех положительных элементов массива")
            dialog.setText(str(sum([x for x in xlist if x > 0])))
            dialog.exec()
        if value == 7:
            dialog = QMessageBox()
            dialog.setWindowTitle("Произведение всех положительных элементов массива")
            dialog.setText(str(reduce(lambda x, y: x * y, filter(lambda x: x > 0, xlist))))
            dialog.exec()

    # Функция вывода положительных и отрицательных чисел массива
    def max_min(self, value):
        s = 0.5
        x_min = -3
        x_max = 3.5
        xlist = numpy.arange(x_min, x_max, s)
        if value == 0:
            ll = [x for x in xlist if x > 0]
            self.ui.textEdit.setText((str(ll)))
        if value == 1:
            nn = [x for x in xlist if x < 0]
            self.ui.textEdit_8.setText((str(nn)))

    # Функция вывода автора программы в диалоговом окне
    def author_program(self):
        self.message_box('Программа рассчитывает функцию y(x) \nАвтор: Мамичева Н.Д.')

    def message_box(self, body, title='О программе'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

    # Функция выхода из программы с подтверждением пользователя в диалоговом окне
    def exit(self):
        reply = QtWidgets.QMessageBox.question(self, 'Информация', "Вы уверены, что хотите выйти?",
                                               QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()
        else:
            pass


# Сервисные команды
def main():
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())


main()
