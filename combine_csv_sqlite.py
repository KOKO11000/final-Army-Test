import csv
import sqlite3

class ImportCsvToSQLite:
    def import_csv_to_sqlite(csv_file, db_file, table_name):
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()

            cursor.execute(F'''
            CREATE TABLE IF NOT EXISTS {table_name}(
                id INTEGER PRIMARY KEY,
                firstName TEXT NOT NULL,
                lastName TEXT,
                gender TEXT,
                city TEXT NOT NULL,
                distance INTEGER NOT NULL,
                placement_status TEXT NOT NULL
            )
            ''')
            conn.commit()
        
            with open(csv_file,'r',encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    cursor.execute(f'''
                    INSERT INTO {table_name} (id,firstName,lastName,gender,city,distance,placement_status)
                    VALUES (?,?,?,?,?,?,?)''',(row["id"],row['firstName'],row['lastName'],row['gender'],row['city'],row['distance'],row['placement_status']))
            
            conn.commit()


        

