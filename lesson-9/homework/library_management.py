class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

class Member:
    def __init__(self, name, borrowed_books=None):
        self.name = name
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

class Library:
    def __init__(self, books : list[Book], members : list[Member]):
        self.books = books
        self.members = members
    def borrow(self, book : Book, member: Member):
        if book not in self.books:
            raise BookNotFoundException(f"Book: {book.title} not found")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book: {book.title} is already borrowed")
        if len(member.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"Member: {member.name}'s limit exceeded")

        self.books.remove(book)
        book.is_borrowed = True
        member.borrowed_books.append(book)
        print(f"The book {book.title} has been borrowed by {member.name}")
    def get_back(self, book : Book, member: Member):
        if book not in member.borrowed_books:
            print(f"The book {book.title} is not borrowed by {member.name}")
            return None
        self.books.append(book)
        member.borrowed_books.remove(book)
        book.is_borrowed = False
        print(f"The book {book.title} has been returned by {member.name}")

if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")
    book4 = Book("Moby Dick", "Herman Melville")

    member1 = Member("Alice")

    library = Library([book1, book2, book3, book4], [member1])

    try:
        library.borrow(book1, member1)
        library.borrow(book2, member1)
        library.borrow(book3, member1)
        library.borrow(book4, member1) #error
    except Exception as e:
        print(f"Error: {e}")

    try:
        library.get_back(book1, member1)
        library.get_back(book4, member1) #error
    except Exception as e:
        print(f"Error: {e}")