from tkinter import *
import pymysql 
from membership import *
from books import *
from loans import *
from reservations import *
from fine import *
from report import *

mypass = ''
mydatabase = 'ALibrarySystem'

connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase)
cursor = connection.cursor()

### HOME PAGE ###   
# initialising the window and its size
root = Tk()
root.title("A Library System")
root.minsize(width = 400, height = 400)
root.geometry("800x600")

Canvas1 = Canvas(root)
Canvas1.config(bg="#f7f1e3")
Canvas1.pack(expand=True, fill=BOTH)

# adding a heading Frame to library
headingFrame1 = Frame(root, bg="#B0E0E6", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headingLabel = Label(headingFrame2, text="Welcome To \n A Library System (ALS)", bg="black", 
                fg="white", font=('Courier',15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# adding buttons
### comment out whatever you are not testing ###
btn1 = Button(root,text="Membership",bg='black', fg='black', command=membershipMenu)
btn1.place(relx=0.10,rely=0.3, relwidth=0.2,relheight=0.1)

btn2 = Button(root,text="Books",bg='black', fg='black', command=booksMenu)
btn2.place(relx=0.40,rely=0.3, relwidth=0.2,relheight=0.1)

btn3 = Button(root,text="Loans",bg='black', fg='black', command=loansMenu)
btn3.place(relx=0.70,rely=0.3, relwidth=0.2,relheight=0.1)

btn4 = Button(root,text="Reservations",bg='black', fg='black', command=reservationsMenu)
btn4.place(relx=0.10,rely=0.6, relwidth=0.2,relheight=0.1)

btn5 = Button(root,text="Fines",bg='black', fg='black', command=finesMenu)
btn5.place(relx=0.40,rely=0.6, relwidth=0.2,relheight=0.1)

btn6 = Button(root,text="Reports",bg='black', fg='black', command=reportMenu)
btn6.place(relx=0.70,rely=0.6, relwidth=0.2,relheight=0.1)

root.mainloop()

