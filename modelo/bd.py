import mysql.connector
from mysql.connector import Error
#pip install mysql-connector-python, debe instalar este paquete para poder importar la librería mysql.connector
def conectar():
    try: 
        conn = mysql.connector.connect(
            host='localhost',
            database='ejemplouser3',
            user='ejemplouser2',
            password='123456'
        )
        return conn
    except Error as e:
        print(f"Error al conectar a MariaDB: {e}")
        return None
