export SETTINGS="config.DevelopmentConfig"

py.test --junitxml=TEST-flask-app-blueprints.xml --cov-report term-missing --cov application tests
