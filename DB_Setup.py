import mysql.connector
from mysql.connector import errorcode

#DataBase_name = input('Name of DataBase: ')
DataBase_name = 'final_project'

config = {
    'user': 'Amin',
    'password': 'Adv@ncePyth0n',
    'host': 'localhost',
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

def Create_database(name):
    sql = f'CREATE DATABASE IF NOT EXISTS {name}'
    cursor.execute(sql)

Tables={}
Tables['dataset'] = (
    'CREATE TABLE IF NOT EXISTS `dataset` ('
    ' `id` SMALLINT NOT NULL AUTO_INCREMENT ,'
    ' `model` VARCHAR (100) ,'
    ' `mileage` FLOAT,'
    ' `age` DATE,'
    ' `color` VARCHAR,'
    ' `accident` INT ,'
    ' `owners` INT,'
    ' `location` FLOAT,'
    ' `PRICE` FLOAT,'
    ' PRIMARY KEY (`ID`)'
    ') ENGINE=InnoDB'
)

#key = ['model', 'mileage', 'age','color', 'accident', 'owners','location','price']

def Create_Tables(Tables):
    cursor.execute(f'USE {DataBase_name}')
    for i in Tables:
        table = Tables[i]
        try:
            print(f"Creating table {i}")
            cursor.execute(table)
        except mysql.connector.Error as err:
            if err == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already Exist")
            else:
                print(err.msg)

Create_database(DataBase_name)
Create_Tables(Tables)
