# Django Elastic Beanstalk demo

A minimal Django site prepared for the individual AWS Elastic Beanstalk assignment.

## Local setup

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py check
python manage.py runserver
```

Open <http://127.0.0.1:8000/> to see the demo page.

## Elastic Beanstalk

The `.ebextensions/django.config` file sets `DJANGO_SETTINGS_MODULE`, `PYTHONPATH`,
and the Django WSGI entry point. The default allowed-host suffix is
`.elasticbeanstalk.com`; local development also allows `localhost` and `127.0.0.1`.

The app uses SQLite for this demonstration and does not include user data. It is
not a production deployment template.
