library = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if len(library) == 0:
            print("No books in library.")
        else:
            print("\nBooks in Library:")
            for i, book in enumerate(library, start=1):
                print(f"{i}. {book}")

    elif choice == "3":
        book = input("Enter book name to search: ")
        if book in library:
            print("Book found!")
        else:
            print("Book not found.")

    elif choice == "4":
        book = input("Enter book name to remove: ")
        if book in library:
            library.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found.")

    elif choice == "5":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")