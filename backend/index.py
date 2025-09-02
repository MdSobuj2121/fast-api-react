from fastapi import FastAPI
from routes.index import user
from config.db import meta, engine
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

meta.create_all(engine)
app.include_router(user)

