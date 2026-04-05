"""module for strip gate related endpoints."""

from fastapi import APIRouter, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.strip import StripGateParams

router = APIRouter()


@router.patch('')
@router.put('')
async def update_strip_gate_params(index: int, params: StripGateParams, voicemeeter=Depends(get_voicemeeter_client)):
    """Update one or more gate parameters for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    updated = {}
    for key, value in params.model_dump(exclude_unset=True).items():
        setattr(strip_gate, key, value)
        updated[key] = getattr(strip_gate, key)
    return updated


@router.get('/knob')
async def get_strip_gate_knob(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gate knob value for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    return {'knob': strip_gate.knob}
