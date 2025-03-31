from fastapi import  HTTPException
import mysql.connector 
from mysql.connector import Error
from models.userModel import User,UpdateUser,createUser,Users
import os
from dotenv import load_dotenv

#El repositorio me permite la comunicación con la base de datos

# Cargar variables de entorno desde .env
load_dotenv()
# Obtener variables de entorno
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# Función para conectar a la base de datos MySQL
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        if connection.is_connected():
            return connection
    except Error as e:
        raise HTTPException(status_code=500, detail=f"Error de conexión a la base de datos: {e}")

async def register_user(user: createUser):
    connection = get_db_connection()
    cursor = connection.cursor()
    # SQL para insertar la fruta en la tabla
    insert_query = """
        INSERT INTO users (name,phone,email)
        VALUES (%s,%s,%s)
    """

    try:
        # Ejecutar la consulta de inserción
        cursor.execute(insert_query, (user.name,user.phone,user.email))
        connection.commit()
        return {"message": "User registrado con éxito"}
    except Error as e:
        connection.rollback()  # Hacer rollback en caso de error
        raise HTTPException(status_code=400, detail=f"Error al registrar el usuario: {e}")
    finally:
        cursor.close()
        connection.close()
        
async def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()

    # SQL para obtener todas las frutas registradas
    select_query = "SELECT u.id as id, u.name as name, u.phone as phone, u.email as email FROM users u order by u.name asc"
    
    try:
        # Ejecutar la consulta para obtener todas las frutas
        cursor.execute(select_query)
        users = cursor.fetchall()  # Obtener todos los resultados

        # Convertir el resultado a una lista de diccionarios
        user_list = [User(id=row[0], name=row[1], phone=row[2], email=row[3]) for row in users]
        
        return Users(users=user_list)
    except Error as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener los users: {e}")
    finally:
        cursor.close()
        connection.close()  