from models.userModel import User,UpdateUser,createUser,Users
from repository.userRepository import register_user, get_users, update_user, delete_user

async def register_user_service(user: createUser):
    return await register_user(user) 

async def get_users_service():
    return await get_users()

async def update_user_service(user_id: int, update: UpdateUser):
    return await update_user(user_id,update)

async def delete_user_service(user_id:int):
    return await delete_user(user_id)