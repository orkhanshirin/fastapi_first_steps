from db import db
from uuid import UUID
from fastapi import HTTPException
from models import UpdatedUser


def del_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
    raise HTTPException(
        status_code=404,
        detail=f"[INFO] User with the id: > {user.id} < does not exist",
    )


def update_user(update_data: UpdatedUser, id: UUID):
    for user in db:
        if update_data.first_name:
            user.first_name = update_data.first_name
        if update_data.last_name:
            user.last_name = update_data.last_name
        if update_data.middle_name:
            user.middle_name = update_data.middle_name
        if update_data.email:
            user.email = update_data.email
        if update_data.gender:
            user.gender = update_data.gender
        if update_data.roles:
            user.roles = update_data.roles
        return
    raise HTTPException(
        status_code=404,
        detail=f"[INFO] User with the id: > {user.id} < does not exist",
    )
