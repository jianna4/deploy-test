from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Simple Calculator API")

# Enable CORS so frontend (Vercel) can call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later: replace with your Vercel URL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Calculator API! Try /add?a=5&b=3"}

@app.get("/add")
def add(a: float, b: float):
    return {"operation": "add", "result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"operation": "subtract", "result": a - b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"operation": "multiply", "result": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed!")
    return {"operation": "divide", "result": round(a / b, 6)}
