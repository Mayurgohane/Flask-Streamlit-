from fastapi import FastAPI, Query
from typing import List
import uvicorn

app = FastAPI()

@app.get("/")
def average(num: List[int] = Query(...)):  
    if len(num) == 0:
        return {"error": "List is empty"}
    
    avg = sum(num) / len(num)
    summ = sum(num)
    
    return {"average": avg, "sum": summ}
