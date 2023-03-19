import csv

class Book():
    # Class attributes
    all = []
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
        Book.all.append(self)

    # Class methods
    @classmethod
    def instantiate_from_csv(cls):  # When we invoke our class methods, the class object itself (cls) is passed implicetely
        with open('OOP/books.csv', 'r') as my_file:
            reader = csv.DictReader(my_file)
            books = list(reader)
            
            for book in books:
                Book(
                    author=book.get('author'),
                    pages=int(book.get('pages')),
                    title=book.get('title')
                )

    # Static methods
    @staticmethod
    def is_integer(num: int | float) -> bool:
        # Check float numbers that are point zero
        # Ex. 5.0, 6.0
        if isinstance(num, float):
            # Check if it is point zero
            return num.is_integer()
        else: 
            return isinstance(num, int)
    # Special methods    
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')
        
    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', '{self.pages}')"

my_book = Book(title='Python rocks', author='Nicolas', pages=1600)
Book.instantiate_from_csv()

print(Book.all)
print(Book.is_integer(1.0))
print(Book.is_integer(2))
print(Book.is_integer(2.3))