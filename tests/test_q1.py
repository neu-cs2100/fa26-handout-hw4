"""HW4 Question 1 Tests"""


import sys

sys.path.append('.')
from src.q1 import Book, get_favorite_book

class TestBook:
    """Tests for the Book class."""


def test_get_favorite_book() -> None:
    """Test the get_favorite_book() function returns a Book instance."""
