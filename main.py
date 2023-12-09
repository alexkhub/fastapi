from typing import List

from fastapi import FastAPI
from pydantic_validator import Trade, User
app = FastAPI()

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


@app.get("/user/{user_id}", response_model=list[User])
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


@app.post("/trades")
def post_trade(trades: list[Trade]):
    fake_trades.extend(trades)
    return {"statys": 200, "data": trades}
