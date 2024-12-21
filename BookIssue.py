def issue():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    cursor.execute("select p_id,sum(qty) from Issue group by p_id")
    r=cursor.fetchall()
    h=input("Do you have your Personal ID(yes/no):")
    print("*"*50)
    if h=="yes" or h=="Yes" or h=="YES":
        sno=int(input("Enter the S.No:"))
        b_id=int(input("Enter the Book ID:"))
        P_Id=int(input("Enter Personal ID:"))
        qtyiu=int(input("Enter the Quantity of the Book Issued:"))
        e="insert into issue values('{}','{}','{}','{}')".format(sno,b_id,P_Id,qtyiu)
        cursor.execute(e)
        mydb.commit()
        print("*"*50)
        print("INFORMATION ADDED")
        print("*"*50)
    else:
        print("Please enter Your details here:")
        import BookUser
        BookUser.add_user()
        print("*"*50)
        print("Your Details are being inserted in User Table now can get the book")
        print("*"*50)
        issue()

def search_issue():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    sno=int(input("Enter the S_No:"))
    print("*"*50)
    a="select * from Issue where S_No='{}'".format(sno)
    cursor.execute(a)
    r=cursor.fetchall()
    print(r)
    print("*"*50)

def display_issue():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    cursor.execute("select * from Issue")
    r=cursor.fetchall()
    for i in r:
        print(i)
    print("*"*50)

def  update_issue():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    print("Menu for modification of detail:")
    print("1.Book ID")
    print("2.Personal ID")
    print("3.Quantity")
    print("*"*50)
    x=int(input("Enter the choice to be Modified:"))
    print("*"*50)
    print("NOTE-The Updation will be done on the basis of S_No provided")
    print("*"*50)
    if x==1:
        p=int(input("Enter the S_No of the User:"))
        B_id=input("Enter the modified Book ID:")
        a='update Issue set I_D="{}" where S_No="{}"'.format(B_id,p)
        cursor.execute(a)
        mydb.commit()
        print("*"*50)
        print("UPDATED")
        print("*"*50)
    elif x==2:
        p=int(input("Enter the S_No of the User:"))
        P_Id=input("Enter the modified Personal ID:")
        a="update Issue set P_Id='{}' where S_No='{}'".format(P_Id,p)
        cursor.execute(a)
        mydb.commit()
        print("*"*50)
        print("UPDATED")
        print("*"*50)
    elif x==3:
        p=int(input("Enter the S_No of the User:"))
        qty=input("Enter the modified Quantity:")
        a="update Issue set QTY='{}' where S_No='{}'".format(qty,p)
        cursor.execute(a)
        mydb.commit()
        print("*"*50)
        print("UPDATED")
        print("*"*50)
    else:
        print("Invalid Entry")
        print("*"*50) 
        
def remove_issue():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    p=int(input("Enter the S_No whose Detail has to be Deleted:"))
    a="delete from Issue where S_No='{}'".format(p)
    cursor.execute(a)
    mydb.commit()
    print("*"*50)
    print("DELETED")
    print("*"*50)

