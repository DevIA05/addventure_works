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

# TO TEST IF WORKS
# cursor.execute("SELECT @@version;")
# row = cursor.fetchone()
# while row:
#     print(row[0])
#     row = cursor.fetchone()
# cursor.close()
# cnxn.close()
# print("done")
