#setting up the main function ill link to the other functions when a user decides which one they want
import tkinter
from tkinter import *
import tkinter.ttk as ttk
import pymysql
from tkinter import messagebox

from addBook import *
from viewBooks import *
#from viewOwnedBooks import *
#from viewNotOwnedBooks import *
from deleteBooks import *
from updateOwned import *
from updateRead import *
from viewReadBooks import *
from viewNotReadBooks import *

#connecting to sql server
mypass = "##########"
mydatabase="books"

con = pymysql.connect( host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

#testing to make sure it gott connected
#mycursor.execute("select * from library")

#result = mycursor.fetchall()

#for i in result:
#    print(i)

#setting the window up
root = tkinter.Tk()
root.title("My personal library")
root.geometry("1920x1080")
root.configure(bg = 'pink')

#Main title
addTitle = Label(root,text = "Your personal library", fg = "white",
                    bg = 'pink',font = ('Courier',110))
addTitle.grid(row = 0, column = 0)

#add book buntton will connect to  addbook function
btnAddBook = Button(root, width = 25, height = 1, text = "Add Book",
                    fg = 'blue violet',command = addBook, font = ('Courier',40))
btnAddBook.grid(row = 2, column = 0)

#Delete book buntton will connect to  deletebook function
btnDeleteBook = Button(root, width = 25, height = 1,  text = "Delete Book",
                    fg = 'blue violet', command = deleteBooks,font = ('Courier',40))
btnDeleteBook.grid(row = 3, column = 0)


#status book buntton will connect to  readbooks function
btnStatus = Button(root, width = 25, height = 1,text = "Updated read status",
                fg = 'blue violet', command =updateRead, font = ('Courier',40))
btnStatus.grid(row = 4, column = 0)

# statusOwned connects to updateOwned
btnStatusOwned = Button(root, width = 25, height = 1,text = "Updated Owned status",
                fg = 'blue violet', command =updateOwned, font = ('Courier',40))
btnStatusOwned.grid(row = 5, column = 0)

#View book buntton will connect to  viewbooks function
btnViewBookList = Button (root, width = 25, height = 1,  text = "View Entire Book List",
                        fg = 'blue violet', command = viewBooks, font = ('Courier',40))
btnViewBookList.grid(row = 6, column = 0)

#all read book buntton will connect to  viewReadBooks function
btnAllRead = Button(root, width = 25, height = 1,text = "Show Only read Books",
                    fg = 'blue violet', command = viewReadBooks, font = ('Courier',40))
btnAllRead.grid(row = 7, column = 0)

#non read books buntton will connect to  viewNotReadBooks function
btnUnRead = Button(root, width = 25, height = 1,text = "Show Only Not read Books",
                    fg = 'blue violet', command=viewNotReadBooks, font = ('Courier',40))
btnUnRead.grid(row = 8, column = 0)

#btnAllOwned = Button(root, text = "Show Only Owned Books", fg = 'hot pink', command = viewOwnedBooks)
#btnAllOwned.grid(row = 9, column = 0)

#btnUnOwned = Button(root, text = "Show Only Non-Owned Books", fg = 'hot pink', command=viewNotOwnedBooks)
#btnUnOwned.grid(row = 10, column = 0)

quitting = Button(root, width = 25, height = 1,text = "Quit", fg = 'blue violet', command = root.destroy, font = ('Courier',40))
quitting.grid(row = 9, column = 0)

root.mainloop()
