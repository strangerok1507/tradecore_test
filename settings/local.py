from settings.base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
# for debug_toolbar
INTERNAL_IPS = ['172.29.0.1']

# comment if you want to test real host
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += [
    'django_extensions',
    "silk",
]

AUTH_PASSWORD_VALIDATORS = []

MIDDLEWARE += [
    "silk.middleware.SilkyMiddleware",
    "qinspect.middleware.QueryInspectMiddleware"
]

SILKY_AUTHENTICATION = False
SILKY_AUTHORISATION = False
SILKY_PYTHON_PROFILER = False
QUERY_INSPECT_ENABLED = False
QUERY_INSPECT_LOG_STATS = False
QUERY_INSPECT_HEADER_STATS = False
QUERY_INSPECT_LOG_QUERIES = False
QUERY_INSPECT_ABSOLUTE_LIMIT = 100  # in milliseconds
QUERY_INSPECT_STANDARD_DEVIATION_LIMIT = 2
QUERY_INSPECT_LOG_TRACEBACKS = False
QUERY_INSPECT_TRACEBACK_ROOTS = ['/path/to/my/django/project/']
QUERY_INSPECT_DUPLICATE_MIN = 1  # to force logging of all queries
