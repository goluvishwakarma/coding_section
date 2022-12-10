# 28/02/2021, text to speech

# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()

# testing
engine.say("hii, this is jumbo")
engine.say("this is my first text to speech program")
engine.say("which i will type here")
engine.say("will be spoken")
engine.say("thanks sir,  have a good day")
engine.say("once again, this is jumbo")

engine.say("if you want to be happy")
engine.say("1st: forget the past")
engine.say("2nd: live in present")
engine.say("3rd: don't worry about future")
engine.say("4th: don't compare yourself with others")
engine.say("and last one, be punctual")
engine.runAndWait()


