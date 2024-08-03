from fastapi import APIRouter

from . import api
from . import pages

from . import editor

topic_routers: tuple[APIRouter, ...] = (
    api.router,
    pages.router,
    *editor.editor_routers,
)
