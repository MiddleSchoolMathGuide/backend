from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

from const import AUTH_COOKIE

from db.src.auth import login, session


router = APIRouter()


@router.post('/auth/login', response_class=ORJSONResponse)
async def login_api(request: Request) -> ORJSONResponse:
    data = await request.json()
    username = data.get('username')
    msg, id_ = login.login(username, data.get('password_hash'))
    response = ORJSONResponse(msg)
    if id_ is not None:
        response.set_cookie(
            key=AUTH_COOKIE,
            value=id_,
        )
        response.set_cookie(
            key='username',
            value=username
        )
    else:
        response.status_code = 401

    return response


@router.get('/auth/is_logged_in', response_class=ORJSONResponse)
async def is_logged_in(request: Request) -> ORJSONResponse:
    if session.is_expired(request.cookies.get(AUTH_COOKIE) or ''):
        return ORJSONResponse(
            {'ok': False, 'msg': 'Session expired or did not exist'},
            status_code=401
        )

    return ORJSONResponse({'ok': True, 'msg': 'User logged in'})
