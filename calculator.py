def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers. Raise an exception if division by zero is attempted."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
