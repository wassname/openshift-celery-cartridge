openshift-celery-cartridge
==========================

Cartridge to Expose Celery as a Daemon on OpenShift

Configuration
---------------------

*  <code>OPENSHIFT_CELERY_CONFIG</code> 
    This is the name of your config file, which by default is $OPENSHIFT_CELERY_DIR/conf.d/celeryconfig.py but you can copy this to $OPENSHIFT_DATA_DIR/config/celeryconfig.py and edit your own copy.

To install
---------------------

    rhc cartridge-add https://raw.github.com/wassname/openshift-celery-cartridge/master/metadata/manifest.yml -a <appname>
    
Any log output will be generated to ${OPENSHIFT_APP_ROOT}logs/celery_log.txt and will be viewable with the rhc tail <appname> command

This was tested using:

    celery==3.1.11
    redis==2.10.3

To manage
---------------------

    $ rhc cartridge-status celeryd -a <yourapp>


