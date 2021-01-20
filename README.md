# Tradecore #

1. [General Information](#general-information)
2. [Dependencies](#dependencies)
3. [Installation](#installation)
4. [Development](#development)
5. [How run bot](#bot)


## General Information ##

[tradecore]() is a REST API.
Test task for tradecore

## Dependencies ##

Take a look at *requirements.txt* for Python dependencies.

## Installation ##

run once:

```sh
$ make docker_dev
```

## Development ##

If you use Docker Django app will be exposing on 9000 port by default. It's up to you to change settings.

run docker compose:
```sh
$ make docker_dev
```

rebuild docker containers:
```sh
$ make docker_dev_rebuild
```

run tests in *web* container:
```sh
$ make test
```

Test coverage: 0%

## Bot ##

For running bot enter in container tradecore_web: python manage.py bot

