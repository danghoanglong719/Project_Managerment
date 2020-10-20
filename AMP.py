from tkinter import *
from tkinter import ttk
import ledger_bk

window = Tk()
window.title("PM2020")
window.geometry("800x520")
window.configure(bg="#99CCFF")
window.resizable(False, False)

lb1 = Label(window, text="Account Management", bg="#6699FF", fg='black',
            font="Oswald 16 bold italic",
            width=60, relief="groove",
            borderwidth=10)
lb1.grid(row=0, column=0, columnspan=5)

#frame chứa các button
frame1 = ttk.Frame(window, borderwidth=5, relief="groove", width=780, height=50)
frame1.grid(row=1, column=0, columnspan=5, pady=7, padx=20)

#DEFINE FUNC
def show_data():
    for row in ledger_bk.viewall():
        tview.insert('', 'end', values=row)
def view_command():
    for row in tview.get_children():
        tview.delete(row)
    for row in ledger_bk.viewall():
        tview.insert('', 'end', values=row)

#Buttons
btnAdd = Button(frame1, text="Add", font="Merriweather 12 bold", width=13).grid(row=0, column=0)
btnUpd = Button(frame1, text="Update", font="Merriweather 12 bold", width=13).grid(row=0, column=1)
btnDel = Button(frame1, text="Delete", font="Merriweather 12 bold", width=13).grid(row=0, column=2)
btnSea = Button(frame1, text="Search", font="Merriweather 12 bold", width=13).grid(row=0, column=3)
btnVie = Button(frame1, text="View All", font="Merriweather 12 bold", width=13, command=view_command).grid(row=0, column=5)

#TREEVIEW
frame2 = ttk.Frame(window, borderwidth=5, relief="groove", width=780, height=50)
frame2.grid(row=2, column=0, columnspan=5, pady=7)

tview = ttk.Treeview(frame2)
#Define Columns
tview['columns'] = ("ID", "Username", "Password", "Date", "Price", "Time")
tview.column('#0', width=0, stretch=NO)
tview.column("ID", width=50, minwidth=50, anchor=W)
tview.column("Username",  width=130, minwidth=31)
tview.column("Password", width=130, minwidth=31)
tview.column("Date", width=130, minwidth=31)
tview.column("Price", width=130, minwidth=31, anchor=W)
tview.column("Time", width=130, minwidth=31, anchor=CENTER)

tview.heading("#0", text="")
tview.heading("ID", text="ID", anchor=W)
tview.heading("Username", text="Username")
tview.heading("Password", text="Password")
tview.heading("Date", text="Date")
tview.heading("Price", text="Price")
tview.heading("Time", text="Time")
tview.grid(row=2, column=0, columnspan=5, rowspan=5, ipady=60)


show_data()
window.mainloop()