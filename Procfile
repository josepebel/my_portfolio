release: python manage.py check
release: python manage.py migrate
web: python manage.py collectstatic --no-input
web: gunicorn portfolio.wsgi --log-file -