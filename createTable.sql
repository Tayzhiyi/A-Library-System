CREATE TABLE Book(
	accessionNo	VARCHAR(3) 		NOT NULL,
    title		VARCHAR(100)	NOT NULL,
    isbn		VARCHAR(13)		NOT NULL,
    publisher	VARCHAR(40)		NOT NULL,
    pubYr		VARCHAR(4)		NOT NULL,
    PRIMARY KEY (accessionNo));

CREATE TABLE BookAuthors(
	accessionNo VARCHAR(3) 		NOT NULL,
    authors		VARCHAR(50)		NOT NULL, 
    FOREIGN KEY (accessionNo) REFERENCES Book(accessionNo));
    
CREATE TABLE Member(
	memberID	VARCHAR(10)		NOT NULL,
    name 		VARCHAR(50)		NOT NULL,
    faculty		VARCHAR(30)		NOT NULL,
    phoneNo 	VARCHAR(8)		NOT NULL,
    email		VARCHAR(40)		NOT NULL,
    PRIMARY KEY (memberID));
    
CREATE TABLE Loan(
	accessionNo	VARCHAR(3)	NOT NULL,
	borrowDate	DATE		NOT NULL,
    dueDate		DATE		NOT NULL,
    memberID	VARCHAR(6)	NOT NULL,
    FOREIGN KEY (accessionNo) 	REFERENCES Book(accessionNo),
    FOREIGN KEY (memberID) 		REFERENCES Member(memberID));

CREATE TABLE Fine(
    memberID	VARCHAR(6)	NOT NULL,
    fineAmount	VARCHAR(4)	NOT NULL,
    FOREIGN KEY (memberID) 	REFERENCES Member(memberID));

CREATE TABLE FinePayment(
	memberID		VARCHAR(6)	NOT NULL,	
    paymentDate		DATE		NOT NULL,
    paymentAmount	VARCHAR(4)	NOT NULL,
    FOREIGN KEY (memberID) REFERENCES Member(memberID)	ON DELETE CASCADE);
    
CREATE TABLE Reservation(
	accessionNo		VARCHAR(3) 	NOT NULL,
    memberID		VARCHAR(6)	NOT NULL,
    reservationDate	DATE 		NOT NULL,
    FOREIGN KEY (accessionNo)	REFERENCES Book(accessionNo),
    FOREIGN KEY (memberID)		REFERENCES Member(memberID) 	ON DELETE CASCADE);
    

    


    
    
    
    