#               BYE BYE CODE
import cowsay
import pyttsx3
engine=pyttsx3.init() 
#To initialize the library for text tot speach

this=input("Whats this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait