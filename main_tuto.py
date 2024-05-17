from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "Sample Item"}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Item deleted"}


class Student(BaseModel):
    student_id: int
    name: str
    email: str

@app.get("/likelion/{student_id}")
def read_student(student_id: int):
    student_data = {
        1: {"name": "김멋사", "email": "kimmutsa@example.com"},
        2: {"name": "이멋사", "email": "leemutsa@example.com"}
    }
    student_info = student_data.get(student_id, {"message": "Student not found"})
    return student_info


@app.post("/projects/")
def create_item(item: Item):
    return {"name": item.name, "description": item.description}

@app.delete("/projects/{project_id}")
def delete_item(project_id: int):
    return {"message": "Project deleted successfully"}