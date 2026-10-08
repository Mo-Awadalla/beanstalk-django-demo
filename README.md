# Django Polls on Elastic Beanstalk

A working Polls application based on Parts 1–4 of the official Django tutorial, prepared for the individual AWS Elastic Beanstalk assignment.

## Run locally

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/polls/> to browse and vote in the sample poll. The root URL redirects to the Polls index. To manage questions in the Django admin, create a local admin account with `python manage.py createsuperuser`, then visit <http://127.0.0.1:8000/admin/>.

## Elastic Beanstalk

The `.ebextensions/django.config` file sets `DJANGO_SETTINGS_MODULE`, `PYTHONPATH`, the WSGI entry point, and runs database migrations during deployment. SQLite is used for this classroom demo. The default allowed-host suffix is `.elasticbeanstalk.com`; local development also allows `localhost` and `127.0.0.1`.

This is a tutorial assignment app, not a production deployment template. The database is stored on the environment instance and can be replaced when the environment is redeployed or rebuilt.
