def add_book():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    i_d=int(input("Enter the Book ID :"))
    name=input("Enter Book Name :")
    author=input("Enter the Author's Name:")
    quantity=int(input("Enter the Quantity of Book:"))
    rec=(i_d,name,author,quantity)
    a='insert into Book values("{}","{}","{}","{}")'.format(i_d,name,author,quantity)
    cursor.execute(a)
    mydb.commit()
    print("*"*50)
    print('NEW BOOK RECORD ADDED')
    print("*"*50)
            
def display_book():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    cursor.execute("select * from Book")
    r=cursor.fetchall()
    for i in r:
        print(i)
    print("*"*50)
    
def delete_book():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    print("Menu for Delecting the details as per:")
    print("1.Book Name \n 2.BookID")
    print("*"*50)
    ch=int(input("Enter your choice:"))
    print("*"*50)
    if ch==1:
        x=(input("Enter the Book Name to be Deleted:"))
        y='delete from Book where name="{}"'.format(x)
        cursor.execute(y)
        mydb.commit()
        print("*"*50)
        print("DELETED")
        print("*"*50)
    elif ch==2:
        x=int(input("Enter the Book ID to be Deleted:"))
        y='delete from Book where i_d="{}"'.format(x)
        cursor.execute(y)
        mydb.commit()
        print("*"*50)
        print("DELETED")
        print("*"*50)
    else:
        print("Wrong Input!!!!!!!")
        print("*"*50)

def update_book():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    print("*"*50)
    print("Menu for modification of detail:")
    print("1.BookId")
    print("2.Book Name")
    print("3.Author Name")
    print("4.Book Quantity")
    print("*"*50)
    ch1=int(input('Enter your choice from the menu which you want to modify:'))
    ch2=int(input("Enter the option(1,2) on the basis of which the details are to be modified:"))
    print("*"*50)
    if ch1==1:
        if ch2==1:
            x=int(input("Enter Book ID to be Added:"))
            z=int(input("Enter Book ID to be Changed:"))
            y="update book set i_d='{}' where i_d='{}'".format(x,z)
            print("*"*50)
            print("UPDATED")
            print("*"*50)
        elif ch2==2:
            x=int(input("Enter Book ID to be Added:"))
            z=(input("Enter Book Name whose Id has to be Changed:"))
            y="update Book set i_d='{}' where name='{}'".format(x,z)
            print("*"*50)
            print("UPDATED")
            print("*"*50)
        elif ch2==3 or ch2==4:
            print("SORRY SELECT 1 Or 2")
            print("*"*50)
        else:
            print("Invalid Entry")
            print("*"*50)
    elif ch1==2:
        if ch2==1:
            x=(input("Enter Book Name to be Added:"))
            z=int(input("Enter Book ID whose Name has to be Changed:"))
            y="update book set name='{}' where i_d='{}'".format(x,z)
            print("*"*50)
            print("UPDATED")
            print("*"*50)
        elif ch2==2:
            x=(input("Enter Book Name to be Added:"))
            z=(input("Enter Book Name to be Changed:"))
            y="update Book set name='{}' where name='{}'".format(x,z)
            print("*"*50)
            print("UPDATED")
            print("*"*50)
        elif ch==3 or ch2==4:
            print("SORRY SELECT 1 Or 2")
            print("*"*50)
        else:
            print("Invalid Entry")
            print("*"*50)
    elif ch1==3:
        if ch2==1:
            x=(input("Enter Book Author Name to be Added:"))
            z=int(input("Enter Book ID whose Author Name has to be Changed:"))
            y="update book set author='{}' where i_d='{}'".format(x,z)
            print("*"*50)
            print("UPDATED")
            print("*"*50)
        elif ch2==2:
            x=(input("Enter Book Author Name to be Added:"))
            z=(input("Enter Book Name whose Author Name has to be Changed:"))
            y="update Book set author='{}' where name='{}'".format(x,z)
            print("*"*50)
            print("UPDATED")
            print("*"*50)
        elif ch==3 or ch2==4:
            print("SORRY SELECT 1 Or 2")
            print("*"*50)
        else:
            print("Invalid Entry")
            print("*"*50)
    elif ch1==4:
        if ch2==1:
            x=int(input("Enter Book Quantity to be Added:"))
            z=int(input("Enter Book ID whose Quantity has to be Changed:"))
            y="update book set quantity='{}' where i_d='{}'".format(x,z)
            print("*"*50)
            print("UPDATED")
            print("*"*50)
        elif ch2==2:
            x=int(input("Enter Book Quantity to be Added:"))
            z=(input("Enter Book Name whose Quantity has to be Changed:"))
            y="update Book set quantity='{}' where name='{}'".format(x,z)
            print("*"*50)
            print("UPDATED")
            print("*"*50)
        elif ch2==3 or ch2==4:
            print("SORRY SELECT 1 Or 2")
            print("*"*50)
        else:
            print("Invalid Entry")
            print("*"*50)
    cursor.execute(y)
    mydb.commit()

def search_book():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    i_d=int(input("Enter the Book ID:"))
    print("*"*50)
    a="select * from Book where I_d='{}'".format(i_d)
    cursor.execute(a)
    r=cursor.fetchall()
    print(r)
    print("*"*50)
