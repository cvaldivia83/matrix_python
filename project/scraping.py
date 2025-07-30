import requests
from bs4 import BeautifulSoup
import logging


def main(url: str) -> str:
    try:
        """ 1. Open HTML page with requests and Parse with Beautiful Soup library """

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        tr_elements = soup.find("table").find_all("tr")
        
        x_col, chars_col, y_col = get_list_column(tr_elements)
       
        """ 2. Find maximum value in x, y columns """

        max_x = find_max_value(x_col)
        max_y = find_max_value(y_col)
        
        """ 3. Creates an empty table structure to receive all the values. """
        
        table_structure = create_table_structure(max_x, max_y)

        """ 4. Inserts the characters in the x and y position of the table. """

        inserted_values = fill_structure(table_structure, x_col, y_col, chars_col)

        """ 5. Transforms all inner lists into a string. """

        string_values = list(map(lambda x: "".join(x), inserted_values))

        """ 6. Transforms inner strings into a single string. """

        return "".join(string_values)
        
    except Exception as e: 
        logging.error("Could not find this HTML element in Google Doc")
        return "Invalid Google Doc"

def get_list_column(tr_list: list) -> list[list[int], list[str], list[int]]:
    """
    Args: tr HTML element list

    Returns a list with all values from one particular column in the table

    If column can't be found it returns an empty list 
    """
    try:
        results = [[], [], []]
        for item in tr_list[1:]: 
            row = item.find_all('td')
            x = row[0].find('p').find('span').get_text()
            results[0].append(int(x))
            chars = row[1].find('p').find('span').get_text()
            results[1].append(chars.capitalize())
            y = row[2].find('p').find('span').get_text()
            results[2].append(int(y))
        return results
    except Exception as e: 
        return [] 

def find_max_value(column: list[int]) -> int:
    """
        Args:
        column - list of integers

        Returns an integer with the highest value found in column. 

        If column is empty it returns 0
    """
    if len(column) > 0:
        return max(column)
    else:
        return 0

def create_table_structure(x: int, y: int) -> list[list[str]]:
    """
        Args:
        x - integer
        y - integer

        Returns a table containing only empty strings with the correct amount of rows and columns. 

        If x and y are equal to 0 it returns an empty list
    """
    if x == 0 and y == 0:
        return []
    else: 
        arr = []
        for i in range(y + 1):
            row = []
            while len(row) < x+ 1:
                row.append(" ")
            arr.append(row)
        return arr

def fill_structure(table: list[list[str]], x: list[int], y: list[int], chars: list[str]) -> list[list[str]]:
    """
        Args:
        table - a table containing the basic structure
        x - list of integers
        y - list of integers
        chars - list of unicode characters

        Returns a table filled with characters in the positions x and y.

        If x, y, and characters are empty lists it returns an empty list
    """

    if len(x) == 0 and len(y) == 0 and len(chars) == 0:
        return []
    else: 
        for index in range(len(chars)):
            if chars[index] == "":
                table[y[index]][x[index]] = " "
            else: 
                table[y[index]][x[index]] = chars[index]
        
        for item in table:
            item.append("\n")
        return table

if __name__ == "__main__":
    main("https://docs.google.com/document/d/e/2PACX-1vSZ1vDD85PCR1d5QC2XwbXClC1Kuh3a4u0y3VbTvTFQI53erafhUkGot24ulET8ZRqFSzYoi3pLTGwM/pub")