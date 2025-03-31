import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)

origins = [
    "http://localhost:5173",
    # Add more origins here
]
