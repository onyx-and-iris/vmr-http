"""Models for the parameters of a bus."""

from typing import Optional

from pydantic import BaseModel


class BusParams(BaseModel):
    """Parameters for a single bus."""

    gain: Optional[float] = None
    mute: Optional[bool] = None
    mono: Optional[int] = None
