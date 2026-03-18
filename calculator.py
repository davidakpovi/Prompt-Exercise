def add(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers and return the result.
    Handles division by zero errors.
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
    
    Returns:
        The quotient of a divided by b
    
    Raises:
        ValueError: If attempting to divide by zero
    """
    if b == 0:
        raise ValueError("Error: Cannot divide by zero!")
    return a / b


def calculator(operation, a, b):
    """
    Main calculator function that performs the requested operation.
    
    Args:
        operation: String indicating the operation ('add', 'subtract', 'multiply', 'divide')
        a: First number
        b: Second number
    
    Returns:
        The result of the operation
    
    Raises:
        ValueError: If attempting to divide by zero or invalid operation
    """
    try:
        if operation.lower() == 'add':
            return add(a, b)
        elif operation.lower() == 'subtract':
            return subtract(a, b)
        elif operation.lower() == 'multiply':
            return multiply(a, b)
        elif operation.lower() == 'divide':
            return divide(a, b)
        else:
            raise ValueError(f"Error: Unknown operation '{operation}'. Use 'add', 'subtract', 'multiply', or 'divide'.")
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"Error: An unexpected error occurred: {str(e)}"


# Example usage
if __name__ == "__main__":
    print("=== Calculator Examples ===\n")
    
    # Addition
    print(f"Add: 10 + 5 = {add(10, 5)}")
    
    # Subtraction
    print(f"Subtract: 10 - 5 = {subtract(10, 5)}")
    
    # Multiplication
    print(f"Multiply: 10 * 5 = {multiply(10, 5)}")
    
    # Division (normal)
    print(f"Divide: 10 / 5 = {divide(10, 5)}")
    
    # Division by zero (error handling)
    print(f"Divide: 10 / 0 = {calculator('divide', 10, 0)}")
    
    # Using the main calculator function
    print("\n=== Using Main Calculator Function ===\n")
    print(f"Calculator('add', 15, 3) = {calculator('add', 15, 3)}")
    print(f"Calculator('subtract', 15, 3) = {calculator('subtract', 15, 3)}")
    print(f"Calculator('multiply', 15, 3) = {calculator('multiply', 15, 3)}")
    print(f"Calculator('divide', 15, 3) = {calculator('divide', 15, 3)}")
    print(f"Calculator('divide', 15, 0) = {calculator('divide', 15, 0)}")
