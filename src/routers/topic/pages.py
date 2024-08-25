from fastapi import APIRouter, Request
from fastapi.responses import FileResponse

from const import PAGES


router = APIRouter()


@router.get('/topic', response_class=FileResponse)
async def topic_page(request: Request) -> FileResponse:
    return FileResponse(f'{PAGES}/topic.html')


@router.get('/t/{topic}/{unit}/{lesson}', response_class=FileResponse)
async def lesson_page(topic: str, unit: str, lesson: str) -> FileResponse:
    return FileResponse(f'{PAGES}/lesson.html')
