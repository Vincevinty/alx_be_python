from book_class import Book

# Create a Book instance
my_book = Book("1984", "George Orwell", 1949)

# Print informal string representation
print(str(my_book))  # Output: '1984' by George Orwell, published in 1949

# Print official representation
print(repr(my_book))  # Output: Book('1984', 'George Orwell', 1949)

# Delete the book instance
del my_book  # Output: Deleting '1984'