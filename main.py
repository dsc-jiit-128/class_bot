import speech_recognition as sr
import os
import webbrowser as wb
import time
from pydub import AudioSegment
from pydub.playback import play

path = "./require"
roll_call = AudioSegment.from_wav("./require/roll_call.wav")
r1 = sr.Recognizer()

f = open(path+"/names.txt",'r')
lines = f.readlines()
f.close()

names = []

for i in lines:
    i = i.rstrip('\n')
    names.append(i)

flag = 0

#link = input("Please provide the Goole Meet link\n")
#wb.open(link)

found_names = []
alert_cmd = "notify-send \"YOUR NAME IS BEING CALLED!!!\" \"Return to your meeting ASAP\"; aplay ./require/alert.wav"
at_alert_cmd = "notify-send \"LOOKS LIKE ATTNEDENCE IS GOING ON!!!!!\" \"Return to your meeting ASAP\"; aplay ./require/alert.wav"


at = 0
at_f = 0

while True:
    flag = 0
    f1 = open('./temp/tempfile1.txt','+r')
    f2 = open('./temp/tempfile2.txt','+r')
    f3 = open('./temp/tempfile3.txt','+r')
    l1 = f1.readlines()
    l2 = f2.readlines()
    l3 = f3.readlines()
    temp = l1 + l2 + l3
    for i in temp:
        i = i.rstrip('\n')
        found_names.append(i)

    #print(found_names)

    if("present" in found_names):
        at+=1
        #print("Present Found")

    if(at_f == 0 and at >= 10):
        os.system(at_alert_cmd)
        at_f = 1

    for i in names:
        if(i in found_names) :
            flag = 1
            os.system(alert_cmd)
            break
    if(flag == 1):
        time.sleep(2)

    f1.close()
    f2.close()
    f3.close()

    f1 = open('./temp/tempfile1.txt','w').close()
    f2 = open('./temp/tempfile2.txt','w').close()
    f3 = open('./temp/tempfile3.txt','w').close()

    del found_names[:]

    time.sleep(4)

















