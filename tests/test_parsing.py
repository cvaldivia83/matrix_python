import pytest
import re
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from project import parsing
from unittest.mock import MagicMock

def test_create_table_structure():
    arr = parsing.create_table_structure(2, 3)
    assert(arr) == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def test_create_table_structure_2():
    arr = parsing.create_table_structure(5, 7)
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
    

def test_get_list_column():
    worksheet = MagicMock()
    worksheet.find.return_value_col = 2
    worksheet.col_values.return_value = ["x-coordinate", "A", "B", "D", "C"]
    result = parsing.get_list_column(worksheet, "x-coordinate")
    assert result == ['A', 'B', 'D', 'C']

def test_find_max_value():
    arr = [0, 1, 4, 3, 6, 5, 7, 9, 8, 11, 2]
    max_value = parsing.find_max_value(arr)
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
    filled_table = parsing.fill_structure(table, x, y, chars)
    assert filled_table == [
        [" ", " ", " ", '\n'],
        ["A", " ", " ", "\n"],
        [" ", "B", " ", "\n"],
        [" ", " ", "C", "\n"]
    ]
