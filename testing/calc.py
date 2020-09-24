def add(a, b):
    """Add function"""
    return a + b


def subtract(a, b):
    """subtract function"""
    return a - b


def multiply(a, b):
    """Multiply function"""
    return a * b


def divide(a, b):
    """Divide function"""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
