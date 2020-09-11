import speech_recognition as sr
import os
import webbrowser as wb
import time

path = "./require"

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

while True:
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

    print(found_names)
    
    for i in names:
        if(i in found_names) :
            print("Name found")
            break
        else :
            print("Name not found")
   
    f1.close()
    f2.close()
    f3.close()
    
    f1 = open('./temp/tempfile1.txt','w').close()
    f2 = open('./temp/tempfile2.txt','w').close()
    f3 = open('./temp/tempfile3.txt','w').close()
    
    del found_names[:]
    
    time.sleep(5)
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
