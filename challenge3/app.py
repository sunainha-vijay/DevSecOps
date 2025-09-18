from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b")

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
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

