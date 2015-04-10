# Modify this file to configure celery. 
# You can move it to your data directory and reference it in enviromental variable $OPENSHIFT_CELERY_CONFIG. 
# You could also insert variables at build using an acton hook.
# config options here http://docs.celeryproject.org/en/2.5/configuration.html#worker-celeryd

import os
import sys

sys.path.append('.')

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "celeryuser"
BROKER_PASSWORD = "celery"
BROKER_VHOST = "celeryvhost"

CELERY_RESULT_BACKEND = "amqp"

# Here we check the env vars first, otherwise go with "tasks"
CELERY_IMPORTS = ( os.getenv("OPENSHIFT_CELERY_IMPORTS","tasks") ,)
