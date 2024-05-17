from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

# @app.get("/user/{user_id}", response_model=User) # response_model사용 시 추가 정보 있더라도 표시안됨
# def get_user(user_id: int):
#     # 실제 구현에서는 데이터베이스에서 사용자 정보를 조회하겠지만, 여기서는 예시 데이터를 사용합니다.
#     return User(name="Alice", age=30)
#     return {"name":"Alice", "age":30, "more":"good"}

@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    # 사용자 생성 로직 (가정)
    return {"message": "User created successfully", "user": user}

@app.get("/hello")
def hello_lion():
    return("Hello, LikeLion!")

@app.get("/user/{user_id}")
def user_data(user_id:int):
    return{"user_id" : user_id, "name" : '이름' , "이메일" : "메일"}

@app.post("/students")
def create_student(name:str, email:str):
    return {"name": name, "email": email}