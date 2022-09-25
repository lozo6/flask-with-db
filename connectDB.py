import sqlite3
import pandas as pd

def get_db_connection():
    conn = sqlite3.connect('patients.db')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
patientListSql = conn.execute('SELECT * FROM patient_table').fetchall() # fetches all the data from database
patientListSql

# save the data to a DataFrame
df = pd.DataFrame(patientListSql)

# rename the columns
df.columns = ['mrn', 'firstname', 'lastname', 'dob']
print(df)