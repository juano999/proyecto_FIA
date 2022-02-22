import speech_recognition as sr
import pyttsx3
from datetime import datetime
import time

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
name_asistant = "Alexa"

text_from_options = "quiero agrear una tarea quiero saber mis tareas pendientes quiero saber mis tareas acabadas"

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen_option():
    try:
        talk("Dime en que te puedo ayudar")
        print("Escuchando ahora...")
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            option = listener.listen(source)
            selection = listener.recognize_google(option, language='es-EC')
            selection = selection.lower()
            if text_from_options in selection:
                selection = selection.replace(text_from_options, '')
    except:
        pass
    return selection

def save_task():
    selection = ''
    
    talk("Dime el nombre de la tarea")
    while( selection == ''):
        print("Escuchando ahora...")
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            option = listener.listen(source)
            selection = listener.recognize_google(option, language='es-EC')
            selection = selection.lower()
            selection = selection + '\n'
            tasks = []
            r = open('task.txt', 'r')
            while(True):
                linea = r.readline()
                tasks.append(linea)
                if not linea:
                    break
            #Corregir el problema de validación de datos repetidos
            print(tasks)
            if selection not in tasks:
                f = open('task.txt','a')
                #f.write(selection + '\n')
                f.write(selection)
                f.close()
                print("Guardando la tarea")
                talk("Guardando la tarea")
                time.sleep(3)
                print("La tarea " + selection + " ha sido guardada con exito")
                talk("La tarea " + selection + " ha sido guardada con exito")
            else:
                selection = ''
                print("Esta tarea ya existe, mencione otra")
                talk("Esta tarea ya existe, mencione otra")
            
    
    return selection

def read_task():
    print("Obtenido las tareas")
    talk("Obteniendo las tareas")
    time.sleep(2)
    f = open("task.txt", "r")
    linea = f.readline()
    if linea == "":
        print(linea)
        print("No hay tareas por el momento")
        talk("No hay tareas por el momento")
    else:
        #print(linea)
        talk(linea)
        while(linea != ""):
            linea = f.readline()
            #print(linea)
            talk(linea)
            if not linea:
                break
    f.close()

def delete_task():
    with open("task.txt", 'r+') as f:
        f.truncate(0)

def run_recover():
    print("Cargando todo lo necesario para grabar el audio")
    talk("Cargando todo lo necesario para grabar el audio")
    time.sleep(3)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Grabando audio...")
        audio = r.listen(source)

        with open("microphone-results.wav", "wb") as h:
             h.write(audio.get_wav_data())

        print("Guargando audio")
        talk("Guardando audio")
        time.sleep(3)
        print("Recuerda que tu audio siempre será el último que has grabado")
        talk("Recuerda que tu audio siempre será el último que has grabado")
        print("Tu audio se encuentra en la carpeta principal de este proyecto")
        talk("Tu audio se encuentra en la carpeta principal de este proyecto")
    
def run_date():
    date = datetime.today().strftime('%Y-%m-%d')
    talk(date)
    print(date)

#Implementar tareas pendientes y tareas finalizadas

def run_program():
    talk("Hola mucho gusto soy " + name_asistant)
    run_options()

def run_options():
    option = listen_option()
    while("nada más" not in option):
        if 'quiero agregar' in option:
            option = option.replace('quiero agregar', 'agregar')
            print("Has seleccionado " + option)
            talk("Has seleccionado " + option)
            save_task()
            option = listen_option()
        if 'quiero saber' in option:
            option = option.replace('quiero saber la', 'conocer la')
            print("Has seleccionado " + option)
            talk("Has seleccionado " + option)
            read_task()
            option = listen_option()
        if 'quiero eliminar' in option:
            option = option.replace('quiero eliminar los datos del', 'la eliminacion del')
            print("Has seleccionado " + option)
            talk("Has seleccionado " + option)
            print("Borrando datos")
            talk("Borrando datos")
            time.sleep(3)
            print("Datos borrados con éxito")
            talk("Datos borrados con éxito")
            delete_task() 
            option = listen_option()
        if 'quiero grabar' in option:
            option = option.replace('quiero grabar', 'grabar')
            print("Has seleccionado " + option)
            talk("Has seleccionado " + option)
            run_recover()
            option = listen_option()
        if 'dime la fecha' in option:
            option = option.replace('dime la fecha', 'conocer la fecha')
            print("Has seleccionado " + option)
            talk("Has seleccionado " + option)
            run_date()
            option = listen_option()
        if "nada más" in option:
            print("Espero haberte ayudado mucho, hasta pronto")
            talk("Espero haberte ayudado mucho, hasta pronto")
            break
    



run_program()