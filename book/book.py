class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Price: ${self.price}")
    
    def read(self, page_number):
        if page_number <= self.pages:
            print(f"Reading page {page_number} of {self.title}.")
        else:
            print("Invalid page number.")
    

class EBook(Book):
    def __init__(self, title, author, pages, price, file_size, format_type):
        super().__init__(title, author, pages, price)
        self.file_size = file_size
        self.format_type = format_type
    
    def display_info(self):
        super().display_info()
        print(f"File Size: {self.file_size}MB")
        print(f"Format Type: {self.format_type}")
    
    def read(self, page_number):
        print(f"Reading page {page_number} of the digital version of {self.title}.")
