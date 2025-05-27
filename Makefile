.PHONY: run clean

run:
	@echo "Running Möbius Strip visualizer..."
	python3 mobius_strip.py

clean:
	@echo "Cleaning temporary files..."
	rm -rf *.pyc __pycache__/
