from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import ledger_bk
import Create
import Update

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
def del_all():
    for row in tview.get_children():
        tview.delete(row)
def show_data():
    for row in ledger_bk.viewall():
        tview.insert('', 'end', values=row)
def view_command():
    del_all()
    for row in ledger_bk.viewall():
        tview.insert('', 'end', values=row)
def search_command():
    del_all()
    for row in ledger_bk.search(user=user.get()):
        tview.insert('', 'end', values=row)
def add_command():
    Create.create()
    view_command()

def delete_clicked():
    res = messagebox.askquestion('Thông báo', ' bạn có thực sự muốn xóa nó không?')
    if res == 'yes':
        del_command()
    else:
        messagebox.showinfo('Thông báo', 'hủy thao tác')

def del_command():
    item = tview.item(tview.focus(), 'values')
    if(item == ""):
        pass
    else:
        id = item[0]
        ledger_bk.delete(id)
        view_command()
        messagebox.showinfo('Message', 'Delete Success!')

def update_command():
    item = tview.item(tview.focus(), 'values')
    if (item == ""):
        pass
    else:
        Update.update(item)
        view_command()
def Reset_command():
    item = tview.item(tview.focus(), 'values')
    if (item == ""):
        pass
    else:
        id = item[0]
        ledger_bk.reset(id,'1')
        view_command()
        messagebox.showinfo('Message', 'Reset Success!')
def Reset_clicked():
    res = messagebox.askquestion('Thông báo', ' bạn có thực sự muốn reset mật khẩu cho tài khoản này không?')
    if res == 'yes':
        Reset_command()
    else:
        messagebox.showinfo('Thông báo', 'hủy thao tác')

#Buttons
btnAdd = Button(frame1, text="Add", font="Merriweather 12 bold", width=13, command=add_command).grid(row=0, column=0)
btnUpd = Button(frame1, text="Update", font="Merriweather 12 bold", width=13, command=update_command).grid(row=0, column=1)
btnDel = Button(frame1, text="Delete", font="Merriweather 12 bold", width=13, command=delete_clicked).grid(row=0, column=2)
btnVie = Button(frame1, text="View All", font="Merriweather 12 bold", width=13, command=view_command).grid(row=0, column=5)
btnRse = Button(frame1, text="Reset", font="Merriweather 12 bold", width=13, command=Reset_clicked).grid(row=0, column=6)


#Frame chứa treeview
frame2 = ttk.Frame(window, borderwidth=5, relief="groove", width=780, height=50)
frame2.grid(row=2, column=0, columnspan=5, pady=7)


btnSea = Button(frame2, text="Search",font="Merriweather 8 bold ", width=13, bg="#8B8386", command=search_command).grid(row=0, column=2, pady=7)
lbSearch = Label(frame2, text="Username").grid(row=0, column=0, pady=7)

user = StringVar()
etSearch = Entry(frame2, textvariable=user, width=40).grid(row=0, column=1, pady=7)
#TREEVIEW
tview = ttk.Treeview(frame2)
#Define Columns
tview['columns'] = ("ID", "Username", "Password", "Date", "Balance", "Time")
tview.column('#0', width=0, stretch=NO)
tview.column("ID", width=50, minwidth=50, anchor=W)
tview.column("Username",  width=130, minwidth=31)
tview.column("Password", width=130, minwidth=31)
tview.column("Date", width=130, minwidth=31)
tview.column("Balance", width=130, minwidth=31, anchor=W)
tview.column("Time", width=130, minwidth=31, anchor=CENTER)

tview.heading("#0", text="")
tview.heading("ID", text="ID", anchor=W)
tview.heading("Username", text="Username")
tview.heading("Password", text="Password")
tview.heading("Date", text="Date")
tview.heading("Balance", text="Balance")
tview.heading("Time", text="Time")
tview.grid(row=2, column=0, columnspan=5, rowspan=5, ipady=60)

show_data()
window.mainloop()

