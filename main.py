from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.interfaces.routes import file_routes, health
from src.interfaces.schedulers import schedule

app = FastAPI()

origins = [
    "http://localhost:8888",  # Adicione a origem do seu frontend React
    "http://127.0.0.1:8888",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(file_routes.router)
app.include_router(health.router)

schedule.scheduler.start()

