# Carbudd

[![Django CI](https://github.com/cutechybyke/Carbudd/actions/workflows/ci.yml/badge.svg)](https://github.com/cutechybyke/Carbudd/actions/workflows/ci.yml)

Carbudd is a **Django-powered automobile community application** for discussions, rooms, messages and automobile-focused conversations.

## Features

- Custom Django user model
- Topic-based discussion rooms
- Room participants and messages
- Django REST Framework support
- CORS middleware
- Environment-driven deployment configuration
- Automated Django model tests
- GitHub Actions CI

## Stack

Python · Django · Django REST Framework · SQLite · django-cors-headers

## Setup

```bash
git clone https://github.com/cutechybyke/Carbudd.git
cd Carbudd
python -m venv .venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Development defaults are provided, while deployment configuration can be supplied through environment variables such as `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS` and `DJANGO_CORS_ALLOW_ALL_ORIGINS`.

## Tests

```bash
python manage.py test
```

The current regression suite exercises core Topic, Room, Message and participant model behavior.

## Engineering improvements

The project was hardened by removing the committed production secret, making security-sensitive deployment settings environment-driven and adding explicit runtime dependencies. A separate test/CI change verifies the model layer and dependency setup on GitHub Actions.
