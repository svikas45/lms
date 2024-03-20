# This is a deliberately poorly implemented main script for a Library Management System.

# from book import book_management 
import book
import user
# from user import user_management
import check

def main_menu():
    '''
        @description : This function acts as a dashboard for library mangement system 
    '''
    major_choice=int()
    minor_choice=int()
    # This is the index page
    print("\n ''''''''")
    print("\n Welcome to Library Management System")
    print("\n ''''''''")


    print("1. Book Management")
    print("2. User Management")
    print("3. Transactions")

    major_choice = int(input("Enter choice: "))
    if major_choice == 1:
        # This is  Book management page
        print("1. Add Book")
        print("2. remove book")
        print("3. update book")
        print("4. List Book details")
        print("5. search by Title")
        print("6. search by Author")
        print("7. search by isbn number")    
        print("8. List Authors")
        print("9. List all isbn")
        print("10. List Titles available")
        print("11. Exit")  
        minor_choice = int(input("Enter choice: "))
    elif major_choice ==2:
        # this is the user management page
        print("1. Add User")
        print("2. remove User")
        print("3. update User")
        print("4. List User details")
        print("5. List User ID")
        print("6. List User name")
        print("7. Search by User name")
        print("8. Search by User ID")
        print("9. Exit")    
        minor_choice = int(input("Enter choice: "))
    elif major_choice == 3:
        # this is Transactions page
        print("1. Checkout")
        print("2. Checkin")
        minor_choice = int(input("Enter choice: ")) 

    else:
        print("Invalid choice, please try again.")

    return [major_choice,minor_choice]

def main():
    while True:
        data = main_menu()
        group = data[0]
        choice = data[1]
        
        if group == 1:
            new_book= book.book_management()
            if choice == 1:
                title = str(input("Enter title: "))
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                new_book= book.book_management(isbn, title, author)
                new_book.add_book()
            elif choice == 2:
                isbn = input("Enter ISBN: ")

                new_book.remove_book(isbn)
                print("Book removed")
            elif choice == 3:
                isbn = input("Enter ISBN: ")
                title = str(input("Enter new title: "))
                author = input("Enter new author: ")
                new_book= book.book_management(isbn, title, author)
                new_book.update_book()
                print("Book updated")
            elif choice == 4:

                print("Book stock details")
                print(new_book.list_books())

            elif choice == 5:
                title = str(input("Enter title: "))

                if new_book.search_by_title(title):
                    print("Book available")
                else:
                    print("Book not available")      

            elif choice == 6:
                author = str(input("Enter author: "))

                if(new_book.search_by_author(author)):
                    print("Book available")
                else:
                    print("Book not available")  
                
            elif choice == 7:
                isbn = str(input("Enter isbn: "))

                if(new_book.search_by_isbn(isbn)):
                    print("Book available")
                else:
                    print("Book not available")  
                
            elif choice == 8:

                print(new_book.list_authors())

            elif choice == 9:

                print(new_book.list_isbn())

            elif choice == 10:

                print(new_book.list_titles())    
                         
            elif choice == 11:
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
        if group == 2:
            new_user= user.user_management()
            if choice == 1:
                user_id = str(input("Enter user Id: "))
                name= input("Enter user name: ")
                new_user = user.user_management(user_id,name)
                new_user.add_user()
                print("user added.")
            elif choice == 2:
                user_id = input("Enter user id ")

                new_user.remove_user(user_id)
                print("user removed")
            elif choice == 3:
                user_id = str(input("Enter user Id: "))
                name= input("Enter user name: ")
                new_user= user.user_management(user_id,name)
                new_user.update_user_data()
                print("user updated")
            elif choice == 4:

                print("user details")
                print(new_user.list_user_data())
            elif choice == 5:

                print(new_user.list_user_id())
            elif choice == 6:

                print(new_user.list_user_name())   
            elif choice == 7:
                user_name = str(input("Enter user name: "))

                if(new_user.search_by_user_name(user_name)):
                    print("User registered")
                else:
                    print("User Unregistered")  
            elif choice == 8:
                user_id = str(input("Enter user id: "))

                if(new_user.search_by_user_id(user_id)):
                    print("User registered")
                else:
                    print("User Unregistered")               
            elif choice == 9:
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")     
        if group == 3:
            new_user= check.checkout_management()
            if choice == 1:
                user_id = str(input("Enter user Id: "))
                isbn = input("Enter isbn : ")
                new_user.checkout_book(user_id, isbn)

            elif choice == 2:
                user_id = str(input("Enter user Id: "))
                isbn = input("Enter isbn : ")
                new_user.checkin_book(user_id=user_id, isbn=isbn)

            elif choice == 3:
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
               


if __name__ == "__main__":
    main()
