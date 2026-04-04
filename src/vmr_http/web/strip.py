"""module for strip-related endpoints."""

from fastapi import APIRouter, Body, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.strip import StripParams

from . import stripcomp, stripdenoiser, stripgate

router = APIRouter()
router.include_router(stripcomp.router, prefix='/comp', tags=['strip comp'])
router.include_router(stripgate.router, prefix='/gate', tags=['strip gate'])
router.include_router(stripdenoiser.router, prefix='/denoiser', tags=['strip denoiser'])


@router.put('/{index}', tags=['strip'])
async def set_strip_params(index: int, request: StripParams, voicemeeter=Depends(get_voicemeeter_client)):
    """Set the parameters for the specified strip index."""
    strip = voicemeeter.strip[index]
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(strip, key, value)

    return {key: getattr(strip, key) for key in request.model_dump(exclude_unset=True)}


@router.get('/{index}/gain', tags=['strip'])
async def get_gain(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current gain value for the specified strip index."""
    return {'gain': voicemeeter.strip[index].gain}


@router.put('/{index}/gain', tags=['strip'])
async def set_gain(
    index: int,
    gain: float = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the gain value for the specified strip index."""
    voicemeeter.strip[index].gain = gain
    return {'gain': voicemeeter.strip[index].gain}


@router.get('/{index}/mute', tags=['strip'])
async def get_mute(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current mute status for the specified strip index."""
    return {'mute': voicemeeter.strip[index].mute}


@router.put('/{index}/mute', tags=['strip'])
async def set_mute(
    index: int,
    mute: bool = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the mute status for the specified strip index."""
    voicemeeter.strip[index].mute = mute
    return {'mute': voicemeeter.strip[index].mute}


@router.get('/{index}/mono', tags=['strip'])
async def get_mono(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current mono status for the specified strip index."""
    return {'mono': voicemeeter.strip[index].mono}


@router.put('/{index}/mono', tags=['strip'])
async def set_mono(
    index: int,
    mono: bool = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the mono status for the specified strip index."""
    voicemeeter.strip[index].mono = mono
    return {'mono': voicemeeter.strip[index].mono}


@router.get('/{index}/solo', tags=['strip'])
async def get_solo(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current solo status for the specified strip index."""
    return {'solo': voicemeeter.strip[index].solo}


@router.put('/{index}/solo', tags=['strip'])
async def set_solo(
    index: int,
    solo: bool = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the solo status for the specified strip index."""
    voicemeeter.strip[index].solo = solo
    return {'solo': voicemeeter.strip[index].solo}


@router.get('/{index}/A1', tags=['strip'])
async def get_A1(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current A1 output status for the specified strip index."""
    return {'A1': voicemeeter.strip[index].A1}


@router.put('/{index}/A1', tags=['strip'])
async def set_A1(
    index: int,
    A1: bool = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the A1 output status for the specified strip index."""
    voicemeeter.strip[index].A1 = A1
    return {'A1': voicemeeter.strip[index].A1}


@router.get('/{index}/A2', tags=['strip'])
async def get_A2(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current A2 output status for the specified strip index."""
    return {'A2': voicemeeter.strip[index].A2}


@router.put('/{index}/A2', tags=['strip'])
async def set_A2(
    index: int,
    A2: bool = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the A2 output status for the specified strip index."""
    voicemeeter.strip[index].A2 = A2
    return {'A2': voicemeeter.strip[index].A2}


@router.get('/{index}/A3', tags=['strip'])
async def get_A3(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current A3 output status for the specified strip index."""
    return {'A3': voicemeeter.strip[index].A3}


@router.put('/{index}/A3', tags=['strip'])
async def set_A3(
    index: int,
    A3: bool = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the A3 output status for the specified strip index."""
    voicemeeter.strip[index].A3 = A3
    return {'A3': voicemeeter.strip[index].A3}


@router.get('/{index}/A4', tags=['strip'])
async def get_A4(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current A4 output status for the specified strip index."""
    return {'A4': voicemeeter.strip[index].A4}


@router.put('/{index}/A4', tags=['strip'])
async def set_A4(
    index: int,
    A4: bool = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the A4 output status for the specified strip index."""
    voicemeeter.strip[index].A4 = A4
    return {'A4': voicemeeter.strip[index].A4}


@router.get('/{index}/A5', tags=['strip'])
async def get_A5(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current A5 output status for the specified strip index."""
    return {'A5': voicemeeter.strip[index].A5}


@router.put('/{index}/A5', tags=['strip'])
async def set_A5(
    index: int,
    A5: bool = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the A5 output status for the specified strip index."""
    voicemeeter.strip[index].A5 = A5
    return {'A5': voicemeeter.strip[index].A5}


@router.get('/{index}/B1', tags=['strip'])
async def get_B1(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current B1 output status for the specified strip index."""
    return {'B1': voicemeeter.strip[index].B1}


@router.put('/{index}/B1', tags=['strip'])
async def set_B1(
    index: int,
    B1: bool = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the B1 output status for the specified strip index."""
    voicemeeter.strip[index].B1 = B1
    return {'B1': voicemeeter.strip[index].B1}


@router.get('/{index}/B2', tags=['strip'])
async def get_B2(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current B2 output status for the specified strip index."""
    return {'B2': voicemeeter.strip[index].B2}


@router.put('/{index}/B2', tags=['strip'])
async def set_B2(
    index: int,
    B2: bool = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the B2 output status for the specified strip index."""
    voicemeeter.strip[index].B2 = B2
    return {'B2': voicemeeter.strip[index].B2}


@router.get('/{index}/B3', tags=['strip'])
async def get_B3(index: int, voicemeeter=Depends(get_voicemeeter_client)):
    """Get the current B3 output status for the specified strip index."""
    return {'B3': voicemeeter.strip[index].B3}


@router.put('/{index}/B3', tags=['strip'])
async def set_B3(
    index: int,
    B3: bool = Body(..., embed=True),
    voicemeeter=Depends(get_voicemeeter_client),
):
    """Set the B3 output status for the specified strip index."""
    voicemeeter.strip[index].B3 = B3
    return {'B3': voicemeeter.strip[index].B3}
