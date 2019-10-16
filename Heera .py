import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import json
import requests
import win32api
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 145)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    
    elif hour >=12 and hour < 18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I'm Heera Sir. Please tell me how may I help you")

def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 600
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:    
        speak("Say that again please")
          
        return "None"
    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    with open("email.txt","r") as f:
        email = f.read()
    with open("pass.txt","r") as f:
        password = f.read()
    server.login(email,password)
    server.sendmail(email, to, content)
    server.close()

if _name_ == "_main_":
    print("\t\t\t\t\tThis application is developed by Mian Hussnain Javed with help of Bashir Jaliyawala")
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Opening... Please Wait")
            chrome_path = "C:\Program Files\Mozilla Firefox\firefox.exe"
            webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('firefox').open_new("youtube.com/")
            speak("Opened")
        elif 'open google' in query:
            speak("Opening... Please Wait")
            chrome_path = "C:\Program Files\Mozilla Firefox\firefox.exe"
            webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('firefox').open_new("google.com")
            speak("Opened")
        elif 'open facebook' in query:
            speak("Opening... Please Wait")
            chrome_path = "C:\Program Files\Mozilla Firefox\firefox.exe"
            webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
            webbrowser.get('firefox').open_new("facebook.com")
            speak("Opened")
        elif 'open instagram' in query:
            speak("Opening... Please Wait")
            chrome_path = "C:\Program Files\Mozilla Firefox\firefox.exe"
            webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path))
            webbrowser.get('firefox').open_new("instagram.com/MianHussnain1")
            speak("Opened")
        elif 'play music' in query:
            music_dir = "J:\Songs\Audio"
            songs = os.listdir(music_dir)
            random_gen = random.randint(0 , len(songs) - 1)
            os.startfile(os.path.join(music_dir , songs[random_gen]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H : %M : %S")
            print(f"Time - {strTime}\n")
            speak(f"Sir, the time is {strTime}")
        elif 'send email' in query:
            try:
                speak("To whom you want to send sir? Please enter a email")
                to = input("Please enter a email : ")
                speak("What should i write?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry sir! I'm not able to send this mail. Please try again")
                print("Please try again...")
        elif 'open gmail' in query:
            speak("Opening... Please Wait")
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new("gmail.com")
            speak("Opened")
        elif 'news' in query:
            i = 1
            speak("News for today")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=f602aaab18054f9ba962600f0ae0717e"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            for article in arts:
                speak("Newspaper")
                speak("Times of india")
                speak("News title is")
                print(f"{i}. News :\n")
                print(article['title'])
                speak(article['title'])
                speak("News discription")
                print("\n")
                print(article['content'])
                speak(article['content'])
                speak("Moving on the next news. You want to listen next news yes or no?")
                i = i+1
                status = input("\nYou want to listen next news yes or no? : ")
                if status == "yes" :
                    continue
                elif status == "no":
                    break
        elif 'wish birthday' in query :
            speak("To whom you want to wish sir? Enter His, Her Name")
            name = input("Enter a name : ")
            print(f"Wish you a many happy returns of the day {name}, HAPPY BIRTHDAY! I hope all your birtday wishes and dreams come true. ")
            speak(f"Wish you a many happy returns of the day {name} HAPPY BIRTHDAY! I hope all your birtday wishes and dreams come true. ")
        elif 'thank you' in query :
            speak("You're Welcome")
        elif 'who are you' in query:
            print("I'm your Heraa. I can help you find answer, get things done, and have fun")
            speak("I'm your Heraa. I can help you find answer, get things done, and have fun")
        elif 'i love you' in query :
            speak("And i love you too. Being your nimra")
        elif 'exit' in query:
            speak('Quitting... Bye Sir')
            exit()