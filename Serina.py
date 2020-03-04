#installed files
from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='eng')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#listens to commands
def myCommand():
    r = sr.Recognizr()
    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        command = r.recongnize_google(audio)
        print('You said: ' + command + '\n')
    #loop back to continue to listen to commands
    except sr.UnknownValueError:
        assistant(myCommand())
    return command

#if statements for execution commands
def assistant(command):
    if 'look up' or 'search' in command:
        chrome_path = '/usr/bin/google-chrome'
        url = 'https://www.https://www.google.com/?safe=active&ssui=on'
        webbrowser.get(chrome_path).open(url)
    if 'what\'s up' or 'how are you' in command:
        talkToMe('I\'m doing Lovely')
    if 'email' in command:
        talkToMe('who is the recipient')
        recipient = myCommand()
        if 'Lange' or ' Brad' in recipient:
            talkToMe('what should I say?' )
            content = myCommand()

            #init gmail SMTP
            mail = smtplid.SMTP('smtp.gulllakecs.org', 587)
            #identify to server
            mail.ehlo()
            #Encrypt session
            mail.starttls()
            #login
            mail.login( 'user', 'pass')
            #send mail
            mail.sendmail('Lange', 'email ', content )
            #close connection
            mail.close()
            talkToMe('Email has been sent')
talkToMe('anything else sir')
while True:
    assistant(myCommand())


