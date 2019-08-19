from .base import *


DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY_MYSITE')
DISQUS_API_KEY = os.environ.get("DISQUS_API_KEY")

ALLOWED_HOSTS = ['hoonha.pythonanywhere.com']