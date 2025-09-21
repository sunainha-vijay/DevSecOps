# app.py

import argparse
import sys

def calculate(operation, a, b):
    """
    Performs a calculation based on the provided operation and numbers.

    Args:
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').
        a (float): The first number.
        b (float): The second number.

    Returns:
        float or None: The result of the calculation, or None if an error occurs.
    """
    # Perform the calculation based on the specified operation
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        # Specifically handle the division by zero edge case
        if b == 0:
            # Print an error to the standard error stream and return None
            print("Error: Division by zero is not allowed.", file=sys.stderr)
            return None
        return a / b

def main():
    """
    Main function to set up the CLI, parse arguments, and run the calculator.
    """
    # 1. --- SETUP THE COMMAND-LINE INTERFACE PARSER ---
    # Create a parser object with a description that will be shown in the help message.
    parser = argparse.ArgumentParser(description="A simple command-line calculator.")

    # 2. --- DEFINE THE ARGUMENTS ---
    # Add a positional argument for the 'operation'.
    # `choices` restricts the user input to the provided list of valid operations.
    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="The calculation to perform."
    )

    # Add a positional argument for the first number 'a'.
    # `type=float` automatically converts the user's input to a floating-point number.
    parser.add_argument(
        "a",
        type=float,
        help="The first number."
    )

    # Add a positional argument for the second number 'b'.
    parser.add_argument(
        "b",
        type=float,
        help="The second number."
    )

    # 3. --- PARSE THE ARGUMENTS ---
    # Parse the arguments provided by the user from the command line.
    # If the user provides invalid arguments (e.g., wrong type, missing values),
    # argparse will automatically show an error and the help message.
    args = parser.parse_args()

    # 4. --- EXECUTE THE LOGIC ---
    # Call the main calculation function with the parsed arguments.
    result = calculate(args.operation, args.a, args.b)

    # 5. --- DISPLAY THE RESULT ---
    # If the calculation was successful (result is not None), print the output.
    if result is not None:
        print(f"Result: {result}")
    else:
        # If there was an error (like division by zero), exit with a non-zero status code.
        sys.exit(1)

# This standard Python construct ensures that the `main()` function is called
# only when the script is executed directly from the command line.
if __name__ == "__main__":
    main()
