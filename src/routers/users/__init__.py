from fastapi import APIRouter

from . import api

users_routers: tuple[APIRouter, ...] = (api.router,)
