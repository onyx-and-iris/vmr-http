"""module for strip gate related endpoints."""

from fastapi import APIRouter, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.strip import StripGateParams

router = APIRouter()


@router.patch('')
@router.put('')
def update_strip_gate_params(index: int, params: StripGateParams, voicemeeter=Depends(get_voicemeeter_client)):
    """Update one or more gate parameters for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    updated = {}
    for key, value in params.model_dump(exclude_unset=True).items():
        setattr(strip_gate, key, value)
        updated[key] = getattr(strip_gate, key)
    return updated


@router.get('/knob')
def get_strip_gate_knob(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gate knob value for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    return {'knob': strip_gate.knob}


@router.get('/threshold')
def get_strip_gate_threshold(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gate threshold value for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    return {'threshold': strip_gate.threshold}


@router.get('/damping')
def get_strip_gate_damping(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gate damping value for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    return {'damping': strip_gate.damping}


@router.get('/bpsidechain')
def get_strip_gate_bpsidechain(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gate sidechain value for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    return {'bpsidechain': strip_gate.bpsidechain}


@router.get('/attack')
def get_strip_gate_attack(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gate attack value for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    return {'attack': strip_gate.attack}


@router.get('/hold')
def get_strip_gate_hold(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gate hold value for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    return {'hold': strip_gate.hold}


@router.get('/release')
def get_strip_gate_release(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gate release value for the specified strip index."""
    strip_gate = voicemeeter.strip[index].gate
    return {'release': strip_gate.release}
