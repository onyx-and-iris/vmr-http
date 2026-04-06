"""module for strip gain layer related endpoints."""

from fastapi import APIRouter, Body, Depends

from vmr_http.dependencies import get_voicemeeter_client

router = APIRouter()


@router.patch('')
@router.put('')
def update_strip_gainlayer_params(
    index: int,
    gainlayer_index: int,
    level: float = Body(..., ge=-60.0, le=12.0, embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Update one or more gain layer parameters for the specified strip index."""
    gainlayer = voicemeeter.strip[index].gainlayer[gainlayer_index]
    gainlayer.gain = level
    return {'gainlayer': {'level': gainlayer.gain}}


@router.get('/level')
def get_strip_gainlayer_level(index: int, gainlayer_index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gain layer level for the specified strip index."""
    return {'gainlayer': {'level': voicemeeter.strip[index].gainlayer[gainlayer_index].gain}}
