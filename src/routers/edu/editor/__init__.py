from fastapi import APIRouter

from . import api
from . import pages

editor_routers: tuple[APIRouter, ...] = (
    api.router,
    pages.router,
)
