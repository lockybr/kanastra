clean:
	@echo Removing unnecessary files...
	@find . -name "*.pyc" -delete && \
	find . -name "*.pyo" -delete && \
	find . -name .pytest_cache | xargs rm -rf || true && \
	find . -name __pycache__ -delete && \
	find . -name ".coverage" -delete && \
	find . -name "*.Identifier" -delete && \
	rm -f .coverage && \
	rm -rf htmlcov && \
	rm -rf test_reports

test: clean
	@echo Runing tests...
	@pytest backend/tests/ -s -v

coverage: clean
	@echo Generating coverage report...
	@pytest --cov-report term-missing --cov=backend/src -s -vv --rootdir=./backend/tests --junitxml=test_reports/junit.xml --cov-branch --cov-report=term --cov-report=html
