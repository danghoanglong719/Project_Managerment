from tkinter import *
from tkinter import ttk

window = Tk()
window.title("PM2020")

window.configure(bg="#99CCFF")

lb1 = Label(window, text="Account Management", bg="#6699FF", fg='black',
            font="Oswald 16 bold italic",
            width=70, relief="groove",
            borderwidth=10)
lb1.grid(row=0, column=0, columnspan=5)

frame1 = ttk.Frame(window, borderwidth=5, relief="groove", width=780, height=50)
frame1.grid(row=1, column=0, columnspan=5)

btnAdd = Button(frame1, text="Add", width=20).grid(row=0, column=0)
btnUpd = Button(frame1, text="Update", width=20).grid(row=0, column=1)
btnDel = Button(frame1, text="Delete", width=20).grid(row=0, column=2)
btnSea = Button(frame1, text="Search", width=20).grid(row=0, column=3)
btnVie = Button(frame1, text="View All", width=20,).grid(row=0, column=5)

frame2 = ttk.Frame(window, borderwidth=10, relief="groove", width=780, height=400)
frame2.grid(row=2, column=0, columnspan=5, rowspan=5)

window.mainloop()