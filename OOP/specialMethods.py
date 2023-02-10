class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # We we use print(instance_of_class), the class will search for __str__ function and make use of that
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')

my_book = Book(title='Python rocks', author='Nicolas', pages=1600)

print(my_book)      # Python rocks by Nicolas
print(len(my_book)) # 1600
del my_book         # A book object has been deleted