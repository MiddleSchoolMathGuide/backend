from fastapi import APIRouter
from fastapi.responses import FileResponse

from const import PAGES

router = APIRouter()


@router.get('/login', response_class=FileResponse)
async def login_page() -> FileResponse:
    return FileResponse(f'{PAGES}/login.html')


@router.get('/signup', response_class=FileResponse)
async def sign_up_page() -> FileResponse:
    return FileResponse(f'{PAGES}/signup.html')
