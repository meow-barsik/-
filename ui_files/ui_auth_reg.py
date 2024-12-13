# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'authorization_and_registration.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(404, 306)
        Dialog.setStyleSheet(u"background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.503, stop:0.333333 rgba(207, 112, 181, 255), stop:1 rgba(255, 255, 255, 255))")
        self.auth_window = QWidget(Dialog)
        self.auth_window.setObjectName(u"auth_window")
        self.auth_window.setGeometry(QRect(0, 0, 411, 301))
        self.auth_window.setStyleSheet(u"background-color: rgb(255, 196, 247)")
        self.verticalLayoutWidget = QWidget(self.auth_window)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(90, 70, 231, 101))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.username_input = QLineEdit(self.verticalLayoutWidget)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(12)
        self.username_input.setFont(font)
        self.username_input.setStyleSheet(u" background-color: rgb(255, 255, 255);\n"
"color: rgb(43, 43, 43);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(255, 85, 255)")

        self.verticalLayout.addWidget(self.username_input)

        self.password_input = QLineEdit(self.verticalLayoutWidget)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(0, 25))
        self.password_input.setFont(font)
        self.password_input.setStyleSheet(u" background-color: rgb(255, 255, 255);\n"
"color: rgb(43, 43, 43);\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(255, 85, 255)")

        self.verticalLayout.addWidget(self.password_input)

        self.horizontalLayoutWidget = QWidget(self.auth_window)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(90, 190, 229, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.auth_button = QPushButton(self.horizontalLayoutWidget)
        self.auth_button.setObjectName(u"auth_button")
        self.auth_button.setStyleSheet(u" background-color: rgb(255, 255, 255);\n"
"color: rgb(43, 43, 43);")

        self.horizontalLayout.addWidget(self.auth_button)

        self.to_reg_button = QPushButton(self.horizontalLayoutWidget)
        self.to_reg_button.setObjectName(u"to_reg_button")
        self.to_reg_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(43, 43, 43);\n"
"")

        self.horizontalLayout.addWidget(self.to_reg_button)

        self.reg_window = QWidget(Dialog)
        self.reg_window.setObjectName(u"reg_window")
        self.reg_window.setGeometry(QRect(0, 0, 411, 311))
        self.reg_window.setStyleSheet(u"background-color: rgb(255, 196, 247)")
        self.widget_3 = QWidget(self.reg_window)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(100, 40, 201, 231))
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 108, 243);\n"
"border-radius:  1em")
        self.us_input = QLineEdit(self.widget_3)
        self.us_input.setObjectName(u"us_input")
        self.us_input.setGeometry(QRect(10, 10, 181, 31))
        self.us_input.setFont(font)
        self.us_input.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"border-radius: 10px")
        self.mail_input = QLineEdit(self.widget_3)
        self.mail_input.setObjectName(u"mail_input")
        self.mail_input.setGeometry(QRect(10, 50, 181, 31))
        self.mail_input.setFont(font)
        self.mail_input.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"border-radius: 10px")
        self.phone_input = QLineEdit(self.widget_3)
        self.phone_input.setObjectName(u"phone_input")
        self.phone_input.setGeometry(QRect(10, 90, 181, 31))
        self.phone_input.setFont(font)
        self.phone_input.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"border-radius: 10px")
        self.passwd_input = QLineEdit(self.widget_3)
        self.passwd_input.setObjectName(u"passwd_input")
        self.passwd_input.setGeometry(QRect(10, 130, 181, 31))
        self.passwd_input.setFont(font)
        self.passwd_input.setStyleSheet(u"color: rgb(66, 66, 66);\n"
"border-radius: 10px")
        self.registr_button = QPushButton(self.widget_3)
        self.registr_button.setObjectName(u"registr_button")
        self.registr_button.setGeometry(QRect(30, 180, 141, 21))
        self.registr_button.setStyleSheet(u"background-color: rgb(253, 197, 255);\n"
"color: rgb(43, 43, 43);\n"
"border-radius: 10px; \n"
"\n"
"")
        self.reg_window.raise_()
        self.auth_window.raise_()

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.username_input.setText("")
        self.username_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.auth_button.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.to_reg_button.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.us_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.mail_input.setText("")
        self.mail_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0447\u0442\u0430", None))
        self.phone_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.passwd_input.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.registr_button.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
    # retranslateUi

