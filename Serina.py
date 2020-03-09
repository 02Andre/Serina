

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
     #Record the audio
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

    myobj = gTTS(text= text, lang= 'en' slow=False)

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
        If phrase in text:
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
    ordinalNumber= [

