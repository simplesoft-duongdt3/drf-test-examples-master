# Django REST-Framework Boilerplate Application
https://studygyaan.com/django/testing-in-django-rest-framework

DRF Application skeleton

## Includes
1. Local settings file with logging, DRF Renderer and local database
2. Dockerfile
3. Docker compose to work with Postgres with health-check
4. Kubernetes configs
5. `.gitignore` file
6. Documentation example

## TODO
1. Linter
2. Sentry setup


# remove psycopg2-binary



# Test library
# mocking

https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html

https://www.pythontutorial.net/python-unit-testing/python-patch/

https://www.20tab.com/about-us/20blog/test-python-mocking

https://docs.python.org/3/library/unittest.mock-examples.html#

# factory_boy
https://factoryboy.readthedocs.io/en/stable/

# django-dynamic-fixture
https://django-dynamic-fixture.readthedocs.io/en/latest/overview.html#basic-example-of-usage

# Anti-library factory
https://lukeplant.me.uk/blog/posts/test-factory-functions-in-django/#custom-factory-functions

# Migrations

https://paulonteri.com/thoughts/should-you-commit-migrations

https://docs.djangoproject.com/en/3.2/topics/migrations/#version-control

https://johnnymetz.com/posts/check-django-migrations/

https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/

https://adamj.eu/tech/2020/12/10/introducing-django-linear-migrations/
https://pypi.org/project/django-linear-migrations/

https://www.algotech.solutions/blog/python/django-migrations-and-how-to-manage-conflicts/

https://riptutorial.com/django/example/23659/solving-migration-conflicts

# create-initial-django-migrations-for-existing-schema
https://micropyramid.com/blog/how-to-create-initial-django-migrations-for-existing-schema


# coverage
https://www.lambdatest.com/blog/pytest-code-coverage-report/

# Run tests

pip install coverage


./manage.py test

./manage.py test lecture_api_testing/

./manage.py test lecture_api_testing/tests/unit_test

./manage.py test lecture_api_testing/tests/integration_test

coverage run manage.py test -v 2

coverage run manage.py test lecture_api_testing  -v 2

pytest lecture_api_testing/tests/integration_test



# Test reports
pytest lecture_api_testing/tests/integration_test --junitxml=test-reports/integration_test.xml

python -m junit2htmlreport test-reports/integration_test.xml test-reports/integration_test.html
python -m junit2htmlreport test-reports/integration_test.xml --report-matrix test-reports/integration_test.html
open test-reports/integration_test.html


pytest --cov --cov-report=html:coverage_reports lecture_api_testing/tests/integration_test --junitxml=test-reports/integration_test.xml

Note: check agruments
-cov-branch