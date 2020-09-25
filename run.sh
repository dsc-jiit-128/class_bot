#!/bin/bash

ps -A | grep python | awk -F' ' '{print $1}' | while read x;do kill $x; done

mod1=`pacmd list-modules | grep null-sink -B 1 | awk -F" " '{print $2}' | head -n 1`
pacmd unload-module $mod1
pacmd load-module module-null-sink sink_name=Temp sink_properties=device.description="Temporary_sink"
str=`pacmd list-sources | grep "stereo.monitor" | sed 's/.*<\(.*\)>/\1/'`
pacmd load-module module-loopback sink=Temp source=${str}

python ./background/bgrun1.py&
python ./background/bgrun2.py&
python ./background/bgrun3.py&
python ./main.py&
