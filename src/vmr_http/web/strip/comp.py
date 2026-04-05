"""module for strip compressor related endpoints."""

from fastapi import APIRouter, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.strip import StripCompParams

router = APIRouter()


@router.patch('')
@router.put('')
async def update_strip_comp_params(index: int, params: StripCompParams, voicemeeter=Depends(get_voicemeeter_client)):
    """Update one or more compressor parameters for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    updated = {}
    for key, value in params.model_dump(exclude_unset=True).items():
        setattr(strip_comp, key, value)
        updated[key] = getattr(strip_comp, key)
    return updated


@router.get('/knob')
async def get_strip_comp_knob(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current compressor knob value for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    return {'knob': strip_comp.knob}


@router.get('/gainin')
async def get_strip_comp_gainin(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current compressor gain in value for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    return {'gainin': strip_comp.gainin}


@router.get('/ratio')
async def get_strip_comp_ratio(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current compressor ratio value for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    return {'ratio': strip_comp.ratio}


@router.get('/threshold')
async def get_strip_comp_threshold(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current compressor threshold value for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    return {'threshold': strip_comp.threshold}


@router.get('/attack')
async def get_strip_comp_attack(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current compressor attack value for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    return {'attack': strip_comp.attack}


@router.get('/release')
async def get_strip_comp_release(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current compressor release value for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    return {'release': strip_comp.release}


@router.get('/knee')
async def get_strip_comp_knee(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current compressor knee value for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    return {'knee': strip_comp.knee}


@router.get('/gainout')
async def get_strip_comp_gainout(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current compressor gain out value for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    return {'gainout': strip_comp.gainout}


@router.get('/makeup')
async def get_strip_comp_makeup(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current compressor makeup status for the specified strip index."""
    strip_comp = voicemeeter.strip[index].comp
    return {'makeup': strip_comp.makeup}
