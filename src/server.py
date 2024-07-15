from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

app = FastAPI()


@app.post('/auth/login', response_class=ORJSONResponse)
async def login(_: Request) -> ORJSONResponse:
    return ORJSONResponse({'ok': False})
