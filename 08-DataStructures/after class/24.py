import re
import json
class ilosc_slow_w_lyrics():
    
    
    def __init__(self, nazwa_pliku):
        self.nazwa = nazwa_pliku
        
        
    def lyrics(self):
        with open(self.nazwa) as file:
            data = file.read()
            self.slowa = re.findall('\w', data)

    
    def ilosc_slow(self):
        self.ilosc_slow = {}
        
        for word in self.slowa:
            
            if word in self.ilosc_slow:
                self.ilosc_slow[word] += 1
            
            else:
                self.ilosc_slow[word] = 1
        
    
    def __str__(self):
        return f"{self.ilosc_slow}"
    
    def zapisac_do_pliku_json(self, nazwa_pliku_json):
        with open(nazwa_pliku_json, "w") as file:
            json.dump(self.ilosc_slow, file, indent=4)
        
    def otworzyc_plik_json(self, nazwa_pliku_json):
        with open(nazwa_pliku_json)as file:
            data = json.load(file)
        for k,v in data.items():
            print(k,":", v)
    
    
ilosc_obj = ilosc_slow_w_lyrics("DontMakeMeWait.txt")

ilosc_obj.lyrics()
ilosc_obj.ilosc_slow()
print(ilosc_obj)
ilosc_obj.zapisac_do_pliku_json("ilosc slow.json")
ilosc_obj.otworzyc_plik_json("ilosc slow.json")

