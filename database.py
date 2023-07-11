import pyodbc

# from pandas import DataFrame

try:
    from utils import getConfig
except:
    from .utils import getConfig


server = "localhost"
database = "AdventureWorksDW2019"
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
    rows = cursor.fetchall()
    # cursor.close() Where to close cursor ?
    return rows


# def sqlRequestDF(sql):
#     cursor.execute(sql)
#     df = DataFrame(cursor.fetchall())
#     print(df.columns)
#     df_pivot = df.pivot(columns="0")
#     # df.columns = cursor.description
#     # return df
#     return df_pivot


# df_test = sqlRequestDF(
#     "SELECT COUNT(Gender) FROM HumanResources.Employee GROUP BY Gender ORDER BY Gender"
# )
# print(df_test)

# TO TEST IF WORKS
# version = sqlRequest("SELECT @@version;")
# print(version)
# test = sqlRequest("SELECT TOP (10) * FROM person.person;")
# print(test)
