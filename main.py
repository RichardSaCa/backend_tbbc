import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#importar modelos
from models.userModel import User,UpdateUser,createUser,Users
#importar servicios
from services.userService import register_user_service, get_users_service, update_user_service
    

app = FastAPI(debug=True)

origins = [
    "http://localhost:5173",
    # Add more origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/users")
async def fun_register_user(user: createUser):
    return await register_user_service(user)

# Ruta para obtener todas los registrados
@app.get("/api/v1/users", response_model=Users)
async def fun_get_users():
    return await get_users_service()
        
# Ruta para actualizar un usuario por id
@app.put("/api/v1/users/{user_id}", )
async def fun_update_user(user_id: int, update: UpdateUser):
    return await update_user_service(user_id,update)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    