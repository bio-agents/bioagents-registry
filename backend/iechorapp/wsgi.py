"""
WSGI config for iechorapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iechorapp.settings")
# os.environ["CELERY_LOADER"] = "django"
sys.path.insert(0,'/iechor/application/backend')
application = get_wsgi_application()
