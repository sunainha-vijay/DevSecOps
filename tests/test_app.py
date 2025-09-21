import subprocess
import sys

def run_command(args):
    """Helper function to run the CLI script and capture its output."""
    # Construct the full command to run, e.g., ["python", "app.py", "add", "10", "5"]
    command = [sys.executable, "app.py"] + args
    # Execute the command
    return subprocess.run(command, capture_output=True, text=True)

def test_cli_addition():
    """Tests the CLI for a valid addition operation."""
    # Act: Run the app with "add 10 5"
    result = run_command(["add", "10", "5"])
    
    # Assert: Check for a successful exit code and the correct output
    assert result.returncode == 0
    assert "15.0" in result.stdout

def test_cli_subtraction():
    """Tests the CLI for a valid subtraction operation."""
    # Act: Run the app with "subtract 20 7"
    result = run_command(["subtract", "20", "7"])

    # Assert: Check for a successful exit code and the correct output
    assert result.returncode == 0
    assert "13.0" in result.stdout

def test_cli_invalid_operation():
    """Tests that the CLI exits with an error for an invalid operation."""
    # Act: Run the app with a made-up operation
    result = run_command(["multiply", "10", "5"])
    
    # Assert: Check for a non-zero exit code (indicating an error)
    assert result.returncode != 0
    # Assert that argparse printed an error message to stderr
    assert "invalid choice" in result.stderr

def test_cli_missing_arguments():
    """Tests that the CLI exits with an error if arguments are missing."""
    # Act: Run the app with only one number
    result = run_command(["add", "10"])

    # Assert: Check for a non-zero exit code
    assert result.returncode != 0
    # Assert that argparse printed its help/error message
    assert "the following arguments are required" in result.stderr
