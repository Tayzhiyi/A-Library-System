from tkinter import *
from tkinter import messagebox
import pymysql

def booksMenu():
    global headingFrame1,headingFrame2,headingLabel,Canvas1,LabelFrame,btn1,btn2,backBtn,root
    root = Tk()
    root.title("Books")
    root.minsize(width = 400, height = 400)
    root.geometry("800x600")

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#f7f1e3")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#40E0D0",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="black")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="Select one of \n the options below:", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="Book Acquisition",bg='black', fg='black', command=bookAcquisition)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Book Withdrawal",bg='black', fg='black', command=bookWithdrawal)
    btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(root,text="Back To Main Menu",bg='#455A64', fg='black', command=root.destroy)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)
    


####### BOOK ACQUISITION #######
def bookAcquisition():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, bookInfo5, bookInfo6, connection, cursor

    mypass = ''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase)
    cursor = connection.cursor()

    # destroy is to remove whatever is on the screen
    global headingFrame1,headingFrame2,headingLabel,Canvas1,labelFrame,backBtn
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    backBtn.destroy()
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#f7f1e3")
    Canvas1.pack(expand=True,fill=BOTH)
    
    #add a heading Frame
    headingFrame1 = Frame(root, bg="#FFBB00", bd=6)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    headingLabel = Label(headingFrame1, text="To acquire Book, please enter the requested information below:", bg="black", fg="white", font=('Courier', 13))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    #frame for form
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #Accession Number
    lb1 = Label(LabelFrame, text="Accession Number: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.1, relheight=0.08)
    #entry label for Accession Number
    bookInfo1 = Entry(LabelFrame)
    bookInfo1.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    #title
    lb2 = Label(LabelFrame, text="Title: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.25, relheight=0.08)
    #entry for title
    bookInfo2 = Entry(LabelFrame)
    bookInfo2.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    #authors
    lb3 = Label(LabelFrame, text="Authors: ", bg="black", fg="white")
    lb3.place(relx=0.05, rely=0.4, relheight=0.08)
    #entry for authors
    bookInfo3 = Entry(LabelFrame)
    bookInfo3.place(relx=0.3, rely=0.4, relwidth=0.62, relheight=0.08)

    #isbn
    lb4 = Label(LabelFrame, text="ISBN: ", bg="black", fg="white")
    lb4.place(relx=0.05, rely=0.55, relheight=0.08)
    #entry for isbn
    bookInfo4 = Entry(LabelFrame)
    bookInfo4.place(relx=0.3, rely=0.55, relwidth=0.62, relheight=0.08)
    
    #publisher
    lb5 = Label(LabelFrame, text="Publisher: ", bg="black", fg="white")
    lb5.place(relx=0.05, rely=0.7, relheight=0.08)
    #entry for publisher
    bookInfo5 = Entry(LabelFrame)
    bookInfo5.place(relx=0.3, rely=0.7, relwidth=0.62, relheight=0.08)

    #publication_year
    lb6 = Label(LabelFrame, text="Publication Year: ", bg="black", fg="white")
    lb6.place(relx=0.05, rely=0.85, relheight=0.08)
    #entry for publication_year
    bookInfo6 = Entry(LabelFrame)
    bookInfo6.place(relx=0.3, rely=0.85, relwidth=0.62, relheight=0.08)

    #submit Button
    SubmitBtn = Button(root, text="Add New Book", bg="#d1ccc0", fg="black", command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #Quit button
    QuitBtn = Button(root, text="Back to Books Menu", bg="#f7f1e3", fg="black", command=lambda:[root.destroy(), booksMenu()])
    QuitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def bookRegister():
    accession_number = bookInfo1.get()
    title = bookInfo2.get()
    authors = bookInfo3.get().split(", ")
    isbn = bookInfo4.get()
    publisher = bookInfo5.get()
    publication_year = bookInfo6.get()
    
    if not accession_number or not title or not authors or not isbn or not publisher or not publication_year :
        notBookCreated()
    else:
        insertBook = "INSERT INTO Book VALUES ('"+accession_number+"','"+title+"','"+isbn+"', '"+publisher+"', '"+publication_year+"')"
        listOfQueries = []
        for author in authors:
            listOfQueries.append("INSERT INTO BookAuthors VALUES ('"+accession_number+"','"+author+"')")
        try:
            cursor.execute(insertBook)
            connection.commit()
            for query in listOfQueries:
                cursor.execute(query)
            connection.commit()
            bookCreated()
        except:
            notBookCreated()


def notBookCreated():
    notCreate_top = Tk()

    notCreate_top.title("Error!")
    notCreate_top.minsize(width = 200, height = 200)
    notCreate_top.geometry("400x400")


    Canvas1 = Canvas(notCreate_top)
    
    Canvas1.config(bg="Red")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_text(215,50, text="Error!", fill = "Yellow", font = ('Courier', 60))
    Canvas1.create_text(215,200, text="Book already added;\n Duplicate, Missing or\n Incomplete fields", fill = "Yellow", font = ('Courier', 20), justify = "center")
    
    Canvas1.pack()
    
    btn1 = Button(notCreate_top,text="Back to\n Acquisition\n Function",bg='green', fg='black', command=lambda:[notCreate_top.destroy(), bookAcquisition()])
    btn1.place(x=140, y=300, relwidth=0.3,relheight=0.15)                    


def bookCreated():
    create_top = Tk()

    create_top.title("Success")
    create_top.minsize(width = 200, height = 200)
    create_top.geometry("400x400")


    Canvas1 = Canvas(create_top)
    
    Canvas1.config(bg="Green")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_text(215,50, text="Success!", fill = "Black", font = ('Courier', 60))
    Canvas1.create_text(215,200, text="New Book added in Library", fill = "Black", font = ('Courier', 20), justify = "center")
    
    Canvas1.pack()
    
    btn1 = Button(create_top,text="Back to\n Acquisition\n Function",bg='green', fg='black', command=lambda:[create_top.destroy(), bookAcquisition()])
    btn1.place(x=140, y=300, relwidth=0.3,relheight=0.15)                    







def bookWithdrawal():
    global accessionNumber1, connection, cursor

    mypass = ''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase)
    cursor = connection.cursor()

    # destroy is to remove whatever is on the screen
    global headingFrame1,headingFrame2,headingLabel,Canvas1,labelFrame,backBtn
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    backBtn.destroy()
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#f7f1e3")
    Canvas1.pack(expand=True,fill=BOTH)

    #add a heading Frame
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    headingLabel = Label(headingFrame1, text="To withdraw book, please enter the requested information below:", bg="black", fg="white", font=('Courier', 13))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    #frame for form
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #Accession Number
    lb1 = Label(LabelFrame, text="Accession Number: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    #entry label for member Id
    accessionNumber1 = Entry(LabelFrame)
    accessionNumber1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
    
    #submit Button
    SubmitBtn = Button(root, text="Withdraw Book", bg="#d1ccc0", fg="black", command= openWithdrawalWindow)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
  
    #Quit button
    QuitBtn = Button(root, text="Back to Books Menu", bg="#f7f1e3", fg="black", command=lambda:[root.destroy(), booksMenu()])
    QuitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


def BookInfoGetter(AccessionNo):
    infoGetter = "SELECT * FROM Book WHERE accessionNo = '%s'" % (AccessionNo)
    cursor.execute(infoGetter)
    for i in cursor:
        return i
        

def openWithdrawalWindow():
    mypass = ''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase);
    cursor = connection.cursor(); 
    
    accessionID2 = accessionNumber1.get()

    BookDetails = BookInfoGetter(accessionID2)

    if not BookDetails:
        unavailBook()

   

    else:
        infoGetter = "SELECT title FROM Book WHERE accessionNo = '"+accessionID2+"';"
        cursor.execute(infoGetter)
        for i in cursor:
            title = i[0]

        infoGetterAuthors = "SELECT GROUP_CONCAT(authors SEPARATOR ', ') FROM BookAuthors WHERE accessionNo = '"+accessionID2+"';"
        cursor.execute(infoGetterAuthors);   
        for j in cursor:
            authors = j[0]
        
        top = Tk()
        top.title("Confirmation Page")
        top.minsize(width = 400, height = 400)
        top.geometry("800x600")


        isbn_nos = "SELECT isbn FROM Book WHERE accessionNo = '"+accessionID2+"';"
        cursor.execute(isbn_nos)
        for k in cursor:
            isbn_no = k[0]

        publishers = "SELECT publisher FROM Book WHERE accessionNo = '"+accessionID2+"';"
        cursor.execute(publishers)
        for l in cursor:
            publisher = l[0]

        years = "SELECT pubYr FROM Book WHERE accessionNo = '"+accessionID2+"';"
        cursor.execute(years)
        for m in cursor:
            pub_year = m[0]


    
        
        Canvas1 = Canvas(top)
    
        Canvas1.config(bg="#f7f1e3")
        Canvas1.pack(expand=True, fill=BOTH)
    
        headingFrame1 = Frame(top, bg="#B0E0E6", bd=5)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
    
        headingLabel = Label(headingFrame1, text="Please Confirm Details To Be Correct:", bg="black", fg="white", font=('Courier', 13))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        bodyLabel1 = Label(top, text="Accession Number: {0}".format(accessionID2), bg='black', fg='white', font=('Courier', 15))
        bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.1)

        bodyLabel2 = Label(top, text="Book Title: {0}".format(title), bg='black', fg='white', font=('Courier', 15))
        bodyLabel2.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.1)

        bodyLabel3 = Label(top, text="Authors: {0}".format(authors), bg='black', fg='white', font=('Courier', 15))
        bodyLabel3.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.1)

        bodyLabel4 = Label(top, text="ISBN: {0}".format(isbn_no), bg='black', fg='white', font=('Courier', 15))
        bodyLabel4.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.1)

        bodyLabel5 = Label(top, text="Publisher: {0}".format(publisher), bg='black', fg='white', font=('Courier', 15))
        bodyLabel5.place(relx=0.1,rely=0.6,relwidth=0.8,relheight=0.1)

        bodyLabel6 = Label(top, text="Year: {0}".format(pub_year), bg='black', fg='white', font=('Courier', 15))
        bodyLabel6.place(relx=0.1,rely=0.7,relwidth=0.8,relheight=0.1)

        btn1 = Button(top,text="Confirm Withdrawal",bg='black', fg='black', command=lambda:[bookWithdraw(), top.destroy()])
        btn1.place(relx=0.1,rely=0.85, relwidth=0.3,relheight=0.15)
    
        btn2 = Button(top,text="Back To\nWithdrawal\nFunction",bg='black', fg='black', command=top.destroy)
        btn2.place(relx=0.6,rely=0.85, relwidth=0.3,relheight=0.15)
    







    
    
def bookWithdraw():
    accessionID = accessionNumber1.get()

    mypass = ''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase)
    cursor = connection.cursor()

    try:
        booksloan = "SELECT accessionNo FROM Loan;"
        cursor.execute(booksloan)
        fly = 0
        for i in cursor:
            if accessionID == i[0]:
                fly = 1
                break;
        if fly == 1:
            bookOnLoan()
        else:
            reservationBook = "SELECT DISTINCT accessionNo FROM Reservation;"
            cursor.execute(reservationBook)
            fly2 = 0
            for w in cursor:
                if accessionID == w[0]:
                    fly2 = 1
                    break;
            if fly2 == 1:
                bookReserved()
            else:
                removebookauthors = "DELETE FROM BookAuthors WHERE accessionNo = '"+accessionID+"';"
                cursor.execute(removebookauthors)
                connection.commit()
                removebook = "DELETE FROM Book WHERE accessionNo = '"+accessionID+"';"
                cursor.execute(removebook)
                connection.commit()
                messagebox.showinfo('Success!', "Book is removed successfully")
    except: 
        unavailBook()

def bookOnLoan():
    loan_top = Tk()

    loan_top.title("Error!")
    loan_top.minsize(width = 200, height = 200)
    loan_top.geometry("400x400")


    Canvas1 = Canvas(loan_top)
    
    Canvas1.config(bg="Red")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_text(215,50, text="Error!", fill = "Yellow", font = ('Courier', 60))
    Canvas1.create_text(215,200, text="Book is currently on Loan", fill = "Yellow", font = ('Courier', 20), justify = "center")
    
    Canvas1.pack()
    
    btn1 = Button(loan_top,text="Return to\n Withdrawal\n Function",bg='green', fg='black', command=lambda:[loan_top.destroy(), bookWithdrawal()])
    btn1.place(x=140, y=300, relwidth=0.3,relheight=0.15)

def bookReserved():
    reserved_top = Tk()

    reserved_top.title("Confirmation Page")
    reserved_top.minsize(width = 200, height = 200)
    reserved_top.geometry("400x400")


    Canvas1 = Canvas(reserved_top)
    
    Canvas1.config(bg="Red")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_text(215,50, text="Error!", fill = "Yellow", font = ('Courier', 60))
    Canvas1.create_text(215,200, text="Book is currently Reserved", fill = "Yellow", font = ('Courier', 20), justify = "center")
    
    Canvas1.pack()
    
    btn1 = Button(reserved_top,text="Back to\n Withdrawal\n Function",bg='green', fg='black', command=lambda:[reserved_top.destroy(), bookWithdrawal()])
    btn1.place(x=140, y=300, relwidth=0.3,relheight=0.15)

def unavailBook():
    unavail_top = Tk()

    unavail_top.title("Confirmation Page")
    unavail_top.minsize(width = 200, height = 200)
    unavail_top.geometry("400x400")


    Canvas1 = Canvas(unavail_top)
    
    Canvas1.config(bg="Red")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_text(215,50, text="Error!", fill = "Yellow", font = ('Courier', 60))
    Canvas1.create_text(215,200, text="Book is not available", fill = "Yellow", font = ('Courier', 20), justify = "center")
    
    Canvas1.pack()
    
    btn1 = Button(unavail_top,text="Back to\n Withdrawal\n Function",bg='green', fg='black', command=unavail_top.destroy)
    btn1.place(x=140, y=300, relwidth=0.3,relheight=0.15)




    
