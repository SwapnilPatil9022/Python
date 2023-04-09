import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        info = listener.recognize_google(voice)
        print(info)
except:
    pass