from fastapi import APIRouter

from .auth import auth_routers
from .user import users_routers
from .edu import edu_routers

routers: list[APIRouter] = []

routers.extend(auth_routers)
routers.extend(users_routers)
routers.extend(edu_routers)
