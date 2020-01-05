import json

def  bieżąca_tabela_notowań():
    dict = {}
    
    
    with open("notowania.json")as file:
        data = json.load(file)
    
#   pobieramy dane z pliku 
    for dane in data:
        dict = dane
    
 
    notowania_str = f"""Bieżąca tabela kursu walut dla daty {dict['effectiveDate']}:
================================================\n"""    
    
    
    for x in range(len(dict['rates'])):
        
        
        if x >= len(dict['rates'][0:len(dict['rates'])-1]):
            notowania_str += f"Waluta: {dict['rates'][x]['currency']}, srednia cena: {dict['rates'][x]['mid']}"
        
        
        else:
            notowania_str += f"Waluta: {dict['rates'][x]['currency']}, srednia cena: {dict['rates'][x]['mid']}\n"
        
    
    return notowania_str
        
        

print(bieżąca_tabela_notowań())