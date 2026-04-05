"""Models for the parameters of a strip."""

from typing import Optional

from pydantic import BaseModel, Field


class StripParams(BaseModel):
    """Parameters for a single strip."""

    gain: Optional[float] = Field(None, ge=-60.0, le=12.0, description='Gain value for the strip')
    mute: Optional[bool] = Field(None, description='Mute status for the strip')
    mono: Optional[bool] = Field(None, description='Mono status for the strip')
    solo: Optional[bool] = Field(None, description='Solo status for the strip')
    A1: Optional[bool] = Field(None, description='A1 output status for the strip')
    A2: Optional[bool] = Field(None, description='A2 output status for the strip')
    A3: Optional[bool] = Field(None, description='A3 output status for the strip')
    A4: Optional[bool] = Field(None, description='A4 output status for the strip')
    A5: Optional[bool] = Field(None, description='A5 output status for the strip')
    B1: Optional[bool] = Field(None, description='B1 output status for the strip')
    B2: Optional[bool] = Field(None, description='B2 output status for the strip')
    B3: Optional[bool] = Field(None, description='B3 output status for the strip')


class StripCompParams(BaseModel):
    """Parameters for the compressor of a strip."""

    knob: Optional[float] = Field(None, ge=0.0, le=10.0, description='Compressor knob value for the strip')
    gainin: Optional[float] = Field(None, ge=-24.0, le=24.0, description='Compressor gain in value for the strip')
    ratio: Optional[float] = Field(None, ge=1.0, le=8.0, description='Compressor ratio value for the strip')
    threshold: Optional[float] = Field(None, ge=-40.0, le=-3.0, description='Compressor threshold value for the strip')
    attack: Optional[float] = Field(None, ge=0.0, le=200.0, description='Compressor attack value for the strip')
    release: Optional[float] = Field(None, ge=0.0, le=5000.0, description='Compressor release value for the strip')
    knee: Optional[float] = Field(None, ge=0.0, le=1.0, description='Compressor knee value for the strip')
    gainout: Optional[float] = Field(None, ge=-24.0, le=24.0, description='Compressor gain out value for the strip')
    makeup: Optional[bool] = Field(None, description='Compressor makeup status for the strip')


class StripGateParams(BaseModel):
    """Parameters for the gate of a strip."""

    knob: Optional[float] = Field(None, ge=0.0, le=10.0, description='Gate knob value for the strip')
    threshold: Optional[float] = Field(None, ge=-60.0, le=-10.0, description='Gate threshold value for the strip')
    damping: Optional[float] = Field(None, ge=-60.0, le=-10.0, description='Gate damping value for the strip')
    bpsidechain: Optional[float] = Field(None, ge=100.0, le=4000.0, description='Gate sidechain value for the strip')
    attack: Optional[float] = Field(None, ge=0.0, le=1000.0, description='Gate attack value for the strip')
    hold: Optional[float] = Field(None, ge=0.0, le=5000.0, description='Gate hold value for the strip')
    release: Optional[float] = Field(None, ge=0.0, le=5000.0, description='Gate release value for the strip')


class StripDenoiserParams(BaseModel):
    """Parameters for the denoiser of a strip."""

    knob: Optional[float] = Field(None, ge=0.0, le=10.0, description='Denoiser knob value for the strip')
