import subprocess
import sys

def run_command(args):
    """A helper function to run the app.py script as a command-line tool."""
    command = [sys.executable, "app.py"] + args
    return subprocess.run(command, capture_output=True, text=True)

def test_cli_addition():
    """Tests a valid addition operation."""
    result = run_command(["add", "20", "5"])
    assert result.returncode == 0
    assert "Result: 25.0" in result.stdout

def test_cli_subtraction():
    """Tests a valid subtraction operation."""
    result = run_command(["subtract", "10", "4"])
    assert result.returncode == 0
    assert "Result: 6.0" in result.stdout

def test_cli_multiplication():
    """Tests a valid multiplication operation."""
    result = run_command(["multiply", "7", "3"])
    assert result.returncode == 0
    assert "Result: 21.0" in result.stdout

def test_cli_division():
    """Tests a valid division operation."""
    result = run_command(["divide", "100", "10"])
    assert result.returncode == 0
    assert "Result: 10.0" in result.stdout

def test_cli_divide_by_zero():
    """Tests the error handling for division by zero."""
    result = run_command(["divide", "10", "0"])
    assert result.returncode != 0  # Should fail
    assert "Error: Division by zero" in result.stderr

def test_cli_invalid_operation():
    """Tests that the CLI exits with an error for an invalid operation."""
    result = run_command(["power", "10", "5"])
    assert result.returncode != 0  # Should fail
    assert "invalid choice" in result.stderr
