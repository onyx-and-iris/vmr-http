"""Models for the parameters of an equalizer."""

from typing import Optional

from pydantic import BaseModel, Field


class EQParams(BaseModel):
    """Parameters for an equalizer."""

    on: Optional[bool] = Field(None, description='Whether the equalizer is enabled or not.')
    ab: Optional[bool] = Field(None, description='Whether the equalizer is in mode A/B.')


class EQChannelCellParams(BaseModel):
    """Parameters for an equalizer channel cell."""

    on: Optional[bool] = Field(None, description='Whether the equalizer channel cell is enabled or not.')
    type: Optional[int] = Field(None, ge=0, le=6, description='Type of the equalizer channel cell.')
    f: Optional[float] = Field(None, ge=20.0, le=20000.0, description='Frequency of the equalizer channel cell.')
    gain: Optional[float] = Field(None, ge=-36.0, le=18.0, description='Gain of the equalizer channel cell.')
    q: Optional[float] = Field(None, ge=0.3, le=100.0, description='Q factor of the equalizer channel cell.')
