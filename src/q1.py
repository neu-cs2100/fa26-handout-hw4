"""HW4 Question 1

The Book class and main function are provided below.
Please do the following:
- implement the __eq__() method in the Book class
- implement a function get_favorite_book(), which returns an instance of the Book 
    class representing your favorite book.
- write tests for the __str__() and __eq__() methods of the Book class in test_q1.py
- write tests for get_favorite_book() in test_q1.py
"""

class Book:
    """A class representing a book."""

    def __init__(self, title: str, author: str, year: int) -> None:
        """Initialize a new Book instance.

        Args:
            title : str
                The title of the book.
            author : str
                The author of the book.
            year : int
            The year the book was published.
        """
        self.title = title
        self.author = author
        self.year = year

    def __eq__(self, other: object) -> bool:
        pass

    def __str__(self) -> str:
        return f"{self.title} by {self.author}, published in {self.year}"

def main() -> None:
    """Main function to print the favorite book."""
    favorite_book = get_favorite_book()
    print(f"My favorite book is {favorite_book}")

if __name__ == "__main__":
    main()
