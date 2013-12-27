import os

BROKER_URL = os.environ.get('OPENSHIFT_MONGODB_DB_URL')
CELERY_RESULT_BACKEND = "mongodb"
CELERY_RESULT_DBURI = os.environ.get('OPENSHIFT_MONGODB_DB_URL')

CELERY_IMPORTS = ('celerytks', )
#CELERYD_LOG_FILE = '{0}log/celery/worker1.log'.format(os.environ.get('OPENSHIFT_TMP_DIR'))
