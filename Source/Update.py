from tkinter import *
import datetime
import ledger_bk
import sqlite3
def update(index):
    root = Toplevel()
    root.title("Update Account")

    def setEntry():
        eUsername.delete(0, END)
        eUsername.insert(0, index[1])
        ePassword.delete(0, END)
        ePassword.insert(0, index[2])
        eBalance.delete(0, END)
        eBalance.insert(0, 0)

    def update_sub():
        finBal = int(index[4]) + balance.get()
        tg = finBal / 5000
        ledger_bk.update(index[0], user.get(), password.get(), finBal, tg)
        root.destroy()
        messagebox.showinfo('Message', 'Success!')


    lb1 = Label(root, text="Update Account ", bg="#6699FF", fg='black',
                font="Oswald 16 bold italic",
                width=30, relief="groove",
                borderwidth=10)
    lb1.grid(row=0, column=0, columnspan=3)
    lbUsername = Label(root, text="Username").grid(row=1, column=0)
    lbPassword = Label(root, text="Password").grid(row=2, column=0)
    lbPrice = Label(root, text="Balance").grid(row=3, column=0)
    lbBalNow = Label(root, text="Now Balance").grid(row=4, column=0)
    lbDate = Label(root, text="Date").grid(row=5, column=0)

    user = StringVar()
    eUsername = Entry(root, width=30, textvariable=user)
    eUsername.grid(row=1, column=1, pady=5)
    password = StringVar()
    ePassword = Entry(root, width=30, textvariable=password)
    ePassword.grid(row=2, column=1, pady=5)
    balance = IntVar()
    eBalance = Entry(root, width=30, textvariable=balance)
    eBalance.grid(row=3, column=1, pady=5)
    lbBalance = Label(root, text=index[4])
    lbBalance.grid(row=4, column=1, pady=5)
    date = StringVar()
    date.set(datetime.date.today())
    lb1date = Label(root, text=date.get()).grid(row=5, column=1, pady=5)

    btnOK = Button(root, width=15,bg="#99CCFF", text="Accept", command=update_sub).grid(row=6, column=0, pady=5)
    btnKO = Button(root, width=15, text="Cancel", command=root.destroy).grid(row=6, column=1, pady=5)
    setEntry()