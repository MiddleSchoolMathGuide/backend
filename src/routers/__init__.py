from fastapi import APIRouter

from .auth import auth_routers
from .users import users_routers

routers: list[APIRouter] = []

routers.extend(auth_routers)
routers.extend(users_routers)
