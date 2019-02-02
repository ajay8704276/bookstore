import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE  IF NOT EXISTS book(id INTEGER  PRIMARY KEY  , title text, aurhtor text ,year integer ,isbn integer )")
        self.conn.commit()

    def insertBook(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO book VALUES (NULL , ?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def viewBook(self):
        self.cursor.execute("SELECT * FROM book")
        row = self.cursor.fetchall()
        return row

    def searchBook(self, title="", author="", year="", isbn=""):
        self.cursor.execute("SELECT * FROM book where title=? or aurhtor =? or year =? or isbn =?",
                       (title, author, year, isbn))
        rows = self.cursor.fetchall()
        return rows

    def deleteBook(self, id):
        self.cursor.execute("DELETE FROM book where id=?", (id,))
        self.conn.commit()

    def updateBook(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE book SET title=? , aurhtor =? , year =? , isbn =? where id =?",
                       (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
