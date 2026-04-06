"""entry point for the FastAPI application."""

from contextlib import asynccontextmanager

import voicemeeterlib
from fastapi import Depends, FastAPI, HTTPException
from voicemeeterlib.error import CAPIError

from .dependencies import get_voicemeeter_client
from .web import bus, command, strip


@asynccontextmanager
async def lifespan(app):
    """Lifespan function to initialize and clean up the Voicemeeter client."""
    app.state.voicemeeter = voicemeeterlib.api('potato', sync=True)
    app.state.voicemeeter.login()
    yield
    app.state.voicemeeter.logout()


app = FastAPI(
    lifespan=lifespan,
    description='A REST API for controlling Voicemeeter.',
    openapi_tags=[
        {'name': 'strip', 'description': 'Endpoints for controlling strip parameters.'},
        {'name': 'bus', 'description': 'Endpoints for controlling bus parameters.'},
    ],
)
app.include_router(strip.router, prefix='/strip/{index}')
app.include_router(bus.router, prefix='/bus/{index}')
app.include_router(command.router, prefix='/command')


@app.get('/health')
def health_check(voicemeeter=Depends(get_voicemeeter_client)):
    """Health check endpoint to verify the service is running."""
    try:
        version = voicemeeter.version
        type_ = voicemeeter.type
    except CAPIError as e:
        raise HTTPException(status_code=503, detail=f'Voicemeeter API error: {str(e)}')
    return {'status': 'ok', 'service': 'vmr-http', 'version': version, 'type': type_}
