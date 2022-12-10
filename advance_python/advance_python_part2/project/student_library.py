# Date: 06-01-2021
"""
    project: student library
    implement a student library system using Oops where student can borrow a book from the list of books.
    create a separate library and student class.
    program must be menu_driven.

"""


class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBook(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("\t*. " + book)

    def borrowBooks(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}, please keep it safe and return it within 30 days")
            self.books.remove(bookName)
        else:
            print("sorry, this book is either not available or has already been issued to someone "
                  "else. please wait until the book is returned ")

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("thanks for returning this book! hope you enjoyed reading it.\nhave a great_day!")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == '__main__':
    centralLibrary = Library(["algorithms", "python", "java", "data structure", "c and c++"])
    student = Student()
    # centralLibrary.displayAvailableBook()

    while True:
        welcomeMsg = '''
        =================  Welcome to central library ==================
        Please choose an option
        1. Listing all the book
        2. Request a book
        3. Add/Return a book
        4. Exit the library
        '''
        print(welcomeMsg)

        choice = int(input("Enter a choice: "))
        if choice == 1:
            centralLibrary.displayAvailableBook()
        elif choice == 2:
            centralLibrary.borrowBooks(student.requestBook())
        elif choice == 3:
            centralLibrary.returnBook(student.returnBook())
        elif choice == 4:
            print("Thanks for choosing central library! Have a great day ahead")
            exit()
        else:
            print("Invalid Choice")
