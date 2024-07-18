from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

import json

from const import AUTH_COOKIE, PAGES

from db.src.auth import session
from db.src.edu import topics


router = APIRouter()


@router.get('/edu/editor{endpoint:path}', response_class=HTMLResponse)
async def editor_page(request: Request) -> HTMLResponse:
    if session.is_expired(request.cookies.get(AUTH_COOKIE)):
        return HTMLResponse(status_code=401)

    topic_name = request.query_params.get('topic')

    with open(f'{PAGES}/edu/editor.html', 'r', encoding='utf-8') as f:
        content = f.read()

    if topic_name != 'new':
        topic = topics.get_topic(topic_name)
        content = content.replace(
            '<div id="dynamic-data" data=\'\'></div>',
            f'<div id="dynamic-data" data=\'{json.dumps(topic, default=str)}\'></div>',
        )

    return HTMLResponse(content)
