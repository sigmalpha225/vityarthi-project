# operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """
    Safely divide two numbers. Raises ZeroDivisionError if b == 0.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b
