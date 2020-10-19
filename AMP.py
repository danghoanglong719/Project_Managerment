from tkinter import *
from tkinter import ttk
import ledger_bk

window = Tk()
window.title("PM2020")

#TREEVIEW
tview = ttk.Treeview(window)
#Define Columns
tview['columns'] = ("Username", "Password", "Date", "Price", "Time")
tview.column("#0", width=50, minwidth=50, anchor=W)
tview.column("Username", width=125, minwidth=30)
tview.column("Password", width=125, minwidth=30)
tview.column("Date", width=125, minwidth=30)
tview.column("Price", width=125, minwidth=30, anchor=W)
tview.column("Time", width=125, minwidth=30, anchor=CENTER)

tview.heading("#0", text="ID", anchor=W)
tview.heading("Username", text="Username")
tview.heading("Password", text="Password")
tview.heading("Date", text="Date")
tview.heading("Price", text="Price")
tview.heading("Time", text="Time")
tview.grid(row=2, column=0, columnspan=5, rowspan=5, pady=10)

tview.insert(parent='', index='end', iid=0, text="0001",
             values=("Loc", "123456", "010101", 10000, "23"))
tview.insert(parent='', index='end', iid=1, text="0002",
             values=("Loc", "123456", "010102", 10000, "23"))
tview.insert(parent='', index='end', iid=2, text="0003",
             values=("Loc", "123456", "010103", 10000, "23"))

#DEFINE FUNC

window.configure(bg="#99CCFF")

lb1 = Label(window, text="Account Management", bg="#6699FF", fg='black',
            font="Oswald 16 bold italic",
            width=70, relief="groove",
            borderwidth=10)
lb1.grid(row=0, column=0, columnspan=5)

frame1 = ttk.Frame(window, borderwidth=5, relief="groove", width=780, height=50)
frame1.grid(row=1, column=0, columnspan=5)
def view_command():
    tview.delete(0, END)
    for row in ledger_bk.viewall():
        tview.insert(END, row)
btnAdd = Button(frame1, text="Add", width=20).grid(row=0, column=0)
btnUpd = Button(frame1, text="Update", width=20).grid(row=0, column=1)
btnDel = Button(frame1, text="Delete", width=20).grid(row=0, column=2)
btnSea = Button(frame1, text="Search", width=20).grid(row=0, column=3)
btnVie = Button(frame1, text="View All", width=20, command=view_command).grid(row=0, column=5)

#frame2 = ttk.Frame(window, borderwidth=10, relief="groove", width=780, height=400)
#frame2.grid(row=2, column=0, columnspan=5, rowspan=5)
#tview.pack()
window.mainloop()