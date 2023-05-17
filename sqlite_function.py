import sqlite3


def create_db():
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()


def create_table_users():
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("create table if not exists users ( \
                username varchar(150), \
                telegram_id int, \
                phone_number varchar(20) \
                )")


# Users Table
def insert_users(username, telegram_id, phone_number):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("insert into users values ('{}', {}, '{}')".format(
        username, telegram_id, phone_number))
    conn.commit()


def select_users(telegram_id):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("select * from users where telegram_id={}".format(telegram_id))
    return cur.fetchone()


def create_table_category():
    conn = sqlite3.connect("baza.db")
    cursor = conn.cursor()
    cursor.execute("create table if not exists Categories ( \
                    id INTEGER PRIMARY KEY autoincrement, \
                    name varchar(50) \
                    )")


def create_table_books():
    conn = sqlite3.connect("baza.db")
    cursor = conn.cursor()
    cursor.execute("create table if not exists Books ( \
                    id INTEGER PRIMARY KEY autoincrement, \
                    category_id int, \
                    book_name varchar(50), \
                    book_description text, \
                    book_photo text \
                   )")


def select_category():
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("select * from Categories")
    return cur.fetchall()


def select_by_category_id(category_id):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("select * from Books where category_id={}".format(category_id))
    return cur.fetchall()


def select_by_id_book(id):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("select * from Books where id={}".format(id))
    return cur.fetchone()
