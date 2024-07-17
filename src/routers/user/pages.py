from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

from const import AUTH_COOKIE, PAGES

from db.src.auth import session

router = APIRouter()


@router.get('/user/me', response_class=FileResponse)
async def login_api(request: Request) -> FileResponse:
    if session.is_expired(request.cookies.get(AUTH_COOKIE)):
        return FileResponse(f'{PAGES}/blocked.html')
    return FileResponse(f'{PAGES}/user/me.html')
