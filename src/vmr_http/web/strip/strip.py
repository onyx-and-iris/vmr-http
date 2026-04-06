"""module for strip-related endpoints."""

from fastapi import APIRouter, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.strip import StripParams
from vmr_http.web import eq

from . import comp, denoiser, gainlayer, gate

router = APIRouter()
router.include_router(gainlayer.router, prefix='/gainlayer/{gainlayer_index}', tags=['strip gainlayer'])
router.include_router(comp.router, prefix='/comp', tags=['strip comp'])
router.include_router(gate.router, prefix='/gate', tags=['strip gate'])
router.include_router(denoiser.router, prefix='/denoiser', tags=['strip denoiser'])
router.include_router(eq.create_router(eq_kind='strip'), prefix='/eq', tags=['strip eq'])


@router.patch('', tags=['strip'])
@router.put('', tags=['strip'])
def update_strip_params(index: int, params: StripParams, voicemeeter=Depends(get_voicemeeter_client)):
    """Update one or more parameters for the specified strip index."""
    strip = voicemeeter.strip[index]
    updated = {}
    for key, value in params.model_dump(exclude_unset=True).items():
        setattr(strip, key, value)
        updated[key] = getattr(strip, key)
    return updated


@router.get('/gain', tags=['strip'])
def get_gain(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gain value for the specified strip index."""
    return {'gain': voicemeeter.strip[index].gain}


@router.get('/mute', tags=['strip'])
def get_mute(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current mute status for the specified strip index."""
    return {'mute': voicemeeter.strip[index].mute}


@router.get('/mono', tags=['strip'])
def get_mono(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current mono status for the specified strip index."""
    return {'mono': voicemeeter.strip[index].mono}


@router.get('/solo', tags=['strip'])
def get_solo(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current solo status for the specified strip index."""
    return {'solo': voicemeeter.strip[index].solo}


@router.get('/A1', tags=['strip'])
def get_A1(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current A1 output status for the specified strip index."""
    return {'A1': voicemeeter.strip[index].A1}


@router.get('/A2', tags=['strip'])
def get_A2(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current A2 output status for the specified strip index."""
    return {'A2': voicemeeter.strip[index].A2}


@router.get('/A3', tags=['strip'])
def get_A3(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current A3 output status for the specified strip index."""
    return {'A3': voicemeeter.strip[index].A3}


@router.get('/A4', tags=['strip'])
def get_A4(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current A4 output status for the specified strip index."""
    return {'A4': voicemeeter.strip[index].A4}


@router.get('/A5', tags=['strip'])
def get_A5(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current A5 output status for the specified strip index."""
    return {'A5': voicemeeter.strip[index].A5}


@router.get('/B1', tags=['strip'])
def get_B1(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current B1 output status for the specified strip index."""
    return {'B1': voicemeeter.strip[index].B1}


@router.get('/B2', tags=['strip'])
def get_B2(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current B2 output status for the specified strip index."""
    return {'B2': voicemeeter.strip[index].B2}


@router.get('/B3', tags=['strip'])
def get_B3(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current B3 output status for the specified strip index."""
    return {'B3': voicemeeter.strip[index].B3}
