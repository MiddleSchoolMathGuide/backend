import bson.json_util
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import ORJSONResponse

import json
import bson

from const import AUTH_COOKIE

from db.src.auth import session
from db.src.topic import topics


router = APIRouter()


@router.get('/api/{topic}/{unit}/{lesson}', response_class=ORJSONResponse)
async def get_lesson_and_context(
    request: Request, topic: str, unit: str, lesson: str
) -> ORJSONResponse:
    if session.is_expired(request.cookies.get(AUTH_COOKIE) or ''):
        raise HTTPException(status_code=401, detail='Not authorized')

    return ORJSONResponse(
        json.loads(bson.json_util.dumps(topics.get_by_titles(topic, unit, lesson)))
    )
