# library_system.py

class Book:
    def __init__(self, title, author):
        """Initializes the title and author of the book."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation of the book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initializes the attributes of the eBook."""
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size  # File size in KB

    def __str__(self):
        """Returns a string representation of the eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initializes the attributes of the print book."""
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count  # Number of pages

    def __str__(self):
        """Returns a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """Initializes an empty library."""
        self.books = []  # List to store book instances

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library."""
        for book in self.books:
            print(book)

