import  sqlite3

def viewall():
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT id, user,password, date ,sodu, time FROM account")
    rows = cur.fetchall()
    con.close()
    return rows

def search(user = ''):
    con = sqlite3.connect("aledger.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM account WHERE user LIKE '%?%'",(user))
    rows = cur.fetchall()
    con.close()
    print(rows)
    return rows