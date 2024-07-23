from fastapi import APIRouter

from .pages import router
from .auth import auth_routers
from .user import users_routers
from .topic import topic_routers

routers: list[APIRouter] = []

routers.extend((router,))
routers.extend(auth_routers)
routers.extend(users_routers)
routers.extend(topic_routers)
