import pandas as pd
import matplotlib.pyplot as plt

BOOKS_FILE = "books.csv"

def load_books():
    return pd.read_csv(BOOKS_FILE)

def save_books(books):
    books.to_csv(BOOKS_FILE, index=False)

def display_books():
    books = load_books()
    print("\nAvailable Books:")
    print(books)

while True:
    print("\n===== Library Management System =====")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Visualize Borrowed Books")
    print("6. Exit")
    print("==============================\n")

    choice = input("Enter choice: ")

    if choice == '1':
        display_books()
    elif choice == '2':
        add_book()
    elif choice == '3':
        borrow_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        visualize_data()
    elif choice == '6':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
