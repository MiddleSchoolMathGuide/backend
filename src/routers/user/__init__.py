from fastapi import APIRouter

from . import api
from . import pages

users_routers: tuple[APIRouter, ...] = (api.router, pages.router,)
