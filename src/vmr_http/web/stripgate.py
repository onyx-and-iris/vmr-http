"""module for strip gate related endpoints."""

from fastapi import APIRouter, Body, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.strip import StripGateParams

router = APIRouter()


@router.put('/{index}/gate')
async def set_strip_gate_params(index: int, request: StripGateParams, voicemeeter=Depends(get_voicemeeter_client)):
    """Set the gate parameters for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(strip_gate, key, value)

    return {key: getattr(strip_gate, key) for key in request.model_dump(exclude_unset=True)}


@router.get('/{index}/gate/knob')
async def get_strip_gate_knob(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gate knob value for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    return {'knob': strip_gate.knob}


@router.put('/{index}/gate/knob')
async def set_strip_gate_knob(
    index: int,
    knob: float = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the gate knob value for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    strip_gate.knob = knob
    return {'knob': strip_gate.knob}
