#!/bin/bash

python ./background/bgrun1.py&
python ./background/bgrun2.py&
python ./background/bgrun3.py&
python ./main.py
