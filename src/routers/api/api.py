import bson.json_util
from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

import json
import bson

from db.src.topic import topics, units


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
async def unit_context(topic: str, unit: str) -> ORJSONResponse:
    topic_res = topics.get_topic_by_title(topic)
    if topic_res['ok'] is not True:
        return ORJSONResponse(topic_res)
    units_ = units.get_all(topic_res['data']['_id'])
    unit_res = units.get_unit_by_title(unit)
    if unit_res['ok'] is not True:
        return ORJSONResponse(unit_res)
    lessons_ = unit_res['data']['lessons']
    print(lessons_)
    print(units_)
    for i, lesson in enumerate(lessons_):
        lesson.pop('_id', None)
        lesson = {
            k: v
            for k, v in lesson.items()
            if k
            not in (
                'credits',
                'icon',
                'status',
                'unit_id',
                'widgets',
            )
        }

        lessons_[i] = lesson

    return ORJSONResponse({
        'ok': True,
        'msg': 'Success',
        'data': {'units': units_, 'lessons': lessons_},
    })
