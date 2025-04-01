from models.userModel import User,UpdateUser,createUser,Users
from repository.userRepository import register_user, get_users, update_user, delete_user

# Es el encargado de la comunicación con el repositorio y 
# controlador donde se encuentran los endpoints

# Para un software mas complejo esta es la lógica del negocio,
# es decir, donde se realizan operaciones matemáticas, algoritmos complejos etc...

# servicio para registrar user
async def register_user_service(user: createUser):
    return await register_user(user) 

# servicio para obtener los users
async def get_users_service():
    return await get_users()

# servicio para actualizar user
async def update_user_service(user_id: int, update: UpdateUser):
    return await update_user(user_id,update)

# servicio para eliminar user
async def delete_user_service(user_id:int):
    return await delete_user(user_id)