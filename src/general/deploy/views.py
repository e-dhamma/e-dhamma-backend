import os
import contextlib
import subprocess

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .commands import DEPLOY_COMMANDS
from utils.opsys import change_dir

RESPONSE_PRE = """<!DOCTYPE HTML>
<html lang="en-US">
<head>
<meta charset="utf-8">
<title>Deploying site</title>
</head>
<body>
<h2>Deploying site</h2>
<pre>
"""
RESPONSE_POST = """
</pre>
<h2>Done!</h2>
</body>
</html>
"""


@csrf_exempt
def deploy(request, deploy_key):
    if str(deploy_key) != settings.DEPLOY_KEY:
        raise PermissionDenied
    return StreamingHttpResponse(command_runner())


def command_runner():
    yield RESPONSE_PRE
    with change_dir(settings.BASE_DIR):
        for command_name, command_action in DEPLOY_COMMANDS:
            yield '-' * 80 + "\nRunning '{}'\n\n".format(command_name)
            try:
                yield run_command(command_action) + '\n\n'
            except Exception as e:
                yield f'EXCEPTION: {e}\n\n'
                break
    yield RESPONSE_POST


def run_command(command):
    cmd = subprocess.Popen(activate_virtualenv(command), shell=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = cmd.communicate()
    result = ['Command: ', '\t' + command]
    if output:
        result.append('Output: ')
        result.append('\t' + output.decode('utf-8'))
    if error:
        result.append('Error: ')
        result.append('\t' + error.decode('utf-8'))
    result = '\n'.join(result)
    if cmd.returncode:
        raise RuntimeError(f"Command '{command}' failed with returncode {cmd.returncode}: {result}")
    return result


def activate_virtualenv(command):
    activate_venv = os.path.join('..', 'venv')
    if os.name == 'nt':
        activate_venv = os.path.join(activate_venv, 'Scripts', 'activate.bat')
    else:
        activate_venv = ". " + os.path.join(activate_venv, 'bin', 'activate')
    return "{} && {}".format(activate_venv, command)
