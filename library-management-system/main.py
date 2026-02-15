#14. Implement a class Library that stores books in a list. Add methods to add, remove, search, and display books.

class Library:
    def __init__(self, books):
        self.books = books

    def add(self, *new_book):  #  "*" means collect more than 1 arguement in a tuple.
        for book in new_book:   # loop through each book to convert tuple into str
            self.books.append(book.lower())

    
    def kick(self, *remove_book):
        for remove in remove_book: # loop through each book to convert tuple into str
            self.books.remove(remove.lower())
    
    def check(self, looking_for):
        if looking_for in self.books:
            print(f"Book Found: {looking_for.lower()}")
        else:
            print(f"Book is not available in the library. {looking_for}")
    
    def __str__(self):
        return f"All available books in the library: {self.books}"


biographies = Library(['steve jobs', 'jansen huang', 'bill gates', 'jack Ma'])

biographies.add('tim Cook', 'elon musk')
print(biographies.books)


biographies.kick("bill gates", "elon musk")
print(biographies.books)


biographies.check('Steve Jobs')

print(biographies)  # str dunder