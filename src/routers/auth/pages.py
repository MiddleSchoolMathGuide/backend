from fastapi import APIRouter
from fastapi.responses import FileResponse

from const import PAGES

router = APIRouter()


@router.get('/login', response_class=FileResponse)
async def login_page() -> FileResponse:
    return FileResponse(f'{PAGES}/login.html')
