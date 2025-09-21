import subprocess
import sys

def run_command(args):
    """Helper function to run the CLI script and capture its output."""
    command = [sys.executable, "app.py"] + args
    return subprocess.run(command, capture_output=True, text=True)

def test_cli_addition():
    """Tests the CLI for a valid addition operation."""
    result = run_command(["add", "10", "5"])
    assert result.returncode == 0
    assert "15.0" in result.stdout

def test_cli_subtraction():
    """Tests the CLI for a valid subtraction operation."""
    result = run_command(["subtract", "20", "7"])
    assert result.returncode == 0
    assert "13.0" in result.stdout

# --- NEW TEST ---
def test_cli_multiplication():
    """Tests the CLI for a valid multiplication operation."""
    result = run_command(["multiply", "10", "5"])
    assert result.returncode == 0
    assert "50.0" in result.stdout

# --- FIXED TEST ---
def test_cli_invalid_operation():
    """Tests that the CLI exits with an error for a truly invalid operation."""
    # Use an operation like "power" which is not implemented.
    result = run_command(["power", "10", "5"])
    assert result.returncode != 0 # Expect a failure
    assert "invalid choice" in result.stderr # Check for argparse error message

def test_cli_missing_arguments():
    """Tests that the CLI exits with an error if arguments are missing."""
    result = run_command(["add", "10"])
    assert result.returncode != 0
    assert "the following arguments are required" in result.stderr
