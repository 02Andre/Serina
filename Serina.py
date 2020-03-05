#installed files
from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
#import weather

def talkToMe(audio):
    "speaks audio as argument"
    print(audio)
    for line in audio.splitlines():
        os.system("say" + audio)

#listens to commands
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen to commands
    except sr.UnknownValueError:
        print('I couldn\'t hear your last command')
        command = myCommand();
    return command

#if statements for execution commands
def assistant(command):
    if 'look up' or 'search' in command:
        chrome_path = '/usr/bin/google-chrome'
        url = 'https://www.https://www.google.com/?safe=active&ssui=on'
        webbrowser.get(chrome_path).open(url)
    elif 'what\'s up' or 'how are you' in command:
        talkToMe('I\'m doing Lovely')
    #elif "current weather in" in command:
        #reg_ex = re.search('current waether in (.*)', command)
        #if reg_ex:
            #city = reg_ex.group(1)
            #weather = Weather()
           # location = weather.lookup_by_location(city)
            #condition = location.condition()
            #talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp()) - 32) / 1.8))
    #elif 'weather forecast in' in command:
        #reg_ex = re.search('weather forecast in (.*)', command)
        #if reg_ex:
           # city = reg_ex.group(1)
            #weather = Weather()
            #location = weather.lookup_by_location(city)
            #forecasts = location.forecast()
            #for i in range(0, 3):
               # talkToMe('On %s will it %s. The maximum temperture will be %.1f degree.'
                         #'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high()) - 32) / 1.8,(int(forecasts[i].low()) - 32) / 1.8))
    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'Andre' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            # init gmail SMTP
            mail = smtplib.SMTP('smtp.gulllakecs.org', 209)

            # identify to server
            mail.ehlo()

            # encrypt session
            mail.starttls()

            # login
            mail.login('02andre.smith@gulllakecs.org', 'Clam61acre')

            # send message
            mail.sendmail('Andre Smith', '15andresmith@gmail.com', content)

            # end mail connection
            mail.close()

            talkToMe('Email sent.')

        else:
            talkToMe('I don\'t know what you mean!')


talkToMe('anything else sir')
while True:
    assistant(myCommand())


