openshift-celery-cartridge
==========================

Cartridge to Expose Celery as a Daemon on OpenShift

Environment Variables
---------------------

- OPENSHIFT_CELERY_BROKER_URL : The connection URL for the broker, omitting the transport.  For example, an amqp value may look like: guest:guest@localhost:5672//

- OPENSHIFT_CELERY_IMPORTS : Defines the modules that celery should import.  Currently only supports 1 module import path

Currently only supports MongoDB as backend for queues, but in progress to support more environment variables to allow vairous backends and configurations.

To install rhc cartridge-add https://raw.github.com/wassname/openshift-celery-cartridge/master/metadata/manifest.yml -a <appname>
