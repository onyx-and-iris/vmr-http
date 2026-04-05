"""module for equalizer related endpoints."""

from fastapi import APIRouter, Body, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.eq import EQChannelCellParams

cell_router = APIRouter()


@cell_router.patch('')
@cell_router.put('')
async def update_strip_eq_channel_cell_params(
    index: int,
    channel_index: int,
    cell_index: int,
    params: EQChannelCellParams,
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Update one or more parameters for the specified strip eq channel cell."""
    cell = voicemeeter.strip[index].eq.channel[channel_index].cell[cell_index]
    updated = {}
    for key, value in params.model_dump(exclude_unset=True).items():
        setattr(cell, key, value)
        updated[key] = getattr(cell, key)
    return updated


@cell_router.get('/on')
async def get_strip_eq_channel_cell_on(
    index: int, channel_index: int, cell_index: int, voicemeeter=Depends(get_voicemeeter_client)
):
    """Get the current on status for the specified strip eq channel cell."""
    return {'on': voicemeeter.strip[index].eq.channel[channel_index].cell[cell_index].on}


@cell_router.get('/type')
async def get_strip_eq_channel_cell_type(
    index: int, channel_index: int, cell_index: int, voicemeeter=Depends(get_voicemeeter_client)
):
    """Get the current type for the specified strip eq channel cell."""
    return {'type': voicemeeter.strip[index].eq.channel[channel_index].cell[cell_index].type}


@cell_router.get('/f')
async def get_strip_eq_channel_cell_f(
    index: int, channel_index: int, cell_index: int, voicemeeter=Depends(get_voicemeeter_client)
):
    """Get the current f value for the specified strip eq channel cell."""
    return {'f': voicemeeter.strip[index].eq.channel[channel_index].cell[cell_index].f}


@cell_router.get('/gain')
async def get_strip_eq_channel_cell_gain(
    index: int, channel_index: int, cell_index: int, voicemeeter=Depends(get_voicemeeter_client)
):
    """Get the current gain value for the specified strip eq channel cell."""
    return {'gain': voicemeeter.strip[index].eq.channel[channel_index].cell[cell_index].gain}


@cell_router.get('/q')
async def get_strip_eq_channel_cell_q(
    index: int, channel_index: int, cell_index: int, voicemeeter=Depends(get_voicemeeter_client)
):
    """Get the current q value for the specified strip eq channel cell."""
    return {'q': voicemeeter.strip[index].eq.channel[channel_index].cell[cell_index].q}


router = APIRouter()
router.include_router(cell_router, prefix='/channel/{channel_index}/cell/{cell_index}')


@router.patch('')
@router.put('')
async def update_strip_eq_params(
    index: int, on: bool = Body(..., embed=True), voicemeeter=Depends(get_voicemeeter_client)
):
    """Update one or more equalizer parameters for the specified strip index."""
    strip_eq = voicemeeter.strip[index].eq
    strip_eq.on = on
    return {'on': strip_eq.on}


@router.get('/on')
async def get_strip_eq_on(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current equalizer on status for the specified strip index."""
    return {'on': voicemeeter.strip[index].eq.on}
