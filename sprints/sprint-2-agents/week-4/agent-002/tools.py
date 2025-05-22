from datetime import datetime

HISTORY_FILE = "history.txt"

def log(entry):
    with open(HISTORY_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {entry}\n")

def add(a, b):
    result = a + b
    log(f"Added {a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    log(f"Subtracted {a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    log(f"Multiplied {a} * {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    result = a / b
    log(f"Divided {a} / {b} = {result}")
    return result

def show_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No history yet."
