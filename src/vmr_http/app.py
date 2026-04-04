from contextlib import asynccontextmanager

import voicemeeterlib
from fastapi import FastAPI

from .web import bus, strip


@asynccontextmanager
async def lifespan(app):
    app.state.voicemeeter = voicemeeterlib.connect("potato", sync=True)
    app.state.voicemeeter.login()
    yield
    app.state.voicemeeter.logout()


app = FastAPI(lifespan=lifespan)
app.include_router(strip.router, prefix="/strip")
app.include_router(bus.router, prefix="/bus")
