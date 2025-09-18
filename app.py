import os
from flask import Flask, request, jsonify

# Create an instance of the Flask application
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """
    Serves as the main landing page for the API.
    Provides basic information and usage examples.
    """
    # This JSON response acts as a simple documentation for API consumers.
    return jsonify({
        "message": "Calculator API is running!",
        "endpoints": {
            "health": "/health (GET)",
            "calculate": "/calculate (POST)"
        },
        "example_usage": {
            "url": "/calculate",
            "method": "POST",
            "body": {
                "operation": "add",
                "a": 10,
                "b": 5
            }
        }
    }), 200

@app.route("/health", methods=["GET"])
def health():
    """
    A simple health check endpoint to confirm the service is running.
    Often used by monitoring services to check application status.
    """
    return jsonify({"status": "ok"}), 200

@app.route("/calculate", methods=["POST"])
def calculate():
    """
    Handles all calculation logic.
    Expects a JSON payload with two numbers ('a', 'b') and an 'operation'.
    """
    # Get the JSON data from the incoming request body
    data = request.get_json()
    
    # Check if any JSON data was sent in the request
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    # Extract the required fields from the JSON data
    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")
    
    # Validate that all required fields are present in the payload
    if operation is None or a is None or b is None:
        return jsonify({"error": "Missing required fields: operation, a, b"}), 400
    
    # Attempt to convert 'a' and 'b' to floating-point numbers for calculation
    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        # Handle cases where 'a' or 'b' are not valid numbers
        return jsonify({"error": "a and b must be numbers"}), 400
    
    # Perform the calculation based on the specified operation
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        # Specifically handle the division by zero edge case
        if b == 0:
            return jsonify({"error": "Division by zero"}), 400
        result = a / b
    else:
        # If the operation is not one of the valid choices, return an error
        return jsonify({"error": "Invalid operation. Use: add, subtract, multiply, divide"}), 400
    
    # If successful, return the result with a 200 OK status
    return jsonify({"result": result}), 200

# This block runs only when the script is executed directly (e.g., `python app.py`)
if __name__ == "__main__":
    # Get the port number from the environment variable 'PORT', defaulting to 5000.
    # This is crucial for deployment platforms like Render.
    port = int(os.environ.get('PORT', 5000))
    
    # Run the Flask development server.
    # host="127.0.0.1" makes it accessible only from the local machine for security.
    # debug=False is important for production/deployment.
    app.run(host="127.0.0.1", port=port, debug=False)
