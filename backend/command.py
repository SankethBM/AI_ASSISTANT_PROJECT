import pyttsx3
import speech_recognition as sr
import time
import eel 

def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    # print(voices)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listining...')
        eel.DisplayMessage('listining...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print('recognizing...')
        eel.DisplayMessage('recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        # speak(query)
    except Exception as e:
        return ""
    
    return query.lower()


@eel.expose
def allCommands():

    try:
        query = takecommand()
        print(query)

        if "open" in query :
            from backend.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from backend.features import PlayYoutube
            PlayYoutube(query)

        elif "send message" in query or "phone call" in query or "video call" in query:
            from backend.features import findContact, whatsApp
            message=""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    message = 'message'
                    speak("What message to send")
                    query = takecommand()

                elif "phone call" in query:
                    message = 'phone call'
                else:
                    message = 'video call'
                
                whatsApp(contact_no, query, message, name)

        else:
            print("not run")
    except:
        print("Error!!!!")
    
    
    eel.ShowHood()

