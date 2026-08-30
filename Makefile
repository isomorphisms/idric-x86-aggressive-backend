PYTHON ?= python3
BUILD := build
IDRIC_REPO ?=
IDRIC_COMPILER ?= $(IDRIC_REPO)/edric
IDRIC_R128_SOURCE ?= $(IDRIC_REPO)/examples/mathematical-one-step/R128Pipeline.idric
ARTIFACT := $(BUILD)/r128.math-one-step
ELF := $(BUILD)/r128-math

.PHONY: all test integration inspect clean

all: test

test:
	$(PYTHON) -m unittest discover -s tests -v

integration:
	test -n "$(IDRIC_REPO)" || { echo "IDRIC_REPO is required for the real compiler handoff" >&2; exit 2; }
	test -x "$(IDRIC_COMPILER)"
	test -f "$(IDRIC_R128_SOURCE)"
	mkdir -p $(BUILD)
	"$(IDRIC_COMPILER)" --emit-math-one-step "$(IDRIC_R128_SOURCE)" -o "$(ARTIFACT)"
	$(PYTHON) backend/idric_x86.py "$(ARTIFACT)" --source "$(IDRIC_R128_SOURCE)" \
		-o "$(ELF)" --listing "$(BUILD)/r128.instructions" \
		--run-receipt "$(BUILD)/r128.execution-receipt"

inspect: integration
	readelf -h -l $(ELF)
	cat $(BUILD)/r128.instructions
	cat $(BUILD)/r128.execution-receipt

clean:
	rm -rf $(BUILD)
