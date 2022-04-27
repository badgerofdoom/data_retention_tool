import pyodbc
user_name: str = 'sa'
password: str = '@SQL_docker_test@'
host: str = 'localhost,1444'
database: str = 'integrations'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + host +
                      ';DATABASE=' + database +
                      ';UID=' + user_name +
                      ';PWD=' + password)

sql: str = """
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

SELECT Id,
    clientId,
    client_name,
    base_folder,
    sub_folders,
    retention_policies
FROM [integrations].[Data_retention].[clients];
"""
