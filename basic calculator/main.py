# main.py

from operations import add, subtract, multiply, divide, modulus, power
from utils import get_float, get_menu_choice
from history import add_record, print_history

def print_menu():
    print("\n===== BASIC PYTHON CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Show History & Exit")

def main():
    while True:
        print_menu()
        choice = get_menu_choice()

        if choice == 7:
            print_history()
            print("Exiting calculator. Goodbye!")
            break

        # Take inputs for all arithmetic options
        num1 = get_float("Enter first number: ")
        num2 = get_float("Enter second number: ")

        try:
            if choice == 1:
                result = add(num1, num2)
                expression = f"{num1} + {num2}"
            elif choice == 2:
                result = subtract(num1, num2)
                expression = f"{num1} - {num2}"
            elif choice == 3:
                result = multiply(num1, num2)
                expression = f"{num1} * {num2}"
            elif choice == 4:
                result = divide(num1, num2)
                expression = f"{num1} / {num2}"
            elif choice == 5:
                result = modulus(num1, num2)
                expression = f"{num1} % {num2}"
            elif choice == 6:
                result = power(num1, num2)
                expression = f"{num1} ** {num2}"
            else:
                # Should never reach here because of validation
                print("Unknown choice.")
                continue

            print(f"Result: {result}")
            add_record(expression, result)

        except ZeroDivisionError as zde:
            print(f"Error: {zde}")

if __name__ == "__main__":
    main()
