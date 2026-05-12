class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
        
    def __len__(self):
        return self.pages
    
my_book = Book("Python Basics", "Guido van Rossum", 250)
print(f"Book details: {my_book}")
print(f"page count: {len(my_book)}")