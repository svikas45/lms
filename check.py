

import user


class checkout_management(user.user_management):

    def add_book_to_user(self,user_id,isbn):
        user_data= user.book.load_json(user.userjsonfile)

        user_data[user_id]["books_allotted"].append(isbn)
        self.dump_json(user_data,user.userjsonfile)
        self.remove_book(isbn)

    def remove_book_to_user(self,user_id,isbn):
        user_data= user.book.load_json(user.userjsonfile)
        print(user_data)
        user_data[user_id]["books_allotted"].remove(isbn)
        self.dump_json(user_data,user.userjsonfile)
        self.isbn=isbn
        self.re_add_book(isbn)
    
    def checkout_book(self,user_id, isbn):

        if self.search_by_user_id(user_id) :
            if self.search_by_isbn(isbn):
                self.add_book_to_user(user_id,isbn)
                print("user and book found, book allotted to user")
            else:
                print("book not found")
                return False
        else:
            print("user not found")
            return False
    
    def checkin_book(self,user_id,isbn):

        if self.search_by_user_id(user_id) :
            if self.search_by_isbn(isbn):
                self.remove_book_to_user(user_id,isbn)
                print("user and book found, book allotted to user")
            else:
                print("book not found")
                return False
        else:
            print("user not found")
            return False
        
        