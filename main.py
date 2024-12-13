import sqlite3
import os
import shutil
import sys
import database
from ui_main import Ui_MainWindow
from ui_form import Ui_Form
from ui_auth_reg import Ui_Dialog
from PySide6.QtWidgets import (QDialog, QMainWindow, QApplication, QLabel, QFileDialog, QMessageBox, QWidget,
                               QHBoxLayout, QVBoxLayout)
from PySide6.QtGui import QFont, QPixmap
from PIL import Image

class Auth_Reg(QDialog, Ui_Dialog):
    def __init__(self, main, parent=None):
        super(Auth_Reg, self).__init__(parent)
        self.setupUi(self)
        self.main = main
        self.exec()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.setWindowTitle("Авторизация и регистрация")
        self.setWindowIcon(QPixmap("icon.png"))
        self.auth_button.clicked.connect(self.auth)
        self.to_reg_button.clicked.connect(self.go_to_reg)
        self.registr_button.clicked.connect(self.reg)
        self.reg_window.hide()

    def auth(self):
        self.main.username = self.username_input.text()
        username = self.username_input.text()
        user_password = self.password_input.text()

        connection, cursor = database.db_connection()
        existing = cursor.execute(f"SELECT EXISTS(SELECT * FROM Users WHERE username_user = ?)", (username,)).fetchone()[0]
        if existing:
            true_data = cursor.execute(
                f"SELECT id_user, password_user FROM Users WHERE username_user = {username}").fetchone()
            database.db_close(connection)
            if true_data[1] == user_password:
                self.close()
                self.main.show()
            else:
                self.show_error_message("Ошибка", "Неправильное имя пользователя или пароль")

        else:
            self.show_error_message("Ошибка", "Неправильное имя пользователя или пароль")


    def go_to_reg(self):
        self.auth_window.hide()
        self.reg_window.show()
        print(1)

    def reg(self):
        username = self.us_input.text()
        mail = self.mail_input.text()
        phone = self.phone_input.text()
        password = self.passwd_input.text()

        connect, curs = database.db_connection()
        existing = curs.execute(f'''SELECT COUNT(*) FROM Users WHERE mail_user = ?
                                          OR username_user = ?''', (mail, username)).fetchone()[0]
        if existing == 0:

            curs.execute("INSERT INTO Users (username_user, mail_user, phone_num_user, password_user) VALUES (?,?,?,?)",
                         (username, mail, phone, password))
            connect.commit()

            curs.execute("SELECT id_user FROM Users WHERE username_user = ?", (username,))
            user_id = curs.fetchone()[0]

            curs.execute("INSERT INTO Form (id_user_form) VALUES (?)", (user_id,))
            connect.commit()

            curs.execute("INSERT INTO Interes (id_user_interes) VALUES (?)", (user_id,))
            connect.commit()

            database.db_close(connect)
            Form(self, user_id)

        else:
            self.show_error_message("Ошибка","Пользователь с таким именем или почтой уже существует")

    def show_error_message(self, title, message):
        error = QMessageBox()
        error.setWindowTitle(title)
        error.setWindowIcon(QPixmap("warning.jpg"))
        error.setText(message)
        error.setIcon(QMessageBox.Warning)
        error.addButton(error.StandardButton.Ok)
        error.exec_()

class Form(QDialog, Ui_Form):
    def __init__(self, auth, us_id):
        super().__init__()
        self.auth = auth
        self.user_id = us_id
        self.setupUi(self)


    def setupUi(self, Form):
        super().setupUi(Form)
        self.setWindowTitle("Анкета")
        self.setWindowIcon(QPixmap("icon.png"))
        self.button_next.clicked.connect(self.go)
        self.add_pic.clicked.connect(self.add_picture)
        self.exec()

    def go(self):
        name = self.name_input.text()
        surname = self.surname_input.text()
        age = self.age_input.text()
        city = self.city_input.text()
        check_box = [[self.theatral, "theatral"], [self.art_check, "art"], [self.music_check, "music"],
                     [self.game_check, "game"], [self.animals_check, "animal"], [self.garden_check, "garden"],
                     [self.vyazanie_check, "vyazanie"], [self.spor_check, "sport"], [self.language_check, "language"],
                     [self.books_check, "books"]]

        connect, curs = database.db_connection()
        curs.execute("UPDATE Form SET name_form=?, surname_form=?, city_form=?, age_form=?",
                     (name, surname, city, age))
        database.db_close(connect)

        connect, curs = database.db_connection()
        for check in check_box:
            if check[0].isChecked() == True:
                curs.execute(f"UPDATE Interes SET {check[1]}=1 WHERE id_user_interes={self.user_id}")
        database.db_close(connect)

        self.close()
        self.auth.auth_window.show()

    def add_picture(self):

        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "",
                                                   "Images (*.png *.jpg *.jpeg *.bmp *.gif);;All Files (*)")
        if self.is_image(file_name):
            project_directory = os.path.join(os.getcwd(), "users_pic")
            os.makedirs(project_directory, exist_ok=True)
            destination = os.path.join(project_directory, os.path.basename(file_name))

            shutil.copy(file_name, destination)
            QMessageBox.information(self, "Успех", f"Аватар добавлен")
            pixmap = QPixmap(destination)
            print(destination)
            self.form_pic.setPixmap(pixmap)
            connect, curs = database.db_connection()
            curs.execute("UPDATE Form SET pic_destination=? WHERE id_user_form=?", (destination, self.user_id))
            database.db_close(connect)

        else:
            QMessageBox.warning(self, "Ошибка", "Файл не является изображением")



    def is_image(self, file_path):
        try:
            img = Image.open(file_path)
            img.verify()
            return True
        except (IOError, SyntaxError):
            return False


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.user_city = None
        self.username = None
        self.user_id = None
        self.users_sorted = []

        self.auth_window = Auth_Reg(self)
        self.setupUi(self)

    def setupUi(self, window):
        super().setupUi(window)
        self.setWindowTitle("Знакомства")
        self.setWindowIcon(QPixmap("icon.png"))
        self.profile_button.clicked.connect(self.show_profile)
        self.home_button.clicked.connect(self.show_home)
        self.like_button.clicked.connect(self.like)
        self.dis_button.clicked.connect(self.dis)
        self.messanger_button.clicked.connect(self.show_messanger)

        connect, curs = database.db_connection()

        curs.execute(f"SELECT id_user FROM Users WHERE username_user={self.username}")
        self.user_id = curs.fetchone()[0]

        curs.execute(f"SELECT pic_destination FROM Form WHERE id_user_form={self.user_id}")
        path_self_pic = str(curs.fetchone()[0])

        curs.execute(f"SELECT name_form, surname_form, city_form, age_form FROM Form WHERE id_user_form={self.user_id}")
        info = curs.fetchone()

        curs.execute(f"SELECT theatral, art, music, game, animal, garden, vyazanie, sport, language, books FROM Interes "
                     f"WHERE id_user_interes={self.user_id}")
        interes = curs.fetchone()
        database.db_close(connect)

        pixmap = QPixmap(path_self_pic)
        self.prof_pic.setPixmap(pixmap)
        self.label_interes = ["Театральное искусство","Художественное искусство", "Музыка", "Игры",
                         "Животные", "Садоводство", "Вязание", "Спорт", "Лингвистика","Книги"]
        self.user_interes = []
        for i in range(len(self.label_interes)):
            a = [interes[i], self.label_interes[i]]
            self.user_interes.append(a)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        for i in self.user_interes:
            print(i)
            if i[0] == 1:
                interes_label = QLabel()
                interes_label.setFont(font)
                interes_label.setText(str(i[1]))
                interes_label.setMinimumHeight(10)
                interes_label.setStyleSheet(u"background-color: rgb(255, 199, 248);\n border: 0px; \n border-radius: 5px; padding: 1px")
                self.self_interes.addWidget(interes_label)

        self.name_prof.setText(str(info[0]))
        self.surname_prof.setText(str(info[1]))
        self.city_prof.setText(str(info[2]))
        self.age_prof.setText(str(info[3]))

        self.user_city = info[2]

        connect, curs = database.db_connection()
        curs.execute(f"SELECT Users.id_user, Form.city_form FROM Users JOIN Form ON Users.id_user=Form.id_user_form ")
        users_unsorted = curs.fetchall()
        database.db_close(connect)

        self.users_cards = []
        users_city = []
        users_other_city = []
        for user in users_unsorted:
            user = [user[0], user[1], 0]
            if user[0] != self.user_id:
                connect, curs = database.db_connection()
                curs.execute(f"SELECT theatral, art, music, game, animal, garden, vyazanie, sport, language, books "
                             f"FROM Interes WHERE id_user_interes={user[0]}")
                for_check = curs.fetchone()
                database.db_close(connect)

                overlap = 0
                for i in range(len(for_check)):
                    if for_check[i]+self.user_interes[i][0] == 2:
                        overlap+=1
                user[2] = overlap

                if user[1] == self.user_city:
                    users_city.append(user)
                else:
                    users_other_city.append(user)

        users_city = sorted(users_city, key=lambda x: x[2])
        users_city.reverse()
        users_other_city = sorted(users_other_city, key=lambda y: y[2])
        users_other_city.reverse()
        self.users_cards = users_city+users_other_city
        print(self.users_cards)

        self.show_likes()
        self.next_user()

    def show_home(self):
        self.main.show()
        self.messanger.hide()
        self.profile.hide()

    def show_messanger(self):
        self.main.hide()
        self.messanger.show()
        self.profile.hide()
    def show_profile(self):
        self.main.hide()
        self.messanger.hide()
        self.profile.show()

    def next_user(self):
        self.now_showing_user = self.users_cards[0][0]
        user = self.users_cards[0]
        print(user)
        self.users_cards.pop(0)

        connect, curs = database.db_connection()
        curs.execute(f"SELECT name_form, age_form, pic_destination FROM Form WHERE id_user_form = {user[0]}")
        info = list(curs.fetchall()[0])
        user += info

        curs.execute("SELECT theatral, art, music, game, animal, garden, vyazanie, sport, language, books "
                             f"FROM Interes WHERE id_user_interes={user[0]}")
        user_interes = list(curs.fetchone())
        print(user_interes)
        database.db_close(connect)

        self.name.setText(str(user[3]))
        self.age.setText(str(user[4]))
        self.city.setText(str(user[1]))
        pixmap = QPixmap(str(user[5]))
        self.photo.setPixmap(pixmap)

        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.labels = [self.label_0, self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6,
                       self.label_7, self.label_8, self.label_9]
        labels = self.labels
        j = 0
        for i in range(len(self.label_interes)):
            if user_interes[i] == 1:
                labels[j].setText(self.label_interes[i])
                j+=1
            else:
                labels = labels[:-1]

                print(labels)

    def like(self):
        for i in self.labels:
            i.setText("")

        connection, cursor = database.db_connection()
        cursor.execute("INSERT INTO Likes(id_user_from, id_user_too, id_from_status, id_too_status)"
                       "VALUES (?,?,?,?)", (self.now_showing_user, self.user_id, 1, 0))
        database.db_close(connection)
        self.next_user()

    def dis(self):
        for i in self.labels:
            i.setText("")
        self.next_user()

    def show_likes(self):
        connection, cursor = database.db_connection()
        cursor.execute(
            f"SELECT id_user_from, id_from_status, id_too_status FROM Likes WHERE id_user_too = {self.user_id}")
        users_likes = cursor.fetchall()
        database.db_close(connection)

        font = QFont()
        font.setPointSize(12)

        css = u"background-color: rgb(255, 207, 251);\n border-radius: 10px; \n border: 0px; \n color: black;\n padding: 1px"
        for user in users_likes:
            connection, cursor = database.db_connection()
            if user[2] == 0:
                cursor.execute(
                    f"SELECT Form.name_form, Form.city_form, Form.age_form, Form.pic_destination, Users.phone_num_user,"
                    f"Users.mail_user FROM Form JOIN Users ON Users.id_user = Form.id_user_form WHERE Form.id_user_form = {user[0]}")
                user_info = cursor.fetchone()
                database.db_close(connection)
                print(user_info)

                self.user_widget = QWidget()
                self.user_widget.setMaximumHeight(150)
                self.user_widget.setStyleSheet(u"background-color: transparent;\nborder: 0px;")
                self.buttons_widget = QWidget()
                self.user_layout = QHBoxLayout()
                self.buttons_layout = QVBoxLayout()
                self.likes_layout = QVBoxLayout()
                self.name = QLabel()
                self.city = QLabel()
                self.age = QLabel()
                self.pic = QLabel()
                self.phone = QLabel()
                self.mail = QLabel()

                self.name.setText(f"Имя: {user_info[0]}")
                self.name.setStyleSheet(css)
                self.name.setFont(font)
                self.name.setMaximumHeight(30)
                self.city.setText(f"Город: {user_info[1]}")
                self.city.setStyleSheet(css)
                self.city.setFont(font)
                self.city.setMaximumHeight(30)
                self.age.setText(f"Возраст: {user_info[2]}")
                self.age.setStyleSheet(css)
                self.age.setFont(font)
                self.age.setMaximumHeight(30)
                self.pic.setMaximumHeight(100)
                self.pic.setMaximumWidth(100)
                self.pic.setPixmap(QPixmap(user_info[3]))
                self.pic.setStyleSheet(css)
                self.pic.setScaledContents(True)

                self.phone.setText(f"Номер: {user_info[4]}")
                self.phone.setFont(font)
                self.phone.setStyleSheet(css)
                self.like_button.setStyleSheet(css)

                self.mail.setText(f"Почта: {user_info[5]}")
                self.mail.setFont(font)
                self.mail.setStyleSheet(css)

                self.buttons_layout.addWidget(self.phone)
                self.buttons_layout.addWidget(self.mail)
                self.buttons_widget.setLayout(self.buttons_layout)

                self.user_layout.addWidget(self.name)
                self.user_layout.addWidget(self.city)
                self.user_layout.addWidget(self.age)
                self.user_layout.addWidget(self.pic)
                self.user_layout.addWidget(self.buttons_widget)

                self.user_widget.setLayout(self.user_layout)
                self.likes_layout.addWidget(self.user_widget)
                self.chats.setLayout(self.likes_layout)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    MainWindow()
    sys.exit(app.exec())
