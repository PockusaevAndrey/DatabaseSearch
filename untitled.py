# использование библиотек pyqt5
from PyQt5 import QtCore, QtGui, QtWidgets


# создание главного класса окна
class Ui_MainWindow(object):
    # функция отрисовки окна
    def setupUi(self, MainWindow):
        # присвоение имени окну
        MainWindow.setObjectName("MainWindow")
        # изменение размера окна
        MainWindow.resize(800, 600)
        # создание центрального объекта окна
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # присвоение имени центриальному виджету
        self.centralwidget.setObjectName("centralwidget")
        # расстановка всех виджетов по вертикали
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        # присвоение имени расстановки
        self.verticalLayout.setObjectName("verticalLayout")
        # создание кнопки
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # присвоение имени кнопке
        self.pushButton_2.setObjectName("pushButton_2")
        # доваление кнопки в расстановку
        self.verticalLayout.addWidget(self.pushButton_2)
        # создание кнопки
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # присвоение имени кнопке
        self.pushButton.setObjectName("pushButton")
        # доваление кнопки в расстановку
        self.verticalLayout.addWidget(self.pushButton)
        # создание кнопки
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        # присвоение имени кнопке
        self.pushButton_3.setObjectName("pushButton_3")
        # доваление кнопки в расстановку
        self.verticalLayout.addWidget(self.pushButton_3)
        # установка центрального виджета
        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
