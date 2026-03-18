def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract two numbers and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
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


def display_menu():
    """Display the calculator menu options."""
    print("\n" + "="*40)
    print("        SIMPLE CALCULATOR")
    print("="*40)
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*40)


def get_numbers():
    """
    Prompt user to input two numbers.
    
    Returns:
        Tuple of two floats
    
    Raises:
        ValueError: If user input is not a valid number
    """
    try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None


def perform_operation(operation, num1, num2):
    """
    Perform the selected arithmetic operation.
    
    Args:
        operation: String representing the operation ('1', '2', '3', or '4')
        num1: First number
        num2: Second number
    
    Returns:
        The result of the operation or an error message
    """
    try:
        if operation == '1':
            result = add(num1, num2)
            print(f"\n{num1} + {num2} = {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"\n{num1} - {num2} = {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"\n{num1} * {num2} = {result}")
        elif operation == '4':
            result = divide(num1, num2)
            print(f"\n{num1} / {num2} = {result}")
        else:
            print("Error: Invalid operation choice. Please select 1, 2, 3, or 4.")
    except ValueError as e:
        print(f"\n{e}")
    except Exception as e:
        print(f"\nError: An unexpected error occurred: {str(e)}")


def main():
    """Main function to run the calculator application."""
    print("\nWelcome to the Simple Calculator!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '5':
            print("\nThank you for using the Simple Calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                perform_operation(choice, num1, num2)
        else:
            print("Error: Invalid choice. Please enter 1, 2, 3, 4, or 5.")


# Run the calculator
if __name__ == "__main__":
    main()
