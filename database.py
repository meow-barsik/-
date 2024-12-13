import sqlite3


def db_connection():
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    return connection, cursor


def db_close(conn):
    conn.commit()
    conn.close()


connect, curs = db_connection()
curs.execute('''CREATE TABLE IF NOT EXISTS Users (
             id_user INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             username_user VARCHAR(255),
             mail_user VARCHAR(255),
             phone_num_user VARCHAR(255),
             password_user VARCHAR(255))''')

curs.execute('''CREATE TABLE IF NOT EXISTS Form (
             id_form INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             id_user_form INTEGER NOT NULL,
             name_form VARCHAR(255) DEFAULT 0,
             surname_form VARCHAR(255) DEFAULT 0,
             city_form VARCHAR(255) DEFAULT 0,
             age_form INTEGER DEFAULT 0,
             pic_destination VARCHAR(255) DEFAULT 0)''')

curs.execute('''CREATE TABLE IF NOT EXISTS Interes (
             id_interes INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             id_user_interes INTEGER NOT NULL,
             theatral TINYINT(1) DEFAULT 0,
             art TINYINT(1) DEFAULT 0,
             music TINYINT(1) DEFAULT 0,
             game TINYINT(1) DEFAULT 0 ,
             animal TINYINT(1) DEFAULT 0,
             garden TINYINT(1) DEFAULT 0,
             vyazanie TINYINT(1) DEFAULT 0,
             sport TINYINT(1) DEFAULT 0,
             language TINYINT(1) DEFAULT 0,
             books TINYINT(1) DEFAULT 0)''')

curs.execute('''CREATE TABLE IF NOT EXISTS Likes (
                id_like INTEGER PRIMARY KEY,
                id_user_from INTEGER,
                id_user_too INTEGER,
                id_from_status INTEGER,
                id_too_status INTEGER)''')

connect.commit()
db_close(connect)
