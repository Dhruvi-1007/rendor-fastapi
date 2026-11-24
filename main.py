from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    print("Its working")
    return "Hello this is my first Fast api"

@app.get("/course")
def course():
    print("course")
    return [
        {
            "id": 1,
            "name": "python",
            "price": 100
        },
        {
            "id": 2,
            "name": "java",
            "price": 200
        }
    ]

@app.get("/course/{id}")
def course_by_id(id: int):
    return {
        "id": id,
        "name": "python",
        "price": 100
    }

@app.get("/products")
def products(name: str, category: str, price: int):
    return {
        "name": name,
        "category": category,
        "price": price
    }

@app.get("/students")
def students():
    return [
        {"roll_no": 1, "name": "Rahul", "city": "Ahmedabad"},
        {"roll_no": 2, "name": "Priya", "city": "Surat"}
    ]

@app.get("/teachers/{id}")
def teachers(id: int):
    return {
        "id": id,
        "name": "Amit Sir",
        "subject": "Python"
    }

@app.get("/order")
def order(item: str, qty: int, total: int):
    return {
        "item": item,
        "qty": qty,
        "total": total
    }
