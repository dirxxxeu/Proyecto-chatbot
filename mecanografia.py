from drive_request import llamar_repuestas
import time
import sys


def mecanografia(texto):  # funcion para el efecto de mecanografia
    lista = texto.split()  # separa el texto en espacios
    for palabra in lista:
        sys.stdout.write(palabra + " ")
        sys.stdout.flush()
        time.sleep(0.3)  # velocidad en la que realiza la mecanografia


textos = llamar_repuestas()


color_verde = '\033[92m'
color_reset = '\033[0m'
longitud = 40  # es el total de caracteres por línea de impresion
relleno = " "  # rellena el texto con espacios en blanco

for x in textos:
    preguntas = x[0]
    respuestas = x[1]


    if preguntas != 'preguntas':
        print(color_verde + preguntas.rjust(longitud,
                                            relleno).title() + color_reset)  # alinea el texto a la derecha y capitaliza la primera letra
        time.sleep(1)
        mecanografia(respuestas)
        print("\n")
        time.sleep(1)
