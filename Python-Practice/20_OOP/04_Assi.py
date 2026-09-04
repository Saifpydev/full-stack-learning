# Mini Project:
# Library Management System using OOP


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    # Add Book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    # Display Books
    def display_books(self):
        print("\n--- All Books ---")

        if not self.books:
            print("No books available.")
            return

        for book in self.books:
            status = "Available" if book.available else "Issued"

            print("Title:", book.title)
            print("Author:", book.author)
            print("Status:", status)
            print("----------------")

    # Issue Book
    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():

                if book.available:
                    book.available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")

                return

        print("Book not found.")

    # Return Book
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():

                if not book.available:
                    book.available = True
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")

                return

        print("Book not found.")

    # Show Available Books
    def show_available_books(self):
        print("\n--- Available Books ---")

        for book in self.books:
            if book.available:
                print(book.title, "-", book.author)


# Create Library Object
library = Library()


# Create Book Objects
book1 = Book("Python Basics", "John")
book2 = Book("Django Guide", "David")
book3 = Book("JavaScript", "Alex")


# Add Books
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


# Display All Books
library.display_books()


# Issue Book
library.issue_book("Python Basics")


# Display Available Books
library.show_available_books()


# Return Book
library.return_book("Python Basics")


# Display Available Books Again
library.show_available_books()