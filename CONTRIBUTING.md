# Contributing

Open pull requests against `main`. Travis CI checks formatting with Black,
lints Python with flake8, and runs the Django test suite with coverage.

Run the checks before pushing:

```sh
python -m pip install -r requirements-dev.txt
black --check .
flake8 .
python manage.py check
coverage run manage.py test
coverage report
```

Pull requests run checks without deploying. Deployment runs only after a
successful build on `main`. AWS credentials are masked in Travis settings
and are not shared with pull requests from forks.
