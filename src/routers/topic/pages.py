import json
from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, HTMLResponse

from db.src.topic import topics, units, lessons

from const import PAGES


router = APIRouter()


@router.get('/topic', response_class=FileResponse)
async def topic_page(request: Request) -> FileResponse:
    return FileResponse(f'{PAGES}/topic.html')


@router.get('/topic/directory/{topic}', response_class=HTMLResponse)
async def topicdir_page(topic: str) -> HTMLResponse:

    with open(f'{PAGES}/topic/topicdir.html', 'r', encoding='utf-8') as f:
        content = f.read()
        f.close()

    data = {'ok': False, 'msg': 'No such topic', 'data': {}}
    topic_id = topics.get_id_by_title(topic)
    if topic_id is not None:
        unit_list = list(units.get_all(topic_id, include_id=True))
        for i, unit in enumerate(unit_list):
            print(unit)
            unit_list[i]['lessons'] = lessons.get_all(unit['_id'])

        data = {'ok': True, 'msg': 'Success', 'data': unit_list}

    content = content.replace(
        '<div id="dynamic-data" data=\'\'></div>',
        f'<div id="dynamic-data" data=\'{json.dumps(data, default=str)}\'></div>',
    )

    return HTMLResponse(content)


@router.get('/t/{topic}/{unit}/{lesson}', response_class=FileResponse)
async def lesson_page(topic: str, unit: str, lesson: str) -> FileResponse:
    return FileResponse(f'{PAGES}/lesson.html')
