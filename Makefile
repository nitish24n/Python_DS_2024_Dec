black:
	black src/

isort:
	isort .

flake8:
	flake8

format: | black isort
