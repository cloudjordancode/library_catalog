class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.checked_out = False

        if not isinstance(year,int) or year <= 0:
            raise ValueError
        self.year = year

    def check_out(self):
        """Mark book as checked out"""
        self.checked_out = True

    def return_book(self):
        """Mark book as returned"""
        self.return_book = False

    def __repr__(self):
        status = "Checked Out" if self.checked_out else "Available"
        return f"{status} {self.title} ({self.author})"

class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size_mb = file_size
        self.checkout_count = 0

    def __repr__(self):
        book_info = super().__repr__()
        return f"{book_info} {self.file_size_mb} mb"

    def check_out(self):
        self.checkout_count += 1

    def return_book(self):
        if self.checkout_count > 0:
            self.checkout_count -= 1

class Catalog: 
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_author(self, author):
        results = []

        for book in self.books:
            if book.author == author:
                results.append(book)
        return results
    
    def search_by_title(self, keyword):
        results = []
        for book in self.books:
            if keyword.lower() in book.title.lower():
                results.append(book)
        return results
            
    def get_available(self):
        results = []
        for book in self.books:
            if book.checked_out == False:
                results.append(book)
        return results

    def summary(self):
        total_books = len(self.books)
        available_books = len(self.get_available())

        checked_out_books = total_books - available_books

        print(f"Total books: {total_books}")
        print(f"Avaiable Books: {available_books}")
        print(f"Checked Out: {checked_out_books}")

catalog = Catalog()
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(EBook("AI Engineering", "Chip Huyen", 2025, 15.2))

# Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"

# Check out
catalog.books[0].check_out()
available = catalog.get_available()
print(f"Available: {len(available)} books")

catalog.summary()