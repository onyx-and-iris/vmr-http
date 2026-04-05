"""module for bus-related endpoints."""

from fastapi import APIRouter, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.bus import BusParams
from vmr_http.web import eq

from . import mode

router = APIRouter()
router.include_router(mode.router, prefix='/mode', tags=['bus mode'])
router.include_router(eq.create_router(eq_kind='bus'), prefix='/eq', tags=['bus eq'])


@router.patch('', tags=['bus'])
@router.put('', tags=['bus'])
async def update_bus_params(index: int, params: BusParams, voicemeeter=Depends(get_voicemeeter_client)):
    """Update one or more parameters for the specified bus index."""
    bus = voicemeeter.bus[index]
    updated = {}
    for key, value in params.model_dump(exclude_unset=True).items():
        setattr(bus, key, value)
        updated[key] = getattr(bus, key)
    return updated


@router.get('/gain', tags=['bus'])
async def get_gain(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gain value for the specified bus index."""
    return {'gain': voicemeeter.bus[index].gain}


@router.get('/mute', tags=['bus'])
async def get_mute(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current mute status for the specified bus index."""
    return {'mute': voicemeeter.bus[index].mute}


@router.get('/mono', tags=['bus'])
async def get_mono(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current mono status for the specified bus index."""
    opts = ['Off', 'On', 'Stereo Reverse']
    return {'mono': opts[voicemeeter.bus[index].mono]}
