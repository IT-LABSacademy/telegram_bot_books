import sqlite3

class Database:
    conn = sqlite3.connect("baza.db")
    cur = conn.cursor()

    def create_table_users(self):
        self.cur.execute("create table if not exists users ( \
                    username varchar(150), \
                    telegram_id int, \
                    phone_number varchar(20) \
                    )")
        
    def create_table_category(self):
        self.cur.execute("create table if not exists Categories ( \
                        id INTEGER PRIMARY KEY autoincrement, \
                        name varchar(50) \
                        )")
    
    def create_table_books(self):
        self.cur.execute("create table if not exists Books ( \
                        id INTEGER PRIMARY KEY autoincrement, \
                        category_id int, \
                        book_name varchar(50), \
                        book_description text, \
                        book_photo text \
                    )")
        
    def select_users(self, telegram_id):
        self.cur.execute("select * from users where telegram_id={}".format(telegram_id))
        return self.cur.fetchone()

    
    
    def select_category(self):
        self.cur.execute("select * from Categories")
        return self.cur.fetchall()
    
    def insert_users(self, username, telegram_id, phone_number):
        self.cur.execute("insert into users values ('{}', {}, '{}')".format(
            username, telegram_id, phone_number))
        self.conn.commit()

    def select_by_id_book(self, id):
        self.cur.execute("select * from Books where id={}".format(id))
        return self.cur.fetchone()
    
    
    def select_by_category_id(self, category_id):
        self.cur.execute("select * from Books where category_id={}".format(category_id))
        return self.cur.fetchall()



