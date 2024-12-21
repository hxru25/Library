import BookDetails
import BookUser
import BookIssue 
def Book():
    while True:
        print("*"*50)
        print('\t\tBOOK MENU')
        print("*"*50)
        print("1.Adding more Books")
        print("2.Removing Books")
        print("3.Display Books")
        print("4.Search Books")
        print("5.Update Books")
        print("6.Return to MAIN MENU")
        print("*"*50)
        choice=int(input("Enter your choice:"))
        print("*"*50)
        if choice==1:
            BookDetails.add_book()
        elif choice==2:
            BookDetails.delete_book()
        elif choice==3:
            BookDetails.display_book()
        elif choice==4:
            BookDetails.search_book()
        elif choice==5:
            BookDetails.update_book()
        elif choice==6:
            break
        else:
            print("Invalid Entry")

def User():
    while True:
        print("*"*50)
        print('\t\tUSER MENU')
        print("*"*50)
        print("1.Add User")
        print("2.Remove User")
        print("3.Display User")
        print("4.Search User")
        print("5.Update User")
        print("6.Return to MAIN MENU")
        print("*"*50)
        choice=int(input("Enter your choice:"))
        print("*"*50)
        if choice==1:
            BookUser.add_user()
        elif choice==2:
            BookUser.delete_user()
        elif choice==3:
            BookUser.display_user()
        elif choice==4:
            BookUser.search_user()
        elif choice==5:
            BookUser.update_user()
        elif choice==6:
            break
        else:
            print("Invalid Entry")

def Issue():
    while True:
        print("*"*50)
        print('\t\tISSUE MENU')
        print("*"*50)
        print("1.Issue Book")
        print("2.Search Issued Detail")
        print("3.Display Issue")
        print("4.Update Issued Book")
        print("5.Remove Issue")
        print("6.Return to MAIN MENU")
        print("*"*50)
        choice=int(input("Enter your choice:"))
        print("*"*50)
        if choice==1:
            BookIssue.issue()
        elif choice==2:
            BookIssue.search_issue()
        elif choice==3:
            BookIssue.display_issue()
        elif choice==4:
            BookIssue.update_issue()
        elif choice==5:
            BookIssue.remove_issue()
        elif choice==6:
            break
        else:
            print("Invalid Entry")

while True:
    print("*"*50)
    print("WELCOME TO PUBLIC LIBRARY")
    print("*"*50)
    print("MENU DRIVE")
    print("1.Book Details Menu Drive")
    print("2.Book User  Menu Drive")
    print("3.Book Issue & Depositing Menu Details")
    print("4.Exit")
    print("*"*50)
    ch=int(input("Enter your choice:"))
    print("*"*50)
    if ch==1:
        Book()
    elif ch==2:
        User()
    elif ch==3:
        Issue()
    elif ch==4:
        print("THANK YOU FOR VISITING PUBLIC LIBRARY")
        print("VISIT AGAIN")
        print("*"*50)
        break
    else:
        print("Invalid Entry")
        print("*"*50)
        
        
        
        
