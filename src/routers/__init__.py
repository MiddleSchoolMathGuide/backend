from fastapi import APIRouter

from .auth import auth_routers
from .user import users_routers
from .topic import topic_routers

routers: list[APIRouter] = []

routers.extend(auth_routers)
routers.extend(users_routers)
routers.extend(topic_routers)
