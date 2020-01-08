class BookStore:

    noOfBooks = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        BookStore.noOfBooks += 1

    def bookInfo(self):
        print("Book Title:", self.title)
        print("Book Author:", self.author, "\n")

# create few instances of BookStore
b1 = BookStore("Great Expectations", "Charles Dickens")
b2 = BookStore("War and Peace", "Leo Tolstoy")
b3 = BookStore("Middlemarch", "George Elliot")

# invoke the member function on BookStore
b1.bookInfo()
b2.bookInfo()
b3.bookInfo()

print("No of Books: ", BookStore.noOfBooks)


