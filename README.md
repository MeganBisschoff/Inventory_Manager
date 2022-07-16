# Inventory Manager

A Python program that manages inventory for a warehouse.

## Description

This program is for a Nike warehouse manager that allows them to capture, view, edit, search and report on shoe inventory for presentaion purposes.

At startup, the program retrieves data from an external file to access the information needed to run the program and then presents the manager with the program menu.

From the menu, the manager is able to:

* Retrieve stock data from the database file _(executed at startup)_
* Capture a new stock item
* View all stock items in the inventory list
* View the stock item with the lowest stock and update it
* Search for a stock item by product code
* Calculate the value of each stock item
* View the stock item with the highest stock and discount it
* Exit the program

A new stock item (object) is captured in the Shoe class. Each menu option calls the corresponding function for action. Any time a shoe item is captured or edited the details are added and updated in the CSV file.

The Shoe class includes the attributes, with get methods for:

* Country
* Code
* Product 
* Cost 
* Quantity

The program includes the functions:

* program() _(the menu)_
* read_shoes_data()
* capture_shoes()
* view_all()
* re_stock()
* search_shoe()
* value_per_item()
* highest_quantity()
* exit()

The program takes input from the inventory.txt file that includes, per line:

* Country that's holding the stock
* Product code
* Name of product
* Cost of product
* Quantity of stock

## Functionality summary

* Read data from a CSV file
* Capture a new object for the database
* View all items in the database
* View and update items in the database
* Search for an item in the database
* Calculate the value of an item in the database
* View and discount item in the database

## Programming principles

This program employs the programming concepts of Python OOP including classes, methods, dot notation and functions. Furthermore it employs fundamental programming techniques that include external databases, lists, comparison operators, conditional logic, loops, indexing and string handling.

## Dependencies

None, however the code can be improved by importing the tabulate library.

## Running the program

Run the inventory.py file in any Python IDE.
View the inventory.txt file in any text editing program, such as Notepad++.

## Code preview

```python
# Function to capture data of a shoe and create object.
def capture_shoes():

    # Prompt user to input shoe details to capture.
    print(f"\n__________ Stock Capture __________\n")
    country = input("Enter the country: ")
    code = input("Enter the shoe code: ")
    product = input("Enter the product name: ")
    cost = input("Enter the product cost: ")
    quantity = input("Enter the product quantity: ")

    # Create new 'Shoe' object from inputted variables,
    # and append to main'shoes_list'.
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(new_shoe)

    # Print 'new_shoe' object with headings.
    print(f"\n__________ New Shoe __________{header_line}"
    f"\n{new_shoe}")

    # Write the updated 'shoes_list' to the inventory.txt file.
    with open('inventory.txt', 'w+') as inventory:
        inventory.write(f"Country,Code,Product,Cost,Quantity\n")
        for lines in shoes_list:
            lines = str(f"{lines.country},{lines.code},{lines.product},{lines.cost},{lines.quantity}\n")
            inventory.write(lines)

        print(f"\nNew shoe '{new_shoe.product}' successfully captured to program database!")
```

## Program preview

```
__________ Stock Capture __________

Enter the country: South Africa
Enter the shoe code: SKU12399
Enter the product name: Softairs
Enter the product cost: 1999
Enter the product quantity: 22

__________ New Shoe __________
Country Code Product Cost Quantity

South Africa SKU12399 Softairs 1999 22

New shoe 'Softairs' successfully captured to program database!
```

&nbsp;
***  
_The more inventory a company has, the less likely they will have what they need._ \~ Taiichi Ohno
***
&nbsp;

## Author

Megan Bisschoff

Project submitted for Software Engineering learnership Level 1 Task 29 at [HyperionDev](https://www.hyperiondev.com/)

[View](https://www.hyperiondev.com/portfolio/86596/) submission results and code review.
