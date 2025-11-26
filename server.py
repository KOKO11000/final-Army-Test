from fastapi import FastAPI, File, UploadFile
import sqlite3
import uvicorn
import csv
from sqlite import CreatTable
from soldier import Soldier
app = FastAPI()
sqlite = CreatTable()

@app.get('/')
def get_page():
    return {"mgs": "Hello World"}


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
    sqlite.cursor.execute("""CREATE TABLE IF NOT EXISTS solder (                                   
                id INTEGER PRIMARY KEY,
                firstName VARCHAR(50) NOT NULL,
                lastName VARCHAR(50) NOT NULL,
                gender varchar (50) not null,
                city VARCHAR(50),
                distance INT NOT NULL,
                Placement_status INT NOT NULL)
                            
            """)
    sqlite.connection.commit()
    for row in rows:
        quary = f"INSERT INTO {file}({','.join(colums)}) VALUES ({','.join(num_params)})"

    return{
        "file_length":file.size,
        "num_lines": len(rows) + 1,
    }

@app.post("/assignWithCsv")
def reader_file(file):
    with open(f'{file}', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sqlite.cursor.execute(f'''
                INSERT INTO {file} (id,firstName,lastName,gender,city,distance,placement_status)
                VALUES (?,?,?,?,?,?,?)''',(row["id"],row['firstName'],row['lastName'],row['gender'],row['city'],row['distance'],row['placement_status']))
            sqlite.connection.commit()
            return{" hello": row}



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
    

