from fastapi import FastAPI
app = FastAPI() 

@app.get("/")
def read_root():        
    return {"Hello": "fastapi"}   

@app.post("/items/{item_id}")
def calculate_percentage(marks:int, total_marks:int):
    percentage = (marks / total_marks) * 100
    return {"the total percentage": percentage}

@app.post("/subjects/{subject_id}")
def sub_percentage(subject_id:int, marks:int, total_marks:int):
    percentage = (marks / total_marks) * 100
    return {"the percentage of subject": percentage}
