#code coped from my own viewReadBooks.py code
import tkinter
from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
#from tkinter import messagebox

con = pymysql.connect(host = "localhost", user = "root", passwd = "##########", database = "books")
cur = con.cursor()

#table name and setting it into libraryTable
libraryTable = "library"

def sortByTitle():
    try:
        cur.execute("SELECT title, author, haveIRead, owned, price FROM library WHERE haveIRead = 'no' ORDER BY title")
        #result = cur.fetchall()
        i = 4
        for library in cur:
            for j in range(len(library)):
                populate = Label(root, width = 20, text = library[j],
                                borderwidth=2,relief='ridge', anchor="w",
                                bg = 'pink', fg = 'ghost white',
                                font = ('Courier', 18))
                populate.grid(row = i, column = j)
                #populate.insert(END, library[j])
            i=i+1
    except:
        messagebox.showinfo("Failed to open database")

def sortByAuthor():
    try:
        cur.execute("SELECT title, author, haveIRead,owned, price FROM library WHERE haveIRead = 'no' ORDER BY author")
        #result = cur.fetchall()
        i = 4
        for library in cur:
            for j in range(len(library)):
                populate = Label(root, width = 20, text = library[j],
                                borderwidth=2,relief='ridge', anchor="w",
                                bg = 'pink', fg = 'ghost white',
                                font = ('Courier', 18))
                populate.grid(row = i, column = j)
                #populate.insert(END, library[j])
            i=i+1
    except:
        messagebox.showinfo("Failed to open database")

def sortByOwned():
    try:
        cur.execute("SELECT title, author, haveIRead,owned, price FROM library WHERE haveIRead = 'no' AND owned = 'yes' ORDER BY title")
        #result = cur.fetchall()
        i = 4
        for library in cur:
            for j in range(len(library)):
                populate = Label(root, width = 20, text = library[j],
                                borderwidth=2,relief='ridge', anchor="w",
                                bg = 'pink', fg = 'ghost white',
                                font = ('Courier', 18))
                populate.grid(row = i, column = j)
                #populate.insert(END, library[j])
            i=i+1
    except:
        messagebox.showinfo("Failed to open database")

def sortByNotOwned():
    try:
        cur.execute("SELECT title, author, haveIRead,owned, price FROM library WHERE haveIRead = 'no' AND owned = 'no' ORDER BY title")
        #result = cur.fetchall()
        i = 4
        for library in cur:
            for j in range(len(library)):
                populate = Label(root, width = 20, text = library[j],
                                borderwidth=2,relief='ridge', anchor="w",
                                bg = 'pink', fg = 'ghost white',
                                font = ('Courier', 18))
                populate.grid(row = i, column = j)
                #populate.insert(END, library[j])
            i=i+1
    except:
        messagebox.showinfo("Failed to open database")

def viewNotReadBooks():
    #setting up global variables in order to use them in other functions
    global root
    #setting the window up
    root = tkinter.Tk()
    root.title("Viweing My Personal library")
    root.geometry("1920x1080")
    root.configure(bg = 'pink')

    #setting up the headers and describing what information will be populated
    viewTitle = Label(root, text = 'Books You Have Not Read',  fg = "white",
                        bg = 'pink',font = ('Courier', 40))
    viewTitle.grid(row = 0, column = 1)

    titleBtn = Button(root, width = 20, height = 1, text = "Sort by Title",
                        fg = 'blue violet', font = ('Courier',13),
                        command = sortByTitle)
    titleBtn.grid(row = 1, column = 0)

    authorBtn = Button(root, width = 20, height = 1, text = "Sort by Author",
                        fg = 'blue violet',font = ('Courier',13),
                        command = sortByAuthor)
    authorBtn.grid(row = 1, column = 2)

    ownedBtn = Button(root, width = 20, height = 1, text = "Sort by owned",
                        fg = 'blue violet', font = ('Courier',13),
                        command = sortByOwned)
    ownedBtn.grid(row = 1, column = 3)

    notOwnedBtn = Button(root, width = 20, height = 1, text = "Sort by not owned",
                        fg = 'blue violet',font = ('Courier',13),
                        command = sortByNotOwned)
    notOwnedBtn.grid(row = 1, column = 4)

    quit = Button(root, width = 20, height = 1, text = "Quit",
                        fg = 'blue violet',font = ('Courier',13),
                        command = root.destroy)
    quit.grid(row = 2, column = 0)

    titlePlace = Label(root, width = 10, text = 'Title: ', anchor="w", bg = 'pink',
                        fg = "white", font = ('Courier', 25))
    titlePlace.grid(row = 3, column = 0)

    authorPlace = Label(root, width = 10, text = 'Author: ', anchor="w", bg = 'pink',
                        fg = "white", font = ('Courier', 25))
    authorPlace.grid(row = 3, column = 1)

    readPlace = Label(root, width = 10, text = 'Read: ', anchor="w", bg = 'pink',
                        fg = "white", font = ('Courier', 25))
    readPlace.grid(row = 3, column = 2)

    ownedPlace = Label(root, width = 10, text = 'Owned: ', anchor="w", bg = 'pink',
                        fg = "white", font = ('Courier', 25))
    ownedPlace.grid(row = 3, column = 3)

    pricePlace = Label(root, width = 10, text = 'Price: ', anchor="w", bg = 'pink',
                        fg = "white", font = ('Courier', 25))
    pricePlace.grid(row = 3, column = 4)

    root.mainloop()
