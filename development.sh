#!/usr/bin/env sh

apk add gcc g++ make libffi-dev openssl-dev python3-dev build-base

yarn install
poetry install

poetry run python manage.py makemigrations
poetry run python manage.py migrate

exec yarn dev
