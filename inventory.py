# This program is for a Nike warehouse manager that 
# allows them to capture, view, edit, search and 
# report on shoe inventory for presentaion purposes.

# ----- Database ----- #

shoes_list = []

# ----- Global variable ----- #

# 'header_line' for print display.
header_line = "\nCountry Code Product Cost Quantity\n"

# ----- Classes & Methods ----- #

# 'Shoe' class to create object.
class Shoe:

    # Initialise instance variables for object.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Method to return cost of shoe object.
    def get_cost(self):
        return int(self.cost)

    # Method to return quantity of shoe object.
    def get_quantity(self):
        return int(self.quantity)
    
    # Method to return a string representatio of class objecs.
    def __str__ (self):
        return (f'{self.country} {self.code} {self.product} {self.cost} {self.quantity}')

# ----- Functions ----- #

# user_option 1: 
# Function to read data from inventory file and create Shoe object.
def read_shoes_data():

    if len(shoes_list) == 0:

        # 'Try' open file to read, 'except' if FileNotFoundError then quit program.
        try:
            with open ('inventory.txt', 'r+') as inventory:

                # Skip header line and start iteration on next() line.
                # Loop through 'inventory' file and create new 'Shoe' object by
                # indexing each element in line as corresponding instance variable.                 
                next(inventory)
                for line in inventory:
                    line = line.strip('\n').split(',')
                    new_shoe = Shoe(line[0], line[1], line[2], int(line[3]), int(line[4]))

                    # Append each 'new_shoe' object to 'shoes_list' database.
                    shoes_list.append(new_shoe)

            print("Nike shoe data succesfully uploaded!")
        
        except FileNotFoundError:
                print(f"\nThe file that you are trying to open does not exist.")
                quit()

    else:
        print("Shoe data is already loaded and accessed by the program. Enter menu '3' to view.")

# user_option 2: 
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

        print(f"\nNew shoe '{new_shoe.product}' successfully captured to the program database!")

# user_option 3:
# Function to view all shoes in the inventory list.
def view_all():
    
    # Loop through 'shoes_list' and print each item to console.
    print(f"\n__________ Warehouse Inventory __________{header_line}")
    for shoes in shoes_list:
        print(shoes)

# user_option 4: 
# Function to view shoe with the lowest stock and update it.
def re_stock():

    # Set base value for 'min_stock' as the first object in the list.
    min_stock = shoes_list[0]

    # Loop through 'shoes_list' to get 'min_stock' by checking if  
    # next objects quantity is < than current objects quantity.
    # Use dot notation to get 'quantity' values.
    for shoe_stock in shoes_list:
        if shoe_stock.quantity < min_stock.quantity:
            min_stock = shoe_stock
    
    # Print 'min_stock' item to console with headings.
    print(f"\n__________ Low Stock __________{header_line}"
    f"\n{min_stock}")

    # Prompt user to update shoe stock.
    add_stock = input("\nEnter Y/N to update the shoes stock: ").lower()

    # Promt user to input stock amount then update 
    # 'quantity' value of 'min_stock' item.
    if add_stock == "y":
        update_stock = int(input("Enter quantity to restock: "))
        min_stock.quantity = update_stock + int(min_stock.quantity)

        # Print updated 'min_stock' item to console with headings.
        print(f"\n__________ Updated Stock __________{header_line}"
        f"\n{min_stock}")

    else:
        quit()
        
    # Write the updated 'shoes_list' to the inventory.txt file.
    with open('inventory.txt', 'w+') as inventory:
        inventory.write(f"Country,Code,Product,Cost,Quantity\n")
        for lines in shoes_list:
            lines = str(f"{lines.country},{lines.code},{lines.product},{lines.cost},{lines.quantity}\n")
            inventory.write(lines)
        
        print(f"\nNew stock for '{min_stock.product}' successfully updated in program database!")

# user_option 5: 
# Function to search for a shoe using the shoe code.
def search_shoe():
    
    # Prompt user to input product code to search.
    print(f"\n__________ Stock Search __________\n")
    code_search = input("Enter the product SKU code to search: ") 

    # Loop through 'shoes_list' to get matching 'stock_item'.
    # Use dot notation to get 'code' value.
    for stock_item in shoes_list:
        if stock_item.code == code_search:

            # Print searched object with headings.
            print(f"\n__________ Search Results __________{header_line}"
            f"\n{stock_item.country} {stock_item.code} {stock_item.product} {stock_item.cost} {stock_item.quantity}")

# user_option 6: 
# Function to calculate the cost * quantity value of each item.
def value_per_item(): #done?

    # Print objects from loop below with added 'Value' heading.
    print(f"\n__________ Stock Value __________"
    f"\nCountry Code Product Cost Quantity \t\t Value\n")

    # Loop through 'shoes_list' to calculate 'stock_value' of each object.
    # Use dot notation to get 'cost' and 'quantity' values.
    for shoe in shoes_list:
        stock_value = int(shoe.cost) * int(shoe.quantity)
        print(f"{shoe.country} {shoe.code} {shoe.product} {shoe.cost} {shoe.quantity} \t\t {stock_value}")

# user_option 7: 
# Function to view shoe with the highest stock and discount it.
def highest_quantity(): 
    
    # Set base value for 'high_stock' as the first object in the list.
    high_stock = shoes_list[0]

    # Loop through 'shoes_list' to get 'high_stock' by checking if 
    # next objects quantity is > than current objects quantity.
    # Use dot notation to get 'quantity' values.
    for shoe_stock in shoes_list:
        if shoe_stock.quantity > high_stock.quantity:
            high_stock = shoe_stock

    # Print 'high_stock' item to console with headings.
    print(f"\n__________ Stock Surplus __________{header_line}"
    f"\n{high_stock}")

    # Promt user to input discount amount then update 
    # 'cost' value of 'high_stock' item.
    stock_sale_price = int(input("\nEnter amount to discount off shoe: "))
    high_stock.cost = int(high_stock.cost) - stock_sale_price

    # Print updated 'high_stock' item, with headings.
    print(f"\n__________ Stock Sale __________{header_line}"
    f"\n{high_stock}")

    # Write the updated 'shoes_list' to the inventory.txt file.
    with open('inventory.txt', 'w+') as inventory:
        inventory.write(f"Country,Code,Product,Cost,Quantity\n")
        for lines in shoes_list:
            lines = str(f"{lines.country},{lines.code},{lines.product},{lines.cost},{lines.quantity}\n")
            inventory.write(lines)

        print(f"\nStock sale for '{high_stock.product}' successfully updated in program database!")

# ----- Program ----- #

# Program menu with 'user_option's
def program():
    print("\n__________ Welcome To The Nike Inventory Manager __________\n")

    # Call function to first retrieve data needed for program.
    read_shoes_data()

    user_option = ""

    # While 'user_option' is not equal to quit(),
    # the user is presented with program options.
    while user_option != 8:

        print(f"\n__________ Program Menu __________")
        # Prompt user to input program action and call corresponding function.
        user_option = int(input('''\nWhat would you like to do?
        1 - Retrieve stock data from file
        2 - Capture new stock item
        3 - View all stock items in the inventory list
        4 - View stock item with the lowest stock and update it
        5 - Search for a stock item
        6 - Calculate the value of each stock item
        7 - View stock item with the highest stock and discount it
        8 - Quit program
        \nEnter number: '''))

        if user_option == 1:
            read_shoes_data()
        elif user_option == 2:
            capture_shoes()
        elif user_option == 3:
            view_all()
        elif user_option == 4:
            re_stock()
        elif user_option == 5:
            search_shoe()
        elif user_option == 6:
            value_per_item()
        elif user_option == 7:
            highest_quantity()
        elif user_option == 8:
            print("\nGoodbye Nike Warehouse Manager!")
            quit()
        else:
            print("\nIncorrect input, please try again!")

# ---- Run Program ----- #

program()
