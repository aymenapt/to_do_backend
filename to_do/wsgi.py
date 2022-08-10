

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'to_do.settings')
from dj_static import Cling
application = Cling(get_wsgi_application())

