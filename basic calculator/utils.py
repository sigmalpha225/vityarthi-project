# utils.py

def get_float(prompt):
    """
    Keeps asking user until they enter a valid number.
    """
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_menu_choice():
    """
    Reads the menu option from user and returns it as an int.
    """
    while True:
        choice = input("Enter your choice (1-7): ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 7:
                return choice
        print("Invalid choice. Please enter a number between 1 and 7.")
