"""module for strip denoiser related endpoints."""

from fastapi import APIRouter, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.strip import StripDenoiserParams

router = APIRouter()


@router.patch('/{index}/denoiser')
@router.put('/{index}/denoiser')
async def update_strip_denoiser_params(
    index: int, params: StripDenoiserParams, voicemeeter=Depends(get_voicemeeter_client)
):
    """Update one or more denoiser parameters for the specified strip index."""
    strip_denoiser = voicemeeter.strip[index].denoiser
    updated = {}
    for key, value in params.model_dump(exclude_unset=True).items():
        setattr(strip_denoiser, key, value)
        updated[key] = getattr(strip_denoiser, key)
    return updated


@router.get('/{index}/denoiser/knob')
async def get_strip_denoiser_knob(
    index: int,
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Get the denoiser knob value for the specified strip index."""
    strip_denoiser = voicemeeter.strip[index].denoiser
    return {'knob': strip_denoiser.knob}
