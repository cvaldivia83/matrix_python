# Matrix Python Project

## Project Overview
This project demonstrates how to use Python to connect to Google Workspace documents:

- **Google Sheets:** Extract specific columns and reconstruct a matrix (table) based on x and y coordinates provided in the sheet. The script reads the data, processes it, and outputs a string representation of the matrix with characters placed at their correct coordinates.
- **Google Docs:** Scrape through a Google Doc to extract specific values or content using Python.

## Key Files
- `project/parsing.py`: Handles Google Sheets extraction, matrix creation, and string output.
- `project/scraping.py`: Scrapes a Google Doc to extract certain values.

## Key Features
- Connects to Google Sheets using a service account and the `gspread` library.
- Extracts columns by title (e.g., `x-coordinate`, `y-coordinate`, `character`).
- Handles missing columns gracefully with error handling.
- Builds a 2D matrix and fills it with characters at specified (x, y) positions.
- Outputs the final matrix as a string.
- Connects to Google Docs and scrapes for specific values or content.

## What I Learned
- How to use the `gspread` library to interact with Google Sheets in Python.
- How to extract and process column data from a spreadsheet.
- How to build and manipulate 2D lists (matrices) in Python.
- The importance of error handling when working with external data sources.
- How to write clean, modular, and professional Python code with type hints and docstrings.
- How to use mock objects for testing and best practices for writing testable code.
- How to use Python to connect to and scrape content from Google Docs.
- The basics of web scraping and parsing document content programmatically.

---
Feel free to use or adapt this project as a template for similar data extraction and transformation tasks!
