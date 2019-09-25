"""
WSGI config for wuviewer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
import logging
import os

from django.core.wsgi import get_wsgi_application
import apollo.scheduler
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wuviewer.settings")
logger=logging.getLogger('wuviewer')

#Startup code to start the scheduler
logger.info("Setting scheduler")
myscheduler=scheduler(1,"myscheduler")
myscheduler.start()

application = get_wsgi_application()
