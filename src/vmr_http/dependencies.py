"""module containing dependencies for the API endpoints."""

from fastapi import Request


def get_voicemeeter_client(request: Request):
    """Dependency to get the Voicemeeter client from the application state."""
    return request.app.state.voicemeeter
