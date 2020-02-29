BOOT_ENV="${APP_ENV:-development}"
APP_ENV=$BOOT_ENV FLASK_ENV=development pipenv run flask run --port 9999
