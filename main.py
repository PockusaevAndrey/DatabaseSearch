import pyodbc

searchString = '71258'
datatype = 'int'
database: str = "ЕТД2финал"
server: str = "LAPTOP-UJBSI6U4"

sql = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                     "Server=" + server + ";"
                                          "Database=" + database + ";"
                                                                   "Trusted_Connection=yes;")
cursor = sql.cursor()
if datatype == 'varchar':
    searchString = "'"+searchString+"'"
cursor.execute(
    "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG='ЕТД2финал'")
tableNames = cursor.fetchall()
if tableNames:
    for tableName in tableNames:
        # print(tableName[0])
        if tableName[0] != 'm_alarm':
            if tableName[0] != 'pLogData':
                cursor.execute("select * from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='" + tableName[0] + "'")
                colNames = cursor.fetchall()
                if colNames:
                    for colName in colNames:
                        # print(colName)
                        if datatype in colName[7]:
                            cursor.execute(
                                "SELECT * FROM [ЕТД2финал].[dbo].[" + tableName[0] + "] WHERE [" + colName[
                                    3] + "] = " + searchString + "")
                            finds = cursor.fetchall()
                            if finds:
                                print("Table: " + tableName[0])
                                print("Column: " + colName[3])
                                for find in finds:
                                    print(find)
                                    pass
                                print("------------------------------------------")
