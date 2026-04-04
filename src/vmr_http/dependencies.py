from fastapi import Request


def get_voicemeeter_client(request: Request):
    return request.app.state.voicemeeter
