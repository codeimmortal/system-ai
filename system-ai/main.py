#!/usr/bin/env python3

import speech_recognition as sr
import pyttsx3
import os
import subprocess
from getListApp import getapplicationlist,checkStatusForApplication
engine = pyttsx3.init()
# get audio from the microphone
appList = getapplicationlist()
def speak( r ):
   "This prints a passed string into this function"
   try:
    print(r.recognize_google(audio))
    engine.say('Good afternoon himanshu  you said' +r.recognize_google(audio))
    engine.runAndWait()
   except sr.UnknownValueError:
    print("Could not understand audio")
   except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
   return

   
r = sr.Recognizer()
loopstatus = True
stopstatus = ""
status = ""
while loopstatus:
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)  # here
    print("Say something!")
    audio = r.listen(source)
    try:
      status = r.recognize_google(audio).lower() 
      print(status)
      engine.say('Good afternoon himanshu  you said' +status)
      engine.runAndWait()
    except sr.UnknownValueError:
      print("Could not understand audio")
      status = ""
    except sr.RequestError as e:
      print("Could not request results; {0}".format(e))
      status = ""
    arraylist = status.split(' ') 
    print(arraylist)
    firstword = arraylist[0] 
      
    print(firstword)
    if len(arraylist) > 1:
      secondword = arraylist[0]    
      if secondword == "stop":
          break
      elif secondword == "run": 
        matchedList = checkStatusForApplication(status[4:].split(' ', 1),appList)
        print(status[4:].split(' ', 1),)
        print(matchedList)
        if len(matchedList) > 0: 
          subprocess.call(matchedList[0])
        else:
          engine.say('There is no application of this name sir')
          engine.runAndWait()  
    else:
       engine.say('This instruction is not for me sir')
       engine.runAndWait()        




