
import json



bookjsonfile ="books_data.json"

def load_json(jsonfile):

    data= json.load(open(jsonfile ,"r"))
    return data

class book_management:

    def __init__(self, isbn="",title="", author=""):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.books_availability=0
        self.books_data=load_json(bookjsonfile)


    def load_json(self,bookjsonfile):

        self.books_data= json.load(open(bookjsonfile ,"r"))

    def dump_json(self,books_data,bookjsonfile):

        json_file=open(bookjsonfile,"w")
        json.dump(books_data,json_file,indent=5)

    def add_book(self):

        self.books_data=load_json(bookjsonfile)
        print(self.books_data)
        self.books_data[self.isbn]={"title":str(self.title),"author":str(self.author),"availability":1}
        self.dump_json(self.books_data,bookjsonfile)
        self.books_availability=1
        print("Book added successfully.")

    def remove_book(self,isbn):

        self.books_data=load_json(bookjsonfile)  

        self.books_data[isbn]["availability"]=0
        self.dump_json(self.books_data,bookjsonfile)

    def update_book(self):
        if self.search_by_isbn(self.isbn):
            self.add_book()
        else:
            print("Book not available")
    
    def list_books(self):
        return self.books_data

    def list_isbn(self):
        self.books_data=load_json(bookjsonfile)
        return self.books_data.keys()
    
    def list_authors(self):
        self.books_data=load_json(bookjsonfile)
        author_list=list()
        for key, value in self.books_data.items():
            author_list.append(value["author"])
        return author_list

    def list_titles(self):
        self.books_data=load_json(bookjsonfile)
        title_list=list()
        for key, value in self.books_data.items():
            title_list.append(value["title"])
        return title_list

    def search_by_isbn(self,isbn):
        self.books_data= load_json(bookjsonfile)

    
        if isbn in self.books_data.keys():
            return True
        else:
            return False      
    
    def search_by_author(self,author):
        self.books_data= load_json(bookjsonfile)
        for key, value in self.books_data.items():
            if author == value["author"]:
            
                return True
        return False

    def search_by_title(self,title):
        self.books_data= load_json(bookjsonfile)
        for key, value in self.books_data.items():
            if title == value["title"]:
          
                return True
        return False
    
    def re_add_book(self,isbn):
        self.books_data=load_json(bookjsonfile)
        self.books_data[isbn]["availability"]=1
        self.dump_json(self.books_data,bookjsonfile)
