openshift-celery-cartridge
==========================

Cartridge to Expose Celery as a Daemon on OpenShift.

Status
---------------------
This work on unscaled applications but only as a plugin cartridge on scaled applications. This means that it's can't scale independently of your main gear. At this point having a celery cartridge is no better than just starting celery in your app.y or action hooks. Further development can combine this with a python cartridge so it can operate in it's own gears.

Instead of using this I recommend starting celery in your action hooks or as part of you app.py instead. This will give more flexibility, and example is here https://github.com/appsembler/appsembler-launch-openshift 

Configuration
---------------------

*  <code>OPENSHIFT_CELERY_CONFIG</code> 
    This is the name of your config file, which by default is `$OPENSHIFT_CELERY_DIR/conf.d/celeryconfig.py` but you can copy this to `$OPENSHIFT_DATA_DIR/config/celeryconfig.py` and edit your own copy.

To install
---------------------

    rhc cartridge-add https://raw.github.com/wassname/openshift-celery-cartridge/master/metadata/manifest.yml -a "appname"
    
Any log output will be generated to `${OPENSHIFT_HOMEDIR}logs/celery_log.txt` and will be viewable with the rhc tail "appname" command

This was tested using:

    celery==3.1.11
    redis==2.10.3

To manage
---------------------

    $ rhc cartridge-status celeryd -a "yourapp"


