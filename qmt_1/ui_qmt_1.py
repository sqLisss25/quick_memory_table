# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qmt_1.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(260, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(80, 250, 100, 32))
        self.square_button_1 = QPushButton(self.centralwidget)
        self.square_button_1.setObjectName(u"square_button_1")
        self.square_button_1.setGeometry(QRect(50, 50, 40, 50))
        self.square_button_2 = QPushButton(self.centralwidget)
        self.square_button_2.setObjectName(u"square_button_2")
        self.square_button_2.setGeometry(QRect(110, 50, 40, 50))
        self.square_button_3 = QPushButton(self.centralwidget)
        self.square_button_3.setObjectName(u"square_button_3")
        self.square_button_3.setGeometry(QRect(170, 50, 40, 50))
        self.square_button_5 = QPushButton(self.centralwidget)
        self.square_button_5.setObjectName(u"square_button_5")
        self.square_button_5.setGeometry(QRect(110, 110, 40, 50))
        self.square_button_6 = QPushButton(self.centralwidget)
        self.square_button_6.setObjectName(u"square_button_6")
        self.square_button_6.setGeometry(QRect(170, 110, 40, 50))
        self.square_button_4 = QPushButton(self.centralwidget)
        self.square_button_4.setObjectName(u"square_button_4")
        self.square_button_4.setGeometry(QRect(50, 110, 40, 50))
        self.square_button_8 = QPushButton(self.centralwidget)
        self.square_button_8.setObjectName(u"square_button_8")
        self.square_button_8.setGeometry(QRect(110, 170, 40, 50))
        self.square_button_9 = QPushButton(self.centralwidget)
        self.square_button_9.setObjectName(u"square_button_9")
        self.square_button_9.setGeometry(QRect(170, 170, 40, 50))
        self.square_button_7 = QPushButton(self.centralwidget)
        self.square_button_7.setObjectName(u"square_button_7")
        self.square_button_7.setGeometry(QRect(50, 170, 40, 50))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 161, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 260, 32))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"qmt v1", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.square_button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.square_button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.square_button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.square_button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.square_button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.square_button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.square_button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.square_button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.square_button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442", None))
    # retranslateUi

