from django.core.exceptions import ImproperlyConfigured #django 구성을 잘못한 경우

import json


with open("secret.json") as f:
    secret = json.loads(f.read())


def get_secret(setting, secret=secret):
    try:
        val =  secret[setting]
        if val == "True":
            val = True
        elif val == "False":
            val = False

        return val
    except KeyError:
        error_msg = "Set the {0] enviroment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


