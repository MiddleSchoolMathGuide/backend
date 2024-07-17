from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from const import ASSETS
from routers import routers
from db.src import init

init.init()
app = FastAPI()
app.mount('/assets', StaticFiles(directory=f'{ASSETS}'), name='static')

for router in routers:
    app.include_router(router)
