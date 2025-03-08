from models.book import Book
from models.library import Libary

def main():

    # b=Book("tamar","wer","i")
    # print(b.print())

    l=Libary()

    print(l.add_book("ggkkkkkkk", "fggjjj", "lgghhhh","action"))
    print(l.add_book("rerjje", "iuhhhi", "wkker","action"))
    print(l.add_book("rere", "iui", "wer", "emotion"))

    # print( l.get_all_book())

    # print(l.borrow_book("lgghhhh"))
    # print(l.get_all_book())
    # print(l.borrow_book("lgghhhh"))
    print(l.get_all_books_by_genere("emotion"))


if __name__ == "__main__":
    main()
