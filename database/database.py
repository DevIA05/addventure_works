import pyodbc
import os
# from dotenv import load_dotenv
# load_dotenv()

server = os.environ["DATABASE_SERVER"]
database = os.environ["DATABASE_NAME"]
username = os.environ["DATABASE_USERNAME"]
password = os.environ["DATABASE_PASSWORD"]

cnxn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};SERVER="
    + server
    + ";DATABASE="
    + database
    + ";UID="
    + username
    + ";PWD="
    + password
    + ";TrustServerCertificate=Yes"
)

cursor = cnxn.cursor()

# TODO: pyodbc.Error: ('HY000', '[HY000] [Microsoft][ODBC Driver 18 for SQL Server]
# Connection is busy with results for another command (0) (SQLExecDirectW)')
# => close connection each time !


def sqlRequest(cursor, sql):
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

# # TO TEST IF WORKS
# version = sqlRequest(cursor, "SELECT @@version;")
# print(version)
# test = sqlRequest(cursor, "SELECT TOP (10) * FROM person.person;")
# print(test)
