import speech_recognition as sr

r = sr.Recognizer()
file = open("text.txt", "w")

with sr.Microphone() as source:
    print('Speek Anything:')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        file.write('You said: {}'.format(text))
        print('you Said: {}'.format(text))
        file.close()
    except r.recognize_google(audio).DoesNotExist:
        print('Sorry could not recognise your Voice')
