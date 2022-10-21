#!/bin/bash

set -e
set -u
set -o pipefail

pycodestyle plotter.py
pycodestyle data_processor.py
pycodestyle test_data_processor.py
python3 test_data_processor.py
bash test_plotter.sh
