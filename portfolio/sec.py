from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



DEBUG = True
SECRET_KEY = '40t7x(($30uev!#*+!2@#m0u^m#2tf5)-ng2vhx$3&*(f^f!wo'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
