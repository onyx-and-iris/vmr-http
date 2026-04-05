"""module for strip gain layer related endpoints."""

from fastapi import APIRouter, Body, Depends

from vmr_http.dependencies import get_voicemeeter_client

router = APIRouter()


@router.patch('')
@router.put('')
async def update_strip_comp_params(
    index: int,
    gainlayer_index: int,
    level: float = Body(..., ge=-60.0, le=12.0, embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Update one or more compressor parameters for the specified strip index."""
    gainlayer = voicemeeter.strip[index].gainlayer[gainlayer_index]
    gainlayer.gain = level
    return {'gain_layer': {'level': gainlayer.gain}}


@router.get('/level')
async def get_strip_gain_layer_level(index: int, gainlayer_index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gain layer level for the specified strip index."""
    return {'gain_layer': {'level': voicemeeter.strip[index].gainlayer[gainlayer_index].gain}}
