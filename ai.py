import pyttsx3
import speech_recognition as sr
import datetime
import requests
import time
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import pygame
import pyautogui
import psutil
import json



def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)  # Adjust the speaking rate (words per minute)
    engine.setProperty('voice', 'hindi')  # Set the voice to Hindi
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        print("Say that again")
        return "None"
    return query


def getWeather(city):
    apiKey = 'aae434f15884030bf61a28ce6556d348'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=aae434f15884030bf61a28ce6556d348&units=metric'
    response = requests.get(url)
    weather_data = json.loads(response.text)
    if weather_data['cod'] == 200:
        temp = weather_data['main']['temp']
        weather_desc = weather_data['weather'][0]['description']
        speak(f"The temperature in {city} is {temp} degrees Celsius with {weather_desc}")
    else:
        speak("Sorry, I couldn't retrieve weather information at the moment.")

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning sir")
    elif hour>12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    
    speak("I am friday, Sir please tell me how can I help you today")


    
def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            speak("Time's up! Alarm triggered wake up sir.")
            # Add your alarm actions or code here
        time.sleep(1)

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\KIIT01\\Pictures\\ss.png")

def cpu():
    usuage = str(psutil.cpu_percent())
    speak('cpu is at '+ usuage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )




def news():
    api_key = 'ab31e4ab418a4d519a661a3ad7267ad4'
    news_url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey=ab31e4ab418a4d519a661a3ad7267ad4'
    news_limit = 5
    try:
        response = requests.get(news_url)
        news_data = response.json()

        if news_data['status'] == 'ok':
            articles = news_data['articles']
            for article in articles:
                title = article['title']
                speak(title)
        else:
            speak("Sorry, I couldn't fetch the news at the moment.")

    except Exception as e:
        print("An error occurred while fetching news:", e)
        speak("Sorry, I couldn't fetch the news at the moment.")

if __name__ == '__main__':
   # print('PyCharm')
    #speak("Hello sir,I am friday")
    #takeCommand()
    wish()

    #while True:
    if 1:
        query = takeCommand().lower()

        #logic building for task

        if "open notebook" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
            speak("opening notebook for you")

        elif "open command prompt" in query:
            os.system("start cmd")
            speak("Opening command prompt for you")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(100)  
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
             ip = get('https://api.ipify.org').text
             speak(f"Your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query: 
            webbrowser.open("youtube.com")

        elif "open facebook" in query: 
            webbrowser.open("facebook.com")
        
        elif "open instagram" in query: 
            webbrowser.open("instagram.com")
        elif "open twitter" in query:
            webbrowser.open("twitter.com")

        elif "open chat gpt" in query: 
            webbrowser.open("chatgpt.com")

        elif "open google" in query:
            speak("Sir, what should I search on Google?")
            search_query = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Here are the search results for {search_query}.")



        elif "play song on youtube" in query:
            speak("Sir,Which song should I play On youtube") 
            cmd = takeCommand().lower()
            kit.playonyt(f"{cmd}")


        elif "no, you can sleep now" in query:
            speak("Thank you for using me sir,Have a good day")
            sys.exit()
        elif "close notepad" in query:
            speak("Okay sir closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke();
            speak(joke)
        
        elif "set alarm" in query:
            speak("At what time would you like to set the alarm?")
            alarm_time_str = takeCommand().lower()

            try:
                alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")
                alarm_time_str = alarm_time.strftime("%H:%M:%S")
                speak(f"Alarm set for {alarm_time_str}.")
                set_alarm(alarm_time_str)
                  # Exit the while loop after setting the alarm

            except ValueError:
                speak("Invalid time format. Please try again.")
            if "exit" in query or "quit" in query:
                speak("Goodbye. Have a great day!")

        elif "shut down the system" in query:
            os.system("Shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("Shutdown /r /t 5")

        elif "sleep" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
       
             
        
        elif "switch the window" in query:
            pyautogui.KeyDOwn("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.KeyUp("alt")
            
        elif "tell me today news" in query:
            speak("Please wait sir, I am finding the latest news ")
            news()
             
        elif "remember" in query:
            speak("what should i remember")
            data = takeCommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif "Do you remember anything" in query:
            remember=open('data.txt', 'r')
            speak("you said to remember me that"+remember.read())
    
        elif "screenshot" in query:
            screenshot()
            speak("done!")

        elif 'cpu' in query:
            cpu()
        
        elif 'tell me the weather' in query:
            speak("Sure, which city's weather would you like to know?")
            city = takeCommand().lower()
            getWeather(city)

        
        elif 'exit' in query:
            speak("Goodbye!")
            exit()