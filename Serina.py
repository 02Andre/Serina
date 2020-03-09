

"pip install"

import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import webbrowser
 #ignore any warning messages
warnings.filterwarnings('ignore')

 # Record audio and return as string
def recordAudio():
    r = sr.Recognizer() #creating a recognizer object
     #Open the microphone and start Recording
    with sr.Microphone()as source:
        print('Say Something!')
        audio = r.listen(source)
        #Use Googles Speech
    data = ' '
    try:
        data = r.recognize_google(audio)
        print('you said: '+ data)
    except sr.UnknownValueError: #Check for unknown errors
        print('Google Speech Recognition could not understand the audio, unknown error')
    except sr.Request as e:
        print('Request results from google Speech service error '+ e)
    return data
#A Function to get the virtual assistant response
def assistanResponse(text):
    print(text)

    myobj = gTTS(text= text, lang= 'en', slow = False)

    # Save the converted audio
    myobj.save('assistant_response.mp3')
    #play the converted file
    os.system('start assistant_response.mp3')

#creat A function for wake word(s) or phrase
def wakeWords(text):
    WAKE_WORDS = ['hey Serina', 'okay Serina', 'Serina'] #list of words

    text = text.lower() # converting the text to all lower case words

    #
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    #If the wake word isnt found in the text
    return False

#function to get the date and time
def getDate():
    now = datetime.datetime.now()
    my_date =  datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()] # e.g. Friday
    monthNum = now.month
    dayNum = now.day

    #list of months
    month_names= ['January', 'February', 'March', 'April', 'May','June','July','August', ' September',
                  'October', 'November', 'December']
    ordinalNumber=  [ '1st', '2nd', ' 3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                      '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th','25th'
                      '26th','27th','28th','29th', '30th', '31st']
    return 'Today is ' +weekday+' '+month_names[monthNum - 1]+' the '+ ordinalNumber[dayNum - 1]+'. '

# A function to return a random greeting response
def greeting(text):


