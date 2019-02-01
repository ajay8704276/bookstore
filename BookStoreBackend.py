import sqlite3


def connectDB():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE  IF NOT EXISTS book(id INTEGER  PRIMARY KEY  , title text, aurhtor text ,year integer ,isbn integer )")
    conn.commit()
    conn.close()


def insertBook(title, author, year, isbn):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO book VALUES (NULL , ?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def viewBook():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book")
    row = cursor.fetchall()
    conn.close()
    return row


def searchBook(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book where title=? or aurhtor =? or year =? or isbn =?",
                   (title, author, year, isbn))
    rows = cursor.fetchall()
    conn.close()
    return rows


def deleteBook(id):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book where id=?", (id,))
    conn.commit()
    conn.close()


def updateBook(id, title, author, year, isbn):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE book SET title=? , aurhtor =? , year =? , isbn =? where id =?",
                   (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connectDB()
