from fastapi import APIRouter

from . import pages

editor_routers: tuple[APIRouter, ...] = (pages.router,)
