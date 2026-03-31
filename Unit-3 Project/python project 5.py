library_books = ["Python", "Java", "C++", "HTML", "Data Science"]
borrowed_books = []

def show_books():
    print("\nAvailable Books:")
    for book in library_books:
        print(book)

def show_borrowed():
    print("\nBorrowed Books:")
    if borrowed_books:
        for book in borrowed_books:
            print(book)
    else:
        print("No books borrowed.")

def borrow_book(book_name):
    if book_name in library_books:
        library_books.remove(book_name)
        borrowed_books.append(book_name)
        print(book_name, "borrowed successfully.")
    else:
        print("Book not available.")

def return_book(book_name):
    if book_name in borrowed_books:
        borrowed_books.remove(book_name)
        library_books.append(book_name)
        print(book_name, "returned successfully.")
    else:
        print("This book was not borrowed.")

while True:
    print("\n----- Library Menu -----")
    print("1. Show Available Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Show Borrowed Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_books()
    elif choice == "2":
        book = input("Enter book name to borrow: ")
        borrow_book(book)
    elif choice == "3":
        book = input("Enter book name to return: ")
        return_book(book)
    elif choice == "4":
        show_borrowed()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")