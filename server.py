from fastapi import FastAPI, File, UploadFile
import sqlite3
import uvicorn
import csv
import sqlite3

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"first test"}


@app.post("/assignWithCsv")
def get_file(file: UploadFile = File()):
    if not "csv" in file.content_type:
        return {"messeage": f"{file.content_type} not allowed"}
    text = file.file.read().decode()

    reader = csv.reader(text.splitlines())
    rows = [row for row in reader]
    colums = rows[0]
    rows = rows[1:]
    num_params = ['?' for _ in colums]

    return{
        "file_length":file.size,
        "num_lines": len(rows) + 1,
    }




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
    

