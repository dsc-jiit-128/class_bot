#!/bin/bash


pacmd load-module module-null-sink sink_name=Temp sink_properties=device.description="Temporary_sink"
str=`pacmd list-sources | grep -e"stereo.monitor" | sed 's/.*<\(.*\)>/\1/'`
pacmd load-module module-loopback sink=Temp source=${str}
nohup python ./background/bgrun1.py&
nohup python ./background/bgrun2.py&
nohup python ./background/bgrun3.py&
nohup python ./main.py&
