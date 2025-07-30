import pytest
import re
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from project import scraping
from unittest.mock import MagicMock

def test_create_table_structure():
    arr = scraping.create_table_structure(2, 3)
    assert(arr) == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def test_create_table_structure_2():
    arr = scraping.create_table_structure(5, 7)
    assert(arr) == [
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " "], 
    [" ", " ", " ", " ", " ", " "]
]

def test_find_max_value():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    max_value = scraping.find_max_value(arr)
    assert max_value == 11

def test_fill_structure(): 
    x = [0, 1, 2]
    y = [1, 2, 3]
    chars = ["A", "B", "C"]
    table = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    filled_table = scraping.fill_structure(table, x, y, chars)
    assert filled_table == [
        [" ", " ", " ", '\n'],
        ["A", " ", " ", "\n"],
        [" ", "B", " ", "\n"],
        [" ", " ", "C", "\n"]
    ]