from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# @app.post('/createevent')
# def create_event():
#     name : str
#     date : datetime
#     people : int
#     return("")


@app.post('/createevent')
def create_event(name : str, date : datetime, people : int):    
    return("등록 완료")