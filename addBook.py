import tkinter
from tkinter import *
import tkinter.ttk as ttk
import pymysql
from tkinter import messagebox

#will get the information from the user input and place it into the databse if
#it can connect to the database
#if it cant connect then itll present the message
def bookRegister():

    title = bookTitle.get('1.0', END)
    author = bookAuthor.get('1.0', END)
    haveIRead = bookRead.get('1.0', END)
    owned = bookOwned.get('1.0', END)
    price = bookPrice.get('1.0', END)
    #status = status.lower()

    insertBooks = "insert into "+libraryTable+" values ('"+title+"','"+author+"','"+haveIRead+"','"+owned+"','"+price+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")

    root.destroy()

#Main function asks the user what to input for the their library
def addBook():

    global bookTitle ,bookAuthor, bookRead,bookOwned, bookPrice, canvas, con, cur, libraryTable, root

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

    addTitle = Label(root, text="Add books",fg = "white", bg = 'pink',
                    font = ('Courier',110))
    addTitle.grid(row = 0, column = 1)

    addTitle = Label(root, text="Title: ",fg = "white",
                    bg = 'pink',font = ("Times", 70))
    addTitle.grid(row = 2, column = 0)

    bookTitle = Text(root, width = 45, height = 1, font = ('Courier',40))
    bookTitle.grid(row = 2, column = 1)

    addAuthor = Label(root, text="Author: ",fg = "white",
                    bg = 'pink',font = ("Times", 70))
    addAuthor.grid(row = 3, column = 0)

    bookAuthor = Text(root, width = 45, height = 1, font = ('Courier',40))
    bookAuthor.grid(row = 3, column = 1)

    bookRead = Label(root, text="read: ",fg = "white",
                    bg = 'pink',font = ("Times", 70))
    bookRead.grid(row = 4, column = 0)

    bookRead = Text(root, width = 45, height = 1, font = ('Courier',40))
    bookRead.grid(row = 4, column = 1)


    addOwned = Label(root, text="Owned: ",fg = "white",
                    bg = 'pink',font = ("Times", 70))
    addOwned.grid(row = 5, column = 0)

    bookOwned = Text(root, width = 45, height = 1, font = ('Courier',40))
    bookOwned.grid(row = 5, column = 1)

    addPrice = Label(root, text="Price: ",fg = "white",
                    bg = 'pink',font = ("Times", 70))
    addPrice.grid(row = 6, column = 0)

    bookPrice = Text(root, width = 45, height = 1, font = ('Courier',40))
    bookPrice.grid(row = 6, column = 1)

    submitting = Button(root,  width = 15, height = 1, text = "Enter",
                        fg = 'blue violet', command = bookRegister)
    submitting.grid(row = 7, column = 1)

    quitting = Button(root, root,  width = 15, height = 1, text = "Quit",
                      fg = 'blue violet', command = root.destroy)
    quitting.grid(row = 8, column = 1)


    root.mainloop()
