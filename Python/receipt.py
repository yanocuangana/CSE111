from ast import If
from asyncore import read
import csv
from itertools import product
from datetime import datetime
print()

def main():
    current_date_and_time = datetime.now()   
    weekday = current_date_and_time.weekday()
    print()
    print("Inkom Emporium")
    print()
    try:
        products_dict = read_dict("products.csv", 0)
        #print(products_dict)
    
        with open("request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            # for the requested elements
            REQUESTED_PRODUCT_INDEX = 0
            REQUESTED_QUANTITY_INDEX = 1

            # for the products_dict elements
            PRODUCT_NAME_INDEX = 1
            PRODUCT_COST_INDEX = 2

            items_total = 0
            subtotal = 0

            for row_list in reader:
                requested_product_number = row_list[REQUESTED_PRODUCT_INDEX]
                requested_quantity = row_list[REQUESTED_QUANTITY_INDEX]

                for key, product in products_dict.items():

                    name = product[PRODUCT_NAME_INDEX]
                    cost = product[PRODUCT_COST_INDEX]

                    if requested_product_number == key:
                        items_total += int(requested_quantity)
                        final_cost = float(cost) * float(requested_quantity)
                        subtotal += final_cost
                        print(f"Item: {name}: {requested_quantity}, ${cost}")
                        
            print()
            tax = subtotal * 0.06
            total = subtotal + tax 
            print(f"Number of items: {items_total}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: {tax:.2f}")
            print(f"Total: ${total:.2f}")           
            print()
            print("Thank you for shopping at the Inkom Emporium!")
            print(f"{current_date_and_time:%d/%m/%Y %H:%M:%S}")  
            print()  
            
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
        print("Please enter a valid ID.")



def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            # This will use the column that will be used as key
            key = row_list[key_column_index]
            price = row_list[2]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()