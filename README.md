openshift-celery-cartridge
==========================

Cartridge to Expose Celery as a Daemon on OpenShift

Environment Variables
---------------------

*  <code>OPENSHIFT_CELERY_BROKER_URL</code> 
    The connection URL for the broker, omitting the transport.  For example, an amqp value may look like: guest:guest@localhost:5672//

*  <code>OPENSHIFT_CELERY_IMPORTS</code> 
    Defines the modules that celery should import.  Currently only supports 1 module import path


To install
---------------------

    rhc cartridge-add https://raw.github.com/wassname/openshift-celery-cartridge/master/metadata/manifest.yml -a <appname>
    
Any log output will be generated to ${OPENSHIFT_TMP_DIR}/celery_log.txt

To manage
---------------------

    $ rhc cartridge-status redis -a <yourapp>


