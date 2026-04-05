"""module for strip compressor related endpoints."""

from fastapi import APIRouter, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.strip import StripCompParams

router = APIRouter()


@router.patch('/{index}/comp')
@router.put('/{index}/comp')
async def update_strip_comp_params(index: int, params: StripCompParams, voicemeeter=Depends(get_voicemeeter_client)):
    """Update one or more compressor parameters for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    updated = {}
    for key, value in params.model_dump(exclude_unset=True).items():
        setattr(strip_comp, key, value)
        updated[key] = getattr(strip_comp, key)
    return updated


@router.get('/{index}/comp/knob')
async def get_strip_comp_knob(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current compressor knob value for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    return {'knob': strip_comp.knob}
