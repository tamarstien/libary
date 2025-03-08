from models.book import Book

class Libary:

    def __init__(self):
       self.list_books ={}

    def add_book(self,name,auther,id,genere):
        book=Book(name,auther,id,genere)
        self.list_books[id]=book
        return f"📚 הספר '{book.name}'נוסף!"

    def get_all_book(self):
      return self.list_books.values()

    def borrow_book(self,id):
        if not self.list_books.get(id).is_borrowed:
            self.list_books[id].is_borrowed = True
            return "very nice!!!!"
        else:
            return "😣😣😣😣😥😥"
    def remove(self):
        return

    def get_all_books_by_genere(self,genere):
        return [book for book in self.list_books.values() if book.genere==genere]

