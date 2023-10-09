from books import add_book, borrow_book, return_book, find_book
from members import register_member, find_member


def display_menu():
    print("\nLibrary Management System")
    print("----------------------------")
    print("1. Add a new book to the library.")
    print("2. Register a new library member.")
    print("3. Borrow a book.")
    print("4. Return a book.")
    print("5. Display all books.")
    print("6. Display all members.")
    print("7. Exit.")
    print("----------------------------")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            # Call function to add a new book
            pass
        elif choice == "2":
            # Call function to register a new member
            pass
        elif choice == "3":
            # Call function to borrow a book
            pass
        elif choice == "4":
            # Call function to return a book
            pass
        elif choice == "5":
            # Call function to display all books
            pass
        elif choice == "6":
            # Call function to display all members
            pass
        elif choice == "7":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()