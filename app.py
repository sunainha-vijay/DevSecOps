import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Add a root route for the home page
@app.route("/", methods=["GET"])
def home():
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
    return jsonify({"status": "ok"}), 200

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    
    # Check if data exists
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")
    
    # Validate inputs
    if operation is None or a is None or b is None:
        return jsonify({"error": "Missing required fields: operation, a, b"}), 400
    
    try:
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return jsonify({"error": "a and b must be numbers"}), 400
    
    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            return jsonify({"error": "Division by zero"}), 400
        result = a / b
    else:
        return jsonify({"error": "Invalid operation. Use: add, subtract, multiply, divide"}), 400
    
    return jsonify({"result": result}), 200

if __name__ == "__main__":
    # Use PORT environment variable for Render deployment
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
