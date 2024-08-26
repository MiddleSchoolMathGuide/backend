from typing import Awaitable, Callable

from fastapi import FastAPI, Request, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import logging
import os

from const import ASSETS, PUBLIC
from routers import routers
from db.src import init

init.init()
app = FastAPI()
app.mount("/assets", StaticFiles(directory=f"{ASSETS}"), name="static")


@app.middleware("http")
async def add_process_time_header(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
):
    response = await call_next(request)
    if response.status_code == 404 and request.method == "GET":
        if request.url.components.path.count('/') == 1:
            filepath = f"{PUBLIC}/generated{request.url.components.path}"
            if os.path.exists(filepath):
                logging.info('Redirecting static file GET request')
                return FileResponse(filepath)

    return response


for router in routers:
    app.include_router(router)
