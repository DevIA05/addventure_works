import pyodbc
import os

# TODO Fix 
try:
    from database.utils import getConfig
except:
    from .utils import getConfig
# TODO Fix 
try:
    server = os.environ["DATABASE_SERVER"]
    database = os.environ["DATABASE_NAME"]
    username = os.environ["DATABASE_USERNAME"]
    password = os.environ["DATABASE_PASSWORD"]
except:

    server = getConfig("SERVER")
    database = getConfig("DATABASE")
    username = getConfig("USERNAME")
    password = getConfig("PASSWORD")

cnxn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
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


def sqlRequest(cursor, sql):
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

# # TO TEST IF WORKS
# version = sqlRequest(cursor, "SELECT @@version;")
# print(version)
# test = sqlRequest(cursor, "SELECT TOP (10) * FROM person.person;")
# print(test)
