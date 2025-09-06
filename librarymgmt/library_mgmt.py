class Book:
    def __init__(self, title, author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"Book: {book.title} added to the Library")
    def remove_book(self,isbn):
        book_to_remove = None
        for book in self.books:
            if book.isbn ==isbn:
                book_to_remove = book
                if book_to_remove:
                    self.books.remove(book_to_remove)
                    print(f"Book: {book.title} removed from the Library")
    def display_books(self):
        if not self.books:
            print("No books to display")
        else :
            for book in self.books:
                book.display_info()
#--Inheriatnce Exxample
class SpecialLibrary(Library):
    def add_book(self,book):
        super().add_book(book)
        print(f"Special handling of the book {book.title}")


book1 = Book("About Life", "Harsh", "HA1234")
book2 = Book("AWS Architecture", "Harsh", "HA6789")
book3 = Book("GraphQL Examples", "Harsh", "HA2468")

#---Add book
my_lib = Library()
my_lib.add_book(book1)
my_lib.add_book(book2)
my_lib.add_book(book3)
#--Display books
my_lib.display_books()

#--Remove book
my_lib.remove_book(book1.isbn)
my_lib.display_books()

#-----Inheritance inheritance
specialLibrary = SpecialLibrary()
specialLibrary.add_book(book2)







