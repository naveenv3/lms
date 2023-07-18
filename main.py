class Book:
    def _init_(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def _str_(self):
        return f"{self.title} by {self.author}"

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book} to the library.")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print(f"{book} is currently borrowed.")
                else:
                    print(f"{book} is available.")
                return
        print(f"Book with title '{title}' not found.")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print(f"{book} is already borrowed.")
                else:
                    book.is_borrowed = True
                    print(f"You have borrowed {book}.")
                return
        print(f"Book with title '{title}' not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    print(f"{book} was not borrowed.")
                else:
                    book.is_borrowed = False
                    print(f"You have returned {book}.")
                return
        print(f"Book with title '{title}' not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)
