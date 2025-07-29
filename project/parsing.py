import gspread
# this script is used with a google service account to read data from a Google Sheet


def main():
    gc = gspread.service_account(filename='project/credentials.json')

    # open a google sheet
    spreadsheet_id = "1q6F30Em5vanLru0VGlHP_AA02hYE9CYfn80XCcCISg8"
    sheet = gc.open_by_key(spreadsheet_id)
    worksheet = sheet.get_worksheet(0)
   

    # 1. Get all values in the columns and remove any empty strings
    
    x_column = get_list_column(worksheet, "x-coordinate")
    y_column = get_list_column(worksheet, "y-coordinate")
    chars_column = get_list_column(worksheet, "character")

   
    # # 2. Find the max_value in the x_coordinate and y_coordinate lists
    max_x = find_max_value(x_column)
    max_y = find_max_value(y_column)

    # # 3. Create an empty matrix structure to receive all the values
    list_structure = create_table_structure(max_x, max_y)
    
    # # 4. Insert all the values
    inserted_values = fill_structure(list_structure, x_column, y_column, chars_column)

    string_values = list(map(lambda x: "".join(x), inserted_values))

    return "".join(string_values)


def get_list_column(worksheet, title: str) -> list: 
    """ 
    Args: 
    worksheet - Google Spreadsheet Object
    title - string

    Returns a list with all values from one particular column in the spreadsheet. 
    
    If column can't be found returns an empty list. 
    """
    
    try:
        cell = worksheet.find(title)
        index = cell.col
        all_values = worksheet.col_values(index)
        if title == "x-coordinate" or title == "y-coordinate":
            return list(map(lambda x: int(x), all_values[1:]))
        else:
            return all_values[1:]
    except Exception as e:
        print(f"Could not find column with title '{title}'.")
        return []
    

def find_max_value(column: list[int]) -> int:
    """
        Args:
        column - list of integers

        Returns an integer with the highest value found in column. 

        If column is empty it returns 0
    """
    if len(column) > 0:
        integer_list = list(map(lambda x: int(x), column))
        return max(integer_list)
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
    main()