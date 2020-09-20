import pyaudio
import speech_recognition as sr
import os
import time
import wave

import  recording

path='./require/'
if(os.path.exists(path+"names.txt")):
    os.remove(path+"names.txt")

r1 = sr.Recognizer()
f = open(path+"names.txt",'w')

print("This is a demo run that helps you select the names by which the bot will recognize you\n")

names = []
ind = 0
while(ind<3):
    with sr.Microphone() as source:
        print("SPEAK YOUR NAME NOW ({})\n".format(ind+1))
        r1.adjust_for_ambient_noise(source, duration=0.2)
        audio = r1.listen(source, phrase_time_limit=5)
        text = r1.recognize_google(audio, language="en-IN", show_all=True)
        print(text)
        try :
            dict = text['alternative']
            for j in dict:
                if(j['transcript'] not in names):
                    names.append(j['transcript'])
            ind+=1
        except TypeError:
            print("Please speak again close to microphone!!\n")

ind=1
for i in names :
    print("{}. ".format(ind), i)
    ind+=1

print("PLEASE ENTER THE NUMBER OF THE NAME YOU THINK IS CLOSEST TO YOURS AND IS NOT SOMETHING THAT'LL BE A PART OF THE MEETING\n")
print("MORE NAMES YOU CHOOSE THE BETTER THE RECOGNITION CHANCES ARE!!\n")
print("Enter the number(s) from the list of names (q to QUIT)\n")
temp = []
while(True):
    a = input()
    if(a == 'q'):
        break
    a = int(a)
    if a not in temp and a>0 and a<=len(names):
        temp.append(a)
        f.write((names[a-1]+os.linesep).lower())
    else:
        print("The name already exists or invalid index number entered!!\n")

#input("PRESS ENTER TO CONTINUE!!\n")
#print("Excellent!!\nNow please be ready to record your audio that will answer your roll call!!\n")

#recording.start_recording()

print("WE ARE ALL SET UP NOW!!\n")

f.close()















