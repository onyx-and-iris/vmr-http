"""Models for the parameters of an equalizer."""

from typing import Optional

from pydantic import BaseModel, Field


class EQParams(BaseModel):
    """Parameters for an equalizer."""

    on: Optional[bool] = Field(description='Whether the equalizer is enabled or not.')
    ab: Optional[bool] = Field(description='Whether the equalizer is in mode A/B.')


class EQChannelCellParams(BaseModel):
    """Parameters for an equalizer channel."""

    on: Optional[bool] = Field(description='Whether the equalizer channel is enabled or not.')
    type: Optional[int] = Field(ge=0, le=6, description='Type of the equalizer channel.')
    f: Optional[float] = Field(ge=20.0, le=20000.0, description='Frequency of the equalizer channel.')
    gain: Optional[float] = Field(ge=-36.0, le=18.0, description='Gain of the equalizer channel.')
    q: Optional[float] = Field(ge=0.3, le=100.0, description='Q factor of the equalizer channel.')
