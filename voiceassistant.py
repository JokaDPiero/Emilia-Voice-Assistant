import pyaudio
import speech_recognition as sr
import pyttsx3 
import pywhatkit as pywk
import wikipedia
import pyjokes
import os
import datetime
import sys
from pygame import mixer
import time
import smtplib
from email.message import EmailMessage
import getpass


def get_info():
    listener=sr.Recognizer()
    try:
        with sr.Microphone() as mic:
            print("Listening...")
            #audio=listener.record(mic,duration=5)
            audio=listener.listen(mic,timeout=3)
            info=listener.recognize_google(audio,language='en-in')
            print(f"You said: {info}\n")
    except:
        talk("Could not recognize your voice Try again!")
        return "None"
    return info
    
def talk(text):
    engine=pyttsx3.init()
    #changing voice
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    #changing rate of speech
    rate=engine.getProperty('rate')
    engine.setProperty('rate', rate-30)
    #changing volume
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+0.25)
    
    engine.say(text)
    engine.runAndWait()    

def send_mail(receiver,subject,body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    user=input("Enter your username(sender) :")
    password=getpass.getpass(prompt='Enter your password (sender) :')
    talk("The Email will be sent from "+user)
    talk("The receiver is "+receiver)
    server.login(user, password)
    email=EmailMessage()
    email['From']=user
    email['To']=receiver
    email['Subject']=subject
    email.set_content(body)
    server.send_message(email)
    server.close()   

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
        talk("Good Evening!")  

    talk("I am Emilia , Please tell me how may I help you sir")
    
if __name__=='__main__':
    wishMe()
    #Add people and their user names to send mail
    names={
        'xyz':'xyz@gmail.com',
        'abc':'abc@gmail.com',
        'pqr':'pqr@rediffmail.com',
        'lmn':'lmn@microsoft.com'
    }
    while True:
            command=get_info().lower()
            
            if 'play' in command:
                song=command.replace('play ','')
                talk("Playing"+song)
                pywk.playonyt(song)
        
            elif 'joke' in command:
                talk(pyjokes.get_joke(category='all',language='en'))
        
            elif 'open link' in command:
                url=command.replace('open link ','') 
                talk("Opening "+url)
                os.system("C:/Program files/Google/Chrome/Application/chrome.exe"+url)
        
            elif 'open' in command:
                fname=command.replace("open ",'')
                talk("Enter Username of ur PC.")
                talk("Opening "+fname)

                if 'jupyter' in fname:
                    os.system("C:/Users/KIIT/anaconda3/Scripts/jupyter-notebook-script.py")
            
                elif 'notepad' in fname:
                    path="C:/WINDOWS/system32/notepad.exe"
                    os.system(path)
            
                elif 'music' in fname:
                    os.system("C:/Program files(x86)/Windows Media Player/wmplayer.exe")
        
                elif 'chrome' in fname:
                    os.system("C:/Users/KIIT/AppData/Local/Google/Chrome/Application/chrome.exe")

                elif 'browser' in fname:
                    os.system("C:/Users/KIIT/AppData/Local/Google/Chrome/Application/chrome.exe")  
                  
                else:
                    talk("Sorry unable to get command!!")  
            
            elif 'i love you' in command:
                talk("I love you too, like the moon loves the sun.")
                talk("For the moon dies every night, for the sun to rise.")
                mixer.init()
                mixer.music.load('C:/Users/KIIT/Downloads/Github/Emilia/Music/hadal ahbek cut 16.mp3')
                mixer.music.play()
                time.sleep(16)
                mixer.music.stop()

            elif 'hate you' in command:
                mixer.init()
                mixer.music.load('C:/Users/KIIT/Downloads/Github/Emilia/Music/Hate me - Ellie goulding ft Juice Wrld.mp3')
                mixer.music.play(start=72)
                time.sleep(39)
                mixer.music.stop()
    
            elif 'who is' in command:
                search=command.replace("who is ","")
                info=wikipedia.summary(search,3)
                #print(info)
                talk(info)
        
            elif 'are you single' in command or 'are you commited' in command:
                talk("I'm already in a relationship with WiFi.")
                mixer.init()
                mixer.music.load('C:/Users/KIIT/Downloads/Github/Emilia/Music/can we kiss forever 17.mp3')
                mixer.music.play()
                time.sleep(17)
                mixer.music.stop()
        
            elif 'who are you' in command:
                talk("I'm Emilia , But you can call me mine.")
                mixer.init()
                mixer.music.load('C:/Users/KIIT/Downloads/Github/Emilia/Music/make you mine cut 19.mp3')
                mixer.music.play()
                time.sleep(19)
                mixer.music.stop()

            elif 'vibe' in command:
                mixer.init()
                mixer.music.load('C:/Users/KIIT/Downloads/Github/Emilia/Music/copines cut 11.mp3')
                mixer.music.play()
                time.sleep(11)
                mixer.music.stop()

            elif 'get date' in command:
                talk("Today is"+datetime.datetime.now().strftime("%d:%m:%y"))

            elif 'date' in command:
                talk("Sorry, I've a headache right now so I can't go.")

            elif 'how are you' in command:
                talk("I am fine sir, how are you?")

            elif 'good' in command:
                talk("Pleased to here that! What are your plans for today")

            elif 'great' in command:
                talk("Pleased to here that! What are your plans for today")   

            elif 'project' in command:
                talk("Okay I got it")          

            elif 'how was your day' in command:
                talk("It was great sir, what about you?")     

            elif 'boring' in command:
                talk("Why was it boring sir?")
                
            elif 'know' in command:
                talk("Okay sir! My day was great") 
        
            elif 'send mail'  in command:
                talk("To whom do you want to send the E-mail sir!")
                name=get_info()
                rcvr=names[name]
                #print(names[name])
                talk("What will be the subject sir!")
                sub=get_info()
                #print(sub)
                talk("Tell me the body of the E-mail sir!")
                body=get_info()
                #print(body)
                send_mail(rcvr,sub,body)
                print("Email sent successfully!!!")

            elif 'spell the word' in command:
                word=command.replace("spell the word ","")
                #print(word)
                ltrs=list(word)
                #print(ltrs)
                for i in ltrs:
                    talk(i)
                    time.sleep(0.1)
                
            elif 'exit' in command:
                talk("I'll miss you dear See ya take care.")
                sys.exit(0)
                
            elif 'get time' in command:
                talk("Today is"+datetime.datetime.now().strftime("%I:%M:%S%p"))
    
            elif 'shutdown pc'  in command:
                talk("Shutting down in 10 secs.")
                pywk.shutdown(time=10)
    