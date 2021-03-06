import sqlite3
from tkinter import messagebox
import hashlib
def create():
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS account(id INTEGER PRIMARY KEY, user TEXT, password TEXT, date TEXT, balance TEXT, time TEXT)")
    con.commit()
    con.close()
def viewall():
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account ORDER BY id DESC")
    rows = cur.fetchall()
    con.close()
    return rows

def search(user):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account WHERE user like ? ", ('%'+user+'%',))
    rows = cur.fetchall()
    con.close()
    return rows
def add(user, password, date, balance, time):
        con = sqlite3.connect('aledger.db')
        cur = con.cursor()
        cur.execute("INSERT INTO account VALUES(NULL,?,?,?,?,?)", (user, password, date, balance, time))
        con.commit()
        con.close()
def update(id, user, password, balance, time):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("UPDATE account SET user=?,password=?, balance=?, time=? WHERE id=?",(user, password, balance, time, id))
    con.commit()
    con.close()
def delete(id):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("DELETE FROM account WHERE id=?", (id,))
    con.commit()
    con.close()


def md5pass(var):
    varutf = var.encode("utf-8")
    hash = hashlib.md5(varutf)
    hexa = hash.hexdigest()
    print (hexa)
    return hexa

def reset(id, password):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    newpass = md5pass(password)
    cur.execute("UPDATE account SET password=? WHERE id=?",(newpass,id))
    con.commit()
    con.close()

create()
#print(search(category="social"))
