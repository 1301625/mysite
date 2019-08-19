from .base import *


DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY_MYSITE')
DISQUS_API_KEY = os.environ.get("DISQUS_API_KEY")
DISQUS_WEBSITE_SHORTNAME = os.environ.get("DISQUS_WEBSITE_SHORTNAME")
ALLOWED_HOSTS = ['hoonha.pythonanywhere.com']