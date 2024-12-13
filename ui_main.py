# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(572, 700)
        MainWindow.setMinimumSize(QSize(572, 650))
        MainWindow.setMaximumSize(QSize(572, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 207, 251)\n"
"")
        self.all_windows = QStackedWidget(self.centralwidget)
        self.all_windows.setObjectName(u"all_windows")
        self.all_windows.setGeometry(QRect(0, 0, 571, 581))
        self.all_windows.setStyleSheet(u"background-color: rgb(255, 207, 251);\n"
"border-radius: 10px")
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"")
        self.show_users = QWidget(self.main)
        self.show_users.setObjectName(u"show_users")
        self.show_users.setGeometry(QRect(10, 10, 551, 571))
        self.show_users.setStyleSheet(u"border-radius: 50px;\n"
"border: 1px solid rgb(143, 143, 143);\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(243, 159, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.user_for_you = QWidget(self.show_users)
        self.user_for_you.setObjectName(u"user_for_you")
        self.user_for_you.setGeometry(QRect(70, 20, 411, 471))
        self.user_for_you.setStyleSheet(u"background-color: rgb(255, 196, 255);\n"
"border: 1px solid rgb(143, 143, 143);\n"
"border-radius:  30px")
        self.photo = QLabel(self.user_for_you)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(100, 10, 211, 241))
        self.photo.setStyleSheet(u"border: 0px")
        self.photo.setScaledContents(True)
        self.name = QLabel(self.user_for_you)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(20, 260, 101, 21))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.name.setFont(font)
        self.name.setStyleSheet(u"border: 0px")
        self.horizontalWidget_2 = QWidget(self.user_for_you)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setGeometry(QRect(10, 290, 401, 41))
        self.horizontalWidget_2.setStyleSheet(u"border: 0px")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_age = QLabel(self.horizontalWidget_2)
        self.label_age.setObjectName(u"label_age")
        self.label_age.setFont(font)
        self.label_age.setStyleSheet(u"word-break: break-all;\n"
"border: 0px")
        self.label_age.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_age.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label_age)

        self.age = QLabel(self.horizontalWidget_2)
        self.age.setObjectName(u"age")
        self.age.setFont(font)
        self.age.setStyleSheet(u"word-break: break-all;\n"
"border: 0px")
        self.age.setTextFormat(Qt.TextFormat.MarkdownText)
        self.age.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.age)

        self.label_city = QLabel(self.horizontalWidget_2)
        self.label_city.setObjectName(u"label_city")
        self.label_city.setFont(font)
        self.label_city.setStyleSheet(u"word-break: break-all;\n"
"border: 0px")
        self.label_city.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_city.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label_city)

        self.city = QLabel(self.horizontalWidget_2)
        self.city.setObjectName(u"city")
        self.city.setFont(font)
        self.city.setStyleSheet(u"word-break: break-all;\n"
"border: 0px")
        self.city.setTextFormat(Qt.TextFormat.MarkdownText)
        self.city.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.city)

        self.gridWidget = QWidget(self.user_for_you)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridWidget.setGeometry(QRect(10, 350, 391, 111))
        self.gridWidget.setStyleSheet(u"border: 0px")
        self.gridLayout = QGridLayout(self.gridWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_0 = QLabel(self.gridWidget)
        self.label_0.setObjectName(u"label_0")
        font1 = QFont()
        font1.setBold(True)
        self.label_0.setFont(font1)
        self.label_0.setStyleSheet(u"border: 0px")

        self.gridLayout.addWidget(self.label_0, 0, 1, 1, 1)

        self.label_4 = QLabel(self.gridWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border: 0px")

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.label_interes_card = QLabel(self.gridWidget)
        self.label_interes_card.setObjectName(u"label_interes_card")
        self.label_interes_card.setFont(font1)
        self.label_interes_card.setStyleSheet(u"border: 0px")

        self.gridLayout.addWidget(self.label_interes_card, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border: 0px")

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)

        self.label_1 = QLabel(self.gridWidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"border: 0px")

        self.gridLayout.addWidget(self.label_1, 1, 1, 1, 1)

        self.label_5 = QLabel(self.gridWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border: 0px")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_6 = QLabel(self.gridWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"border: 0px")

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.label_7 = QLabel(self.gridWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"border: 0px")

        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)

        self.label_8 = QLabel(self.gridWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"border: 0px")

        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)

        self.label_9 = QLabel(self.gridWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"border: 0px")

        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)

        self.label_2 = QLabel(self.gridWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border: 0px")

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.like_button = QPushButton(self.show_users)
        self.like_button.setObjectName(u"like_button")
        self.like_button.setGeometry(QRect(120, 500, 61, 51))
        self.like_button.setStyleSheet(u"border: 0px;\n"
"border-radius: 20px;\n"
"")
        icon = QIcon()
        icon.addFile(u"heart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.like_button.setIcon(icon)
        self.like_button.setIconSize(QSize(50, 50))
        self.dis_button = QPushButton(self.show_users)
        self.dis_button.setObjectName(u"dis_button")
        self.dis_button.setGeometry(QRect(370, 500, 61, 51))
        self.dis_button.setStyleSheet(u"border: 0px;\n"
"border-radius: 20px;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"dislike.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dis_button.setIcon(icon1)
        self.dis_button.setIconSize(QSize(50, 50))
        self.all_windows.addWidget(self.main)
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.user_profile = QWidget(self.profile)
        self.user_profile.setObjectName(u"user_profile")
        self.user_profile.setGeometry(QRect(10, 20, 551, 471))
        self.user_profile.setStyleSheet(u"border-radius: 50px;\n"
"border: 1px solid rgb(143, 143, 143);\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(243, 159, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.prof_pic = QLabel(self.user_profile)
        self.prof_pic.setObjectName(u"prof_pic")
        self.prof_pic.setGeometry(QRect(20, 20, 151, 151))
        self.prof_pic.setStyleSheet(u"background-color: transparent;\n"
"border-radius: 0;\n"
"border: 0px\n"
"\n"
"")
        self.prof_pic.setScaledContents(True)
        self.label_intres = QLabel(self.user_profile)
        self.label_intres.setObjectName(u"label_intres")
        self.label_intres.setGeometry(QRect(20, 200, 101, 38))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_intres.setFont(font2)
        self.label_intres.setStyleSheet(u"color: black;\n"
"background-color: transparent;\n"
"border: 0px")
        self.pushButton = QPushButton(self.user_profile)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 380, 151, 61))
        font3 = QFont()
        font3.setPointSize(12)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 197, 250);\n"
"border: 0px;\n"
"border-radius: 20px;\n"
"color: rgb(0, 0, 0)")
        self.widget = QWidget(self.user_profile)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(180, 20, 361, 171))
        self.widget.setStyleSheet(u"background-color: transparent;\n"
"border-radius: 20px;\n"
"border: 0px")
        self.formLayoutWidget = QWidget(self.widget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 341, 140))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.name_label = QLabel(self.formLayoutWidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setMinimumSize(QSize(0, 30))
        self.name_label.setFont(font2)
        self.name_label.setStyleSheet(u"color: black;\n"
"background-color: transparent;\n"
"border: 0px")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.name_label)

        self.surname_label = QLabel(self.formLayoutWidget)
        self.surname_label.setObjectName(u"surname_label")
        self.surname_label.setMinimumSize(QSize(0, 30))
        self.surname_label.setFont(font2)
        self.surname_label.setStyleSheet(u"color: black;\n"
"background-color: transparent;\n"
"border: 0px")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.surname_label)

        self.city_label_prof = QLabel(self.formLayoutWidget)
        self.city_label_prof.setObjectName(u"city_label_prof")
        self.city_label_prof.setMinimumSize(QSize(0, 30))
        self.city_label_prof.setFont(font2)
        self.city_label_prof.setStyleSheet(u"color: black;\n"
"background-color: transparent;\n"
"border: 0px")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.city_label_prof)

        self.label_age_prof = QLabel(self.formLayoutWidget)
        self.label_age_prof.setObjectName(u"label_age_prof")
        self.label_age_prof.setMinimumSize(QSize(0, 30))
        self.label_age_prof.setFont(font2)
        self.label_age_prof.setStyleSheet(u"color: black;\n"
"background-color: transparent;\n"
"border: 0px")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_age_prof)

        self.name_prof = QLabel(self.formLayoutWidget)
        self.name_prof.setObjectName(u"name_prof")
        self.name_prof.setFont(font2)
        self.name_prof.setStyleSheet(u"color: black;\n"
"background-color: transparent;\n"
"border: 0px")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name_prof)

        self.surname_prof = QLabel(self.formLayoutWidget)
        self.surname_prof.setObjectName(u"surname_prof")
        self.surname_prof.setFont(font2)
        self.surname_prof.setStyleSheet(u"color: black;\n"
"background-color: transparent;\n"
"border: 0px")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.surname_prof)

        self.city_prof = QLabel(self.formLayoutWidget)
        self.city_prof.setObjectName(u"city_prof")
        self.city_prof.setFont(font2)
        self.city_prof.setStyleSheet(u"color: black;\n"
"background-color: transparent;\n"
"border: 0px")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.city_prof)

        self.age_prof = QLabel(self.formLayoutWidget)
        self.age_prof.setObjectName(u"age_prof")
        self.age_prof.setFont(font2)
        self.age_prof.setStyleSheet(u"color: black;\n"
"background-color: transparent;\n"
"border: 0px")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.age_prof)

        self.widget_2 = QWidget(self.user_profile)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(130, 190, 251, 271))
        self.widget_2.setStyleSheet(u"border: 0px;\n"
"background-color: transparent")
        self.verticalLayoutWidget = QWidget(self.widget_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 231, 231))
        self.self_interes = QVBoxLayout(self.verticalLayoutWidget)
        self.self_interes.setObjectName(u"self_interes")
        self.self_interes.setContentsMargins(0, 0, 0, 0)
        self.all_windows.addWidget(self.profile)
        self.messanger = QWidget()
        self.messanger.setObjectName(u"messanger")
        self.chats = QWidget(self.messanger)
        self.chats.setObjectName(u"chats")
        self.chats.setGeometry(QRect(10, 20, 581, 471))
        self.chats.setStyleSheet(u"border-radius: 50px;\n"
"border: 1px solid rgb(143, 143, 143);\n"
"background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(243, 159, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.all_windows.addWidget(self.messanger)
        self.navigation = QWidget(self.centralwidget)
        self.navigation.setObjectName(u"navigation")
        self.navigation.setGeometry(QRect(10, 600, 551, 41))
        self.navigation.setStyleSheet(u"background-color: rgb(255, 170, 255);\n"
"border-radius: 1em;\n"
"background-color: qlineargradient(spread:repeat, x1:0.5, y1:0, x2:0.480556, y2:1, stop:0.305556 rgba(247, 189, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border: 1px solid rgb(143, 143, 143);")
        self.horizontalLayoutWidget = QWidget(self.navigation)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 551, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_button = QPushButton(self.horizontalLayoutWidget)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setMaximumSize(QSize(100, 39))
        self.home_button.setStyleSheet(u"background-color: rgb(255, 196, 255);\n"
"border: 1px solid rgb(255, 255, 255)")
        icon2 = QIcon(QIcon.fromTheme(u"go-home"))
        self.home_button.setIcon(icon2)
        self.home_button.setIconSize(QSize(31, 31))

        self.horizontalLayout.addWidget(self.home_button)

        self.messanger_button = QPushButton(self.horizontalLayoutWidget)
        self.messanger_button.setObjectName(u"messanger_button")
        self.messanger_button.setMaximumSize(QSize(100, 39))
        self.messanger_button.setStyleSheet(u"background-color: rgb(255, 196, 255);\n"
"border: 1px solid rgb(255, 255, 255)")
        icon3 = QIcon(QIcon.fromTheme(u"emblem-mail"))
        self.messanger_button.setIcon(icon3)
        self.messanger_button.setIconSize(QSize(31, 31))

        self.horizontalLayout.addWidget(self.messanger_button)

        self.profile_button = QPushButton(self.horizontalLayoutWidget)
        self.profile_button.setObjectName(u"profile_button")
        self.profile_button.setMaximumSize(QSize(100, 39))
        self.profile_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.profile_button.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.profile_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.profile_button.setAutoFillBackground(False)
        self.profile_button.setStyleSheet(u"background-color: rgb(255, 196, 255);\n"
"border: 1px solid rgb(255, 255, 255)")
        icon4 = QIcon(QIcon.fromTheme(u"address-book-new"))
        self.profile_button.setIcon(icon4)
        self.profile_button.setIconSize(QSize(31, 31))
        self.profile_button.setFlat(True)

        self.horizontalLayout.addWidget(self.profile_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 572, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.like_button.clicked.connect(self.widget.repaint)

        self.all_windows.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.photo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_age.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.age.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.label_city.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.city.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.label_0.setText("")
        self.label_4.setText("")
        self.label_interes_card.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.label_3.setText("")
        self.label_1.setText("")
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_2.setText("")
        self.like_button.setText("")
        self.dis_button.setText("")
        self.prof_pic.setText("")
        self.label_intres.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u043b\u0435\u0447\u0435\u043d\u0438\u044f:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.surname_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f:", None))
        self.city_label_prof.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434:", None))
        self.label_age_prof.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442:", None))
        self.name_prof.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.surname_prof.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.city_prof.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.age_prof.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.home_button.setText("")
        self.messanger_button.setText("")
        self.profile_button.setText("")
    # retranslateUi

