import json
import os

data_file = "library.txt"

def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)  
    return []       

def save_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of the book: ")
    genre = input("Enter the genre of the book: ")
    read = input("Have you read the book? (yes/no): ").strip().lower() == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(new_book)
    save_data(library)
    print(f"Book '{title}' added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    initial_length = len(library)
    
    updated_library = [book for book in library if book["title"].lower() != title]

    if len(updated_library) == initial_length:
        print(f"Book '{title}' not found.")
    else:
        save_data(updated_library)
        print(f"Book '{title}' removed successfully!")
    
    return updated_library

def search_library(library):
    search_by = input("Search by title or author: ").strip().lower()
    
    if search_by not in ["title", "author"]:
        print("Invalid choice. Please enter 'title' or 'author'.")
        return

    search_term = input(f"Enter {search_by}: ").strip().lower()
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "read" if book["read"] else "not read"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} | Status: {status}")     
    else:
        print(f"No books found for {search_term}.")

def display_all_library(library):                  
    if library:
        for book in library:
            status = "read" if book["read"] else "not read"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} | Status: {status}")
    else:
        print("No books found in the library.")

def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book["read"]])
    unread_books = total_books - read_books

    print(f"Total books: {total_books}")
    print(f"Read books: {read_books}")
    print(f"Unread books: {unread_books}")

def display_menu():
    library = load_data()
    
    while True:
        print("\nLibrary Menu:")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search library")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            library = remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_library(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    display_menu()
# This code is a simple library manager that allows users to add, remove, search, and display books in their library.
# It also provides statistics on the number of read and unread books.