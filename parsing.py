import pandas as pd
import os
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mysqlisbetterthanyours!",
    auth_plugin = "mysql_native_password",
    database = "pyparsingdb"
)

path = "./data/"

for filename in os.listdir(path):
    if filename.endswith(".csv"):
        csv = pd.read_csv(os.path.join(path, filename))
        continue
    else:
        continue
