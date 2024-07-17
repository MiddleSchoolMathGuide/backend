from fastapi import APIRouter
from fastapi.responses import FileResponse

from const import PAGES

router = APIRouter()


@router.get('/user/me', response_class=FileResponse)
async def login_api() -> FileResponse:
    return FileResponse(f'{PAGES}/me.html')
