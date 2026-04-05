"""module for bus mode related endpoints."""

from fastapi import APIRouter, Body, Depends, HTTPException

from vmr_http.dependencies import get_voicemeeter_client

router = APIRouter()

_readable_busmodes = {
    'normal': 'Normal',
    'amix': 'Mix Down A',
    'bmix': 'Mix Down B',
    'repeat': 'Stereo Repeat',
    'composite': 'Composite',
    'tvmix': 'Up Mix TV',
    'upmix21': 'Up Mix 2.1',
    'upmix41': 'Up Mix 4.1',
    'upmix61': 'Up Mix 6.1',
    'centeronly': 'Center Only',
    'lfeonly': 'Low Frequency Effect Only',
    'rearonly': 'Rear Only',
}
_reversed_busmodes = {v: k for k, v in _readable_busmodes.items()}


@router.patch('')
@router.put('')
async def update_bus_mode(index: int, mode: str = Body(..., embed=True), voicemeeter=Depends(get_voicemeeter_client)):
    """Update the bus mode for the specified bus index."""
    if mode not in _reversed_busmodes:
        raise HTTPException(
            status_code=400, detail=f'Invalid mode. Valid modes are: {", ".join(_reversed_busmodes.keys())}'
        )
    setattr(voicemeeter.bus[index].mode, _reversed_busmodes[mode], True)
    return {'mode': _readable_busmodes[_reversed_busmodes[mode]]}


@router.get('')
async def get_bus_mode(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current bus mode for the specified bus index."""
    return {'mode': _readable_busmodes.get(voicemeeter.bus[index].mode.get(), 'Unknown')}
