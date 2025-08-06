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


(base) ➜  Desktop python csvpromax.py
📊 CSV Table Formatter Turbo Mode v3.1
--------------------------------------

📁 File Selection:
1. Navigate folders
2. Enter path manually
Choose (1/2): 2
📄 Enter CSV file path: /Users/ghostshinobi/Desktop/test.csv 
✅ File loaded successfully with encoding: utf-8

📄 Preview:
+--------+-----------+-------+---------+--------------------------+------------+-------------+
| Nome   | Cognome   |   Età | Città   | Email                    |   Telefono |   Stipendio |
|--------+-----------+-------+---------+--------------------------+------------+-------------|
| Mario  | Rossi     |    32 | Milano  | mario.rossi@email.com    | 3331234567 |       45000 |
| Anna   | Bianchi   |    28 | Roma    | anna.bianchi@email.com   | 3337654321 |       38000 |
| Luca   | Verdi     |    45 | Napoli  | luca.verdi@email.com     | 3339876543 |       52000 |
| Sofia  | Neri      |    29 | Torino  | sofia.neri@email.com     | 3334567890 |       41000 |
| Pietro | Ferrari   |    38 | Bologna | pietro.ferrari@email.com | 3338765432 |       47000 |
+--------+-----------+-------+---------+--------------------------+------------+-------------+

📋 Operations Menu:
1. Delete columns
2. Sort data (alphabetic or numeric)
3. Remove duplicates
4. Save and exit
5. Exit without saving
Choose (1-5): 1


📑 Column List:
1: Nome
2: Cognome
3: Età
4: Città
5: Email
6: Telefono
7: Stipendio

Enter column numbers to delete (e.g., 1,3): 4
✅ Columns deleted.

📄 Preview:
+--------+-----------+-------+--------------------------+------------+-------------+
| Nome   | Cognome   |   Età | Email                    |   Telefono |   Stipendio |
|--------+-----------+-------+--------------------------+------------+-------------|
| Mario  | Rossi     |    32 | mario.rossi@email.com    | 3331234567 |       45000 |
| Anna   | Bianchi   |    28 | anna.bianchi@email.com   | 3337654321 |       38000 |
| Luca   | Verdi     |    45 | luca.verdi@email.com     | 3339876543 |       52000 |
| Sofia  | Neri      |    29 | sofia.neri@email.com     | 3334567890 |       41000 |
| Pietro | Ferrari   |    38 | pietro.ferrari@email.com | 3338765432 |       47000 |
+--------+-----------+-------+--------------------------+------------+-------------+

📋 Operations Menu:
1. Delete columns
2. Sort data (alphabetic or numeric)
3. Remove duplicates
4. Save and exit
5. Exit without saving
Choose (1-5): 3
🧹 Removed duplicate rows: 0

📄 Preview:
+--------+-----------+-------+--------------------------+------------+-------------+
| Nome   | Cognome   |   Età | Email                    |   Telefono |   Stipendio |
|--------+-----------+-------+--------------------------+------------+-------------|
| Mario  | Rossi     |    32 | mario.rossi@email.com    | 3331234567 |       45000 |
| Anna   | Bianchi   |    28 | anna.bianchi@email.com   | 3337654321 |       38000 |
| Luca   | Verdi     |    45 | luca.verdi@email.com     | 3339876543 |       52000 |
| Sofia  | Neri      |    29 | sofia.neri@email.com     | 3334567890 |       41000 |
| Pietro | Ferrari   |    38 | pietro.ferrari@email.com | 3338765432 |       47000 |
+--------+-----------+-------+--------------------------+------------+-------------+

📋 Operations Menu:
1. Delete columns
2. Sort data (alphabetic or numeric)
3. Remove duplicates
4. Save and exit
5. Exit without saving
Choose (1-5): 4


💾 In what format would you like to save the file?
1. CSV
2. TXT (formatted table)
Choose (1/2/3): 2

✅ File saved as: /Users/ghostshinobi/Desktop/test_formatted.txt


<img width="1440" height="900" alt="Schermata 2025-08-06 alle 09 58 26" src="https://github.com/user-attachments/assets/debb1a9d-51b4-4ed4-8993-805fefee270e" />

<img width="1440" height="900" alt="Schermata 2025-08-06 alle 09 58 21" src="https://github.com/user-attachments/assets/e75612c1-cf4a-4cc0-9d47-cb70eb4696f3" />

