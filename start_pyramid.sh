#!/bin/sh
cd backend
python setup.py develop
pserve development.ini