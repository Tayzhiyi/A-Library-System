from tkinter import *
from tkinter import messagebox
import pymysql

def finesMenu():
    global headingFrame1,headingFrame2,headingLabel,Canvas1,labelFrame,btn1,backBtn,root
    root = Tk()
    root.title("Fines Menu")
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
    
    btn1 = Button(root,text="Fine Payment",bg='black', fg='black', command=finePaying)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
    backBtn = Button(root,text="Back To Main Menu",bg='#455A64', fg='black', command=root.destroy)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)


####### FINE PAYMENT #########
def fineConfirmation():
    
    global headingFrame1,headingFrame2,headingLabel,Canvas1,bodyLabel1,bodyLabel2,bodyLabel3,bodyLabel4,btn1,backBtn,root_confirm
    member_id = fineInfo1.get()
    date = fineInfo2.get()
    amount = fineInfo3.get()
    
    if not member_id or not date or not amount:
        missing_fields()
    else:
        root_confirm = Tk()
        root_confirm.title("Confirmation Page")
        root_confirm.minsize(width = 200, height = 300)
        root_confirm.geometry("300x400")
        
        Canvas1 = Canvas(root_confirm)
        Canvas1.config(bg="green")
        Canvas1.pack(expand=True, fill=BOTH)
        
        headingFrame1 = Frame(root_confirm,bg="green")
        headingFrame1.place(relx=0.01,rely=0.01,relwidth=0.8,relheight=0.1)
            
        headingLabel = Label(headingFrame1, text="Please confirm that your \n details are correct", bg='green', fg='black', font=('Courier', 14))
        headingLabel.place(relx=0.1,rely=0.1, relwidth=1, relheight=1)
        
        bodyLabel1 = Label(root_confirm, text="Payment Due:\n${0}".format(amount), bg='green', fg='black', font=('Courier', 12))
        bodyLabel1.place(relx=0.05,rely=0.3,relwidth=0.4,relheight=0.1)
        
        bodyLabel2 = Label(root_confirm, text="Member ID:\n  {0}".format(member_id), bg='green', fg='black', font=('Courier', 12))
        bodyLabel2.place(relx=0.55,rely=0.3,relwidth=0.4,relheight=0.1)
        
        bodyLabel3 = Label(root_confirm, text="Exact Fee Only", bg='green', fg='black', font=('Courier', 12))
        bodyLabel3.place(relx=0.05,rely=0.45,relwidth=0.4,relheight=0.1)
        
        bodyLabel4 = Label(root_confirm, text="Payment Date:\n{0}".format(date), bg='green', fg='black', font=('Courier', 12))
        bodyLabel4.place(relx=0.55,rely=0.45,relwidth=0.4,relheight=0.1)
        
        btn1 = Button(root_confirm,text="Confirm\nPayment",bg='black', fg='black', command=lambda:[finePayment(), root_confirm.destroy()])
        btn1.place(relx=0.1,rely=0.8, relwidth=0.3,relheight=0.15)
        
        backBtn = Button(root_confirm,text="Back To\nPayment\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
        backBtn.place(relx=0.6,rely=0.8, relwidth=0.3,relheight=0.15)

def payment_success():
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
    
    bodyLabel1 = Label(root_confirm, text="Fine successfully paid.", bg='green', fg='black', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nMain\nMenu",bg='#455A64', fg='black', command=lambda:[root_confirm.destroy(), root.destroy()])
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)

def input_error():
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
    
    bodyLabel1 = Label(root_confirm, text="Incorrect input format.", bg='red', fg='yellow', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nPayment\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)
    
def incorrect_fine_amt():
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
    
    bodyLabel1 = Label(root_confirm, text="Incorrect fine payment amount.", bg='red', fg='yellow', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nPayment\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)
    
def member_no_fine():
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
    
    bodyLabel1 = Label(root_confirm, text="Member has no fine.", bg='red', fg='yellow', font=('Courier', 14))
    bodyLabel1.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.2)
    
    backBtn = Button(root_confirm,text="Back To\nPayment\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)

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
    
    backBtn = Button(root_confirm,text="Back To\nPayment\nFunction",bg='#455A64', fg='black', command=root_confirm.destroy)
    backBtn.place(relx=0.35,rely=0.8, relwidth=0.3,relheight=0.15)
    
def finePayment():
    member_id = fineInfo1.get()
    date = fineInfo2.get()
    amount = fineInfo3.get()
    
    def fineChecker(member_id):
        fineChecker = "SELECT * FROM Fine WHERE memberID = '%s'" % (member_id)
        cursor.execute(fineChecker)
        for i in cursor:
            return i[0]
    
    def fineAmountChecker(member_id, amount):
        fineAmountChecker = "SELECT fineAmount FROM Fine WHERE memberID = '%s'" % (member_id)
        cursor.execute(fineAmountChecker)
        for i in cursor:
            return i[0] == amount
        
    payFineRecord = "INSERT INTO FinePayment VALUES ('"+member_id+"','"+date+"','"+amount+"')"
    payFine = "DELETE FROM Fine WHERE memberID = '%s'" % (member_id)
    
    if fineChecker(member_id) or fineAmountChecker(member_id, '0'):
        if fineAmountChecker(member_id, amount):
            try:
                cursor.execute(payFine)
                cursor.execute(payFineRecord)
                connection.commit()
                payment_success()

            except:
                connection.rollback()
                input_error()
        else:
            incorrect_fine_amt()
    else:
        member_no_fine()

    fineInfo1.delete(0, END)
    fineInfo2.delete(0, END)
    fineInfo3.delete(0, END)


def finePaying():
    global fineInfo1, fineInfo2, fineInfo3, connection, cursor

    mypass=''
    mydatabase = 'ALibrarySystem'

    connection = pymysql.connect(host = 'localhost', user = 'root', password = mypass, database = mydatabase);
    cursor = connection.cursor();

    # destroy is to remove whatever is on the screen
    global headingFrame1,headingFrame2,headingLabel,Canvas1,labelFrame,backBtn
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    backBtn.destroy()

    #set bg colour
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#f7f1e3")
    Canvas1.pack(expand=True,fill=BOTH)

    #add a heading Frame
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.13)
    headingLabel = Label(headingFrame1, text="To pay a fine, please enter information below:", bg="black", fg="white", font=('Courier', 14))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    #frame for form
    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    #member ID
    lb1 = Label(LabelFrame, text="Membership ID: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    #entry label for member Id
    fineInfo1 = Entry(LabelFrame)
    fineInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    #payment date
    lb2 = Label(LabelFrame, text="Payment Date: \n(YYYY/MM/DD)", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.3, relheight=0.18)
    #entry for payment date
    fineInfo2 = Entry(LabelFrame)
    fineInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    #payment amount
    lb3 = Label(LabelFrame, text="Payment Amount: ", bg="black", fg="white")
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)
    #entry for payment amount
    fineInfo3 = Entry(LabelFrame)
    fineInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    #submit Button
    SubmitBtn = Button(root, text="Pay Fine", bg="#d1ccc0", fg="black", command=fineConfirmation)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #Quit button
    QuitBtn = Button(root, text="Back to Fines Menu", bg="#f7f1e3", fg="black", command=lambda:[root.destroy(), finesMenu()])
    QuitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


