from fastapi import  HTTPException
import mysql.connector 
from mysql.connector import Error
from models.userModel import User,UpdateUser,createUser,Users
import os
from dotenv import load_dotenv

#El repositorio es el único que me permite la comunicación con la base de datos

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

#método para registrar un usuario
async def register_user(user: createUser):
    connection = get_db_connection()
    cursor = connection.cursor()
    # SQL para insertar el user en la tabla
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
        
#método para obtener todos los users
async def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()

    # SQL para obtener todos los user registrados y organizar alfabéticamente
    select_query = "SELECT u.id as id, u.name as name, u.phone as phone, u.email as email FROM users u order by u.name asc"
    
    try:
        # Ejecutar la consulta para obtener todas los users
        cursor.execute(select_query)
        users = cursor.fetchall()  # Obtener todos los resultados

        # Convertir el resultado a una lista
        user_list = [User(id=row[0], name=row[1], phone=row[2], email=row[3]) for row in users]
        
        return Users(users=user_list)
    except Error as e:
        raise HTTPException(status_code=400, detail=f"Error al obtener los users: {e}")
    finally:
        cursor.close()
        connection.close()  
        
#actualizar a un usuario
async def update_user(user_id: int, update: UpdateUser):
    connection = get_db_connection()
    cursor = connection.cursor()

    # SQL para actualizar el nombre del user
    update_query = """
        UPDATE users SET name = %s, phone = %s, email = %s WHERE id = %s 
    """
    
    try:
        # Ejecutar la consulta de actualización
        cursor.execute(update_query, (update.name, update.phone, update.email, user_id))
        connection.commit()

        # Verificar si user fue actualizada (si no, user no existe)
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User no encontrado")

        return {"message": "User actualizado con éxito"}
    except Error as e:
        connection.rollback()  # Hacer rollback en caso de error
        raise HTTPException(status_code=400, detail=f"Error al actualizar user: {e}")
    finally:
        cursor.close()
        connection.close()  
        
#método para eliminar un usuario       
async def delete_user(user_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()

    # SQL para eliminar la user
    delete_query = """
        DELETE FROM users WHERE id = %s
    """
    try:
        # Ejecutar la consulta de eliminación
        cursor.execute(delete_query, (user_id,))
        connection.commit()

        # Verificar si user fue eliminado (si no, el user no existe)
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User no encontrado")

        return {"message": "User eliminado con éxito"}
    except Error as e:
        connection.rollback()  # Hacer rollback en caso de error
        raise HTTPException(status_code=400, detail=f"Error al eliminar el user: {e}")
    finally:
        cursor.close()
        connection.close()