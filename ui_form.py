# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(551, 482)
        Form.setStyleSheet(u"background-color: rgb(255, 184, 255)")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 170, 531, 131))
        self.widget.setStyleSheet(u"background-color: rgb(254, 217, 255);\n"
"border: 1px solid rgb(255, 85, 255);\n"
"border-radius: 10px")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 81, 111))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 170, 255);\n"
"border: 0px")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(100, 10, 421, 111))
        self.widget_3.setStyleSheet(u"background-color: rgb(255, 170, 255);\n"
"border: 0px")
        self.gridLayoutWidget = QWidget(self.widget_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 421, 111))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.game_check = QCheckBox(self.gridLayoutWidget)
        self.game_check.setObjectName(u"game_check")

        self.gridLayout.addWidget(self.game_check, 3, 0, 1, 1)

        self.music_check = QCheckBox(self.gridLayoutWidget)
        self.music_check.setObjectName(u"music_check")

        self.gridLayout.addWidget(self.music_check, 2, 0, 1, 1)

        self.theatral = QCheckBox(self.gridLayoutWidget)
        self.theatral.setObjectName(u"theatral")

        self.gridLayout.addWidget(self.theatral, 0, 0, 1, 1)

        self.art_check = QCheckBox(self.gridLayoutWidget)
        self.art_check.setObjectName(u"art_check")

        self.gridLayout.addWidget(self.art_check, 1, 0, 1, 1)

        self.animals_check = QCheckBox(self.gridLayoutWidget)
        self.animals_check.setObjectName(u"animals_check")

        self.gridLayout.addWidget(self.animals_check, 4, 0, 1, 1)

        self.garden_check = QCheckBox(self.gridLayoutWidget)
        self.garden_check.setObjectName(u"garden_check")

        self.gridLayout.addWidget(self.garden_check, 0, 1, 1, 1)

        self.vyazanie_check = QCheckBox(self.gridLayoutWidget)
        self.vyazanie_check.setObjectName(u"vyazanie_check")

        self.gridLayout.addWidget(self.vyazanie_check, 1, 1, 1, 1)

        self.spor_check = QCheckBox(self.gridLayoutWidget)
        self.spor_check.setObjectName(u"spor_check")

        self.gridLayout.addWidget(self.spor_check, 2, 1, 1, 1)

        self.language_check = QCheckBox(self.gridLayoutWidget)
        self.language_check.setObjectName(u"language_check")

        self.gridLayout.addWidget(self.language_check, 3, 1, 1, 1)

        self.books_check = QCheckBox(self.gridLayoutWidget)
        self.books_check.setObjectName(u"books_check")

        self.gridLayout.addWidget(self.books_check, 4, 1, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 10, 531, 151))
        self.widget_2.setStyleSheet(u"background-color: rgb(254, 217, 255);\n"
"border: 1px solid rgb(255, 85, 255);\n"
"border-radius: 10px")
        self.formLayoutWidget = QWidget(self.widget_2)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 511, 131))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(255, 170, 255);\n"
"border: 0px")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(90, 0))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 170, 255);\n"
"border: 0px")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(90, 25))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 170, 255);\n"
"border: 0px;\n"
"text-align: centre")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(90, 27))
        self.label_4.setMaximumSize(QSize(16777215, 27))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 170, 255);\n"
"border: 0px")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.name_input = QLineEdit(self.formLayoutWidget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setMinimumSize(QSize(0, 27))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_input)

        self.surname_input = QLineEdit(self.formLayoutWidget)
        self.surname_input.setObjectName(u"surname_input")
        self.surname_input.setMinimumSize(QSize(0, 27))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.surname_input)

        self.age_input = QLineEdit(self.formLayoutWidget)
        self.age_input.setObjectName(u"age_input")
        self.age_input.setMinimumSize(QSize(0, 27))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.age_input)

        self.city_input = QLineEdit(self.formLayoutWidget)
        self.city_input.setObjectName(u"city_input")
        self.city_input.setMinimumSize(QSize(0, 27))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.city_input)

        self.button_next = QPushButton(Form)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setGeometry(QRect(380, 440, 141, 31))
        self.button_next.setFont(font1)
        self.button_next.setStyleSheet(u"background-color: rgb(255, 170, 255);\n"
"border: 1px solid rgb(255, 85, 255);\n"
"border-radius: 10px")
        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 310, 351, 161))
        self.widget_4.setStyleSheet(u"background-color: rgb(254, 217, 255);\n"
"border: 1px solid rgb(255, 85, 255);\n"
"border-radius: 10px")
        self.add_pic = QPushButton(self.widget_4)
        self.add_pic.setObjectName(u"add_pic")
        self.add_pic.setGeometry(QRect(200, 120, 141, 31))
        self.add_pic.setStyleSheet(u"background-color: rgb(255, 170, 255);\n"
"border: 1px solid rgb(255, 85, 255);\n"
"border-radius: 10px")
        self.form_pic = QLabel(self.widget_4)
        self.form_pic.setObjectName(u"form_pic")
        self.form_pic.setGeometry(QRect(10, 10, 181, 141))
        self.form_pic.setScaledContents(True)
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 10, 141, 31))
        self.label_6.setStyleSheet(u"background-color: rgb(255, 170, 255);\n"
"border: 0px;\n"
"padding: 2px")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0423\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f:", None))
        self.game_check.setText(QCoreApplication.translate("Form", u"\u0418\u0433\u0440\u044b", None))
        self.music_check.setText(QCoreApplication.translate("Form", u"\u041c\u0443\u0437\u044b\u043a\u0430", None))
        self.theatral.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u0430\u0442\u0440\u0430\u043b\u044c\u043d\u043e\u0435 \u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u043e", None))
        self.art_check.setText(QCoreApplication.translate("Form", u"\u0425\u0443\u0434\u043e\u0436\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0435 \u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u043e", None))
        self.animals_check.setText(QCoreApplication.translate("Form", u"\u0416\u0438\u0432\u043e\u0442\u043d\u044b\u0435", None))
        self.garden_check.setText(QCoreApplication.translate("Form", u"\u0421\u0430\u0434\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e", None))
        self.vyazanie_check.setText(QCoreApplication.translate("Form", u"\u0412\u044f\u0437\u0430\u043d\u0438\u0435", None))
        self.spor_check.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u043e\u0440\u0442", None))
        self.language_check.setText(QCoreApplication.translate("Form", u"\u041b\u0438\u043d\u0433\u0432\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.books_check.setText(QCoreApplication.translate("Form", u"\u041a\u043d\u0438\u0433\u0438", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.button_next.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.add_pic.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.form_pic.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
    # retranslateUi

