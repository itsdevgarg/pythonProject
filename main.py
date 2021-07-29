import os
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import smtplib
import random
import wikipedia
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishUser():
    user_name = "Sir"
    hours = datetime.datetime.now().hour

    if hours >= 1 and hours < 13:
        speak("Good Morning " + user_name)


    elif hours >= 12 and hours <= 16:
        speak("Good Afternoon " + user_name)

    else:
        speak("Good Evening " + user_name)

    speak("My name is Jarvis, How i can help you?")


def take_command():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print('User Said : ' + query)

    except Exception:
        print('Please say it again...')
        return 'none'

    return query

def sendEmail(to, content):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("devmora1234@gmail.com", "deV37Mora88$#")
        server.sendmail("devmora1234@gmail.com",to,content)
        server.close()



if __name__ == "__main__":
    start = take_command().lower()
    active = False

    if start == "ok dev":
        wishUser()
        active = True

    while active:
        query = take_command().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak("According to wikipedia, " + result)


        if "open youtube" in query:
            webbrowser.open('https://youtube.com', new=1)

        elif "open google" in query:
            webbrowser.open('https://google.com', new=1)

        elif "open timer" in query:
            timerDir = "C:\\Users\\admin\\AppData\\Local\\TogglDesktop\\TogglDesktop.exe"
            os.startfile(dir)

        elif "play music" in query:
            music_dir = "C:\\Users\\admin\\Desktop\\Temp\\audio"
            songs = os.listdir(music_dir)
            noOfSongs = len(songs)
            songIndex = 0

            for i in range(noOfSongs):
                songList = [0,]
                # songList.append(i)
                songIndex = random.choice(songList)

            print(songIndex)
            os.startfile(os.path.join(music_dir, songs[songIndex]))

        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak("The Current Time is : " + time)

        elif "bye" in query or "bhai" in query:
            active = False
            speak("Bye Sir, See you later.")

        elif "jokes" in query or "joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)


        elif "send email" in query:
            try:
                speak("To who you want to send?")
                recieverName = take_command()
                to = ""

                if recieverName == "mummy":
                    to = "anjugargdel@gmail.com"

                elif recieverName == "papa":
                    to = "parveenyng@gmail.com"

                speak("What you want to send")
                content = take_command()

                sendEmail(to,content)
                speak("Your email has been sent.")

            except:
                speak("Sorry, Email not sent, please try again later.")


