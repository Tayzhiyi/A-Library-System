from tkinter import *
from tkinter import messagebox
import pymysql
import datetime

def loansMenu():
    global headingFrame1,headingFrame2,headingLabel,Canvas1,labelFrame,backBtn, root, btn1
    root = Tk()
    root.title("Loans Menu")
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
    
    btn1 = Button(root,text="Books Borrowing",bg='black', fg='black', command=bookBorrowing)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="Books Returning",bg='black', fg='black', command=bookReturning)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(root,text="Back To Main Menu",bg='#455A64', fg='black', command=root.destroy)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

def bookBorrowing():
    global accessionID
    global membershipID
    global headingFrame1,headingFrame2,headingLabel,Canvas1,labelFrame,backBtn, btn1

    
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    btn1.destroy()
    Canvas1.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#f7f1e3")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.55, relheight=0.13)
    
    headingLabel = Label(headingFrame1, text="To Borrow a Book, Please Enter Information Below:", bg="black", fg="white", font=('Courier', 13))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #frame for form
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #accessionID
    lb1 = Label(LabelFrame, text="Accession Number: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2,relheight=0.08)
    #entry label for accession Id
    accessionID = Entry(LabelFrame)
    accessionID.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)


    #membership ID
    lb2 = Label(LabelFrame, text="Membership ID: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.3,relheight=0.18)
    #entry label for membership Id
    membershipID = Entry(LabelFrame)
    membershipID.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    #submit Button
    SubmitBtn = Button(root, text="Borrow Book", bg="#d1ccc0", fg="black", command=testingfactor)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #back Button
    backBtn = Button(root,text="Back To Loans Menu",bg='#455A64', fg='black', command=lambda:[root.destroy(), loansMenu()])
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()

def testingfactor():
    accessionID2 = accessionID.get()
    membershipID2 = membershipID.get()

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = mydatabase);
    cursor = connection.cursor(); 

    #test if user is in database
    userquery = "SELECT COUNT(*) FROM Member WHERE memberID = '"+membershipID2+"';"
    cursor.execute(userquery)
    for i in cursor:
        useravailable = i[0]
    bookquery = "SELECT COUNT(*) FROM Book WHERE accessionNo = '"+accessionID2+"';"
    cursor.execute(bookquery)
    for j in cursor:
        bookavailable = j[0]
    if useravailable == 0 or bookavailable == 0:
        messagebox.showinfo("Error!", "Book/Member not available")
    else:
        openloanwindow()
    
def openloanwindow():
    global returndate
    accessionID2 = accessionID.get()
    membershipID2 = membershipID.get()

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = mydatabase);
    cursor = connection.cursor(); 

    infoGetter = "SELECT title FROM Book WHERE accessionNo = '"+accessionID2+"';"
    cursor.execute(infoGetter)
    for i in cursor:
        title = i[0]

    infoGetterAuthors = "SELECT * FROM BookAuthors WHERE accessionNo = '"+accessionID2+"';"
    cursor.execute(infoGetterAuthors);
    
    for j in cursor:
        authors = j[1]
    top = Tk()
    top.title("Confirmation Page")
    top.minsize(width = 400, height = 400)
    top.geometry("800x600")

    current_date = "SELECT CURDATE();"
    cursor.execute(current_date)
    for w in cursor:
        date = w[0]

    return_date = "SELECT DATE_ADD(CURDATE(),INTERVAL 2 WEEK);"
    cursor.execute(return_date)
    for y in cursor:
        returndate = str(y[0])

    member_names = "SELECT name FROM Member WHERE memberID = '"+membershipID2+"';"
    cursor.execute(member_names)
    for z in cursor:
        member_name = z[0]
        
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

    bodyLabel3 = Label(top, text="Borrow Date: {0}".format(date), bg='black', fg='white', font=('Courier', 15))
    bodyLabel3.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.1)

    bodyLabel4 = Label(top, text="Membership ID: {0}".format(membershipID2), bg='black', fg='white', font=('Courier', 15))
    bodyLabel4.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.1)

    bodyLabel5 = Label(top, text="Member Name: {0}".format(member_name), bg='black', fg='white', font=('Courier', 15))
    bodyLabel5.place(relx=0.1,rely=0.6,relwidth=0.8,relheight=0.1)

    bodyLabel6 = Label(top, text="Due Date: {0}".format(returndate), bg='black', fg='white', font=('Courier', 15))
    bodyLabel6.place(relx=0.1,rely=0.7,relwidth=0.8,relheight=0.1)

    btn1 = Button(top,text="Confirm Loan",bg='black', fg='black', command=lambda:[loanRegister(), top.destroy()])
    btn1.place(relx=0.1,rely=0.85, relwidth=0.3,relheight=0.15)
    
    btn2 = Button(top,text="Back To\nBorrow\nFunction",bg='black', fg='black', command=top.destroy)
    btn2.place(relx=0.6,rely=0.85, relwidth=0.3,relheight=0.15)
    
    
def loanRegister():

    global date
    accessionID2 = accessionID.get()
    membershipID2 = membershipID.get()

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = mydatabase);
    cursor = connection.cursor()

    #to get the currentdate
    current_date = "SELECT CURDATE();"
    cursor.execute(current_date)
    for w in cursor:
        date = str(w[0])
        #to get the returndate
    return_date = "SELECT DATE_ADD(CURDATE(),INTERVAL 2 WEEK);"
    cursor.execute(return_date)
    for y in cursor:
        returndate = str(y[0])
        #see if the book is on loan or not
    checkavailability = "SELECT accessionNo FROM Loan GROUP BY accessionNo HAVING count(accessionNo) > 0"
    cursor.execute(checkavailability)
    flag = 0
    for j in cursor:
        if (j[0] == accessionID2):
            flag = 1
            break;
    if flag == 1:
        currentlyLoaned()
    else:
        #No loans
        #check fines -- if fine -- return hasfines()
        #check reservation -- reservation will return order via date and has no fines -- if number 1 == checker == 0
        #else return checker == 1
        checkfines = "SELECT COUNT(*) FROM Fine WHERE memberiD = '"+membershipID2+"';"
        cursor.execute(checkfines)
        for q in cursor:
            finenumber = q[0]
        if finenumber != 0:
            hasfines()
        else:
            if checkreservation() == 1:
                messagebox.showinfo('Error!', 'Others have already reserved it')
            else:
                deletereservation = "DELETE FROM Reservation WHERE accessionNo = '"+accessionID2+"' AND memberID = '"+membershipID2+"';"
                cursor.execute(deletereservation)
                connection.commit()
                checkmembers = "SELECT memberID FROM Loan GROUP BY memberID HAVING count(memberID) > 1"
                cursor.execute(checkmembers)
                checker2 = 0
                for e in cursor:
                    if (e[0] == membershipID2):
                        checker2 = 1
                        break;
                if checker2 == 0:
                    insertLoan2 = "INSERT INTO Loan Values('"+accessionID2+"', '"+date+"' , '"+returndate+"' , '"+membershipID2+"')"
                    cursor.execute(insertLoan2)
                    connection.commit()
                    messagebox.showinfo('Success!', "Loan is successful")
                else:
                    loanedmorethantwo()
                
#def checkforfines():
    #accessionID2 = accessionID.get()
    #membershipID2 = membershipID.get()

    #mypass=''
    #mydatabase = 'ALibrarySystem'

    #connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = mydatabase);
    #cursor = connection.cursor();

    #current_date = "SELECT CURDATE();"
    #cursor.execute(current_date)
    #for w in cursor:
        #currentdate = str(w[0])
    #checkfinesforbook = "SELECT dueDate FROM Loan WHERE memberID = '"+membershipID2+"';"
    #cursor.execute(checkfinesforbook)
    #checkers = 0
    #for m in cursor:
        #duedate = str(m[0])
        #datediff = "SELECT DATEDIFF('"+duedate+"', '"+currentdate+"');"
        #cursor.execute(datediff)
        #for z in cursor:
            #datediff = int(z[0])
        #if datediff < 0:
            #checkers = 1
            #break;
    #if checkers != 0:
        #return True

def checkreservation():
    accessionID2 = accessionID.get()
    membershipID2 = membershipID.get()

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = mydatabase);
    cursor = connection.cursor();
    checker = 1
    reservationforBook = "SELECT COUNT(*) FROM Reservation WHERE accessionNo = '"+accessionID2+"';"
    cursor.execute(reservationforBook)
    for i in cursor:
        totalreservation = i[0]
        break;
    if totalreservation == 0:
        checker = 0
    else:
        reservationcompetition = "SELECT memberID FROM Reservation WHERE accessionNo = '"+accessionID2+"' ORDER BY reservationDate;"
        cursor.execute(reservationcompetition)
        for j in cursor:
            if checkfines(j[0]) == False:
                if j[0] == membershipID2:
                    checker  = 0
                    break
                else:
                    checker = 1
                    break
    return checker

def checkfines(x):
    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = mydatabase);
    cursor = connection.cursor();

    current_date = "SELECT CURDATE();"
    cursor.execute(current_date)
    for w in cursor:
        currentdate = str(w[0])
    member = x
    fines = "SELECT COUNT(*) FROM Fine WHERE memberID = '"+member+"';"
    cursor.execute(fines)
    for i in cursor:
        fine = i[0]
        if fine == 0:
            return False
        else:
            return True
    
            
        
    
def currentlyLoaned():
    error_top = Tk()

    error_top.title("Confirmation Page")
    error_top.minsize(width = 200, height = 200)
    error_top.geometry("400x400")


    Canvas1 = Canvas(error_top)
    
    Canvas1.config(bg="Red")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_text(215,50, text="ERROR!", fill = "Yellow", font = ('Courier', 60))
    Canvas1.create_text(215,200, text="Book currently on Loan until:", fill = "Yellow", font = ('Courier', 20), justify = "center")
    Canvas1.create_text(200,230, text=str(returndate), fill = "Yellow", font = ('Courier', 20), justify = "center")
    Canvas1.pack()
    
    btn1 = Button(error_top,text="Back to\n Borrow Function",bg='green', fg='black', command=lambda:[error_top.destroy(), bookBorrowing()])
    btn1.place(x=140, y=300, relwidth=0.3,relheight=0.15)                    

def loanedmorethantwo():
    error_top = Tk()

    error_top.title("Confirmation Page")
    error_top.minsize(width = 200, height = 200)
    error_top.geometry("400x400")


    Canvas1 = Canvas(error_top)
    
    Canvas1.config(bg="Red")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_text(215,50, text="ERROR!", fill = "Yellow", font = ('Courier', 60))
    Canvas1.create_text(215,200, text="Member loan quota exceeded.", fill = "Yellow", font = ('Courier', 20), justify = "center")
    Canvas1.pack()

    #TRY TO SEE IF WE CAN GO BACK TO THE LOAN WINDOW
    btn1 = Button(error_top,text="Back to\n Main Menu",bg='green', fg='black', command=error_top.destroy)
    btn1.place(x=140, y=300, relwidth=0.3,relheight=0.15)  


def hasfines():
    error_top = Tk()

    error_top.title("Confirmation Page")
    error_top.minsize(width = 200, height = 200)
    error_top.geometry("400x400")


    Canvas1 = Canvas(error_top)
    
    Canvas1.config(bg="Red")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_text(215,50, text="ERROR!", fill = "Yellow", font = ('Courier', 60))
    Canvas1.create_text(215,200, text="Member has outstanding fines.", fill = "Yellow", font = ('Courier', 20), justify = "center")
    Canvas1.pack()
    
    btn1 = Button(error_top,text="Back to\n Borrow Function",bg='green', fg='black', command=error_top.destroy)
    btn1.place(x=140, y=300, relwidth=0.3,relheight=0.15)
    
def bookReturning():
    global accessionID
    global membershipID
    global headingFrame1,headingFrame2,headingLabel,Canvas1,labelFrame,backBtn, btn1

    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    btn1.destroy()
    Canvas1.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#f7f1e3")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.55, relheight=0.13)
    headingLabel = Label(headingFrame1, text="To Return a Book, Please Enter Information Below:", bg="black", fg="white", font=('Courier', 13))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #frame for form
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #accessionID
    lb1 = Label(LabelFrame, text="Accession Number: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    #entry label for accession Id
    accessionID = Entry(LabelFrame)
    accessionID.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)


    #membership ID
    lb2 = Label(LabelFrame, text="Membership ID: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.3,relheight=0.18)
    #entry label for membership Id
    membershipID = Entry(LabelFrame)
    membershipID.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    #submit Button
    SubmitBtn = Button(root, text="Return Book", bg="#d1ccc0", fg="black", command=testingreturn)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #back Button
    backBtn = Button(root,text="Back To Loans Menu",bg='#455A64', fg='black', command=lambda:[root.destroy(), loansMenu()])
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()

def testingreturn():
    accessionID2 = accessionID.get()
    membershipID2 = membershipID.get()

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = mydatabase);
    cursor = connection.cursor(); 

    #test if user is in database
    userquery = "SELECT COUNT(*) FROM Member WHERE memberID = '"+membershipID2+"';"
    cursor.execute(userquery)
    for i in cursor:
        useravailable = i[0]
    bookquery = "SELECT COUNT(*) FROM Book WHERE accessionNo = '"+accessionID2+"';"
    cursor.execute(bookquery)
    for j in cursor:
        bookavailable = j[0]
    bookuserquery = "SELECT COUNT(*) FROM Loan WHERE accessionNo = '"+accessionID2+"' AND memberID = '"+membershipID2+"';"
    cursor.execute(bookuserquery)
    for w in cursor:
        bookuseravailable = w[0]
    if useravailable == 0 or bookavailable == 0:
        messagebox.showinfo("Error!", "Book/Member not available")
    elif bookuseravailable == 0:
        messagebox.showinfo("Error!", "Member didn't borrow such a book!")
    else:
        openreturnwindow()

def openreturnwindow():
    global top
    accessionID2 = accessionID.get()
    membershipID2 = membershipID.get()

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = mydatabase);
    cursor = connection.cursor(); 

    #get book title
    infoGetter = "SELECT title FROM Book WHERE accessionNo = '"+accessionID2+"';"
    cursor.execute(infoGetter)
    for i in cursor:
        title = i[0]

    #Member Name
    infoMemberName= "SELECT name FROM Member WHERE memberID = '"+membershipID2+"';"
    cursor.execute(infoMemberName);
    for j in cursor:
        infoMemberName = j[0]
    
    #Return Date
    current_date = "SELECT CURDATE();"
    cursor.execute(current_date)
    for w in cursor:
        date = str(w[0])

    #Fine
    return_selectedbookduedate = "SELECT dueDATE FROM Loan WHERE accessionNo = '"+accessionID2+"';"
    cursor.execute(return_selectedbookduedate)
    for n in cursor:
        duedate = str(n[0])
    datediff = "SELECT DATEDIFF('"+duedate+"', '"+date+"');"
    cursor.execute(datediff)
    for m in cursor:
        datediff = int(m[0])
    if datediff < 0:
        currentfineforuser = "SELECT count(*) FROM Fine where memberID = '"+membershipID2+"';"
        cursor.execute(currentfineforuser)
        for a in cursor:
            currentfine = int(a[0])
        if currentfine == 0:
            newfineamount= str(abs(datediff))
        else:
            currentfineforuser2 = "SELECT fineAmount FROM Fine where memberID = '"+membershipID2+"';"
            cursor.execute(currentfineforuser2)
            for b in cursor:
                currentfine2 = int(b[0])
            newfineamount = str(currentfine2 + abs(datediff))
    else:
        newfineamount = "0"

    top = Tk()
    top.title("Confirmation Page")
    top.minsize(width = 400, height = 400)
    top.geometry("800x600")
    
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

    bodyLabel3 = Label(top, text="Membership ID: {0}".format(membershipID2), bg='black', fg='white', font=('Courier', 15))
    bodyLabel3.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.1)

    bodyLabel4 = Label(top, text="Member Name: {0}".format(infoMemberName), bg='black', fg='white', font=('Courier', 15))
    bodyLabel4.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.1)

    bodyLabel5 = Label(top, text="Return Date: {0}".format(date), bg='black', fg='white', font=('Courier', 15))
    bodyLabel5.place(relx=0.1,rely=0.6,relwidth=0.8,relheight=0.1)

    bodyLabel6 = Label(top, text="Fine: {0}".format(newfineamount), bg='black', fg='white', font=('Courier', 15))
    bodyLabel6.place(relx=0.1,rely=0.7,relwidth=0.8,relheight=0.1)

    btn1 = Button(top,text="Confirm Return",bg='black', fg='black', command=bookReturn)
    btn1.place(relx=0.1,rely=0.85, relwidth=0.3,relheight=0.15)
    
    btn2 = Button(top,text="Back To\nReturn\nFunction",bg='black', fg='black', command=lambda:[top.destroy(), bookReturning()])
    btn2.place(relx=0.6,rely=0.85, relwidth=0.3,relheight=0.15)

def bookReturn():
    accessionID2 = accessionID.get()
    membershipID2 = membershipID.get()


    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = mydatabase);
    cursor = connection.cursor(); 
            
    #get current date to check if expiry is up
    current_date = "SELECT CURDATE();"
    cursor.execute(current_date)
    for w in cursor:
        date = str(w[0])
    all_bookloaned = "SELECT accessionNo FROM Loan;"
    cursor.execute(all_bookloaned)
    bookchecker = 0
    for i in cursor:
        if i[0] == accessionID2:
            bookchecker = 1
            break;
    if bookchecker == 1:
        #Book duedate
        return_selectedbookduedate = "SELECT dueDATE FROM Loan WHERE accessionNo = '"+accessionID2+"';"
        cursor.execute(return_selectedbookduedate)
        for j in cursor:
            duedate = str(j[0])
        return_selectedbook = "DELETE FROM Loan WHERE accessionNo = '"+accessionID2+"';"
        cursor.execute(return_selectedbook)
        connection.commit()
        #See if the book is actually returned after duedate or not
        datediff = "SELECT DATEDIFF('"+duedate+"', '"+date+"');"
        cursor.execute(datediff)
        for w in cursor:
            datediff = int(w[0])
        if datediff < 0:
            currentfineforuser = "SELECT count(*) FROM Fine where memberID = '"+membershipID2+"';"
            cursor.execute(currentfineforuser)
            for a in cursor:
                currentfine = int(a[0])
            if currentfine == 0:
                newfineamount= str(abs(datediff))
                newtotalfine = "INSERT INTO Fine VALUES('"+membershipID2+"', '"+newfineamount+"');"
                cursor.execute(newtotalfine)
                connection.commit()
                returnedwithfines()
            else:
                currentfineforuser2 = "SELECT fineAmount FROM Fine where memberID = '"+membershipID2+"';"
                cursor.execute(currentfineforuser2)
                for b in cursor:
                    currentfine2 = int(b[0])
                newfineamount = str(currentfine2 + abs(datediff))
                remove = "DELETE FROM Fine WHERE memberID = '"+membershipID2+"';"
                cursor.execute(remove)
                connection.commit()
                newtotalfine = "INSERT INTO Fine VALUES('"+membershipID2+"', '"+newfineamount+"');"
                cursor.execute(newtotalfine)
                connection.commit()
                returnedwithfines()
        else:
            messagebox.showinfo('Success', "Book Successfully Returned")
    else:
        messagebox.showinfo('Error!', "Invalid Book Id")


def returnedwithfines():
    error_top = Tk()

    error_top.title("Confirmation Page")
    error_top.minsize(width = 200, height = 200)
    error_top.geometry("400x400")


    Canvas1 = Canvas(error_top)
    
    Canvas1.config(bg="Red")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_text(215,50, text="ERROR!", fill = "Yellow", font = ('Courier', 60))
    Canvas1.create_text(215,200, text="Book returned successfully:", fill = "Yellow", font = ('Courier', 20), justify = "center")
    Canvas1.create_text(200,230, text='but has fines', fill = "Yellow", font = ('Courier', 20), justify = "center")
    Canvas1.pack()
    
    btn1 = Button(error_top,text="Back to\n Return Function",bg='green', fg='black', command=lambda:[top.destroy(), error_top.destroy(), bookReturning()])
    btn1.place(x=140, y=300, relwidth=0.3,relheight=0.15)    
