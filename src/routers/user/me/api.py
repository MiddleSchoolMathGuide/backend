from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

from const import AUTH_COOKIE

from db.src.auth import session
from db.src.users import profile


router = APIRouter()


@router.get('/user/me/profile', response_class=ORJSONResponse)
async def is_logged_in(request: Request) -> ORJSONResponse:
    if session.is_expired(request.cookies.get(AUTH_COOKIE)):
        return ORJSONResponse(
            {'ok': False, 'msg': 'Session expired or invalid'}, status_code=401
        )

    return ORJSONResponse(profile.fetch(request.cookies.get('username')))
