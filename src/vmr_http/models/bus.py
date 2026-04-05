"""Models for the parameters of a bus."""

from typing import Optional

from pydantic import BaseModel, Field


class BusParams(BaseModel):
    """Parameters for a single bus."""

    gain: Optional[float] = Field(None, ge=-60.0, le=12.0, description='Gain value for the bus')
    mute: Optional[bool] = Field(None, description='Mute status for the bus')
    mono: Optional[int] = Field(None, description='Mono status for the bus')
