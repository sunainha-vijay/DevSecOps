import subprocess
import sys

def run_command(args):
    """A helper function to run the app.py script as a command-line tool."""
    command = [sys.executable, "app.py"] + args
    return subprocess.run(command, capture_output=True, text=True)

def test_cli_addition():
    """Covers the 'add' operation in the calculate function."""
    result = run_command(["add", "20", "5"])
    assert result.returncode == 0
    assert "Result: 25.0" in result.stdout

def test_cli_subtraction():
    """Covers the 'subtract' operation in the calculate function."""
    result = run_command(["subtract", "10", "4"])
    assert result.returncode == 0
    assert "Result: 6.0" in result.stdout

def test_cli_multiplication():
    """Covers the 'multiply' operation in the calculate function."""
    result = run_command(["multiply", "7", "3"])
    assert result.returncode == 0
    assert "Result: 21.0" in result.stdout

def test_cli_division():
    """Covers a valid 'divide' operation in the calculate function."""
    result = run_command(["divide", "100", "10"])
    assert result.returncode == 0
    assert "Result: 10.0" in result.stdout

def test_cli_divide_by_zero():
    """Covers the division by zero error handling in the calculate function."""
    result = run_command(["divide", "10", "0"])
    # A non-zero return code indicates the script exited with an error, as expected.
    assert result.returncode != 0
    # Check that the specific error message is printed to the standard error stream.
    assert "Error: Division by zero" in result.stderr
