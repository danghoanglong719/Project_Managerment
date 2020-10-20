from tkinter import *
import datetime
import sqlite3

root = Tk()
root.title("Create Account")


def add(date, user, password, price, time):
    con = sqlite3.connect('aledger.db')
    cur = con.cursor()
    cur.execute("INSERT INTO account VALUES(NULL,?,?,?,?,?)", (date, user, password, price, time))
    con.commit()
    con.close()


def add_sub():
    tg = price.get() / 5000
    add(date.get(), user.get(), password.get(), price.get(), tg)
    root.quit()


lb1 = Label(root, text="Create Account ", bg="#6699FF", fg='black',
            font="Oswald 16 bold italic",
            width=30, relief="groove",
            borderwidth=10)
lb1.grid(row=0, column=0, columnspan=2)
lbUsername = Label(root, text="UserName:").grid(row=1, column=0)
lbPassword = Label(root, text="PassWord").grid(row=2, column=0)
lbPrice = Label(root, text="Price").grid(row=3, column=0)
lbDate = Label(root, text="Date").grid(row=4, column=0)

user = StringVar()
eUsername = Entry(root, width=30, textvariable=user).grid(row=1, column=1)
password = StringVar()
ePassword = Entry(root, width=30, textvariable=password).grid(row=2, column=1)
price = IntVar()
ePrice = Entry(root, width=30, textvariable=price).grid(row=3, column=1)
date = StringVar()
date.set(datetime.date.today())
lb1date = Label(root, text=date.get()).grid(row=4, column=1)

btnOK = Button(root, width=15, text="Accept", command=add_sub).grid(row=5, column=0)
btnKO = Button(root, width=15, text="Cancel", command=root.quit).grid(row=5, column=1)

root.mainloop()
