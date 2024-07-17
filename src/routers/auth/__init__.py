from fastapi import APIRouter

from . import api
from . import pages

auth_routers: tuple[APIRouter, ...] = (api.router, pages.router,)
