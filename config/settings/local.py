from .base import *


DEBUG = True

SECRET_KEY = get_secret("SECRET_KEY")

DISQUS_API_KEY =  get_secret("DISQUS_API_KEY")
DISQUS_WEBSITE_SHORTNAME = get_secret("DISQUS_WEBSITE_SHORTNAME")

ALLOWED_HOSTS = ['127.0.0.1',
                 'localhost']

INSTALLED_APPS += [
    'debug_toolbar',  ##debug-toolbar 설정
]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware', ##debug-toolbar 설정
]
INTERNAL_IPS = ('127.0.0.1',) ##debug-toolbar 설정