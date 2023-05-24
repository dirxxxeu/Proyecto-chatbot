import gspread,json
import pandas as pd

with open('chatbot.json') as f:
        data = json.load(f)

gc = gspread.service_account(filename='chatbot.json')

sh = gc.open_by_key(data['hoja'])

def llamar_repuestas():
        
        hoja = sh.get_worksheet(0)
        
        preguntas = hoja.get_all_values()
        
        sheet1=pd.DataFrame(preguntas, columns=preguntas.pop(0))

        return sheet1

print(llamar_repuestas())