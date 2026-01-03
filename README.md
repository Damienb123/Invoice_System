# Invoice_System

## Tech Stack
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-Editor-blue?logo=visualstudiocode&logoColor=white)

## How the Code Works
The program allows the user to enter multiple invoice items, each with a name, quantity, and unit price. Each item’s total is automatically calculated and added to the invoice subtotal. A fixed 10% tax is applied, and an optional discount code (SAVE10) can reduce the subtotal by 10%. The system generates a unique invoice number and records the date and time of the transaction. The invoice is displayed in a clean, formatted receipt-style layout for easy reading. Users are given the option to save the generated invoice to a text file for record keeping.

# Added feature for improved usability
The system includes a file-saving feature that allows users to store completed invoices as text files on their computer. After generating an invoice, the user is prompted to choose whether to save it, and if confirmed, the program automatically creates a uniquely named file based on the invoice number. This enables easy record keeping, future reference, and printing of past invoices.

# How to Execute the file
1. Make sure Python 3 is installed on the computer
2. Download or clone the repository in the terminal or command prompt
3. Open a terminal or command prompt and navigate to the project folder
4. Run the program using the following command:
```
python invoice_system.py
```
5. Follow the on screen details of required user input. Here's what you can expect:
```
python invoice_system.py
Enter invoice items (type 'done' when finished):
Item name: socks
Quantity: 3
Price per item: 3
Item name: notebook
Quantity: 4
Price per item: 10
Item name: done
Enter discount code (or press Enter to skip): 
```
6. When asked, choose whether to save the invoice. If you select "y", the invoice will be saved as a ".txt." file in the same project folder

## Example Output
```
=============================================
INVOICE #6164
Date: 2026-01-03 10:24
=============================================
Item              Qty    Price      Total
---------------------------------------------
socks               4 $   6.00 $    24.00
pants               2 $  26.00 $    52.00
pens                2 $   2.36 $     4.72
---------------------------------------------
Subtotal:                      $    80.72
Tax (10%):                     $     8.07
Discount:                      -$    8.07
=============================================
Grand Total:                   $    80.72
=============================================
```
