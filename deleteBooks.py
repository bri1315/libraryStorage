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
    #status = status.lower()

    deleteSql = "delete from "+libraryTable+" where title = '"+title+"'"

    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo('Success',"Book has successfully been Deleted")
    except:
        messagebox.showinfo("Error","Can't add data into Database")

    root.destroy()

def deleteBooks():

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

    addTitle = Label(root, text="Deleting book by Title",fg = "white",
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
