import gspread,json
import pandas as pd

#aqui abrimos el json con las credenciales
with open('chatbot.json') as f:
        data = json.load(f)
#aqui conectamos con el api de google sheets                            
gc = gspread.service_account(filename='chatbot.json')

#aqui llamamos el strin que necesitamos con la llave del diccionario que contiene el json
sh = gc.open_by_key(data['hoja'])

#esta funcion genera un dataframe del contenido del excel
def llamar_repuestas():
        #esto crea una hoja en bruto de excel
        hoja = sh.get_worksheet(0)
        #esto no se que hace pero es importante ponerlo
        preguntas = hoja.get_all_values()
        #aqui generamos el dataframe con pandas
        sheet1=pd.DataFrame(preguntas, columns=preguntas.pop(0))

        return sheet1

print(llamar_repuestas())
