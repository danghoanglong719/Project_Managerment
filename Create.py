from tkinter import *
import hashlib
import datetime
import ledger_bk
import sqlite3
def create():
    root = Toplevel()
    root.title("Create Account")

    def md5pass(var):
        varutf = var.encode("utf-8")
        hash = hashlib.md5(varutf)
        hexa = hash.hexdigest()
        print(hexa)
        return hexa

    def add_sub():
        try:
            tg = balance.get() / 5000
            newpassword = md5pass(password.get())
            ledger_bk.add(user.get(), newpassword, date.get(), balance.get(), tg)
            root.destroy()
            messagebox.showinfo('Message', 'Success!')
        except:
            messagebox.showinfo('Message', 'Username are not available!')


    lb1 = Label(root, text="Create Account ", bg="#6699FF", fg='black',
                font="Oswald 16 bold italic",
                width=30, relief="groove",
                borderwidth=10)
    lb1.grid(row=0, column=0, columnspan=2)
    lbUsername = Label(root, text="Username").grid(row=1, column=0)
    lbPassword = Label(root, text="Password").grid(row=2, column=0)
    lbPrice = Label(root, text="Balance").grid(row=3, column=0)
    lbDate = Label(root, text="Date").grid(row=4, column=0)

    user = StringVar()
    eUsername = Entry(root, width=30, textvariable=user).grid(row=1, column=1, pady=5)
    password = StringVar()
    ePassword = Entry(root, width=30, textvariable=password).grid(row=2, column=1, pady=5)
    balance = IntVar()
    eBalance = Entry(root, width=30, textvariable=balance).grid(row=3, column=1, pady=5)
    date = StringVar()
    date.set(datetime.date.today())
    lb1date = Label(root, text=date.get()).grid(row=4, column=1, pady=5)

    btnOK = Button(root, width=15,bg="#99CCFF", text="Accept", command=add_sub).grid(row=5, column=0, pady=5, padx=25)
    btnKO = Button(root, width=15, text="Cancel", command=root.destroy).grid(row=5, column=1, pady=5)
