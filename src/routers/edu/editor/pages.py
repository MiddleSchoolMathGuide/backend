from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

from const import AUTH_COOKIE, PAGES

from db.src.auth import session


router = APIRouter()


@router.get('/edu/editor', response_class=FileResponse)
async def editor_page(request: Request) -> FileResponse:
    if session.is_expired(request.cookies.get(AUTH_COOKIE)):
        return FileResponse(status_code=401)

    return FileResponse(f'{PAGES}/edu/editor.html')
