# history.py

_calculation_history = []  # private list

def add_record(expression, result):
    """
    Stores a single calculation in history.
    Example: "2 + 3 = 5"
    """
    _calculation_history.append(f"{expression} = {result}")

def print_history():
    """
    Prints all past calculations.
    """
    if not _calculation_history:
        print("No calculations performed yet.")
    else:
        print("\n--- Calculation History ---")
        for record in _calculation_history:
            print(record)
        print("---------------------------\n")
