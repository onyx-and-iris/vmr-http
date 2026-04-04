"""Models for the parameters of a strip."""

from typing import Optional

from pydantic import BaseModel


class StripParams(BaseModel):
    """Parameters for a single strip."""

    gain: Optional[float] = None
    mute: Optional[bool] = None
    mono: Optional[bool] = None
    solo: Optional[bool] = None
    A1: Optional[bool] = None
    A2: Optional[bool] = None
    A3: Optional[bool] = None
    A4: Optional[bool] = None
    A5: Optional[bool] = None
    B1: Optional[bool] = None
    B2: Optional[bool] = None
    B3: Optional[bool] = None


class StripCompParams(BaseModel):
    """Parameters for the compressor of a strip."""

    knob: Optional[float] = None
    gainin: Optional[float] = None
    ratio: Optional[float] = None
    threshold: Optional[float] = None
    attack: Optional[float] = None
    release: Optional[float] = None
    knee: Optional[float] = None
    gainout: Optional[float] = None
    makeup: Optional[bool] = None


class StripGateParams(BaseModel):
    """Parameters for the gate of a strip."""

    knob: Optional[float] = None
    threshold: Optional[float] = None
    damping: Optional[float] = None
    bpsidechain: Optional[float] = None
    attack: Optional[float] = None
    hold: Optional[float] = None
    release: Optional[float] = None


class StripDenoiserParams(BaseModel):
    """Parameters for the denoiser of a strip."""

    knob: Optional[float] = None
