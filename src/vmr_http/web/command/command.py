"""module for command related endpoints."""

from fastapi import APIRouter, Depends

from vmr_http.dependencies import get_voicemeeter_client

router = APIRouter(tags=['command'])


###
# Although these endpoints are technically modifying the state of the Voicemeeter application,
# they are commands that trigger an action rather than resource updates.
# Therefore, they are implemented as POST.
###


@router.post('/show')
def show_command(voicemeeter=Depends(get_voicemeeter_client)):
    """Show the Voicemeeter application."""
    voicemeeter.command.show()
    return {'status': 'Voicemeeter shown'}


@router.post('/hide')
def hide_command(voicemeeter=Depends(get_voicemeeter_client)):
    """Hide the Voicemeeter application."""
    voicemeeter.command.hide()
    return {'status': 'Voicemeeter hidden'}


@router.post('/shutdown')
def shutdown_command(voicemeeter=Depends(get_voicemeeter_client)):
    """Shutdown the Voicemeeter application."""
    voicemeeter.command.shutdown()
    return {'status': 'Voicemeeter shutdown'}


@router.post('/restart')
def restart_command(voicemeeter=Depends(get_voicemeeter_client)):
    """Restart the Voicemeeter application."""
    voicemeeter.command.restart()
    return {'status': 'Voicemeeter restarted'}


@router.post('/lock')
def lock_command(voicemeeter=Depends(get_voicemeeter_client)):
    """Lock the Voicemeeter application."""
    voicemeeter.command.lock = True
    return {'status': 'Voicemeeter locked'}


@router.post('/unlock')
def unlock_command(voicemeeter=Depends(get_voicemeeter_client)):
    """Unlock the Voicemeeter application."""
    voicemeeter.command.lock = False
    return {'status': 'Voicemeeter unlocked'}
