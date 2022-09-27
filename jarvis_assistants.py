# Requires PyAudio and PySpeech.
import webbrowser
import wikipedia
from time import ctime
import time
import datetime
import pywhatkit                  # for more web automation (pip install --upgrade pip setuptools wheel)
import random                     # to choose random words from list
import requests
# from ecapture import ecapture as ec
import wolframalpha
import subprocess
import os
# local files
import data
import functions



print('Loading AI personal assistant - Noor')
functions.speak("Loading AI personal assistant Noor")

def mainFunction():
        functions.wishMe()
        while True:
            statement = functions.takeCommand().lower()
            if statement==0:
                continue
            
            if statement in data.bye_words:
                functions.speak('First enter password to shutting down system')
                takePassword = input("Enter password here: ")
                if(takePassword == "noor"):
                    functions.speak('correct password. your personal assistant Noor is shutting down, Good bye')
                    break
                else:
                    functions.speak('Sorry, password incorrect and i Can not close system now!')
                    
            elif statement in data.hi_words:
                functions.speak('Hi Sir, I can help you?')
                
            elif(statement == data.robot_name):
                functions.speak("I am here sir")
            elif statement in data.calcOpen:
                functions.openCalculator()
            elif statement in data.calcClose:
                functions.closeProgram("Calculator")
            elif 'create folder' in statement:
                functions.speak("Where you want create, sir?")
                path = functions.takeCommand()
                functions.speak("What is name of folder, sir?")
                folderName = functions.takeCommand()
                if path != '' and folderName != '':
                    functions.makeFolder(path, folderName)
            elif 'remove folder' in statement:
                functions.speak("Where is it, sir?")
                path = functions.takeCommand()
                functions.speak("What is name of folder, sir?")
                folderName = functions.takeCommand()
                if path != '' and folderName != '':
                    functions.deleteFolder(path, folderName)
            elif 'create file' in statement:
                functions.speak("Where you want create, sir?")
                path = functions.takeCommand()
                functions.speak("What is name of file, sir?")
                fileName = functions.takeCommand()
                if path != '' and fileName != '':
                    functions.makeFile(path, fileName)
            elif 'remove file' in statement:
                functions.speak("Where is it, sir?")
                path = functions.takeCommand()
                functions.speak("What is name of file, sir?")
                fileName = functions.takeCommand()
                if path != '' and fileName != '':
                    functions.deleteFile(path, fileName)
            elif 'play music' in statement:
                functions.start_playlist(functions.getMusic())
            elif 'open code' in statement:
                codePath = data.paths["vs_code"]
                os.startfile(codePath)
            elif 'ip address' in statement:
                ip_address = functions.find_my_ip()
                functions.speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')

            elif 'wikipedia' in statement:
                functions.speak('What do you want to search on Wikipedia, sir?')
                search_query = functions.takeCommand().lower()
                results = functions.search_on_wikipedia(search_query)
                functions.speak(f"According to Wikipedia, {results}")
                functions.speak("For your convenience, I am printing it on the screen sir.")
                print(results)

            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                functions.speak("youtube is open now")
                time.sleep(5)
            elif 'open command prompt' in statement or 'open cmd' in statement:
                functions.open_cmd()

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                functions.speak("Google chrome is open now")
                time.sleep(5)

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("gmail.com")
                functions.speak("Google Mail open now")
                time.sleep(5)

            elif "send whatsapp message" in statement:
                functions.speak('On what number should I send the message sir? Please enter in the console: ')
                number = input("Enter the number: ")
                functions.speak("What is the message sir?")
                message = functions.takeCommand().lower()
                functions.send_whatsapp_message(number, message)
                functions.speak("I've sent the message sir.")

            elif "send an email" in statement:
                functions.speak("On what email address do I send sir? Please enter in the console: ")
                receiver_address = input("Enter email address: ")
                functions.speak("What should be the subject sir?")
                subject = functions.takeCommand().capitalize()
                functions.speak("What is the message sir?")
                message = functions.takeCommand().capitalize()
                if functions.send_email(receiver_address, subject, message):
                    functions.speak("I've sent the email sir.")
                else:
                    functions.speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                functions.speak(f"the time is {strTime}")
            elif 'date' in statement:
                date = datetime.date.today()
                functions.speak(f"the date is {date}")

            elif 'who are you' in statement or 'what can you do' in statement:
                functions.speak('I am Noor version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                    'opening youtube,+ chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                    'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

            elif 'news' in statement:
                functions.speak(f"I'm reading out the latest news headlines, sir")
                functions.speak(functions.get_latest_news())
                functions.speak("For your convenience, I am printing it on the screen sir.")
                print(*functions.get_latest_news(), sep='\n')

            elif 'weather' in statement:
                ip_address = functions.find_my_ip()
                city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
                functions.speak(f"Getting weather report for your city {city}")
                weather, temperature, feels_like = functions.get_weather_report(city)
                functions.speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
                functions.speak(f"Also, the weather report talks about {weather}")
                functions.speak("For your convenience, I am printing it on the screen sir.")
                print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

            elif "who maker" in statement or "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                functions.speak("I was built by Hamed")
                print("I was built by Hamed")

            elif "open stackoverflow" in statement or "open stack overflow" in statement:
                webbrowser.open_new_tab("https://stackoverflow.com")
                functions.speak("Here is stackoverflow") 
            elif "open twitter" in statement or "twitter" in statement:
                webbrowser.open_new_tab(" https://twitter.com/home")
            elif "add new tweet" in statement or "new tweet" in statement:
                webbrowser.open_new_tab(" https://twitter.com/compose/tweet")
            elif 'news' in statement:
                
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                functions.speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(6)

            elif "camera" in statement:
                functions.openCamera()
            
            elif "open notepad" in statement:
                functions.openNotepad()

            elif 'search'  in statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(statement)
                time.sleep(5)

            elif 'ask' in statement:
                functions.speak('I can answer to computational and geographical questions and what question do you want to ask now')
                question= functions.takeCommand()
                app_id="R2K75H-7ELALHR35X"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                functions.speak(answer)
                print(answer)

            elif "log off" in statement or "sign out" in statement:
                functions.speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
                

if __name__ == '__main__':
    mainFunction()