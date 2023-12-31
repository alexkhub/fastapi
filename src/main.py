from fastapi import FastAPI, Depends

from auth.base_config import auth_backend, fastapi_users, current_user
from auth.schemas import UserRead, UserCreate
from auth.models import User
from core.router import router as core_router

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
app.include_router(core_router)


@app.get("/protected-route/")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.full_name}"




@app.get("/")
def hello():
    return f"Go to docs"


