from __future__ import absolute_import, unicode_literals

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


DEBUG = False


SECRET_KEY = 'sx@r#x@+&38p&$7ks4))zacsy!t9cv$o&+lvjl1rhqat^-l8)x'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '202.51.74.199']

# MEDIA_ROOT = "/var/www/example.com/media/"



# OPBEAT = {
#     'ORGANIZATION_ID': '463c8be84d4e4dfeb1e5feca945b5998',
#     'APP_ID': '08fc72e7cb',
#     'SECRET_TOKEN': '66633d40a419436743afcac979e302c1b004c4ee',
# }
