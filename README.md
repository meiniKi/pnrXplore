# pnrXplore

pnrXplore is a Python package that bundles data from CAD/EDA physical design implementation (e.g., place & route) into an archive file. You can view it with pnrXplore-viewer.

## Quick Start

The best starting point is the provided example in `example/bundle.py`. Running the example provides a bundle that can be uploaded to the viewer. Optionally, install the package in a virtual environment, as in the snippet below.

```bASH
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
python example/bundle.py
```