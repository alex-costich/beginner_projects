import pandas as pd
import speech_recognition as sr
import pyttsx3
import win32api
import pandas as pd
from c_exam_class import sayFunction, listenFunction

class Student:
    def __init__(self, student_id, password) -> None:
        self.student_id = student_id
        self.password = password

students = []

lock = 1

textSource = [
    "PLATAFORMA DE EXÁMENES UAG",
    "1 - Iniciar sesión",
    "2 - Registrarse",
    "3 - Salir",
    "Opción inválida.",
    "Por favor ingrese número de registro.",
    "Por favor ingrese contraseña.",
    "Cuenta registrada.",
    "Bienvenido.",
    "La cuenta o contraseña son incorrectos/no existen."
]

while lock == 1:
    for i in range(0, 4):
        sayFunction(textSource[i])
        
    choice = input("Ingrese el número de opción a utilizar.\n")
    
    if choice == "1":
        studentId = input(sayFunction(textSource[5]))
        passwrd = input(sayFunction(textSource[6]))
        
        # Check if the student exists in the list
        found_student = None
        for student in students:
            if student.student_id == studentId and student.password == passwrd:
                found_student = student
                break

        if found_student:
            sayFunction(textSource[8])
        else:
            sayFunction(textSource[9])
            
    elif choice == "2":
        studentId = input(sayFunction(textSource[5]))
        passwrd = input(sayFunction(textSource[6]))
        obj = Student(studentId, passwrd)
        students.append(obj)  # Add the new student object to the list
        sayFunction(textSource[7])
        
    elif choice == "3":
        lock = 0
        break
        
    else:
        sayFunction(textSource[4])
