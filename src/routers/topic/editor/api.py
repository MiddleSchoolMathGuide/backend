from fastapi import APIRouter, Request
from fastapi.responses import ORJSONResponse

from const import AUTH_COOKIE

from db.src.auth import session
from db.src.topic import topics


router = APIRouter()


@router.put('/topic/editor', response_class=ORJSONResponse)
async def update_topic(request: Request) -> ORJSONResponse:
    if session.is_expired(request.cookies.get(AUTH_COOKIE)):
        return ORJSONResponse(
            {'ok': False, 'msg': 'Authentication error'}, status_code=401
        )

    topic_update = await request.json()
    if not topic_update or topic_update.get('ok') is not True:
        return ORJSONResponse(
            {'ok': False, 'msg': 'Invalid topic update'}, status_code=401
        )

    topics.set(topic_update['content'])
    return ORJSONResponse({'ok': True, 'msg': 'Update successful'})
