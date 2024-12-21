def add_user():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    P_Id=int(input("Enter the Personal ID:"))
    rec=(P_Id,)
    Name=input("Enter the User Name:")
    Pno=int(input("Enter the Phone No:"))
    #P_Id=int(input("Enter the Personal ID"))
    City=input("Enter the City:")
    print("*"*50)
    a='insert into User values("{}","{}","{}","{}")'.format(Name,Pno,P_Id,City,)
    cursor.execute(a)
    mydb.commit()
    print("USER DETAILS ADDED")
    print("*"*50)
            
def display_user():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    cursor.execute("select * from User")
    r=cursor.fetchall()
    for i in r:
        print(i)
    print("*"*50)

def delete_user():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    p=int(input("Enter the Personal ID whose Detail has to be Deleted:"))
    a="delete from User where P_Id='{}'".format(p)
    cursor.execute(a)
    mydb.commit()
    print("*"*50)
    print("DELETED")
    print("*"*50)
    
def update_user():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    print("*"*50)
    print("Menu for modification of detail:")
    print("1.Name")
    print("2.Phone")
    print("3.City")
    print("*"*50)
    x=int(input("Enter the choice to be Modified:"))
    print("*"*50)
    print("NOTE-The Updation will be done on the basis of P_Id provided")
    print("*"*50)
    if x==1:
        p=int(input("Enter the Personal ID of the User:"))
        Name=input("Enter the modified Name:")
        a='update user set Name="{}" where P_Id="{}"'.format(Name,p)
        cursor.execute(a)
        mydb.commit()
        print("*"*50)
        print("UPDATED")
        print("*"*50)
    elif x==2:
        p=int(input("Enter the Personal ID of the User:"))
        Phone=input("Enter the modified Phone No:")
        a="update user set PhoneNo='{}' where P_Id='{}'".format(Phone,p)
        cursor.execute(a)
        mydb.commit()
        print("*"*50)
        print("UPDATED")
        print("*"*50)
    elif x==3:
        p=int(input("Enter the Personal ID of the User:"))
        City=input("Enter the modified City:")
        a="update user set City='{}' where P_Id='{}'".format(City,p)
        cursor.execute(a)
        mydb.commit()
        print("*"*50)
        print("UPDATED")
        print("*"*50)
    else:
        print("Invalid Entry")
        print("*"*50)

def search_user():
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="Library")
    cursor=mydb.cursor()
    p=input("Enter the Personal ID of the user to be Searched:")
    print("*"*50)
    y='select * from User where P_Id="{}"'.format(p)
    cursor.execute(y)
    r=cursor.fetchall()
    for i in r:
        print(r)
    print("*"*50)

