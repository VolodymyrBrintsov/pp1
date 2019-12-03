import random
class Kostka():
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.rezultaty = ''
        self.suma_rezultatu = 0
        
    def rzut(self):
        for ilosc in range(3):
            rzut_kostki = random.randint(self.min,self.max)
            self.suma_rezultatu += rzut_kostki
            print(f'Wyrzucono: {rzut_kostki}')
        
        print(f'Suma rzutow: {self.suma_rezultatu}')
            
los = Kostka(1,6)
los.rzut()

        