import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#importar modelos
from models.userModel import User,UpdateUser,createUser,Users
#importar servicios
from services.userService import register_user_service, get_users_service, update_user_service, delete_user_service
    
# Actúa como el controlador es decir encargado de recibir y enviar peticiones http.
# Depende de los servicios para poder responder a las peticiones

app = FastAPI(debug=True)

# para evitar problemas de cors
origins = [
    "http://3.148.114.153:8085",
    "http://localhost:5173"
    # Add more origins here
]

# Este middleware en FastAPI se usa para configurar CORS (Cross-Origin Resource Sharing), 
# permitiendo que tu backend acepte solicitudes desde diferentes dominios.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# endpoint para registrar un user
@app.post("/api/v1/users")
async def fun_register_user(user: createUser):
    return await register_user_service(user)

# endpoint para obtener todas los users registrados
@app.get("/api/v1/users", response_model=Users)
async def fun_get_users():
    return await get_users_service()
        
# endpoint para actualizar un users por id
@app.put("/api/v1/users/{user_id}", )
async def fun_update_user(user_id: int, update: UpdateUser):
    return await update_user_service(user_id,update)

# endpoint para eliminar un user por su ID
@app.delete("/api/v1/users/{users_id}")
async def fun_delete_user(users_id: int):
    return await delete_user_service(users_id)
       
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    