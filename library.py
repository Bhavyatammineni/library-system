import tkinter as tk
from tkinter import messagebox

class LibraryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Library System")

        self.library = Library()

        # Labels
        self.label_title = tk.Label(master, text="Title:")
        self.label_author = tk.Label(master, text="Author:")

        # Entry Widgets
        self.entry_title = tk.Entry(master)
        self.entry_author = tk.Entry(master)

        # Buttons
        self.button_add = tk.Button(master, text="Add Book", command=self.add_book)
        self.button_borrow = tk.Button(master, text="Borrow Book", command=self.borrow_book)
        self.button_return = tk.Button(master, text="Return Book", command=self.return_book)
        self.button_display = tk.Button(master, text="Display Books", command=self.display_books)

        # Grid Layout
        self.label_title.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.label_author.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_title.grid(row=0, column=1, padx=10, pady=5)
        self.entry_author.grid(row=1, column=1, padx=10, pady=5)
        self.button_add.grid(row=2, column=0, columnspan=2, pady=10)
        self.button_borrow.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_return.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_display.grid(row=5, column=0, columnspan=2, pady=10)

    def add_book(self):
        title = self.entry_title.get()
        author = self.entry_author.get()
        self.library.add_book(title, author)
        messagebox.showinfo("Library System", f"Book '{title}' added to the library.")

    def borrow_book(self):
        title = self.entry_title.get()
        self.library.borrow_book(title)
        messagebox.showinfo("Library System", f"You have borrowed '{title}'.")

    def return_book(self):
        title = self.entry_title.get()
        self.library.return_book(title)
        messagebox.showinfo("Library System", f"You have returned '{title}'.")

    def display_books(self):
        books = self.library.get_books()
        if books:
            book_list = "\n".join(books)
            messagebox.showinfo("Library System - Available Books", book_list)
        else:
            messagebox.showinfo("Library System - Available Books", "No books available.")

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_title, author):
        if book_title not in self.books:
            self.books[book_title] = {"author": author, "available": True}

    def borrow_book(self, book_title):
        if book_title in self.books and self.books[book_title]["available"]:
            self.books[book_title]["available"] = False

    def return_book(self, book_title):
        if book_title in self.books and not self.books[book_title]["available"]:
            self.books[book_title]["available"] = True

    def get_books(self):
        available_books = [f"{title} by {info['author']}" for title, info in self.books.items() if info["available"]]
        return available_books

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
