"""Models for the parameters of an equalizer."""

from typing import Optional

from pydantic import BaseModel


class EQChannelCellParams(BaseModel):
    """Parameters for an equalizer channel."""

    on: Optional[bool] = None
    type: Optional[int] = None
    f: Optional[float] = None
    gain: Optional[float] = None
    q: Optional[float] = None
