import mysql.connector
from DB_Setup import DataBase_name

db_name = DataBase_name
config ={
    'user': 'Amin',
    'password': 'Adv@ncePyth0n',
    'host': 'localhost',
    'database': db_name
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

def Insert_Table(Table_name,keys,values):
    key = str(keys)
    key = key.replace("[", "")
    key = key.replace("]", "")
    key = key.replace("'", "")
    key = key.replace('"', '')
    val = str(values)
    val = val.replace("[", "")
    val = val.replace("]", "")
    sql = f"INSERT INTO {Table_name} ({key}) VALUES ({val})"
    cursor.execute(sql)
    db.commit()

def Read_all_Data(Table_name):
    sql = f"SELECT * FROM {Table_name}"
    cursor.execute(sql)
    ad = cursor # ad == All Data
    return ad

def Read_all_Rows(Table_name):
    sql = f"SELECT * FROM {Table_name}"
    cursor.execute(sql)
    ad = cursor.fetchall() # ad == All Data
    return ad

def read_all_distinct(Table_name):
    sql = f"SELECT DISTINCT * FROM {Table_name}"
    cursor.execute(sql)
    ad = cursor
    return ad

