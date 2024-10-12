#!/home/betashort/anaconda3/envs/calendar-api/bin/python
# encoding: UTF-8

import sys, os

sys.path.insert(0, '/home/betashort/anaconda3/envs/calendar-api/bin')
sys.path.append('/home/betashort-lab.com/public_html/calendar-api/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from wsgiref.handlers import CGIHandler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
CGIHandler().run(application)
