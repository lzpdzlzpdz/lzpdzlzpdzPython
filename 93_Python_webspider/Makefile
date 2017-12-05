PYTHON:=$(shell which python3)

all: python

.PHONY: clean python test flake8

python: setup.py requirements.txt
	pip install virtualenv
	echo "\n Creating python virtual environment......\n"
	virtualenv -p $(PYTHON) env
	echo "\n Use python virtual environment to install required packages......\n"
	env/bin/pip install -e .

test: flake8
	./runtests.sh

flake8:
	env/bin/flake8

clean:
	-rm -r env cover *eggs *.egg-info *.egg
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
