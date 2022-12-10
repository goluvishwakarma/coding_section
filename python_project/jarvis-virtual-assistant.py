import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):  # here we create a speak() function
    # pass
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # wishMe()
    hour = int(datetime.datetime.now().hour)
    if hour == 0 and hour < 12:
        speak("Good Morning")

    elif 12 <= hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am param sundri, sagarika  , what can i help you baby")


def takeCommand():  # it takes the command as in voice
    # it's take the microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")

    except Exception as e1:
        print(e1)
        print("say that again please...")
        return "None"
    return command


def sendEmail(to1, content1):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # pas = open("password.txt", "r")
    server.login('codewithpy001@gmail.com', '@code')
    server.sendEmail('codewithpy001@gmail.com', to1, content1)
    server.close()


if __name__ == "__main__":
    wishMe()  # here we call the wishMe()
    # while True:
    if 3:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        # here we are going to perform browsing action
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")  # here it searching wikipedia
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)  # it will take only 2 sentences from wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:  # here 'open youtube' is query,
            webbrowser.open("youtube.com")  # here we have to give 'open youtube' command to our sun_dari

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:  # here we performed music action
            music_dir = '[iSongs.info] 04 - Kanureppala Kaalam'  # music_directory
            songs = os.listdir(music_dir)
            print(songs)
            # print(len(songs))  # it will give the length of the songs
            os.startfile(os.path.join(music_dir))
            # os.startle(os.path.join(music_dir, songs[random.randint(0, len(songs))]))
            # here we can also generate random numbers, i.e random songs

        elif 'the time' in query:  # what is the time now is
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:  # here we performed program action
            codePath = "C:\\coding software\\Microsoft VS Code\\Code.exe"  # vsCode_location
            os.startfile(codePath)

        # elif 'close code' in query:
        #     codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
        #     os.close(int(codePath))

        elif 'the pycharm' in query:
            codePath = "E:\\New folder\\PyCharm Community Edition 2020.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'email to golu' in query:  # from here we start performing messaging action
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "goluvishwakarma586@gmail.com"
                sendEmail(to, content)
                speak("Email has been send")
            except Exception as e:
                print(e)
                speak("Sorry to say, sir. I am not able to send this email!!!")
                a = input()