release: python manage.py check
release: python manage.py migrate
web: python manage.py collectstatic --noinput
web: gunicorn my_portfolio.wsgi --log-file -