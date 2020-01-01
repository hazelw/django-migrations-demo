## Django Migrations Demo Examples

This repo contains a bunch of Django projects with the intention of teaching a bit about how Django migrations work (and what to do when they go wrong). Each folder contains a complete, independent Django project and a README.md explaining it's state. For simplicity's sake each project has the same set of requirements so can all be run in the same virtual environment.


### Setup
1. Make sure you have pip and virtualenvwrapper installed globally.
2. `virtualenv venv && . ./venv/bin/activate && pip install -r requirements.txt`
2.1. If you have issues with your system Python version (eg. if it's not version 3.6+), you can specify a version or a path when creating the virtualenv (eg. `virtualenv venv --python=python3.6`).
3. cd into one of the folders beneath this one and run the project using ``./manage.py runserver``.
