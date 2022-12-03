setup:
	pip install -r requirements.txt


run: setup
	mypy main.py
	mypy library.py
	flake8 main.py
	flake8 --ignore=E501 library.py
	pytest
	python main.py