users = []

import json

import book


userjsonfile ="user_data.json"

class user_management(book.book_management):

    def __init__(self, user_id="",name=""):
        self.user_id= user_id
        self.name= name


    def add_user(self):

        user_data=book.load_json(userjsonfile)
        user_data[self.user_id]={"name":self.name,"Books_allotted":[]}
        self.dump_json(user_data,userjsonfile)
        print("Book added successfully.")

    def remove_user(self,user_id):

        user_data=book.load_json(userjsonfile)        
        user_data.pop(user_id)
        self.dump_json(user_data,userjsonfile)

    def update_user_data(self):
        if self.search_by_user_id(self.user_id):
            self.add_user()
        else:
            print("user not found")
    
    def list_user_data(self):
        print(book.load_json(userjsonfile))
    
    def list_user_id(self):
        user_data=book.load_json(userjsonfile)
        return user_data.keys()
    
    def list_user_name(self):
        user_data=book.load_json(userjsonfile)
        author_list=list()
        for key, value in user_data.items():
            author_list.append(value["name"])
        return author_list

    def search_by_user_id(self,user_id):
        user_data= book.load_json(userjsonfile)
        if user_id in user_data.keys():
            return True
        else:
            return False
        
    def search_by_user_name(self,name):
        user_data= book.load_json(userjsonfile)
        for key, value in user_data.items():
            if name == value["name"]:
                return True
        return False

