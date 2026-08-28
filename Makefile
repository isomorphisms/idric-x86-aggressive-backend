PYTHON ?= python3
BUILD := build

.PHONY: all test inspect clean

all: $(BUILD)/print-x

$(BUILD)/print-x: fixtures/print_x.idric backend/idric_x86.py
	mkdir -p $(BUILD)
	$(PYTHON) backend/idric_x86.py $< -o $@ --listing $(BUILD)/print-x.instructions

test:
	$(PYTHON) -m unittest discover -s tests -v

inspect: all
	readelf -h -l $(BUILD)/print-x
	dd if=$(BUILD)/print-x of=$(BUILD)/print-x.code bs=1 skip=4096 count=42 status=none
	objdump -D -b binary -m i386:x86-64 -Mintel --adjust-vma=0x401000 $(BUILD)/print-x.code
	cat $(BUILD)/print-x.instructions

clean:
	rm -rf $(BUILD)
