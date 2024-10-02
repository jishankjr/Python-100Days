# Write a Library class with no_of_books and books as two instance variables. 
# Write a program to create a library from this Library class and show how you 
# can print all books, add a book and get the number of books using different methods. 
# Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.no_of_books = 0  
        self.books = []       

    def add_book(self, book_name):
        self.books.append(book_name) 
        self.no_of_books = len(self.books)  

    def show_info(self):
        if self.no_of_books == 1:
            print(f"\nThere is {self.no_of_books} books. The book is:")
            for book in self.books:
                print(book)
        
        else: 
            print(f"\nThere are {self.no_of_books} books. The books are:")
            for book in self.books:
                print(book)


library = Library()
while True:
    choice = input("~ Add a book? (y or n): ")
    if choice == 'n':
        break
    else:
        book_name = input("Book name: ")
        library.add_book(book_name)  

library.show_info()
print("\nThe program has ended. The library information is lost!\n")
