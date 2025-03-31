from models.userModel import User,UpdateUser,createUser,Users
from repository.userRepository import register_user, get_users

async def register_user_service(user: createUser):
    return await register_user(user) 

async def get_users_service():
    return await get_users()