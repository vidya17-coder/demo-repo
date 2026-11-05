from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, name: str = None): 
    return {"item_id": item_id, "name": name}

@app.patch("/items/{item_id}")
def update_item(item_id: int, name: str = None, description: str = None):
    return {"item_id": item_id, "name": name, "description": description}