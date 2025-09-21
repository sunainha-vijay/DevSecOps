"""
A simple, command-line calculator application.
... (rest of docstring)
"""

import argparse
import sys

def calculate(operation, a, b):
    """
    Performs a calculation based on the provided operation and numbers.
    ... (this function does not need to change)
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            print("Error: Division by zero is not allowed.", file=sys.stderr)
            return None
        return a / b

def main():
    """
    Main function to set up the CLI, parse arguments, and run the calculator.
    Returns an exit code: 0 for success, 1 for failure.
    """
    parser = argparse.ArgumentParser(description="A simple command-line calculator.")

    parser.add_argument(
        "operation",
        choices=["add", "subtract", "multiply", "divide"],
        help="The calculation to perform."
    )
    parser.add_argument("a", type=float, help="The first number.")
    parser.add_argument("b", type=float, help="The second number.")

    args = parser.parse_args()
    result = calculate(args.operation, args.a, args.b)

    # --- THIS LOGIC IS NOW CHANGED ---
    if result is not None:
        print(f"Result: {result}")
        return 0  # Return 0 for success
    else:
        return 1  # Return 1 for failure

# --- THIS BLOCK IS NOW CHANGED ---
# This calls main() and uses its return value as the process exit code.
# This is a standard practice that makes scripts testable.
if __name__ == "__main__":
    sys.exit(main())
