import pandas as pd
import os
import mysql.connector
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base 


engine = sqlalchemy.create_engine(
    'mysql+mysqlconnector://root:mysqlisbetterthanyours!@localhost:3306/pyparsingdb',
    echo=True)

path = "./data/"


for filename in os.listdir(path):
    if filename.endswith(".csv"):
        csv = pd.read_csv(os.path.join(path, filename))
        connection = engine.connect()
        tablename = filename.translate({ord(i): None for i in '.csv'})
        try:
            frame = csv.to_sql(tablename, connection, if_exists='fail')
        except ValueError as vx:
            print(vx)
        except Exception as ex:
            print(ex)
        else:
            print("Table %s created successfully."%tablename)   
        finally:
            connection.close()
        continue
    else:
        continue
