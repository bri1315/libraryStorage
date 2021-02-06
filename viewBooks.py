#View books function will show all of the books in the databse
#it  will order it by title, author, read, owned, and price
#will also show buttons to  see if the user wants it ordered by title
#or author in alphabetical order
import tkinter
from tkinter import *
import tkinter.ttk as ttk
import pymysql
from tkinter import messagebox

mypass = "##########"
mydatabase="books"

con = pymysql.connect( host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
libraryTable = "library" # Book Table

#The function will sort all the items in the databse by title
#first will try to connet and if not successul will present a failed to opeen messagebox
#if sucessul will store data and show it in the grid
def sortByTitle():
        try:
            cur.execute("SELECT title, author, haveIRead, owned, price FROM library ORDER BY title")
            i = 3
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
#The function will sort all the items in the databse by author
#first will try to connet and if not successul will present a failed to opeen messagebox
#if sucessul will store data and show it in the grid
def sortByAuthor():
        try:
            cur.execute("SELECT title, author, haveIRead, owned, price FROM library ORDER BY author")
            #result = mycursor.fetchall()
            i = 3
            for library in cur:
                for j in range(len(library)):
                    populate = Label(root, width = 20, text = library[j],
                                    borderwidth=2,relief='ridge', anchor="w",
                                    bg = 'pink',fg = 'ghost white',
                                    font = ('Courier', 18))
                    populate.grid(row = i, column = j)
                    #populate.insert(END, library[j])
                i=i+1
        except:
            messagebox.showinfo("Failed to open database")

def viewBooks():
    #setting up global variables in order to use them in other functions
    global root

    #setting the window up
    root = tkinter.Tk()
    root.title("Viweing My Personal library")
    root.geometry("1920x1080")
    root.configure(bg = 'pink')

    #setting up the headers and describing what information will be populated
    viewTitle = Label(root, width = 18, text = 'View Book List', fg = "white",
                        bg = 'pink',font = ('Courier', 30))
    viewTitle.grid(row = 0, column = 1)

    titleBtn = Button(root, width = 18, height = 1, text = "sort by Title",
                    fg = 'blue violet', font = ('Courier',18),
                    command = sortByTitle)
    titleBtn.grid(row = 1, column = 0)

    authorBtn = Button(root, width = 18, height = 1, text = "sort by Author",
                    fg = 'blue violet', font = ('Courier',18),
                    command = sortByAuthor)
    authorBtn.grid(row = 1, column = 2)

    quit = Button(root, width = 18, height = 1,text = "Quit",
                fg = 'blue violet', font = ('Courier',18),
                command = root.destroy)
    quit.grid(row = 1, column = 3)

    titlePlace = Label(root, width = 18, text = 'Title: ', anchor="w", bg = 'pink',
                        fg = "white", font = ('Courier', 25))
    titlePlace.grid(row = 2, column = 0)

    authorPlace = Label(root, width = 18, text = 'Author: ', anchor="w", bg = 'pink',
                    fg = "white", font = ('Courier', 25))
    authorPlace.grid(row = 2, column = 1)

    readPlace = Label(root, width = 18, text = 'Read: ', anchor="w", bg = 'pink',
                    fg = "white", font = ('Courier', 25))
    readPlace.grid(row = 2, column = 2)

    ownedPlace = Label(root, width = 18, text = 'Owned: ', anchor="w", bg = 'pink',
                    fg = "white", font = ('Courier', 25))
    ownedPlace.grid(row = 2, column = 3)

    pricePlace = Label(root, width = 18, text = 'Price: ', anchor="w", bg = 'pink',
                    fg = "white", font = ('Courier', 25))
    pricePlace.grid(row = 2, column = 4)

    root.mainloop()
