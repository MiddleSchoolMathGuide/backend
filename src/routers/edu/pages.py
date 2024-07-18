from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import FileResponse

from const import AUTH_COOKIE, PAGES

from db.src.auth import session


router = APIRouter()


@router.get('/edu', response_class=FileResponse)
async def edu_page(request: Request) -> FileResponse:
    if session.is_expired(request.cookies.get(AUTH_COOKIE)):
        raise HTTPException(status_code=401, detail="Not authorized")
    return FileResponse(f'{PAGES}/edu.html')
