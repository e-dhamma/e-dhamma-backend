from django.utils.log import DEFAULT_LOGGING

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Assure that errors end up to Apache error logs via console output
# when debug mode is disabled
DEFAULT_LOGGING['handlers']['console']['filters'] = []

ALLOWED_HOSTS = ['edhamma.pythonanywhere.com','217.146.67.80']