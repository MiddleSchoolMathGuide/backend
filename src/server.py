from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from db.src.auth import login

app = FastAPI()


@app.post('/auth/login', response_class=ORJSONResponse)
async def login_api(request: Request) -> ORJSONResponse:
    data = await request.json()
    msg, id_ = login.login(data.get('username'), data.get('password_hash'))
    response = ORJSONResponse(msg)
    if id_ is not None:
        response.set_cookie(
            key='auth_cookie',
            value=id_,
        )
    else:
        response.status_code = 401

    return response
