import sqlite3

# connect to data base using sqlite3
# will create a database if it doesn't exist
connect = sqlite3.connect('patients.db')

# db object
db = connect.cursor()

# delete table table patient_table if it exists
db.execute('DROP TABLE IF EXISTS patient_table')
connect.commit() # pushes change to database

# use query to create table
table = """CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL
            ); """
db.execute(table)
connect.commit()

# insert *dummy* data into table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('12345','John', 'Smith', '01/01/1999')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('23456','Jane', 'Doe', '02/02/1999')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('34567','Mary', 'Smith', '03/03/1999')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('45678','Bob', 'Smith', '04/04/1999')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('56789','John', 'Doe', '05/05/1999')")

connect.commit()

connect.close() # closes connection to database