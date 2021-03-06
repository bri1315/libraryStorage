#code coped from my own viewbooks.py code
import tkinter
from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
#from tkinter import messagebox

con = pymysql.connect(host = "localhost", user = "root", passwd = "####s", database = "books")
mycursor = con.cursor()

#table name and setting it into libraryTable
libraryTable = "library"

def sortByTitle():
        try:
            mycursor.execute("SELECT title, author, haveIRead, owned, price FROM library WHERE owned = 'yes' ORDER BY title")
            #result = mycursor.fetchall()
            i = 3
            for library in mycursor:
                for j in range(len(library)):
                    populate = Label(root, width = 25, text = library[j], borderwidth=2,relief='ridge', anchor="w", bg = 'pink')
                    populate.grid(row = i, column = j)
                    #populate.insert(END, library[j])
                i=i+1
        except:
            messagebox.showinfo("Failed to open database")

def sortByAuthor():
        try:
            mycursor.execute("SELECT title, author, haveIRead, owned, price FROM library WHERE owned = 'yes' ORDER BY author")
            #result = mycursor.fetchall()
            i = 3
            for library in mycursor:
                for j in range(len(library)):
                    populate = Label(root, width = 25, text = library[j], borderwidth=2,relief='ridge', anchor="w", bg = 'pink')
                    populate.grid(row = i, column = j)
                    #populate.insert(END, library[j])
                i=i+1
        except:
            messagebox.showinfo("Failed to open database")

def viewOwnedBooks():
    #setting up global variables in order to use them in other functions
    global root
    #setting the window up
    root = tkinter.Tk()
    root.title("Viweing My Personal library")
    root.geometry("950x405")
    root.configure(bg = 'pink')

    #setting up the headers and describing what information will be populated
    viewTitle = Label(root, text = 'View Books that are owned',  fg = "white", bg = 'pink',font = ("Times", 20))
    viewTitle.grid(row = 0, column = 1)

    titleBtn = Button(root, text = "Sort by Title", bg = 'pink', command = sortByTitle)
    titleBtn.grid(row = 0, column = 0)

    authorBtn = Button(root, text = "Sort by Author", bg = 'pink', command = sortByAuthor)
    authorBtn.grid(row = 0, column = 2)

    quit = Button(root, text = "Quit", command = root.destroy)
    quit.grid(row = 0, column = 3)

    titlePlace = Label(root, width = 25, text = 'Title: ', anchor="w", bg = 'pink',fg = "white", font = ("Times", 16))
    titlePlace.grid(row = 2, column = 0)

    authorPlace = Label(root, width = 25, text = 'Author: ', anchor="w", bg = 'pink',fg = "white", font = ("Times", 16))
    authorPlace.grid(row = 2, column = 1)

    readPlace = Label(root, width = 20, text = 'Read: ', anchor="w", bg = 'pink',fg = "white", font = ("Times", 16))
    readPlace.grid(row = 2, column = 2)

    ownedPlace = Label(root, width = 20, text = 'Owned: ', anchor="w", bg = 'pink',fg = "white", font = ("Times", 16))
    ownedPlace.grid(row = 2, column = 3)

    pricePlace = Label(root, width = 20, text = 'Price: ', anchor="w", bg = 'pink',fg = "white", font = ("Times", 16))
    pricePlace.grid(row = 2, column = 4)


    root.mainloop()
