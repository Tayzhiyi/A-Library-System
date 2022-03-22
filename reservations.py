from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql

def reservationsMenu():
    global headingFrame1,headingFrame2,headingLabel,Canvas1,btn1,btn2,labelFrame,backBtn, root
    root = Tk()
    root.title("Reservations")
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
    
    btn1 = Button(root,text="Book Reservation",bg='black', fg='black', command=bookReservation)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Reservation Cancellation",bg='black', fg='black', command=reservationCancellation)
    btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(root,text="Back To Main Menu",bg='#455A64', fg='black', command=root.destroy)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

##Function 1: to get user input##
def bookReservation():
    global accessionID
    global membershipID
    global reservationdate
    global headingFrame1,LabelFrame,headingLabel,Canvas1,backBtn,SubmitBtn

    #destroy is to remove whatever is on the screen 
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()
    backBtn.destroy()

    #set bg colour
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#f7f1e3")
    Canvas1.pack(expand=True,fill=BOTH)
    
    #add a heading Frame
    headingFrame1 = Frame(root, bg="#FFBB00", bd=6)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    headingLabel = Label(headingFrame1, text="To Reserve a Book, Please Enter Information below:", bg="black", fg="white", font=('Courier', 13))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    #frame for form
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #accessionID
    lb1 = Label(LabelFrame, text="Accession Number: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.35, relheight=0.08)
    #entry label for accession Id
    accessionID = Entry(LabelFrame)
    accessionID.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    #membership ID
    lb2 = Label(LabelFrame, text="Membership ID: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.50, relheight=0.08)
    #entry label for membership Id
    membershipID = Entry(LabelFrame)
    membershipID.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    #reservation date
    lb3 = Label(LabelFrame, text="Reserve Date:\n(YYYY/MM/DD)", bg="black", fg="white")
    lb3.place(relx=0.05, rely=0.6, relheight=0.18)
    #entry for reservation date
    reservationdate = Entry(LabelFrame)
    reservationdate.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    #submit Button
    SubmitBtn = Button(root, text="Reserve Book", bg="#d1ccc0", fg="black", command=testingfactor1)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #back Button
    backBtn = Button(root,text="Back To\nReservation Menu",bg='#455A64', fg='black', command=lambda:[root.destroy(), reservationsMenu()])
    backBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def testingfactor1():
    accessionID2 = accessionID.get()
    membershipID2 = membershipID.get()

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase);
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
        BookReservationConfirmation()

def BookReservationConfirmation():
    global headingFrame1,headingLabel,Canvas1,btn1,backBtn,root_confirm

    accessionID2 = accessionID.get()
    membershipID2 = membershipID.get()
    reservation_date2 =reservationdate.get()  

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase);
    cursor = connection.cursor();

    #Get title from accession number
    infoGetter = "SELECT title FROM Book WHERE accessionNo = '"+accessionID2+"';"
    cursor.execute(infoGetter)
    for i in cursor:
        title = i[0]

    #Get Member name from membership_id
    member_names = "SELECT name FROM Member WHERE memberID = '"+membershipID2+"';"
    cursor.execute(member_names)
    for z in cursor:
        member_name = z[0]

    root_confirm = Tk()
    root_confirm.title("Confirmation Page")
    root_confirm.minsize(width = 200, height = 300)
    root_confirm.geometry("300x400") 
        
    Canvas1 = Canvas(root_confirm)
    Canvas1.config(bg="green")
    Canvas1.pack(expand=True, fill=BOTH)
        
    headingFrame1 = Frame(root_confirm,bg="green")
    headingFrame1.place(relx=0.01,rely=0.01,relwidth=0.9,relheight=0.1)
            
    headingLabel = Label(headingFrame1, text="Confirm Reservation \nDetails To Be Correct", bg='green', fg='black', font=('Courier', 15))
    headingLabel.place(relx=0.05,rely=0.1, relwidth=1, relheight=1)
        
    bodyLabel1 = Label(root_confirm, text="Accession Number: {0}".format(accessionID2), bg='green', fg='black', font=('Courier', 12))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.1)
        
    bodyLabel2 = Label(root_confirm, text="Book Title:\n{0}".format(title), bg='green', fg='black', font=('Courier', 12))
    bodyLabel2.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.1)
        
    bodyLabel3 = Label(root_confirm, text="Membership ID: {0}".format(membershipID2), bg='green', fg='black', font=('Courier', 12))
    bodyLabel3.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.1)
        
    bodyLabel4 = Label(root_confirm, text="Name: {0}".format(member_name), bg='green', fg='black', font=('Courier', 12))
    bodyLabel4.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.1)
        
    bodyLabel5 = Label(root_confirm, text="Reserve Date:\n{0}".format(reservation_date2), bg='green', fg='black', font=('Courier', 12))
    bodyLabel5.place(relx=0.1,rely=0.6,relwidth=0.8,relheight=0.1)
        
    btn1 = Button(root_confirm,text="Confirm\nReservation",bg='black', fg='black', command=lambda:[bookReservationCheck(), root_confirm.destroy()])
    btn1.place(relx=0.1,rely=0.8, relwidth=0.3,relheight=0.15)
        
    backBtn = Button(root_confirm,text="Back To\nReserve\nFunction",bg='#455A64', fg='black', command=lambda:[root_confirm.destroy(), bookReservation()])
    backBtn.place(relx=0.6,rely=0.8, relwidth=0.3,relheight=0.15)

def bookReservationCheck():
    member_id = membershipID.get()
    accession_no = accessionID.get()
    reservation_date = reservationdate.get()
    
    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase)
    cursor = connection.cursor()

    def checkfineamount(member_id):  #checkfineamount
        checkfineamount = "SELECT fineAmount FROM Fine WHERE memberID = '%s'" % (member_id)
        cursor.execute(checkfineamount)
        amount = '0'
        for i in cursor:
            if len(i) != 0:
                return i[0]
        return amount

    def numofreservations(member_id): #checknumberofreservation
        numofreservations ="SELECT COUNT(memberID) FROM Reservation WHERE memberID = '%s'" % (member_id)
        cursor.execute(numofreservations)
        for i in cursor:
            return i[0]

    try:
        if numofreservations(member_id) == 2:
            reservedmorethantwo()
        elif checkfineamount(member_id) != '0':
            amount = checkfineamount(member_id)
            hasfines(amount)
        else:
                addbookreservation = "INSERT INTO Reservation VALUES ('%s','%s','%s')" % (accession_no, member_id, reservation_date)
                cursor.execute(addbookreservation)
                connection.commit()
                messagebox.showinfo('Success!', "Book has been reserved.")
    except:
        messagebox.showinfo('Error', "Should not happen")

    root.destroy()


def reservedmorethantwo():
    top = Tk()

    top.title("Error!")
    top.minsize(width = 200, height = 200)
    top.geometry("400x400")

    Canvas1 = Canvas(top)
    
    Canvas1.config(bg="Red")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_text(215,50, text="ERROR!", fill = "Yellow", font = ('Courier', 60))
    Canvas1.create_text(215,200, text="Member currently has:", fill = "Yellow", font = ('Courier', 20), justify = "center")
    Canvas1.create_text(200,230, text="2 Books on Reservation", fill = "Yellow", font = ('Courier', 20), justify = "center")
    Canvas1.pack()
    
    btn1 = Button(top,text="Back to\n Reserve Function",bg='green', fg='black', command=lambda:[top.destroy(), reservationsMenu()])
    btn1.place(x=140, y=300, relwidth=0.3,relheight=0.15)


def hasfines(amount):
    error_top = Tk()

    error_top.title("Error!")
    error_top.minsize(width = 200, height = 200)
    error_top.geometry("400x400")


    Canvas1 = Canvas(error_top)
    
    Canvas1.config(bg="Red")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_text(215,50, text="ERROR!", fill = "Yellow", font = ('Courier', 60))
    Canvas1.create_text(215,200, text="Member has Outstanding Fine of: ", fill = "Yellow", font = ('Courier', 20), justify = "center")
    Canvas1.create_text(200,230, text=f'${str(amount)}', fill = "Yellow", font = ('Courier', 20), justify = "center")
    Canvas1.pack()
    
    btn1 = Button(error_top,text="Back to\n Reserve Function",bg='green', fg='black', command=lambda:[error_top.destroy(), reservationsMenu()])
    btn1.place(x=140, y=300, relwidth=0.3,relheight=0.15)
    
##Reservation Cancellation##
def reservationCancellation():
    global accessionIDR
    global membershipIDR
    global canceldate
    global headingFrame1,LabelFrame,headingLabel,Canvas1,backBtn,SubmitBtn

    # destroy is to remove whatever is on the screen 
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    #btn2.destroy()
    backBtn.destroy()

    #set bg colour
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#f7f1e3")
    Canvas1.pack(expand=True,fill=BOTH)
    
    #add a heading Frame
    headingFrame1 = Frame(root, bg="#FFBB00", bd=6)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    headingLabel = Label(headingFrame1, text="To cancel a Reservation, Please Enter Information Below:", bg="black", fg="white", font=('Courier', 13))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    #frame for form
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #accessionID
    lb1 = Label(LabelFrame, text="Accession Number: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.35, relheight=0.08)
    #entry label for accession Id
    accessionIDR = Entry(LabelFrame)
    accessionIDR.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    #membership ID
    lb2 = Label(LabelFrame, text="Membership ID: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.50, relheight=0.08)
    #entry label for membership Id
    membershipIDR = Entry(LabelFrame)
    membershipIDR.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    #cancel date
    lb3 = Label(LabelFrame, text="Cancel Date:\n(YYYY/MM/DD)", bg="black", fg="white")
    lb3.place(relx=0.05, rely=0.60, relheight=0.18)
    #entry for reservation date
    canceldate = Entry(LabelFrame)
    canceldate.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    #submit Button
    SubmitBtn = Button(root, text="Cancel Reservation", bg="#d1ccc0", fg="black", command=testingfactor2)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #back Button
    backBtn = Button(root,text="Back To\nReservation Menu",bg='#455A64', fg='black', command=lambda:[root.destroy(), reservationsMenu()])
    backBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def testingfactor2():
    accessionID3 = accessionIDR.get()
    membershipID3 = membershipIDR.get()

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase);
    cursor = connection.cursor(); 

    #test if user is in database
    userquery = "SELECT COUNT(*) FROM Member WHERE memberID = '"+membershipID3+"';"
    cursor.execute(userquery)
    for i in cursor:
        useravailable = i[0]
    bookquery = "SELECT COUNT(*) FROM Book WHERE accessionNo = '"+accessionID3+"';"
    cursor.execute(bookquery)
    for j in cursor:
        bookavailable = j[0]
    if useravailable == 0 or bookavailable == 0:
        messagebox.showinfo("Error!", "Reservation not available")
    else:
        BookCancellationConfirmation()

def BookCancellationConfirmation():
    global headingFrame1,headingLabel,Canvas1,btn1,backBtn,root_confirm
    accessionID3 = accessionIDR.get()
    membershipID3 = membershipIDR.get()
    cancellation_date3 =canceldate.get()  #double check 

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase);
    cursor = connection.cursor();

    #Get title from accession number
    infoGetter = "SELECT title FROM Book WHERE accessionNo = '"+accessionID3+"';"
    cursor.execute(infoGetter)
    for i in cursor:
        title = i[0]

    #Get Member name from membership_id
    member_names = "SELECT name FROM Member WHERE memberID = '"+membershipID3+"';"
    cursor.execute(member_names)
    for z in cursor:
        member_name = z[0]

    root_confirm = Tk()
    root_confirm.title("Confirmation Page")
    root_confirm.minsize(width = 200, height = 300)
    root_confirm.geometry("300x400") 
        
    Canvas1 = Canvas(root_confirm)
    Canvas1.config(bg="green")
    Canvas1.pack(expand=True, fill=BOTH)
        
    headingFrame1 = Frame(root_confirm,bg="green")
    headingFrame1.place(relx=0.01,rely=0.01,relwidth=0.9,relheight=0.2)
            
    headingLabel = Label(headingFrame1, text="Confirm Reservation\nCancellation Details\nTo Be Correct", bg='green', fg='black', font=('Courier', 15))
    headingLabel.place(relx=0.05,rely=0.1, relwidth=1, relheight=1)
        
    bodyLabel1 = Label(root_confirm, text="Accession Number: {0}".format(accessionID3), bg='green', fg='black', font=('Courier', 12))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.1)
        
    bodyLabel2 = Label(root_confirm, text="Book Title: {0}".format(title), bg='green', fg='black', font=('Courier', 12))
    bodyLabel2.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.1)
        
    bodyLabel3 = Label(root_confirm, text="Membership ID: {0}".format(membershipID3), bg='green', fg='black', font=('Courier', 12))
    bodyLabel3.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.1)
        
    bodyLabel4 = Label(root_confirm, text="Member Name: {0}".format(member_name), bg='green', fg='black', font=('Courier', 12))
    bodyLabel4.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.1)
        
    bodyLabel5 = Label(root_confirm, text="Cancellation Date:\n{0}".format(cancellation_date3), bg='green', fg='black', font=('Courier', 12))
    bodyLabel5.place(relx=0.1,rely=0.6,relwidth=0.8,relheight=0.1)
        
    btn1 = Button(root_confirm,text="Confirm\nCancellation",bg='black', fg='black', command=lambda:[bookcancellationCheck(), root_confirm.destroy()])
    btn1.place(relx=0.1,rely=0.8, relwidth=0.3,relheight=0.15)
        
    backBtn = Button(root_confirm,text="Back To\nCancellation\nFunction",bg='#455A64', fg='black', command=lambda:[root_confirm.destroy(), bookCancellation()])
    backBtn.place(relx=0.6,rely=0.8, relwidth=0.3,relheight=0.15)


def bookcancellationCheck():
    member_id = membershipIDR.get()
    accession_id = accessionIDR.get()

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase)
    cursor = connection.cursor()

    def checkreservation(member_id):
        checkreservation = "SELECT COUNT(*) FROM Reservation WHERE memberID = '"+member_id+"' AND accessionNo = '"+accession_id+"';"
        cursor.execute(checkreservation)
        for i in cursor:
            return i[0]
    try: 
        if checkreservation(member_id) == 0:
            noReservation()
        else:  
            deletereservation = "DELETE FROM Reservation WHERE memberID = '"+member_id+"' AND accessionNo = '"+accession_id+"';"
            cursor.execute(deletereservation)
            connection.commit()
            messagebox.showinfo('Success!', "Reservation has been cancelled.")
            root.destroy()
    except: 
        messagebox.showinfo('Error', 'Member not found')

def noReservation():
    error_top = Tk()

    error_top.title("Error!")
    error_top.minsize(width = 200, height = 200)
    error_top.geometry("400x400")


    Canvas1 = Canvas(error_top)
    
    Canvas1.config(bg="Red")
    Canvas1.pack(expand=True, fill=BOTH)

    Canvas1.create_text(215,50, text="ERROR!", fill = "Yellow", font = ('Courier', 60))
    Canvas1.create_text(215,200, text="Member has no such reservation.", fill = "Yellow", font = ('Courier', 20), justify = "center")
    Canvas1.pack()
    
    btn1 = Button(error_top,text="Back to\n Cancellation\n Function",bg='green', fg='black', command=error_top.destroy)
    btn1.place(x=140, y=300, relwidth=0.3,relheight=0.15)
    
