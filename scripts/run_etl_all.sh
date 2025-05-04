#!/bin/bash

bash scripts/reset_dbs.sh

python ETLBLSTimeSeries.py
python ETLImports.py
python ETLExports.py
python ETLCIK.py
python ETLEdgar.py
