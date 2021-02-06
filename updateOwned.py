

#code coped from my own viewbooks.py code
import tkinter
from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk,Image #PIL -> Pillow
#import mysql.connector
import pymysql
from tkinter import messagebox



#table name and setting it into libraryTable
def bookRegister():

    title = bookTitle.get()
    #status = status.lower()

    updateStatus = "update "+libraryTable+" set owned = 'yes' where title = '"+title+"'"

    try:
        cur.execute(updateStatus)
        con.commit()
        messagebox.showinfo('Success',"Book has successfully been updated")
    except:
        messagebox.showinfo("Error","Book does not exist in your databse")

    root.destroy()

def updateOwned():

    global bookTitle, canvas, con, cur, libraryTable, root

    root = Tk()
    root.title("My personal library")
    root.geometry("1920x1080")
    root.configure(bg = 'pink')


    mypass = "##########"
    mydatabase="books"

    con = pymysql.connect( host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    libraryTable = "library" # Book Table

    addTitle = Label(root, text="Now Owned",fg = "white",
                    bg = 'pink',font = ("Times", 110))
    addTitle.grid(row = 0, column = 1)

    addTitle = Label(root, text="Title: ",fg = "white",
            bg = 'pink',font = ("Times", 70))
    addTitle.grid(row = 2, column = 0)

    bookTitle = Text(root, width = 45, height = 1, font = ('Courier',40))
    bookTitle.grid(row = 2, column = 1)

    submitting = Button(root,  width = 25, height = 2,text = "Enter",
                        fg = 'blue violet', command = bookRegister)
    submitting.grid(row = 6, column = 1)

    quitting = Button(root, width = 25, height = 2, text = "Quit",
                      fg = 'blue violet',command = root.destroy)
    quitting.grid(row = 7, column = 1)


    root.mainloop()
