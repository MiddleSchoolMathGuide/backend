from fastapi import APIRouter

from . import api

api_routers: tuple[APIRouter, ...] = (
    api.router,
)
