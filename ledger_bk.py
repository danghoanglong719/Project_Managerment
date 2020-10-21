import sqlite3
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

def search(user=""):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account WHERE user=? ", (user,))
    rows = cur.fetchall()
    con.close()
    return rows
def add(user, password, date, balance, time):
    con = sqlite3.connect('aledger.db')
    cur = con.cursor()
    cur.execute("INSERT INTO account VALUES(NULL,?,?,?,?,?)", (user, password, date, balance, time))
    con.commit()
    con.close()
def update(id,name,user,password,category,cdate):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("UPDATE account SET name=?,user=?,password=?,category=?,cdate=? WHERE id=?",(name,user,password,category,cdate,id))
    con.commit()
    con.close()
def delete(id):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("DELETE FROM account WHERE id=?", (id,))
    con.commit()
    con.close()
create()
#print(search(category="social"))
