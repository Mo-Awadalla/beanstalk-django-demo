# Django Polls on Elastic Beanstalk

[![Build Status](https://app.travis-ci.com/Mo-Awadalla/beanstalk-django-demo.svg?branch=main)](https://app.travis-ci.com/github/Mo-Awadalla/beanstalk-django-demo)
[![Coverage Status](https://coveralls.io/repos/github/Mo-Awadalla/beanstalk-django-demo/badge.svg?branch=main)](https://coveralls.io/github/Mo-Awadalla/beanstalk-django-demo?branch=main)

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

## Continuous integration

Travis CI runs Black, flake8, Django system checks, and the initial Polls test
suite on pushes and pull requests. Coverage is measured with coverage.py and
reported to Coveralls. A successful build on `main` deploys to the existing
Elastic Beanstalk environment; pull-request builds do not deploy.

Run the same checks locally:

```sh
python -m pip install -r requirements-dev.txt
black --check .
flake8 .
python manage.py check
coverage run manage.py test
coverage report
```

The tests cover published and future questions, voting, invalid choices,
redirects, and the recent-publication date range.

Travis repository settings must contain masked
`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` deployment credentials. The
existing application, environment, and source bucket are set in `.travis.yml`. Connect
this repository to Coveralls and configure a masked `COVERALLS_REPO_TOKEN` if
required by the integration. Never commit credentials or expose them to fork
pull requests.

Assignment URLs:

- [Travis dashboard](https://app.travis-ci.com/github/Mo-Awadalla/beanstalk-django-demo)
- [Deployed Polls application](http://django-assignment-demo-env.eba-gmjqs92i.us-east-1.elasticbeanstalk.com/polls/)
- [GitHub repository](https://github.com/Mo-Awadalla/beanstalk-django-demo)
