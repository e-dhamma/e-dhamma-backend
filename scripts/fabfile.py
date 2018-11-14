# import os, sys

# from fabric.api import run, cd, prefix

# BASE_DIR = os.path.join('..', 'src')
# sys.path.append(BASE_DIR)

# from deploy.commands import DEPLOY_COMMANDS

# REMOTE_DEPLOY_DIR = '/var/www/projects/herbfoods/wholesaler/src'

# def deploy():
#     with cd(REMOTE_DEPLOY_DIR), prefix('. ../venv/bin/activate'):
#         for command_name, command_action in DEPLOY_COMMANDS:
#             print("Running '{}'".format(command_name))
#             run(command_action)
