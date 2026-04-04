"""module for strip denoiser related endpoints."""

from fastapi import APIRouter, Body, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.strip import StripDenoiserParams

router = APIRouter()


@router.put('/{index}/denoiser')
async def set_strip_denoiser_params(
    index: int,
    request: StripDenoiserParams,
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the denoiser parameters for the specified strip index."""
    strip_denoiser = voicemeeter.strip[index].denoiser
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(strip_denoiser, key, value)

    return {key: getattr(strip_denoiser, key) for key in request.model_dump(exclude_unset=True)}


@router.get('/{index}/denoiser/knob')
async def get_strip_denoiser_knob(
    index: int,
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Get the denoiser knob value for the specified strip index."""
    strip_denoiser = voicemeeter.strip[index].denoiser
    return {'knob': strip_denoiser.knob}


@router.put('/{index}/denoiser/knob')
async def set_strip_denoiser_knob(
    index: int,
    knob: float = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the denoiser knob value for the specified strip index."""
    strip_denoiser = voicemeeter.strip[index].denoiser
    strip_denoiser.knob = knob
    return {'knob': strip_denoiser.knob}
