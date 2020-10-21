from tkinter import *
from tkinter import ttk
import ledger_bk
import  account

window = Tk()
window.title("PM2020")

#TREEVIEW


#DEFINE FUNC
window.geometry("790x520")
window.configure(bg="#99CCFF")
window.resizable(False,False)

lb1 = Label(window, text="Account Management", bg="#6699FF", fg='black',
            font="Oswald 16 bold italic",
            width=70, relief="groove",
            borderwidth=10)
lb1.grid(row=0, column=0, columnspan=5)

#frame chứa các button
frame1 = ttk.Frame(window, borderwidth=5, relief="groove", width=780, height=50)
frame1.grid(row=1, column=0, columnspan=5)




#frame chứa treeview
frame2 = ttk.Frame(window, borderwidth=5, relief="groove", width=780, height=50)
frame2.grid(row=3, column=0, columnspan=5)

tview = ttk.Treeview(frame2,height =15)
#Define Columns
tview['columns'] = ("Username", "Password", "Date", "Price", "Time")
tview.column("#0", width=40, minwidth=30, anchor=W)
tview.column("Username",  width=138, minwidth=31)
tview.column("Password", width=135, minwidth=31)
tview.column("Date", width=135, minwidth=31)
tview.column("Price", width=135, minwidth=31, anchor=E)
tview.column("Time", width=135, minwidth=31, anchor=CENTER)

tview.heading("#0", text="ID", anchor=W)
tview.heading("Username", text="Username")
tview.heading("Password", text="Password")
tview.heading("Date", text="Date")
tview.heading("Price", text="Price")
tview.heading("Time", text="Time")
tview.grid(row=2, column=0, columnspan=5, rowspan=5, pady=10)



def xoa():
    for i in tview.get_children():
        tview.delete(i)

def view_command():

    for row in account.viewall():
        tview.insert('',END,text= row[0], values = (row[1],row[2],row[3],row[4],row[5]))

view_command()

def search_command():
    xoa()
    i=0
    for row in account.search(user = user.get()):
        tview.insert('',END,values = row)




# các button
btnAdd = Button(frame1, text="Add",font= "Merriweather 12 bold", width=17).grid(row=0, column=0)
btnUpd = Button(frame1, text="Update",font= "Merriweather 12 bold", width=17).grid(row=0, column=1)
btnDel = Button(frame1, text="Delete",font= "Merriweather 12 bold", width=17).grid(row=0, column=2)
btnVie = Button(frame1, text="View All",font= "Merriweather 12 bold", width=17, command=view_command).grid(row=0, column=5)


btnSea = Button(frame2, text="Search",font= "Merriweather 8 bold ", width=13,bg="#8B8386", command=search_command).grid(row=0, column=2)
lbSearch = Label(frame2, text= "Tìm kiếm").grid(row=0,column =0)

user = StringVar()
etSearch = Entry(frame2,textvariable =user, width =40).grid(row=0, column=1)


window.mainloop()