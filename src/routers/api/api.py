import bson.json_util
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

import json
import bson

from db.src.topic import topics


router = APIRouter()


@router.get('/api/t/{topic}/{unit}/{lesson}', response_class=ORJSONResponse)
async def get_lesson_and_context(topic: str, unit: str, lesson: str) -> ORJSONResponse:

    return ORJSONResponse(
        json.loads(bson.json_util.dumps(topics.get_by_titles(topic, unit, lesson)))
    )


@router.get('/api/topics', response_class=ORJSONResponse)
async def get_topics() -> ORJSONResponse:
    return ORJSONResponse({'ok': True, 'msg': 'Success', 'data': topics.get_all()})


@router.get('/api/unit_context/{topic}/{unit}', response_class=ORJSONResponse)
async def unit_context(unit: str)