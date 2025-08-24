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

def add_book():
    books = load_books()
    bid = int(input("Enter Book ID: "))
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    copies = int(input("Enter Number of Copies: "))
    books = pd.concat([books, pd.DataFrame({"BookID": [bid], "Title": [title], "Author": [author], "Available": [copies], "Borrowed": [0]})], ignore_index=True)
    save_books(books)
    print("Book added successfully!")

def borrow_book():
    books = load_books()
    bid = int(input("Enter Book ID to borrow: "))
    if bid in books["BookID"].values:
        idx = books[books["BookID"] == bid].index[0]
        if books.at[idx, "Available"] > 0:
            books.at[idx, "Available"] -= 1
            books.at[idx, "Borrowed"] += 1
            save_books(books)
            print(f"You borrowed '{books.at[idx, 'Title']}'")
        else:
            print("Book not available!")
    else:
        print("Invalid Book ID")

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
