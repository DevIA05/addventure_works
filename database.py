import pyodbc

try:
    from utils import getConfig
except:
    from .utils import getConfig


server = "localhost"
database = "AdventureWorks2019"
username = "SA"
password = getConfig("PASSWORD")

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


def sqlRequest(sql):
    cursor.execute(sql)
    row = cursor.fetchall()
    # cursor.close() Where to close cursor ?
    return row


# TO TEST IF WORKS
# version = sqlRequest("SELECT @@version;")
# print(version)
# test = sqlRequest("SELECT TOP (10) * FROM person.person;")
# print(test)
