from fastapi import APIRouter

from . import pages

from .me import api

users_routers: tuple[APIRouter, ...] = (pages.router, api.router,)
