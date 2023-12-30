from fastapi import FastAPI, Depends

from auth.base_config import auth_backend, fastapi_users, current_user
from auth.schemas import UserRead, UserCreate
from auth.models import User
from core.schemas import Pydantic_User

app = FastAPI()

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.full_name}"


fake_users = [
    {'id': 1, 'username': 'alexk', 'status': 'admin'},
    {'id': 2, 'username': 'alexk2', 'status': None}
]

fake_trades = [
    {'id': 1, 'sum': 100, 'discount': 0},
    {'id': 2, 'sum': 200, 'discount': 1},
]


@app.get("/")
def hello():
    return 'hi'


@app.get("/user/{user_id}", response_model=list[Pydantic_User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


@app.post("/user/{user_id}")
def change_username(user_id: int, username: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, fake_users))[0]
    current_user['username'] = username
    return {"statys": 200, "data": current_user}


@app.get("/trades")
def get_trades(limit: int = 10, offset: int = 0):
    return fake_trades[offset:][:limit]
