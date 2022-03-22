from tkinter import *
from tkinter import messagebox
import pymysql
import re

def reportMenu():
    global headingFrame1,headingFrame2,headingLabel,Canvas1,labelFrame,backBtn,root,btn1,btn2,btn3,btn4,btn5
    root = Tk()
    root.title("Reports Menu")
    root.minsize(width = 400, height = 400)
    root.geometry("800x600")

    #set bg colour
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#f7f1e3")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(root,bg="#40E0D0",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingFrame2 = Frame(headingFrame1,bg="black")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
    headingLabel = Label(headingFrame2, text="Select one of \n the options below:", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root,text="Book Search",bg='black', fg='black', command=bookSearch)
    btn1.place(relx=0.28,rely=0.25, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Books on Loan",bg='black', fg='black', command=booksOnLoan)
    btn2.place(relx=0.28,rely=0.37, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="Books on Reservation",bg='black', fg='black', command=booksOnReservation)
    btn3.place(relx=0.28,rely=0.49, relwidth=0.45,relheight=0.1)
    
    btn4 = Button(root,text="Outstanding Fines",bg='black', fg='black', command=outstandingFines)
    btn4.place(relx=0.28,rely=0.61, relwidth=0.45,relheight=0.1)
    
    btn5 = Button(root,text="Books on Loan to Member",bg='black', fg='black', command=booksOnLoanByID)
    btn5.place(relx=0.28,rely=0.73, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(root,text="Back To Main Menu",bg='#455A64', fg='black', command=root.destroy)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)


####### BOOK SEARCH #########
def bookSearch():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, bookInfo5, connection, cursor

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase);
    cursor = connection.cursor();

    # destroy is to remove whatever is on the screen
    global headingFrame1,headingLabel,Canvas1,LabelFrame,SubmitBtn,QuitBtn,nextID
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    btn5.destroy()
    backBtn.destroy()

    #set bg colour
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#f7f1e3")
    Canvas1.pack(expand=True,fill=BOTH)

    #add a heading Frame
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Search based on one of the categories below:\n Please enter only one word.", bg="black", fg="white", font=('Courier', 14))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    #frame for form
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #title
    lb1 = Label(LabelFrame, text="Title: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    #entry label for title
    bookInfo1 = Entry(LabelFrame)
    bookInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
    
    #authors
    lb2 = Label(LabelFrame, text="Authors: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
    #entry for authors
    bookInfo2 = Entry(LabelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    #isbn
    lb3 = Label(LabelFrame, text="ISBN: ", bg="black", fg="white")
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)
    #entry for isbn
    bookInfo3 = Entry(LabelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    #publisher
    lb4 = Label(LabelFrame, text="Publisher: ", bg="black", fg="white")
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)
    #entry for publisher
    bookInfo4 = Entry(LabelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)
    
    #publication year
    lb5 = Label(LabelFrame, text="Publication Year: ", bg="black", fg="white")
    lb5.place(relx=0.05, rely=0.80, relheight=0.08)
    #entry for publication year
    bookInfo5 = Entry(LabelFrame)
    bookInfo5.place(relx=0.3, rely=0.80, relwidth=0.62, relheight=0.08)

    #submit Button
    SubmitBtn = Button(root, text="Search Book", bg="#d1ccc0", fg="black", command=searchSubmit)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #Quit button
    QuitBtn = Button(root, text="Back to\nReports Menu", bg="#f7f1e3", fg="black", command=lambda:[root.destroy(), reportMenu()])
    QuitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def search_books(title, authors, isbn, publisher, pubYr):
    checker = ['title', 'authors', 'isbn', 'publisher', 'pubYr']
    input_list = [title, authors, isbn, publisher, pubYr]
    for i in range(len(input_list)):
        if len(input_list[i]) != 0:
            input = input_list[i]
            attribute = checker[i]
            index = i
            search_query = "SELECT b.accessionNo, b.title, GROUP_CONCAT(a.authors SEPARATOR ', ') AS authors, b.isbn, b.publisher, b.pubYr\
            FROM Book b LEFT JOIN BookAuthors a ON a.accessionNo = b.accessionNo GROUP BY b.accessionNo HAVING "+attribute+" LIKE '%"+input+"%';"
    try:
        cursor.execute(search_query)
        list_of_books = []
        for i in cursor:
            if bool(re.search(r'\b{}\b'.format(input.lower()), i[index + 1].lower())):
                list_of_books.append(i)
        return list_of_books
    except:
        return []


def no_entry():
    root_confirm = Tk()
    root_confirm.title("Error")
    root_confirm.minsize(width = 200, height = 300)
    root_confirm.geometry("300x400")
    
    Canvas1 = Canvas(root_confirm)
    Canvas1.config(bg="red")
    Canvas1.pack(expand=True, fill=BOTH)
    
    headingFrame1 = Frame(root_confirm,bg="red")
    headingFrame1.place(relx=0.01,rely=0.01,relwidth=0.9,relheight=0.1)
        
    headingLabel = Label(headingFrame1, text="Error!", bg='red', fg='yellow', font=('Courier', 15))
    headingLabel.place(relx=0.05,rely=0.1, relwidth=1, relheight=1)
    
    bodyLabel1 = Label(root_confirm, text="No input detected.", bg='red', fg='yellow', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nSearch\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)


def input_too_long():
    root_confirm = Tk()
    root_confirm.title("Error")
    root_confirm.minsize(width = 200, height = 300)
    root_confirm.geometry("300x400")
    
    Canvas1 = Canvas(root_confirm)
    Canvas1.config(bg="red")
    Canvas1.pack(expand=True, fill=BOTH)
    
    headingFrame1 = Frame(root_confirm,bg="red")
    headingFrame1.place(relx=0.01,rely=0.01,relwidth=0.9,relheight=0.1)
        
    headingLabel = Label(headingFrame1, text="Error!", bg='red', fg='yellow', font=('Courier', 15))
    headingLabel.place(relx=0.05,rely=0.1, relwidth=1, relheight=1)
    
    bodyLabel1 = Label(root_confirm, text="Invalid input\nPlease key in one word only.", bg='red', fg='yellow', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nSearch\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)

def no_of_input_checker(title, authors, isbn, publisher, pubYr):
    list_of_inputs = [title, authors, isbn, publisher, pubYr]
    count = 0
    for input in list_of_inputs:
        if len(input) > 0:
            count += 1
    return count != 1

def too_many_input():
    root_confirm = Tk()
    root_confirm.title("Error")
    root_confirm.minsize(width = 200, height = 300)
    root_confirm.geometry("300x400")
    
    Canvas1 = Canvas(root_confirm)
    Canvas1.config(bg="red")
    Canvas1.pack(expand=True, fill=BOTH)
    
    headingFrame1 = Frame(root_confirm,bg="red")
    headingFrame1.place(relx=0.01,rely=0.01,relwidth=0.9,relheight=0.1)
        
    headingLabel = Label(headingFrame1, text="Error!", bg='red', fg='yellow', font=('Courier', 15))
    headingLabel.place(relx=0.05,rely=0.1, relwidth=1, relheight=1)
    
    bodyLabel1 = Label(root_confirm, text="Invalid input\nToo many inputs", bg='red', fg='yellow', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nSearch\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)

def searchSubmit():
    title = bookInfo1.get()
    authors = bookInfo2.get()
    isbn = bookInfo3.get()
    publisher = bookInfo4.get()
    pubYr = bookInfo5.get()
    

    if not title and not authors and not isbn and not publisher and not pubYr:
        no_entry()
    elif title.count(" ") > 0 or authors.count(" ") > 0 or isbn.count(" ") > 0 or publisher.count(" ") > 0 or pubYr.count(" ") > 0:
        input_too_long()
    elif no_of_input_checker(title, authors, isbn, publisher, pubYr):
        too_many_input()
    else:
        book_search = Tk()
        book_search.title("Book Search Results")
        book_search.minsize(width = 400, height = 400)
        book_search.geometry("1200x600")
        book_search.configure(background='green')

        listOfBooks = [('Accession Number', 'Title', 'Authors', 'ISBN', 'Publisher' , 'Year')] + search_books(title, authors, isbn, publisher, pubYr)
        
        book_search.grid_columnconfigure(1, weight=1)
        book_search.grid_columnconfigure(2, weight=1)
        book_search.grid_columnconfigure(4, weight=1)
        rows = []
        for i in range(len(listOfBooks)):
            cols = []
            for j in range(6):
                e = Entry(book_search, width=20, font=("Courier", 14))
                e.grid(row = i, column = j, sticky='nsew', padx = 1, pady = 1)
                e.insert(END, listOfBooks[i][j])
                cols.append(e)
            rows.append(cols)
        
        backBtn = Button(book_search,text="Back To\nSearch Function",bg='#455A64', fg='black', command=book_search.destroy)
        backBtn.place(relx=0.5, rely=0.9, anchor=CENTER)
                
        root.mainloop()


####### BOOKS ON LOAN #########
def getBooksOnLoan():
    booksAuthors = "SELECT b.accessionNo, b.title, GROUP_CONCAT(a.authors SEPARATOR ', ') AS authors, b.isbn, b.publisher, b.pubYr FROM Loan l JOIN Book b \
                    ON b.accessionNo = l.accessionNo JOIN BookAuthors a \
                    ON a.accessionNo = l.accessionNo \
                    GROUP BY b.accessionNo;"
    cursor.execute(booksAuthors)
    list_of_books = []
    for i in cursor:
        list_of_books.append(i)
    return list_of_books


def booksOnLoan():
    global connection, cursor

    mypass = ''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase);
    cursor = connection.cursor();
    
    book_loans = Tk()
    book_loans.title("Books On Loans")
    book_loans.minsize(width = 400, height = 400)
    book_loans.geometry("1200x600")
    book_loans.configure(background='green')

    listOfBooks = [('Accession Number', 'Title', 'Authors', 'ISBN', 'Publisher' , 'Year')] + getBooksOnLoan()

    book_loans.grid_columnconfigure(1, weight=1)
    book_loans.grid_columnconfigure(2, weight=1)
    book_loans.grid_columnconfigure(4, weight=1)
    rows = []
    for i in range(len(listOfBooks)):
        cols = []
        for j in range(6):
            e = Entry(book_loans, width=20, font=("Courier", 14))
            e.grid(row = i, column = j, sticky='nsew', padx = 1, pady = 1)
            e.insert(END, listOfBooks[i][j])
            cols.append(e)
        rows.append(cols)
    
    backBtn = Button(book_loans,text="Back To\nReports Menu",bg='#455A64', fg='black', command=book_loans.destroy)
    backBtn.place(relx=0.5, rely=0.9, anchor=CENTER)
            
    root.mainloop()

####### BOOKS ON RESERVATION #########
def getBooksOnReservation():
    booksOnReservation = "SELECT m.memberID, m.name, b.accessionNo, b.title\
                            FROM Reservation r JOIN Member m \
                            ON m.memberID = r.memberID JOIN Book b \
                            ON b.accessionNo = r.accessionNo;"
    cursor.execute(booksOnReservation)
    list_of_info = []
    for i in cursor:
        list_of_info.append(i)
    return list_of_info

def booksOnReservation():
    global connection, cursor

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase);
    cursor = connection.cursor();
    
    root_fines = Tk()
    root_fines.title("Books On Reservation")
    root_fines.minsize(width = 400, height = 400)
    root_fines.geometry("900x600")
    root_fines.configure(background='green')
    
    
    
    #set bg colour
    #Canvas1 = Canvas(fines)
    #Canvas1.config(bg="green")
    #Canvas1.pack(expand=True,fill=BOTH)
    
    listOfReservations = [('Membership ID', 'Name', 'Accession Number', 'Title')] + getBooksOnReservation()
        
    #create table
    root_fines.grid_columnconfigure(3, weight=1)
    rows = []
    for i in range(len(listOfReservations)):
        cols = []
        for j in range(4):
            e = Entry(root_fines, width=20, font=("Courier", 14))
            e.grid(row = i, column = j, sticky='nsew', padx = 1, pady = 1)
            e.insert(END, listOfReservations[i][j])
            cols.append(e)
        rows.append(cols)
    
    backBtn = Button(root_fines,text="Back To\nReports Menu",bg='#455A64', fg='black', command=root_fines.destroy)
    backBtn.place(relx=0.5, rely=0.9, anchor=CENTER)
            
    root.mainloop()
    
    

####### MEMBERS WITH OUTSTANDING FINES #########
def getOutstandingFines():
    outstandingFines = "SELECT m.memberID, m.name, m.faculty, m.phoneNo, m.email\
                        FROM Fine f LEFT JOIN Member m \
                        ON m.memberID = f.memberID;"
    cursor.execute(outstandingFines)
    list_of_fines = []
    for i in cursor:
        list_of_fines.append(i)
    return list_of_fines

def outstandingFines():
    global connection, cursor

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase);
    cursor = connection.cursor();
    
    root_fines = Tk()
    root_fines.title("Members with Outstanding Fines")
    root_fines.minsize(width = 400, height = 400)
    root_fines.geometry("900x600")
    root_fines.configure(background='green')
    
    
    #set bg colour
    #Canvas1 = Canvas(fines)
    #Canvas1.config(bg="green")
    #Canvas1.pack(expand=True,fill=BOTH)
    
    listOfFines = [('Membership ID', 'Name', 'Faculty', 'Phone Number', 'Email Address')] + getOutstandingFines()
        
    #create table
    root_fines.grid_columnconfigure(4, weight=1)
    rows = []
    for i in range(len(listOfFines)):
        cols = []
        for j in range(5):
            e = Entry(root_fines, width=20, font=("Courier", 14))
            e.grid(row = i, column = j, sticky='nsew', padx = 1, pady = 1)
            e.insert(END, listOfFines[i][j])
            cols.append(e)
        rows.append(cols)
    
    backBtn = Button(root_fines,text="Back To\nReports Menu",bg='#455A64', fg='black', command=root_fines.destroy)
    backBtn.place(relx=0.5, rely=0.9, anchor=CENTER)
            
    root.mainloop()
    
    

####### BOOKS ON LOAN BY MEMBER ID #########
def booksOnLoanByID():
    global memberInfo1, connection, cursor

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase);
    cursor = connection.cursor();

    # destroy is to remove whatever is on the screen
    global headingFrame1,headingLabel,Canvas1,LabelFrame,SubmitBtn,QuitBtn
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    backBtn.destroy()
    
    #set bg colour
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#f7f1e3")
    Canvas1.pack(expand=True,fill=BOTH)

    #add a heading Frame
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    headingLabel = Label(headingFrame1, text="Books on Loan to Member", bg="black", fg="white", font=('Courier', 14))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    #frame for form
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #member ID
    lb1 = Label(LabelFrame, text="Membership ID: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    #entry label for member Id
    memberInfo1 = Entry(LabelFrame)
    memberInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    #submit button
    SubmitBtn = Button(root, text="Search Member", bg="#d1ccc0", fg="black", command=bookSearchByID)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
    #Quit button
    QuitBtn = Button(root, text="Back to\nReports Menu", bg="#f7f1e3", fg="black", command=lambda:[root.destroy(), reportMenu()])
    QuitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def getBooksOnLoanByID(member_id):
    search_query = "SELECT m.memberID, b.accessionNo, b.title, GROUP_CONCAT(a.authors SEPARATOR ', ') AS authors, b.isbn, b.publisher, b.pubYr FROM Loan l JOIN Book b\
                    ON b.accessionNo = l.accessionNo JOIN Member m ON m.memberID = l.memberID\
                    JOIN BookAuthors a ON a.accessionNo = l.accessionNo GROUP BY m.memberID, b.accessionNo\
                    HAVING m.memberID = '%s';" % (member_id)
    cursor.execute(search_query)
    list_of_books = []
    for i in cursor:
        list_of_books.append(i[1:])
    return list_of_books

def memberInfoGetter(member_id):
    infoGetter = "SELECT * FROM Member WHERE memberID = '%s'" % (member_id)
    cursor.execute(infoGetter)
    for i in cursor:
        return i
        
def bookSearchByID():
    member_id = memberInfo1.get()
    member_details = memberInfoGetter(member_id)
    
    ##handle id not in databse
    if not member_details:
        messagebox.showinfo('Error!', "Member not in database.")
    ##handle id without books on loan
    elif not getBooksOnLoanByID(member_id):
        messagebox.showinfo('Error!', "Member does not have book on loan.")
    else:
        root_fines = Tk()
        root_fines.title("Books on Loan to Member")
        root_fines.minsize(width = 400, height = 400)
        root_fines.geometry("1000x600")
        root_fines.configure(background='green')
        
        listOfBooks = [('Accession\nNumber', 'Title', 'Authors', 'ISBN', 'Publisher', 'Year')] + getBooksOnLoanByID(member_id)
            
        #create table
        root_fines.grid_columnconfigure(1, weight=1)
        root_fines.grid_columnconfigure(2, weight=1)
        root_fines.grid_columnconfigure(4, weight=1)
        rows = []
        for i in range(len(listOfBooks)):
            cols = []
            for j in range(6):
                e = Entry(root_fines, width=20, font=("Courier", 14))
                e.grid(row = i, column = j, sticky='nsew', padx = 1, pady = 1)
                e.insert(END, listOfBooks[i][j])
                cols.append(e)
            rows.append(cols)
        
        backBtn = Button(root_fines,text="Back To\nReports Menu",bg='#455A64', fg='black', command=root_fines.destroy)
        backBtn.place(relx=0.5, rely=0.9, anchor=CENTER)
                
        root.mainloop()


