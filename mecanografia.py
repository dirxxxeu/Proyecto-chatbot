from drive_request import llamar_repuestas
import time
import sys

def mecanografia(texto): # funcion para el efecto de mecanografia
    lista = texto.split() # separa el texto en espacios
    for palabra in lista:
        sys.stdout.write(palabra + " ")
        sys.stdout.flush()
        time.sleep(0.4)# velocidad en la que realiza la mecanografia

textos =llamar_repuestas()

for x in textos:
    preguntas=x[0]
    respuestas=x[1]
    if preguntas!='preguntas':
        print(preguntas.capitalize())
        mecanografia(respuestas)
        print("\n")