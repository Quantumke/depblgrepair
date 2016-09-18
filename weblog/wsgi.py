"""
WSGI config for weblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/opt/python/current/app/')
sys.path.append('/opt/python/current/app/')
sys.executable = '/usr/local/python-2.7.2/bin/python'

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weblog.settings")

application = get_wsgi_application()
