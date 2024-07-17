from fastapi import APIRouter

from . import api


me_routers: tuple[APIRouter, ...] = (api.router,)
