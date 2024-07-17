from fastapi import APIRouter

from . import pages

from . import me

users_routers: tuple[APIRouter, ...] = (pages.router, *me.me_routers)
