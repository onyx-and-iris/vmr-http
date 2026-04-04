"""module for strip compressor related endpoints."""

from fastapi import APIRouter, Body, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.strip import StripCompParams

router = APIRouter()


@router.put('/{index}/comp')
async def set_strip_comp_params(index: int, request: StripCompParams, voicemeeter=Depends(get_voicemeeter_client)):
    """Set the compressor parameters for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(strip_comp, key, value)

    return {key: getattr(strip_comp, key) for key in request.model_dump(exclude_unset=True)}


@router.get('/{index}/comp/knob')
async def get_strip_comp_knob(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current compressor knob value for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    return {'knob': strip_comp.knob}


@router.put('/{index}/comp/knob')
async def set_strip_comp_knob(
    index: int,
    knob: float = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the compressor knob value for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    strip_comp.knob = knob
    return {'knob': strip_comp.knob}
