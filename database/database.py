import pyodbc

# from pandas import DataFrame

try:
    from database.utils import getConfig
except:
    from .utils import getConfig


server = getConfig("SERVER")
database = getConfig("DATABASE")
username = getConfig("USERNAME")
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

# turnover_data = sqlRequest(
#     "SELECT SUM(UnitPrice) AS Sales , YEAR(OrderDate) as YearOfSale \
#     FROM "+getConfig("DATABASE")+".dbo.FactInternetSales \
#     GROUP BY YEAR(OrderDate) ORDER by YearOfSale"
# )
# print(turnover_data)

# y = []
# x = []

# for elt in turnover_data:
#     # print(elt)
#     y.append(elt[1])
#     x.append(float(elt[0]))

# print("x", x)
# print("y", y)
