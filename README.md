This is a powerful command-line tool written in Python for manipulating and formatting CSV files. It offers a simple, menu-driven interface to perform common data cleaning and organization tasks.

Key Features

File Navigation: Easily browse your computer's file system to select a CSV file, or enter the path manually.

Robust File Loading: The script attempts to open files using multiple common encodings (utf-8, latin-1, cp1252) to prevent errors with different file types.

Column Management: Delete one or more columns by their index number.

Advanced Sorting: Sort data by any column, choosing between alphabetical or numerical order.

Duplicate Removal: Quickly remove all duplicate rows from your dataset.

Multiple Output Formats: Save your modified data in three different formats:

CSV: A standard CSV file.

TXT: A neatly formatted, human-readable table.

PDF: A clean, professional table in a PDF document (requires the reportlab library).

Prerequisites

To run this tool, you need Python and a few libraries.

You can install the required libraries using pip:

Bash
pip install pandas tabulate
For optional PDF support, you will also need to install reportlab:

Bash
pip install reportlab
How to Use

Save the script: Save the provided code as a Python file, for example, csvpromax.py.

Run the script: Open a terminal or command prompt, navigate to the directory where you saved the file, and run the following command:

Bash
python csvpromax.py
Follow the prompts: The tool will guide you through the process:

File Selection: Choose to either navigate your folders or enter a file path directly.

Operations Menu: Once a file is loaded, you will see a menu of options to modify your data.

Save: When you are finished, select the "Save and exit" option to choose an output format for your modified file.





<img width="1440" height="900" alt="Schermata 2025-08-06 alle 09 58 26" src="https://github.com/user-attachments/assets/debb1a9d-51b4-4ed4-8993-805fefee270e" />

<img width="1440" height="900" alt="Schermata 2025-08-06 alle 09 58 21" src="https://github.com/user-attachments/assets/e75612c1-cf4a-4cc0-9d47-cb70eb4696f3" />

