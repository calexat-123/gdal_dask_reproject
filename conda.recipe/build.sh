#!/bin/bash

set -e
set -x

$PYTHON setup.py --quiet install --single-version-externally-managed --record=record.txt