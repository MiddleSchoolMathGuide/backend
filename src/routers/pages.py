from fastapi import APIRouter
from fastapi.responses import FileResponse

from const import PAGES

router = APIRouter()


@router.get('/', response_class=FileResponse)
async def homepage() -> FileResponse:
    return FileResponse(f'{PAGES}/index.html')
