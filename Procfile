release: python manage.py check
release: python manage.py migrate
release: python manage.py collectstatic --noinput
web: gunicorn my_portfolio.wsgi --log-file -