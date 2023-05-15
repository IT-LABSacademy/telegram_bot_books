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
    cur.execute("insert into users values ('{}', {}, '{}')".format(username, telegram_id, phone_number))
    conn.commit()
    

def select_users(telegram_id):
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()
    cur.execute("select * from users where telegram_id={}".format(telegram_id))
    return cur.fetchone()
