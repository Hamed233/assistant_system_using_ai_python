import shutil
from gtts import gTTS
from playsound import playsound
import os
import requests
import speech_recognition as sr
import cv2
import datetime
import subprocess as sp
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
# from decouple import config
import wmi
import pygame


import data
# ----------------------- Speak function -----------------------
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    finalName = 'audio.mp3'
    tts.save(finalName)
    # os.system("mpg321 audio.mp3")
    playsound(finalName)
    os.remove(finalName)
    

# ------------ Take command from user -----------------------
def takeCommand():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

# ------------ Open camera -----------------------
def openCamera():
    sp.run('start microsoft.windows.camera:', shell=True)
    speak("Camera Opend, Nice Photo")

# ------------ Open Notepad -----------------------
def openNotepad():
    os.startfile(data.paths['notepad'])
    speak("Notepad opend sir!")
    
# ------------ Open cmd -----------------------
def open_cmd():
    os.system('start cmd')
    speak("Command propmet opend sir!")

# ------------ Open Music -----------------------
pygame.init()

def start_playlist(playList):
    # setting up pygame
    speak("Music playing sir!")
    # Loading first audio file into our player
    # for song in playList:
    #     os.startfile(song)
    pygame.mixer.music.load(playList[0])
      
    # Removing the loaded song from our playlist list
    playList.pop(0)
  
    # Playing our music
    pygame.mixer.music.play()
  
    # Queueing next song into our player
    pygame.mixer.music.queue(playList[0])
    playList.pop(0)
  
    # setting up an end event which host an event
    # after the end of every song
    # pygame.mixer.music.set_endevent(pygame.MUSIC_END)
  
    # Playing the songs in the background
    running = True
    while running:
        
        # checking if any event has been
        # hosted at time of playing
        for event in pygame.event.get():
            
            # A event will be hosted
            # after the end of every song
            print(event.type);
            if event.type == pygame.QUIT:
                print('Song Finished')
                # Checking our playList
                # that if any song exist or
                # it is empty
                if len(playList) > 0:
                    
                    # if song available then load it in player
                    # and remove from the player
                    pygame.mixer.music.queue(playList[0])
                    playList.pop(0)
  
            # # Checking whether the 
            # # player is still playing any song
            # # if yes it will return true and false otherwise
            if not pygame.mixer.music.get_busy():
                print("Playlist completed")
                  
                # When the playlist has
                # completed playing successfully
                # we'll go out of the
                # while-loop by using break
                running = False
                break

def getMusic():
    path = r"D:\\videos&audios\\test"
    dirr = os.listdir(path)
    musicList = []
    audio_extenions =["3gp","aa","aac","aax","act","aiff","alac","amr","ape","au","awb","dct","dss","dvf","flac","gsm","iklax","ivs","m4a","m4b","m4p","mmf","mp3","mpc","msv","nmf","ogg","oga","mogg","opus","ra","rm","raw","rf64","sln","tta","voc","vox","wav","wma","wv","webm","8svx","cda"]

    for file in dirr:
        # if os.path.isfile(file):
        #     print(file)
            if file.endswith(tuple(audio_extenions)):
                musicList.append(path + "\\" + file)
    return musicList

# ------------ Open Calculator -----------------------
def openCalculator():
    sp.Popen(data.paths['calculator'])
    speak("calculator opend sir!")
# ------------ close any programm -----------------------
def closeProgram(program):
    appIsFound = False
    speak("Just Minute sir!")
    processName = program + '.exe'
    f = wmi.WMI()
    for process in f.Win32_Process():
        if process.name == processName:
            process.Terminate()
            appIsFound = True
    # Check if app found and close
    if appIsFound:
        speak(program + " closed sir!")
    else:
        speak(program + " not found sir!")

# ------------ Send WhatsApp Message Function -----------------------
def send_whatsapp_message(phoneNumber, message):
    kit.sendwhatmsg_instantly(f"+20{phoneNumber}", message)

# ------------ Find my IP Address Function -----------------------
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

# ------------ Get Path Function -----------------------
def getPath(_path, _name):
    path = ''
    if _path == "desktop":
        path = data.paths["desktop"] + '\\' + _name
        return path
    elif path == "d":
        path = data.paths["D"] + '\\' + _name
        return path

# ------------ Make folder Function -----------------------
def makeFolder(path, folderName):
    fullPath = getPath(path, folderName)
    
    if not os.path.exists(fullPath):
        os.makedirs(fullPath)
        speak("Folder Created sir!")
    else:
        speak("Folder Already exist sir!")

# ------------ Delete folder Function -----------------------
def deleteFolder(path, folderName):
    fullPath = getPath(path, folderName)
    
    if os.path.exists(fullPath):
        shutil.rmtree(fullPath) 
        speak("Folder Removed sir!")
    else:
        speak("Folder Not exist sir!")

# ------------ Make File Function -----------------------
def makeFile(path, fileName):
    fullPath = getPath(path, fileName)
    
    if not os.path.exists(fullPath):
        open(fullPath,"w")
        speak("File Created sir!")
    else:
        speak("File Already exist sir!")

# ------------ Delete File Function -----------------------
def deleteFile(path, fileName):
    fullPath = getPath(path, fileName)
    
    if os.path.exists(fullPath):
        os.remove(fullPath) 
        speak("File Removed sir!")
    else:
        speak("File Not exist sir!")

# ------------ Send Email Function -----------------------

EMAIL = ""
PASSWORD = ""


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False


# ------------ Get Latest News Headlines Function -----------------------
NEWS_API_KEY = ""


def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]


# ------------ Get Weather Report Function -----------------------
OPENWEATHER_APP_ID = ""


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

# ------------ wishMe -----------------------
def wishMe():
    hour= datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning Hamed, What are tasks for today?")
        tasks = takeCommand()
        print(tasks)
        print("Hello, Good Morning Hamed")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon Hamed")
        print("Hello,Good Afternoon Hamed")
    else:
        speak("Hello, Good Evening Hamed")
        print("Hello, Good Evening Hamed")
        
    