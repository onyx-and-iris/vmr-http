from fastapi import APIRouter, Depends

from vmr_http.dependencies import get_voicemeeter_client

router = APIRouter()


@router.get("/{index}/gain")
async def get_gain(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    return {"gain": voicemeeter.strip[index].gain}
