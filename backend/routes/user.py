from fastapi import APIRouter
from config.db import con
from models.user import users
from schemas.index import User

user = APIRouter()

@user.get("/")
def read_users():
    result = con.execute(users.select()).fetchall()
    return [dict(r._mapping) for r in result]

@user.get("/{user_id}")
def read_user(user_id: int):
    result = con.execute(users.select().where(users.c.id == user_id)).fetchone()
    return dict(result._mapping) if result else {"message": f"No user found with id {user_id}"}

@user.post("/")
def create_user(user: User):
    result = con.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    ))
    con.commit()
    return {"message": "User created successfully", "id": result.lastrowid}

@user.put("/{user_id}")
def update_user(user_id: int, user: User):
    result = con.execute(
        users.update()
        .where(users.c.id == user_id)
        .values(
            name=user.name,
            email=user.email,
            password=user.password
        )
    )
    con.commit()
    if result.rowcount:
        return {"message": f"User with id {user_id} updated successfully"}
    else:
        return {"message": f"No user found with id {user_id}"}

@user.delete("/{user_id}")
def delete_user(user_id: int):
    result = con.execute(users.delete().where(users.c.id == user_id))
    con.commit()
    if result.rowcount:
        return {"message": "User deleted successfully"}
    else:
        return {"message": f"No user found with id {user_id}"}
