# Connecting MySQL Database to Python
import mysql.connector as a
con = a.connect(host="localhost", user="root", password="golaghat@123", database="ldms")


# Add function used to add details of a book
def addbook():
    print("\t ADDING BOOK DATA INTO DATABASE ")
    print("*************************************************************************")
    bn = input("Enter BOOK Name: ")
    c = input("Enter BOOK Code: ")
    t = input("Total BOOKS: ")
    s = input("Enter Subject: ")
    data = (bn,c,t,s)
    sql = "insert into books values(%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    print(">------------------------------------------------------------------------<\n")
    print("")
    main()

# issue book function used to issue a book to a particular student
def issueb():
    print("\t ISSUING BOOK TO A STUDENT ")
    print("*************************************************************************")
    n = input("Enter Name: ")
    r = input("Enter Reg. No: ")
    co = input("Enter Book Code: ")
    d = input("Enter Date: ")
    data = (n,r,co,d)
    a = "insert into issued values(%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(a,data)
    
    con.commit()
    print("Book issued to: ",n)
    print(">------------------------------------------------------------------------<\n")
    print("")
    bookup(co,-1)

# Submit Book function used to submit the book that the student borrowed
def submitb():
    print("\t RECEIVING BORROWED BOOK FROM STUDENT ")
    print("*************************************************************************")
    n = input("Enter Name: ")
    r = input("Enter Reg. No: ")
    co = input("Enter Book Code: ")
    d = input("Enter Date: ")
    data = (n,r,co,d)
    a = "insert into submit values(%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print("Book is Submitted from: ",n)
    print(">------------------------------------------------------------------------<\n")
    print("")
    bookup(co,1)

# This function updates record in 'Book' Table in the database
def bookup(co,u):
    a = "select TOTAL from books where BCODE = %s"
    data = (co,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    t = myresult[0] + u
    sql = "update books set TOTAL = %s where BCODE = %s"
    d = (t,co)
    c.execute(sql,d)
    con.commit()
    main() 

# This function used to delete details of a book using it's ID
def deleteb():
    print("\t DELETING BOOK RECORD FROM THE DATABASE ")
    print("*************************************************************************")
    ac = input("Enter Book Code: ")
    a = "delete from books where bcode = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print("Book data deleted")
    print(">------------------------------------------------------------------------<\n")
    print("")
    main()
    
# This Funtion used to display all the details of the book
def dispbook():
    print("\t BOOK DETAILS ")
    print("*************************************************************************")
    a = "select * from books"
    c = con.cursor()
    c.execute(a)
    myresult = c.fetchall()
    for i in myresult:
        print("Book Name: " ,i[0])
        print("Book code: " ,i[1])
        print("Total: " ,i[2])
        print("Subject: " ,i[3])
        print(">------------------------------------------------------------------------<\n")
        print("")
    main()

# THE MAIN PROGRAME STARTS FROM HERE
def main():
    print("|***********************************************************************************|\n")
    print("|                         \tLIBRARY MANAGER                                     |\n")
    print("|***********************************************************************************|\n" )                                        
    print("|                           1.ADD BOOK                                              |\n")
    print("|                           2.ISSUE BOOK                                            |\n")
    print("|                           3.SUBMIT BOOK                                           |\n")
    print("|                           4.DELETE BOOK                                           |\n")
    print("|                           5.DISPLAY BOOKS                                         |\n")
    print("|                           6.EXIT                                                  |\n")
    print("*************************************************************************************")
    choice = input("Enter Task No:")
    print(">------------------------------------------------------------------------<\n")
    print("")
    if (choice == '1'):
        addbook()
    elif (choice == '2'):
        issueb()
    elif (choice == '3'):
        submitb()        
    elif (choice == '4'):
        deleteb()
    elif (choice == '5'):
        dispbook()
    elif (choice == '6'):
        exit()        
    else:
        print("Wrong Choice!!!")
        main()

# System Password Login
def pswd():
    ps = input("Enter Password: ")
    if ps == "techtoy007":
        main()
    else:
        print("Wrong password!!!")

pswd()       
