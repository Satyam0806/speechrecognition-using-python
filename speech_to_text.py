# first install speech recongition using pip3 install speechrecognition in your terminal 
#record an audio file
#convert the audio file into wav extension
import speech_recognition as sr
import speech_to_text
AUDIO_FILE=('give the file name .wav')

r=sr.Recognizer() #intialize the recogniser
with sr.AudioFile(AUDIO_FILE) as source: #open the audio file
    audio = r.record(source) #read the audio file
try:
   print("Audio filr contain:"+r.recognize_google(audio)) #print what you said
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError:    #this is used if we cannot get the outcome from google
    print("Service is down")

      



