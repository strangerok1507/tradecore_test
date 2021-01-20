# general
MANAGE=manage.py
COVERAGE=coverage
COVER=apps

DOCKER_COMPOSE=docker-compose
DOCKER_DEV_CONFIG=docker-compose.yml
DOCKER_TEST_CONFIG=docker-test.yml
DOCKER_STAGE_CONFIG=docker-stage.yml
CELERY_CONFIG=config.celery_app


celery:
	celery -A $(CELERY_CONFIG) worker -l info

celery_beat:
	rm -f celerybeat-schedule.db && rm -f celerybeat.pid && celery -A $(CELERY_CONFIG) beat -l INFO

flower:
	flower -A $(CELERY_CONFIG) --port=5555

test:
	DJANGO_SETTINGS_MODULE=settings.unittests python3 $(MANAGE) test

test_with_coverage:
	$(COVERAGE) erase; \
	$(COVERAGE) run --source $(COVER) $(MANAGE) test; \
	$(COVERAGE) report

test_with_warnings:
	python3 -Wall $(MANAGE) test

dev_package:
	pip3 install -r requirements_dev.txt

package:
	pip3 install -r requirements.txt

migrate:
	python3 $(MANAGE) migrate

test_with_warnings:
	python3 -Wall $(MANAGE) test

test_app:
	# a command to run tests in a particular app, depends on compose running
	@echo "Enter app name to test: ";
	@read -p "> " app_name; \
	$(DOCKER_COMPOSE) exec web bash -c "python3 $(MANAGE) test apps.$$app_name -s"

run_tests:
	set +e
	$(DOCKER_COMPOSE) run --rm web bash -c "pip install -r requirements_dev.txt; NOSE_OUTPUT=xml make test; make lintxml"
	set -e

docker_stop:
	$(DOCKER_COMPOSE) -f $(DOCKER_DEV_CONFIG) stop

docker_dev:
	$(DOCKER_COMPOSE) -f $(DOCKER_DEV_CONFIG) up

docker_stage_up:
	$(DOCKER_COMPOSE) -f $(DOCKER_STAGE_CONFIG) up --build -d

lint:
	$(DOCKER_COMPOSE) -f $(DOCKER_DEV_CONFIG) run --rm web prospector --profile=/web/prospector.yaml

lintxml:
	prospector --profile=/web/prospector.yaml -o xunit >  prospector.xml

docker_dev_rebuild:
	$(DOCKER_COMPOSE) -f $(DOCKER_DEV_CONFIG) up --build

docker_status:
	$(DOCKER_COMPOSE) -f $(DOCKER_DEV_CONFIG) ps

docker_dev_with_recreating_db:
	echo RECREATE_DB=1 > docker_env.env; \
	$(DOCKER_COMPOSE) -f $(DOCKER_DEV_CONFIG) up --build; \
	> docker_env.env

docker_dev_reset_db:
	echo RESET_DB=1 > docker_env.env; \
	$(DOCKER_COMPOSE) -f $(DOCKER_DEV_CONFIG) up --build; \
	> docker_env.env
