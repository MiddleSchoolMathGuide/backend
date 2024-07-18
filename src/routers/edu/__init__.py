from fastapi import APIRouter

from . import pages

from . import editor

edu_routers: tuple[APIRouter, ...] = (
    pages.router,
    *editor.editor_routers,
)
