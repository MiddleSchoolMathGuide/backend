from fastapi import APIRouter

from . import pages

users_routers: tuple[APIRouter, ...] = (pages.router,)
