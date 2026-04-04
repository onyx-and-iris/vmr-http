"""module for bus-related endpoints."""

from fastapi import APIRouter, Body, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.bus import BusParams

from . import busmode

router = APIRouter()
router.include_router(busmode.router, prefix='/mode', tags=['bus mode'])


@router.put('/{index}', tags=['bus'])
async def set_bus_params(index: int, request: BusParams, voicemeeter=Depends(get_voicemeeter_client)):
    """Set multiple parameters of a bus at once."""
    bus = voicemeeter.bus[index]
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(bus, key, value)

    return {key: getattr(bus, key) for key in request.model_dump(exclude_unset=True)}


@router.get('/{index}/gain', tags=['bus'])
async def get_gain(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gain value for the specified bus index."""
    return {'gain': voicemeeter.bus[index].gain}


@router.put('/{index}/gain', tags=['bus'])
async def set_gain(
    index: int,
    gain: float = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the gain value for the specified bus index."""
    voicemeeter.bus[index].gain = gain
    return {'gain': voicemeeter.bus[index].gain}


@router.get('/{index}/mute', tags=['bus'])
async def get_mute(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current mute status for the specified bus index."""
    return {'mute': voicemeeter.bus[index].mute}


@router.put('/{index}/mute', tags=['bus'])
async def set_mute(
    index: int,
    mute: bool = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the mute status for the specified bus index."""
    voicemeeter.bus[index].mute = mute
    return {'mute': voicemeeter.bus[index].mute}
