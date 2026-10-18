from fastapi import FastAPI, HTTPException

app = FastAPI(title="Simple Calculator API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Calculator! Go to /docs to test it."}

@app.get("/calculate")
def calculate(operation: str, num1: float, num2: float):
    if operation == "add":
        return {"result": num1 + num2}
    elif operation == "subtract":
        return {"result": num1 - num2}
    elif operation == "multiply":
        return {"result": num1 * num2}
    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        return {"result": num1 / num2}
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Choose add, subtract, multiply, or divide.")
