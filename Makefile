HTMLCOV_DIR ?= htmlcov

install-dependencies:
	pip install -U -e "gateway/.[dev]"
	pip install -U -e "products/.[dev]"


coverage-html:
	coverage html --omit="*/test*" -d $(HTMLCOV_DIR) --fail-under 0

coverage-report:
	coverage report -m --omit="*/test*"

tests:
	coverage run -m pytest gateway/test
	coverage run --append -m pytest products/test


coverage: tests coverage-report coverage-html

