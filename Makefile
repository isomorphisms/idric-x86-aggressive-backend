PYTHON ?= python3
IDRIC_REPO ?= $(CURDIR)/.idric
IDRIC_COMPILER_REVISION := $(shell tr -d '\n' < IDRIC_COMPILER_REVISION)

.PHONY: unit ci-unit integration ci

unit:
	$(PYTHON) -m unittest discover -s tests -v

ci-unit:
	EDRIC_COMPILER="$(IDRIC_REPO)/edric" \
	EDRIC_R128_SOURCE="$(IDRIC_REPO)/examples/mathematical-one-step/R128Pipeline.idric" \
	$(PYTHON) scripts/run_test_suite.py --fail-on-skip

integration:
	IDRIC_REPO="$(IDRIC_REPO)" \
	IDRIC_COMPILER_REVISION="$(IDRIC_COMPILER_REVISION)" \
	scripts/run_checked_integration.sh

ci: ci-unit integration
