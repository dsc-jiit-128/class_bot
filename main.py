import speech_recognition as sr
import os
import webbrowser as wb

path = "./require"

r1 = sr.Recognizer()

f = open(path+"/names.txt",'r')
lines = f.readlines()
f.close()

names = []

for i in lines:
    i = i.strip()
    i = i.rstrip('\n')
    names.append(i)

flag = 0

link = input("Please provide the Goole Meet link\n")
wb.open_new(link)

while True:
    flag = 0
    with sr.Microphone() as source :
        print('\nSPEAK NOW\n')
        r1.adjust_for_ambient_noise(source, duration=0.2)
        audio = r1.listen(source, phrase_time_limit = 5)
        text = r1.recognize_google(audio, language="en-IN", show_all=True)
        try:
            dict = text['alternative']
            for i in dict:
                str = i["transcript"].lower()
                for j in names:
                    if str.find(j)!=-1:
                        flag =1
                        break

            if(flag == 1) :
                print("Name found")
            else :
                print("Name not found")
        except TypeError:
            print("No one Speaking")
