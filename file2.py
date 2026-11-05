from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, name: str = None): 
    return {"item_id": item_id, "name": name}

@app.post("/diff")
def diff(a: int, b: int):
    difference = a - b
    return {"the difference is": difference}
@app.post("/sum")       
def sum(a: int, b: int):
    total = a + b
    return {"the total is": total}  