from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql

def membershipMenu():

    global headingFrame1,headingFrame2,headingLabel,Canvas1,labelFrame,backBtn,root,btn1,btn2,btn3
    root = Tk()
    root.title("Membership Menu")
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
    
    btn1 = Button(root,text="Membership Creation",bg='black', fg='black', command=memberCreation)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
    btn2 = Button(root,text="Membership Deletion",bg='black', fg='black', command=memberDeletion)
    btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)
    
    btn3 = Button(root,text="Membership Update",bg='black', fg='black', command=memberUpdating1)
    btn3.place(relx=0.28,rely=0.60, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(root,text="Back To Main Menu",bg='#455A64', fg='black', command=root.destroy)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)


####### MEMBER REGISTRATION AND CREATION #########   
def memberCreation():
    global memberInfo1, memberInfo2, memberInfo3, memberInfo4, memberInfo5, connection, cursor

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
    backBtn.destroy()

    #set bg colour
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#f7f1e3")
    Canvas1.pack(expand=True,fill=BOTH)

    #add a heading Frame
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    headingLabel = Label(headingFrame1, text="To create membership, please enter the requested information below:", bg="black", fg="white", font=('Courier', 14))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    #frame for form
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #member ID
    def getMaxMemberID():
        maxMemberID = "SELECT MAX(substring(memberID, 2)) FROM Member"
        cursor.execute(maxMemberID)
        for i in cursor:
            return i
    maxMemberID = int(getMaxMemberID()[0])
    nextID = "A" + str(maxMemberID + 1)
    
    lb1 = Label(LabelFrame, text="Membership ID: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    #entry label for member Id
    memberLabel = Label(LabelFrame, text=nextID, bg="black", fg="white")
    memberLabel.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    #name
    lb2 = Label(LabelFrame, text="Name: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
    #entry for name
    memberInfo2 = Entry(LabelFrame)
    memberInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    #faculty
    lb3 = Label(LabelFrame, text="Faculty: ", bg="black", fg="white")
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)
    #entry for faculty
    memberInfo3 = Entry(LabelFrame)
    memberInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    #phone number
    lb4 = Label(LabelFrame, text="Phone Number: ", bg="black", fg="white")
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)
    #entry for phone number
    memberInfo4 = Entry(LabelFrame)
    memberInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)
    
    #email
    lb5 = Label(LabelFrame, text="Email Address: ", bg="black", fg="white")
    lb5.place(relx=0.05, rely=0.80, relheight=0.08)
    #entry for email
    memberInfo5 = Entry(LabelFrame)
    memberInfo5.place(relx=0.3, rely=0.80, relwidth=0.62, relheight=0.08)

    #submit Button
    SubmitBtn = Button(root, text="Create Member", bg="#d1ccc0", fg="black", command=memberRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #Quit button
    QuitBtn = Button(root, text="Back to\nMembership Menu", bg="#f7f1e3", fg="black", command=lambda:[root.destroy(), membershipMenu()])
    QuitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
    
def missing_fields():
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
    
    bodyLabel1 = Label(root_confirm, text="Missing or Incomplete fields.", bg='red', fg='yellow', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nCreate\nFunction",bg='#455A64', fg='black', command=lambda:[root_confirm.destroy(), memberCreation()])
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)

def membership_success():
    ## Success popup
    root_confirm = Tk()
    root_confirm.title("Success")
    root_confirm.minsize(width = 200, height = 300)
    root_confirm.geometry("300x400")
    
    Canvas1 = Canvas(root_confirm)
    Canvas1.config(bg="green")
    Canvas1.pack(expand=True, fill=BOTH)
    
    headingFrame1 = Frame(root_confirm,bg="green")
    headingFrame1.place(relx=0.01,rely=0.01,relwidth=0.9,relheight=0.1)
        
    headingLabel = Label(headingFrame1, text="Success!", bg='green', fg='black', font=('Courier', 15))
    headingLabel.place(relx=0.05,rely=0.1, relwidth=1, relheight=1)
    
    bodyLabel1 = Label(root_confirm, text="ALS Membership created.", bg='green', fg='black', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nMain\nMenu",bg='#455A64', fg='black', command=lambda:[root_confirm.destroy(), root.destroy()])
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)
        
def membership_exists():
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
    
    bodyLabel1 = Label(root_confirm, text="Member already exist.\nMembership ID in use.", bg='red', fg='yellow', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nCreate\nFunction",bg='#455A64', fg='black', command=lambda:[root_confirm.destroy(), memberCreation()])
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)

        
def memberRegister():
    member_id = nextID
    name = memberInfo2.get()
    faculty = memberInfo3.get()
    phone_number = memberInfo4.get()
    email = memberInfo5.get()

    insertMember = "INSERT INTO Member (memberID, name, faculty, phoneNo, email) VALUES ('"+member_id+"','"+name+"','"+faculty+"','"+phone_number+"', '"+email+"')"
    
    if not member_id or not name or not faculty or not phone_number or not email:
        missing_fields()
    else:
        try:
            cursor.execute(insertMember)
            connection.commit()
            membership_success()
            
        except:
            connection.rollback()
            membership_exists()
            
    memberInfo2.delete(0, END)
    memberInfo3.delete(0, END)
    memberInfo4.delete(0, END)
    memberInfo5.delete(0, END)

####### MEMBER DELETION #########
def memberInfoGetter(member_id):
    infoGetter = "SELECT * FROM Member WHERE memberID = '%s'" % (member_id)
    cursor.execute(infoGetter)
    for i in cursor:
        return i
        
def member_not_in_database1():
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
    
    bodyLabel1 = Label(root_confirm, text="Member not in database.", bg='red', fg='yellow', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nDelete\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)
    
def deleteMemberConfirmation():
    global headingFrame1,headingFrame2,headingLabel,Canvas1,bodyLabel1,bodyLabel2,bodyLabel3,bodyLabel4,bodyLabel5,btn1,backBtn,root_confirm
    member_id = memberInfo1.get()
    
    memberDetails = memberInfoGetter(member_id)
    
    if not memberDetails:
        member_not_in_database1()
    
    else:
        name = memberDetails[1]
        faculty = memberDetails[2]
        phone_number = memberDetails[3]
        email = memberDetails[4]
        
        root_confirm = Tk()
        root_confirm.title("Confirmation Page")
        root_confirm.minsize(width = 200, height = 300)
        root_confirm.geometry("300x400")
        
        Canvas1 = Canvas(root_confirm)
        Canvas1.config(bg="green")
        Canvas1.pack(expand=True, fill=BOTH)
        
        headingFrame1 = Frame(root_confirm,bg="green")
        headingFrame1.place(relx=0.01,rely=0.01,relwidth=0.9,relheight=0.1)
            
        headingLabel = Label(headingFrame1, text="Please confirm that your \ndetails are correct", bg='green', fg='black', font=('Courier', 15))
        headingLabel.place(relx=0.05,rely=0.1, relwidth=1, relheight=1)
        
        bodyLabel1 = Label(root_confirm, text="Member ID: {0}".format(member_id), bg='green', fg='black', font=('Courier', 12))
        bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.1)
        
        bodyLabel2 = Label(root_confirm, text="Name: {0}".format(name), bg='green', fg='black', font=('Courier', 12))
        bodyLabel2.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.1)
        
        bodyLabel3 = Label(root_confirm, text="Faculty: {0}".format(faculty), bg='green', fg='black', font=('Courier', 12))
        bodyLabel3.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.1)
        
        bodyLabel4 = Label(root_confirm, text="Phone Number: {0}".format(phone_number), bg='green', fg='black', font=('Courier', 12))
        bodyLabel4.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.1)
        
        bodyLabel5 = Label(root_confirm, text="Email Address:\n{0}".format(email), bg='green', fg='black', font=('Courier', 12))
        bodyLabel5.place(relx=0.1,rely=0.6,relwidth=0.8,relheight=0.1)
        
        btn1 = Button(root_confirm,text="Confirm\nDeletion",bg='black', fg='black', command=lambda:[deleteMember(), root_confirm.destroy()])
        btn1.place(relx=0.1,rely=0.8, relwidth=0.3,relheight=0.15)
        
        backBtn = Button(root_confirm,text="Back To\nDelete\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
        backBtn.place(relx=0.6,rely=0.8, relwidth=0.3,relheight=0.15)
    
def delete_success():
    root_confirm = Tk()
    root_confirm.title("Success")
    root_confirm.minsize(width = 200, height = 300)
    root_confirm.geometry("300x400")
    
    Canvas1 = Canvas(root_confirm)
    Canvas1.config(bg="green")
    Canvas1.pack(expand=True, fill=BOTH)
    
    headingFrame1 = Frame(root_confirm,bg="green")
    headingFrame1.place(relx=0.01,rely=0.01,relwidth=0.9,relheight=0.1)
        
    headingLabel = Label(headingFrame1, text="Success!", bg='green', fg='black', font=('Courier', 15))
    headingLabel.place(relx=0.05,rely=0.1, relwidth=1, relheight=1)
    
    bodyLabel1 = Label(root_confirm, text="Member Deleted.", bg='green', fg='black', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nMain\nMenu",bg='#455A64', fg='black', command=lambda:[root_confirm.destroy(), root.destroy()])
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)
    
def has_outstanding_fines():
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
    
    bodyLabel1 = Label(root_confirm, text="Member has loans or\noutstanding fines.", bg='red', fg='yellow', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nDelete\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)
    
def deleteMember():
    member_id = memberInfo1.get()
    deleteMember = "DELETE FROM Member WHERE memberID = '%s'" % (member_id)
    ## dunnid to do specific handling of cases because the foreign key constraints already handles it
    try:
        cursor.execute(deleteMember)
        connection.commit()
        delete_success()
        
    except:
        connection.rollback()
        has_outstanding_fines()

    memberInfo1.delete(0, END)
        
def memberDeletion():
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
    headingLabel = Label(headingFrame1, text="To delete member, please enter Membership ID:", bg="black", fg="white", font=('Courier', 14))
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
    SubmitBtn = Button(root, text="Delete Member", bg="#d1ccc0", fg="black", command=deleteMemberConfirmation)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)
    
    #Quit button
    QuitBtn = Button(root, text="Back to\nMembership Menu", bg="#f7f1e3", fg="black", command=lambda:[root.destroy(), membershipMenu()])
    QuitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


####### MEMBER UPDATE #########
def memberUpdating1():
    global memberInfo1, connection, cursor

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase);
    cursor = connection.cursor();

    # destroy is to remove whatever is on the screen
    global headingFrame1,headingFrame2,headingLabel,Canvas1,LabelFrame,SubmitBtn,QuitBtn
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
    headingLabel = Label(headingFrame1, text="To update member, please enter Membership ID:", bg="black", fg="white", font=('Courier', 14))
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
    
    #submit Button
    SubmitBtn = Button(root, text="Update Member", bg="#d1ccc0", fg="black", command=memberUpdating2)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #Quit button
    QuitBtn = Button(root, text="Back to\nMembership Menu", bg="#f7f1e3", fg="black", command=lambda:[root.destroy(), membershipMenu()])
    QuitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
    
def member_not_in_database2():
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
    
    bodyLabel1 = Label(root_confirm, text="Member not in database.", bg='red', fg='yellow', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nUpdate\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)
    
def memberUpdating2():
    global memberInfo2, memberInfo3, memberInfo4, memberInfo5
    member_id = memberInfo1.get()
    memberDetails = memberInfoGetter(member_id)
    
    global headingFrame1,headingLabel,Canvas1,labelFrame,backBtn,SubmitBtn,QuitBtn
    if not memberDetails:
        member_not_in_database2()
    else:
        # destroy is to remove whatever is on the screen
        headingFrame1.destroy()
        headingLabel.destroy()
        Canvas1.destroy()
        SubmitBtn.destroy()
        QuitBtn.destroy()
        
        #set bg colour
        Canvas1 = Canvas(root)
        Canvas1.config(bg="#f7f1e3")
        Canvas1.pack(expand=True,fill=BOTH)

        #add a heading Frame
        headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
        headingLabel = Label(headingFrame1, text="Please enter requested information below:", bg="black", fg="white", font=('Courier', 14))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        #frame for form
        LabelFrame = Frame(root, bg="black")
        LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)
        
        #member ID
        lb1 = Label(LabelFrame, text="Membership ID: ", bg="black", fg="white")
        lb1.place(relx=0.05, rely=0.2, relheight=0.08)
        #entry label for member Id
        memberLabel = Label(LabelFrame, text=memberInfo1.get(), bg="black", fg="white")
        memberLabel.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
        
        #name
        lb2 = Label(LabelFrame, text="Name: ", bg="black", fg="white")
        lb2.place(relx=0.05, rely=0.35, relheight=0.08)
        #entry for name
        memberInfo2 = Entry(LabelFrame)
        memberInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

        #faculty
        lb3 = Label(LabelFrame, text="Faculty: ", bg="black", fg="white")
        lb3.place(relx=0.05, rely=0.50, relheight=0.08)
        #entry for faculty
        memberInfo3 = Entry(LabelFrame)
        memberInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

        #phone number
        lb4 = Label(LabelFrame, text="Phone Number: ", bg="black", fg="white")
        lb4.place(relx=0.05, rely=0.65, relheight=0.08)
        #entry for phone number
        memberInfo4 = Entry(LabelFrame)
        memberInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)
        
        #email
        lb5 = Label(LabelFrame, text="Email Address: ", bg="black", fg="white")
        lb5.place(relx=0.05, rely=0.80, relheight=0.08)
        #entry for email
        memberInfo5 = Entry(LabelFrame)
        memberInfo5.place(relx=0.3, rely=0.80, relwidth=0.62, relheight=0.08)

        #submit Button
        SubmitBtn = Button(root, text="Update Member", bg="#d1ccc0", fg="black", command=memberUpdateConfirmation)
        SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

        #Quit button
        QuitBtn = Button(root, text="Back to\nMembership Menu", bg="#f7f1e3", fg="black", command=lambda:[root.destroy(), membershipMenu()])
        QuitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

        root.mainloop()

def missing_fields1():
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
    
    bodyLabel1 = Label(root_confirm, text="Missing or Incomplete fields", bg='red', fg='yellow', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nUpdate\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)

def memberUpdateConfirmation():
    global headingFrame1,headingFrame2,headingLabel,Canvas1,bodyLabel1,bodyLabel2,bodyLabel3,bodyLabel4,bodyLabel5,btn1,backBtn,root_confirm
    member_id = memberInfo1.get()
    name = memberInfo2.get()
    faculty = memberInfo3.get()
    phone_number = memberInfo4.get()
    email = memberInfo5.get()
    
    if not member_id or not name or not faculty or not phone_number or not email:
        missing_fields1()
    else:
        root_confirm = Tk()
        root_confirm.title("Confirmation Page")
        root_confirm.minsize(width = 200, height = 300)
        root_confirm.geometry("300x400")
        
        Canvas1 = Canvas(root_confirm)
        Canvas1.config(bg="green")
        Canvas1.pack(expand=True, fill=BOTH)
        
        headingFrame1 = Frame(root_confirm,bg="green")
        headingFrame1.place(relx=0.01,rely=0.01,relwidth=0.9,relheight=0.1)
            
        headingLabel = Label(headingFrame1, text="Please confirm that your \ndetails are correct", bg='green', fg='black', font=('Courier', 15))
        headingLabel.place(relx=0.05,rely=0.1, relwidth=1, relheight=1)
        
        bodyLabel1 = Label(root_confirm, text="Member ID: {0}".format(member_id), bg='green', fg='black', font=('Courier', 12))
        bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.1)
        
        bodyLabel2 = Label(root_confirm, text="Name: {0}".format(name), bg='green', fg='black', font=('Courier', 12))
        bodyLabel2.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.1)
        
        bodyLabel3 = Label(root_confirm, text="Faculty: {0}".format(faculty), bg='green', fg='black', font=('Courier', 12))
        bodyLabel3.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.1)
        
        bodyLabel4 = Label(root_confirm, text="Phone Number: {0}".format(phone_number), bg='green', fg='black', font=('Courier', 12))
        bodyLabel4.place(relx=0.1,rely=0.5,relwidth=0.8,relheight=0.1)
        
        bodyLabel5 = Label(root_confirm, text="Email Address:\n{0}".format(email), bg='green', fg='black', font=('Courier', 12))
        bodyLabel5.place(relx=0.1,rely=0.6,relwidth=0.8,relheight=0.1)
        
        btn1 = Button(root_confirm,text="Confirm\nUpdate",bg='black', fg='black', command=lambda:[updateMember(), root_confirm.destroy()])
        btn1.place(relx=0.1,rely=0.8, relwidth=0.3,relheight=0.15)
        
        backBtn = Button(root_confirm,text="Back To\nUpdate\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
        backBtn.place(relx=0.6,rely=0.8, relwidth=0.3,relheight=0.15)

def update_success():
    root_confirm = Tk()
    root_confirm.title("Success")
    root_confirm.minsize(width = 200, height = 300)
    root_confirm.geometry("300x400")
    
    Canvas1 = Canvas(root_confirm)
    Canvas1.config(bg="green")
    Canvas1.pack(expand=True, fill=BOTH)
    
    headingFrame1 = Frame(root_confirm,bg="green")
    headingFrame1.place(relx=0.01,rely=0.01,relwidth=0.9,relheight=0.1)
        
    headingLabel = Label(headingFrame1, text="Success!", bg='green', fg='black', font=('Courier', 15))
    headingLabel.place(relx=0.05,rely=0.1, relwidth=1, relheight=1)
    
    bodyLabel1 = Label(root_confirm, text="ALS Membership Updated.", bg='green', fg='black', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.1)
    
    btn1 = Button(root_confirm,text="Create\nAnother\nMember",bg='black', fg='black', command=lambda:[root.destroy(), root_confirm.destroy(), membershipMenu()])
    btn1.place(relx=0.1,rely=0.8, relwidth=0.3,relheight=0.15)
    
    backBtn = Button(root_confirm,text="Back To\nMain\nMenu",bg='#455A64', fg='black', command=lambda:[root_confirm.destroy(), root.destroy()])
    backBtn.place(relx=0.6,rely=0.8, relwidth=0.3,relheight=0.15)

def updateMember():
    member_id = memberInfo1.get()
    name = memberInfo2.get()
    faculty = memberInfo3.get()
    phone_number = memberInfo4.get()
    email = memberInfo5.get()

    updateMember = "UPDATE Member SET name = '{0}', faculty = '{1}', phoneNo = '{2}', email = '{3}' \
WHERE memberID = '{4}'".format(name, faculty, phone_number, email, member_id)
    
    try:
        cursor.execute(updateMember)
        connection.commit()
        update_success()
        
    except:
        connection.rollback()
        #messagebox.showinfo('Error!', "Missing or Incomplete fields.")

    memberInfo1.delete(0, END)
    memberInfo2.delete(0, END)
    memberInfo3.delete(0, END)
    memberInfo4.delete(0, END)
    memberInfo5.delete(0, END)

