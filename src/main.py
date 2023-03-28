from fastapi import FastAPI
from db import db
from models import User, UpdatedUser
from typing import List, Dict
from uuid import UUID
from handlers import del_user, update_user

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {
        "init": 0,
        "data": "hi",
    }


@app.get("/api/v1/users")
async def get_users() -> List:
    return db


@app.post("/api/v1/users")
async def add_user(user: User) -> Dict:
    db.append(user)
    return {
        "id": user.id,
        "msg": "New user added!",
    }


@app.delete("/api/v1/users/{user_id}")
async def remove_user(user_id: UUID):
    del_user(user_id)
    return {
        "msg": f"{user_id} deleted",
    }


@app.put("/api/v1/users/{user_id}")
async def update_user(update_data: UpdatedUser, user_id: UUID):
    update_user(update_data, user_id)
    return {
        "msg": f"[INFO] The user with id: > {user_id} < got updated.",
    }
