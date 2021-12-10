# ------------------------------------------------------------------------ #
# Title: ZW-Assignment08
# Description: Working with classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Zeb W, 07Dec2021, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
str_file_name = 'xmas_list.txt'
objFile = None
lst_of_products = []
str_choice = ""
str_prod = ""
str_price = ""
str_status = ""
lst_of_objects = []


class Product:
    """Stores data about a product:

    properties:
        str_product_name: (string) with the product's  name
        float_product_price: (float) with the product's standard price
    methods:
        __init__: initialize products
        str_product_name getter:
        str_product_name setter:
        float_product_price getter:
        float_product_price setter:
        __str__: prints object parameters

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Zeb W., 07Dec2021, Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self, str_product_name, float_product_price):
        # -- Attributes
        self.__str_product_name = str_product_name
        self.__float_product_price = float_product_price

    # -- Properties --
    # -- Getters --
    @property
    def str_product_name(self):
        return str(self.__str_product_name).title()

    @property
    def float_product_price(self):
        f = round(float(self.__float_product_price), 2)
        return f

    # -- Setters -- Only used when changing the name, not when initializing an object
    @str_product_name.setter
    def str_product_name(self, value):
        if not str(value).isnumeric():
            self.__str_product_name = value
        else:
            print("""
Product names cannot be numbers, please check the file and run the program again
            """)
            raise Exception("Names cannot be numbers")

    @float_product_price.setter
    def float_product_price(self, value):
        if not str(value).isalpha():
            self.__float_product_price = value
        else:
            print("""
The price must be a number, please check the file and run the program again
            """)
            raise Exception("The price must be a number")

    # -- Methods --
    def __str__(self):
        return self.__str_product_name + ", " + str(self.__float_product_price)


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        read_data_from_file(file_name, list_of_product_objects): from a .txt file, create a list of product objects
        add_data_to_list(list_of_product_objects, name, price): add more products to list
        remove_data_from_list(list_of_product_objects, name, price): remove products from list
        write_data_to_file(file_name, list_of_product_objects): save current list of products back into .txt file

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Zeb W, 07Dec2021, Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        """Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) data from file:
        :return: (list) of dictionary rows
        """
        obj = Product("", None)  # create empty object using __init__ method
        list_of_product_objects.clear()
        file = open(file_name, "r")
        for line in file:
            name, price = line.split(", ")  # split list into name and price columns
            if not len(name) >= 1:
                print("""
A product name was left blank, please check the file and run the program again
                """)
                raise EmtpyItemInFileError
            elif not len((str(price).lstrip("$").rstrip())) >= 1:
                print("""
A product price was left blank, please check the file and run the program again
                """)
                raise EmtpyItemInFileError
            elif name.isnumeric():
                print("""
Product names cannot be numeric, please check the file and run the program again
                """)
                raise FileAlphaNumericError
            else:
                try:
                    price = float(str(price).lstrip("$").rstrip()).__round__(2)
                except ValueError as e:
                    # print(e)
                    print("""
All product prices must be a numeric, please check the file and run the program again                    
                    """)
                    # print(e)
                obj.str_product_name = name  # use setter to change object name from "" to name in list
                obj.float_product_price = price  # use setter to change price from None to price in list
                new_row = {"Name": obj.str_product_name,
                           "Price": ("$" + str(obj.float_product_price))}  # use getter to add to list
                list_of_product_objects.append(new_row)
        file.close()
        return list_of_product_objects, "Success!"

    @staticmethod
    def add_data_to_list(list_of_product_objects, name, price):
        """Add new product row to list

        :param list_of_product_objects: (list) of products in dictionary rows
        :param name: (string) task name
        :param price: (string) task priority
        """
        obj = Product("", None)  # create emtpy object using __init__
        obj.str_product_name = name  # use setters to set name and price
        obj.float_product_price = price
        new_row = {"Name": obj.str_product_name, "Price": ("$" + str(obj.float_product_price))}
        list_of_product_objects.append(new_row)  # pass into list
        return list_of_product_objects, "Success! \n"

    @staticmethod
    def remove_data_from_list(list_of_product_objects, name, row_removed=None, status=''):
        """Remove product row from list

        :param list_of_product_objects: (list) of dictionary rows
        :param name: (string) product to remove
        :param row_removed: (boolean) determine if row was removed
        :param status: (string) status of task removal
        """
        for row in list_of_product_objects:
            if row["Name"].lower() == name.lower():
                lst_of_products.remove(row)
                row_removed = True
            if row_removed == True:
                status = 'Success!\n'
            else:
                status = 'Product not found in list\nIf you want to remove an item, select "2" from the menu,' \
                         '\nAnd enter the product\n '
        return list_of_product_objects, status

    @staticmethod
    def write_data_to_file(file_name, list_of_product_objects):
        """write new list into .txt file

        :param file_name: (string) name of text file
        :param list_of_product_objects: (list) rows of dictionary products to write into file
        """
        file = open(file_name, "w")
        for row in list_of_product_objects:
            file.write(row["Name"] + ", " + row["Price"] + "\n")
        file.close()
        return list_of_product_objects, 'Success!'


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Presents information to the user, captures user input for processing:

    methods:
        print_welcome: prints welcome message to user
        show_current_list: shows current list to user
        print_menu: prints user menu
        get_user_choice: captures user's menu selection
        add_product: allows user to add products to list
        remove_product: allows user to remove a product from the list

    changelog: (When,Who,What)
        Zeb W, 07Dec2021, Modified code to complete assignment 8
    """

    @staticmethod
    def print_welcome():
        print('Welcome to the Christmas List generator. This program will allow you')
        print("To edit and store your Christmas List!")

    @staticmethod
    def show_current_list(list_of_product_objects):
        """ Shows the current Tasks in the list of dictionaries rows
        :param list_of_product_objects: (list) of rows you want to display"""
        print()
        print('======= The current Xmas List is: =======')
        for row in list_of_product_objects:
            print(row["Name"] + ", " + row["Price"])
        print('============================================')

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user"""
        print()
        print('Menu of Options')
        print('1) Add a new product')
        print('2) Remove an existing product')
        print('3) Save Christmas List and Exit')
        print()

    @staticmethod
    def get_user_choice():
        """ Gets the menu choice from a user
        :return: string"""
        str_choice = str(input('Which option would you like to perform? [1 to 3]: ')).strip()
        print()
        return str_choice

    @staticmethod
    def get_yes_or_no(message):
        """ Gets a yes or no choice from the user
        :return: string"""
        return str(input(message)).strip().lower()

    @staticmethod
    def press_to_continue(message):
        """Pause program and show a message before continuing
        :param message: message printed to user"""
        print(message)
        input("Press the [Enter] key to continue.")


    @staticmethod
    def get_name_to_add():
        """Gets name of product user wants to add"""
        # name = str(input("What is the name of the product?: ")).strip()
        # return name


        while True:
            name = str(input("What is the name of the product?: ")).strip()
            if name.isnumeric():
                print("""
The name must not be numeric, please try again
                """)
            elif len(name) == 0:
                print("""
You didn't enter anything, please try again                
                """)
            else:
                return name

    @staticmethod
    def get_price_to_add():
        """Gets name and price of product user wants to add"""
        price = None
        while price is None:
            try:
                price = float(input("How much does it cost?: $"))
                if type(price) == float:
                    print()
            except ValueError:
                print()
                print("The price must be numeric, please try again.")
                print()
            else:
                return price

    @staticmethod
    def get_product_to_remove():
        """Gets name of product user wants to remove"""
        name = str(input("Which product would you like to remove?: ")).strip()
        print()
        return name


class EmtpyItemInFileError(Exception):
    """Product names and prices must not be blank in the starting .txt file"""
    def __str__(self):
        return "A product name or price was left blank, please check the file and try again"


class FileAlphaNumericError(Exception):
    """All names from the .txt file must not be numeric
    All prices from the .txt file must be numeric"""
    def __str__(self):
        return "A product name or price was formatted incorrectly, please check the file and try again"

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Step 1:  Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file("xmas_list.txt", lst_of_products)

# Step 2: Print welcome message
IO.print_welcome()

# Step 3: Print current list, print menu, get user choice
while True:
    IO.show_current_list(lst_of_products)
    IO.print_menu()
    str_choice = IO.get_user_choice()

    # Step 4: Let user add products to the list
    if str_choice.strip() == "1":
        str_prod = IO.get_name_to_add()
        str_price = IO.get_price_to_add()
        lst_of_products, str_status = FileProcessor.add_data_to_list(lst_of_products, str_prod, str_price)
        IO.press_to_continue(str_status)

    # Step 5: Let user remove products from the list
    elif str_choice.strip() == "2":
        str_prod = IO.get_product_to_remove()
        lst_of_products, str_status = FileProcessor.remove_data_from_list(lst_of_products, str_prod)
        IO.press_to_continue(str_status)

    # Step 6: Let user save current data to file and exit program
    elif str_choice.strip() == "3":
        str_choice = IO.get_yes_or_no("Save this data to xmas_list.txt? Y/N: ")
        if str_choice.lower() == "y":
            print()
            lst_of_products, str_status = FileProcessor.write_data_to_file(str_file_name, lst_of_products)
            IO.press_to_continue(str_status + "\n")
            break
        elif str_choice.lower() == "n":
            print()
            IO.press_to_continue("Save Cancelled!\n")
        else:
            print()
            print('That is not a choice!')
            print('If you want to save, select "3" from the menu,')
            print('And enter either "y" or "n"')
            IO.press_to_continue("Press [Enter] to Continue")
        continue  # to menu
    else:
        IO.press_to_continue("That is not a choice!")

# Main Body of Script  ---------------------------------------------------- #
