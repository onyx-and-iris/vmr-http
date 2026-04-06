"""Module for equalizer related endpoints, supporting both strip and bus parents via a factory function."""

from typing import Literal

from fastapi import APIRouter, Depends

from vmr_http.dependencies import get_voicemeeter_client
from vmr_http.models.eq import EQChannelCellParams, EQParams


def create_router(eq_kind: str) -> APIRouter:
    """Create an APIRouter for equalizer endpoints, with the specified kind ('strip' or 'bus')."""
    if eq_kind not in ('strip', 'bus'):
        raise ValueError(f'Invalid router kind: {eq_kind}')
    parent_attr: Literal['strip', 'bus'] = eq_kind

    def target_cls(voicemeeter, index):
        return getattr(voicemeeter, parent_attr)[index]

    cell_router = APIRouter()

    @cell_router.patch('')
    @cell_router.put('')
    def update_eq_channel_cell_params(
        index: int,
        channel_index: int,
        cell_index: int,
        params: EQChannelCellParams,
        voicemeeter=Depends(get_voicemeeter_client),
    ):
        """Update one or more parameters for the specified eq channel cell."""
        cell = target_cls(voicemeeter, index).eq.channel[channel_index].cell[cell_index]
        updated = {}
        for key, value in params.model_dump(exclude_unset=True).items():
            setattr(cell, key, value)
            updated[key] = getattr(cell, key)
        return updated

    @cell_router.get('/on')
    def get_eq_channel_cell_on(
        index: int, channel_index: int, cell_index: int, voicemeeter=Depends(get_voicemeeter_client)
    ):
        """Get the current on status for the specified eq channel cell."""
        return {'on': target_cls(voicemeeter, index).eq.channel[channel_index].cell[cell_index].on}

    @cell_router.get('/type')
    def get_eq_channel_cell_type(
        index: int, channel_index: int, cell_index: int, voicemeeter=Depends(get_voicemeeter_client)
    ):
        """Get the current type for the specified eq channel cell."""
        return {'type': target_cls(voicemeeter, index).eq.channel[channel_index].cell[cell_index].type}

    @cell_router.get('/f')
    def get_eq_channel_cell_f(
        index: int, channel_index: int, cell_index: int, voicemeeter=Depends(get_voicemeeter_client)
    ):
        """Get the current f value for the specified eq channel cell."""
        return {'f': target_cls(voicemeeter, index).eq.channel[channel_index].cell[cell_index].f}

    @cell_router.get('/gain')
    def get_eq_channel_cell_gain(
        index: int, channel_index: int, cell_index: int, voicemeeter=Depends(get_voicemeeter_client)
    ):
        """Get the current gain value for the specified eq channel cell."""
        return {'gain': target_cls(voicemeeter, index).eq.channel[channel_index].cell[cell_index].gain}

    @cell_router.get('/q')
    def get_eq_channel_cell_q(
        index: int, channel_index: int, cell_index: int, voicemeeter=Depends(get_voicemeeter_client)
    ):
        """Get the current q value for the specified eq channel cell."""
        return {'q': target_cls(voicemeeter, index).eq.channel[channel_index].cell[cell_index].q}

    router = APIRouter()
    router.include_router(cell_router, prefix='/channel/{channel_index}/cell/{cell_index}')

    @router.patch('')
    @router.put('')
    def update_eq_params(index: int, params: EQParams, voicemeeter=Depends(get_voicemeeter_client)):
        """Update one or more equalizer parameters for the specified index."""
        eq = target_cls(voicemeeter, index).eq
        updated = {}
        for key, value in params.model_dump(exclude_unset=True).items():
            setattr(eq, key, value)
            updated[key] = getattr(eq, key)
        return updated

    @router.get('/on')
    def get_eq_on(index: int, voicemeeter=Depends(get_voicemeeter_client)):
        """Get the current equalizer on status for the specified index."""
        return {'on': target_cls(voicemeeter, index).eq.on}

    @router.get('/ab')
    def get_eq_ab(index: int, voicemeeter=Depends(get_voicemeeter_client)):
        """Get the current equalizer A/B status for the specified index."""
        return {'ab': target_cls(voicemeeter, index).eq.ab}

    return router
