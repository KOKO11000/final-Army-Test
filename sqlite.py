import csv
import sqlite3
from soldier import Soldier
class CreatTable:
    def __init__(self, name_db = 'soldier.db'):
        self.db_name = name_db
        self.connection = sqlite3.connect(name_db)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS soldier (                                   
                id INTEGER PRIMARY KEY,
                firstName VARCHAR(50) NOT NULL,
                lastName VARCHAR(50) NOT NULL,
                gender varchar (50) not null,
                city VARCHAR(50),
                distance INT NOT NULL,
                Placement_status INT NOT NULL)
                            
            """)
        self.connection.commit()
        
    def insert_soldier(self, id, firstName, lastName, gender, city, distance, Placement_status):
        quary = "INSERT INTO soldier(id,firstName,lastName,gender,city,distance,placement_status) VALUES (?,?,?,?,?,?,?)"
        self.cursor.execute(quary,(id, firstName, lastName, gender, city, distance, Placement_status))



