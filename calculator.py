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
        raise ValueError("Error: Cannot divide by zero! Division by zero is undefined.")
    return a / b


def display_menu():
    """Display the calculator menu options."""
    print("\n" + "="*50)
    print("               SIMPLE CALCULATOR")
    print("="*50)
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*50)


def get_valid_number(prompt):
    """
    Repeatedly prompt user for a valid number until one is provided.
    
    Args:
        prompt: The message to display to the user
    
    Returns:
        A float value entered by the user
    """
    while True:
        try:
            user_input = input(prompt).strip()
            
            # Check if input is empty
            if not user_input:
                print("Error: Input cannot be empty. Please enter a valid number.")
                continue
            
            # Try to convert to float
            number = float(user_input)
            return number
            
        except ValueError:
            print(f"Error: '{user_input}' is not a valid number. Please enter a numeric value (e.g., 10, -5, 3.14).")
        except Exception as e:
            print(f"Error: An unexpected error occurred: {str(e)}. Please try again.")


def get_numbers():
    """
    Prompt user to input two valid numbers with error handling.
    
    Returns:
        Tuple of two floats
    """
    print("\n" + "-"*50)
    num1 = get_valid_number("Enter the first number: ")
    num2 = get_valid_number("Enter the second number: ")
    print("-"*50)
    return num1, num2


def get_valid_operation():
    """
    Repeatedly prompt user for a valid operation choice until one is provided.
    
    Returns:
        A valid operation choice ('1', '2', '3', or '4')
    """
    while True:
        choice = input("Enter your choice (1-5): ").strip()
        
        # Check if input is empty
        if not choice:
            print("Error: Input cannot be empty. Please select 1, 2, 3, 4, or 5.")
            continue
        
        # Check if input is a valid choice
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print(f"Error: '{choice}' is not a valid choice. Please enter 1, 2, 3, 4, or 5.")


def perform_operation(operation, num1, num2):
    """
    Perform the selected arithmetic operation with comprehensive error handling.
    
    Args:
        operation: String representing the operation ('1', '2', '3', or '4')
        num1: First number
        num2: Second number
    
    Returns:
        None (prints result or error message)
    """
    try:
        if operation == '1':
            result = add(num1, num2)
            print(f"\n✓ Result: {num1} + {num2} = {result}")
            
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"\n✓ Result: {num1} - {num2} = {result}")
            
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"\n✓ Result: {num1} * {num2} = {result}")
            
        elif operation == '4':
            try:
                result = divide(num1, num2)
                print(f"\n✓ Result: {num1} / {num2} = {result}")
            except ValueError as ve:
                print(f"\n✗ {ve}")
                return
        else:
            print(f"Error: Invalid operation choice '{operation}'.")
            
    except ZeroDivisionError:
        print("\n✗ Error: Cannot divide by zero! Division by zero is undefined.")
    except TypeError:
        print("\n✗ Error: Invalid operand types. Please enter valid numbers.")
    except OverflowError:
        print("\n✗ Error: The result is too large to be represented.")
    except Exception as e:
        print(f"\n✗ Error: An unexpected error occurred: {str(e)}")


def main():
    """Main function to run the calculator application."""
    print("\n" + "="*50)
    print("    Welcome to the Enhanced Simple Calculator!")
    print("="*50)
    
    while True:
        try:
            display_menu()
            choice = get_valid_operation()
            
            # Exit option
            if choice == '5':
                print("\n" + "="*50)
                print("Thank you for using the Simple Calculator!")
                print("Goodbye!")
                print("="*50 + "\n")
                break
            
            # Get numbers and perform operation
            if choice in ['1', '2', '3', '4']:
                num1, num2 = get_numbers()
                perform_operation(choice, num1, num2)
                
                # Ask if user wants to continue
                while True:
                    continue_choice = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
                    if continue_choice in ['yes', 'y', 'no', 'n']:
                        if continue_choice in ['no', 'n']:
                            print("\n" + "="*50)
                            print("Thank you for using the Simple Calculator!")
                            print("Goodbye!")
                            print("="*50 + "\n")
                            return
                        break
                    else:
                        print("Error: Please enter 'yes' or 'no'.")
                        
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted by user.")
            print("="*50)
            print("Thank you for using the Simple Calculator!")
            print("Goodbye!")
            print("="*50 + "\n")
            break
        except Exception as e:
            print(f"Error: An unexpected error occurred in the main loop: {str(e)}")
            print("Please try again.\n")


# Run the calculator
if __name__ == "__main__":
    main()    """Display the calculator menu options."""
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
