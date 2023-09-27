import pandas as pd
import speech_recognition as sr
import pyttsx3
import win32api
import os

# WIFI IS REQUIRED FOR THE USE OF THIS PROGRAM

# VOICE RECON

r = sr.Recognizer() # creation of voice recognition object

engine = pyttsx3.init() # engine selection (pytexttospeech3)

voices = engine.getProperty('voices')
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")

engine.setProperty("voice", voices[2].id) # sets voice to second third in my computer's voice list (mexican spanish), varies from device to device

def sayFunction(text): # function for voicing text, returns nothing
    print(text)
    engine.say(text)
    engine.runAndWait()
    
def listenFunction(): # function for listening to text, returns text or None
    callout = "Estoy esperando tu respuesta."
    print(callout)
    engine = pyttsx3.init()
    engine.say(callout)
    engine.runAndWait()

    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Procesando audio...")
            text = r.recognize_google(audio, language='es-MX')
            confirmation = (f"Has dicho: \"{text}\"?")
            sayFunction(confirmation) # asks user to confirm what was heard is correct
            confAudio = r.listen(source)
            confText = r.recognize_google(confAudio, language='es-MX')
            confText = confText.lower() # lowercases answer
            #print(confText) # prints answer (use for testing)
            if confText.find("sí") != -1:  # if the word "yes" is contained anywhere in the confirmation answer, it checks it out as correct
                return str(text) # returns text
            else: # if the word "yes" is not contained anywhere in the confirmation answer, function recalls itself for another try
                retry = "Okey, intentemos de nuevo."
                sayFunction(retry)
                return listenFunction() # recall the function
            
        except sr.UnknownValueError: # error if audio was not understood
            print("No se pudo entender lo que dijiste")
        except sr.RequestError as e: # error for connection issues
            print("Error al conectarse con el servicio de reconocimiento de voz; {0}".format(e))

    return None  # return None if speech is not recognized

# EXAM CLASS
class Exams:
    def __init__(self, topic, key, score):
        self.topic = topic # subject name
        self.key = key # exam key (excel sheet name from file)
        self.score = 0 # score starts at 0

    def rescore(self, score): # rescores exam
        self.score = score

    def selectExam(self): # creates dataframe from exam using the exam key (which is the excel sheet name holding the data)
        return pd.read_excel('examen_materias_POO.xlsx', sheet_name = self.key)
        

clear = lambda: os.system('cls') # definition for clear() function

exams = [
        Exams("Algebra y Geometría Analítica", "AAG0", 0),
        Exams("Programación Orientada a Objetos", "OOP0", 0),
        Exams("Idiomas: Inglés I", "EL00", 0)
        ]

y = 0
lock = 1
score = 0

clear()

while lock != 0: # loop repeats until exit is selected
    print("LISTA DE EXÁMENES DISPONIBLES:") # menu
    for i in range(len(exams)):
        print(f"{i+1} - {exams[i].topic} | [{exams[i].score}/100]")
    print(f"{i+2} - Salir")

    choice = int(input("Seleccione.\n"))-1

    clear()

    if choice != i + 1:
        examDf = exams[choice].selectExam() # generates dataframe using class function

        rightAnswer = f"Respuesta correcta!"
        wrongAnswer = f"Respuesta incorrecta."

        for z in range(0, 4): # range for question and answer reading (5 questions = (0,5), 3 questions = (0,3) and so on)
            for x in range(z * 6, (z * 6) + 6): # for printing slot 1 (question) and (2-5) answers, lands on slot 6 (right answer)
                if x - (z * 6) != 5:
                    sayFunction(examDf.iloc[x, 0])
            
            getchar = input("Presiona cualquier tecla cuando estés list@ para responder.")
            answer = listenFunction()

            clear()

            if examDf.iloc[x, 0].find(answer) != -1: # if answer is right
                score += 1
                #print(score)   # for visualizing score (testing)
                sayFunction(rightAnswer)
            else: # if answer is not right
                sayFunction(wrongAnswer)

            clear()

            exams[choice].rescore(score*25) # rescores exam

    else: # for when the exit option is selected
        lock = 0
        break

    score = 0

    