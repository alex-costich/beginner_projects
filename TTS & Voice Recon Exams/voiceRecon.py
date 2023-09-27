import speech_recognition as sr
import pyttsx3
import win32api

# Creamos un objeto de reconocimiento de voz
r = sr.Recognizer()

"""
# Utilizamos el micrófono como fuente de audio
with sr.Microphone() as source:
    print("Di algo...")
    texto0="Hola buenos días ¿puedes decir algo?..."
    engine = pyttsx3.init()
    engine.say(texto0) # engine habla
    engine.runAndWait()
    
    audio = r.listen(source) # escuchar el audio

# Utilizamos el reconocimiento de voz de Google para transcribir el audio
try:
    texto = r.recognize_google(audio, language='es-MX')
    print("Has dicho: " + texto)
except sr.UnknownValueError:
    print("No se pudo entender lo que dijiste")
except sr.RequestError as e:
    print("Error al conectarse con el servicio de reconocimiento de voz; {0}".format(e))

"""    

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")

engine.setProperty("voice", voices[2].id) # sets voice to second third in my voice list (mexican spanish)

def sayFunction(text): # function for voicing text, returns nothing
    print(text)
    engine.say(text)
    engine.runAndWait()
    
def listenFunction(): # function for listening to text, returns text
    callout = "Estoy esperando tu respuesta."
    engine = pyttsx3.init()
    engine.say(callout)
    engine.runAndWait()

    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Procesando audio...")
            text = r.recognize_google(audio, language='es-MX')
            print(f"Has dicho: \"{text}\"")
        except sr.UnknownValueError:
            print("No se pudo entender lo que dijiste")
        except sr.RequestError as e:
            print("Error al conectarse con el servicio de reconocimiento de voz; {0}".format(e))
    
    return text