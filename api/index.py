# api/index.py (this is where Vercel will look for serverless functions)
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/calculate")
def calculate(operation: str, a: float, b: float):
    if operation == "add":
        return {"result": a + b}
    elif operation == "subtract":
        return {"result": a - b}
    elif operation == "multiply":
        return {"result": a * b}
    elif operation == "divide":
        if b == 0:
            return JSONResponse(status_code=400, content={"error": "Division by zero"})
        return {"result": a / b}
