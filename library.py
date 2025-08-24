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