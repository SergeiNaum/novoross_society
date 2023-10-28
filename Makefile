PORT ?= 8000

install:
	poetry install

dev:
	python manage.py runserver

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

lint:
	poetry run flake8 society_main


build:
	./build.sh


.PHONY: install lint start
