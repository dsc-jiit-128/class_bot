#!/bin/bash

ps -A | grep python | awk -F' ' '{print $1}' | while read x;do kill $x; done
mod1=`pacmd list-modules | grep null-sink -B 1 | awk -F" " '{print $2}' | head -n 1`
pacmd unload-module $mod1 
rm -rf nohup.out
notify-send "RUN THE BOT AGAIN IF YOU WANT TO CONTINUE" "Run ./run.sh"; aplay ./require/alert.wav;

