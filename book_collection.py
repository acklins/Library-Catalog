class Book:
    """Base class for a book."""

    def __init__(self, title, author, year):
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Year must be a positive integer.")
        
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False

    def check_out(self):
        self.checked_out = True

    def return_book(self):
        self.checked_out = False

    def __repr__(self):
        status = "Checked out" if self.checked_out else "Available"
        return f"'{self.title}' by {self.author} {status}"

class EBook(Book):
    """Electronic book that supports mutile checkouts."""
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb
        self.checkout_count = 0

#To handle the multiple simultaneous checkouts of ebooks using a counter
    def check_out(self):
        self.checkout_count += 1

#One checkout can be returned via override of return_book
    def return_book(self):
        if self.check_count > 0:
            self.checkout_count -= 1
# Override __repr__
    def __repr__(self):
        return (
            f"{self.title} by {self.author}"
            f"{self.file_size_mb} MB, "
            f"{self.checkout_count} active checkouts)"
        )
    
class Catalog:
    """Stores and searches books."""
    def __init__(self): #starting with a list
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_author(self, author):
        results = []
        for book in self.books:
            if author.lower() in book.author.lower():
                results.append(book)
        return results
    
    def search_by_title(self, keyword):
        results = []
#case-insensitive & finds the keyword anywhere in the title
        for book in self.books:
            if keyword.lower() in book.title.lower():
                results.append(book)
        return results
    
    def get_available(self):
        available = []

        for book in self.books:
            if isinstance(book, EBook):
                available.append(book)
            elif not book.checked_out:
                available.append(book)

        return available
    
    def summary(self):
        print("=== Library Catalog Summary ===")
        print(f"Total books: {len(self.books)}")
        print(f"Available books: {len(self.get_available())}")

        for book in self.books:
            print(book)

catalog = Catalog()

catalog.add_book(
    Book("Python Crash Course", "Eric Matthes", 2019)
)
catalog.add_book(
    Book("Clean Code", "Robert Martin", 2008)
)
catalog.add_book(
    EBook("AI Engineering", "Chip Huyen ", 2025, 15.2)
)
#Search
results = catalog.search_by_title("python")
print(results)

#Check out first physical book
catalog.books[0].check_out()

available = catalog.get_available()
print(f"Available: {len(available)} books")

catalog.summary()