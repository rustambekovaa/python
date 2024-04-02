
class Book:
    def __init__(self,title, author, data):
        self.title = title
        self.author = author
        self.data = data

class library:
    def __init__(self, name, adres,books = []):
        self.name = name
        self.adres = adres
        self.books = books
        
    def add_book(self, book ):
        self.books.append(book)
    
    def find_book(self,fbook):
        # self.fbook = fbook
        for k in self.books:
            if k.title == fbook:
                print()
                print(f"Автор книги '{fbook}': {k.author}" )
                return
        print()
        print(f"Now this book")


first_b = Book("Xrupkoe ravnovesia","Anna Sheri","1932")
second_b= Book("Napominanie o nem","Kolen Guver","2022")
library_first =library("liberi","Abdykadyrova ")
library_first.add_book(first_b)
library_first.add_book(second_b)
library_first.find_book( "Napominanie o nem")


print()
print(library_first.name)
print(library_first.adres)
print()
for book in library_first.books:
    print("Название:", book.title)
    print("Автор:", book.author)
    print("Дата:", book.data)
    print()

