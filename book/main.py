from book import Book, EBook  # Import the classes from book.py

# Creating an instance of Book
book1 = Book("1984", "George Orwell", 328, 19.99)
book1.display_info()
book1.read(10)

print("\n")

# Creating an instance of EBook
ebook1 = EBook("The Great Gatsby", "F. Scott Fitzgerald", 180, 9.99, 2, "ePub")
ebook1.display_info()
ebook1.read(5)
