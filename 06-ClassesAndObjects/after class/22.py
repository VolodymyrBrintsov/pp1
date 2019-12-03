import random
class Termometr():
    def __init__(self):
        self.biezoca_temp = 0
        
    def zmierz(self):
        zmierznie_temp = random.uniform(34.0,42.0)
        self.biezoca_temp += round(zmierznie_temp,1)
        
    def status(self):
        if self.biezoca_temp == 0:
            print('Trzeba zmierzyc temperature.')
        elif self.biezoca_temp >= 34.0 and self.biezoca_temp < 37.0:
            print(f'Temperatura: {self.biezoca_temp}C.')
        elif self.biezoca_temp >= 37 and self.biezoca_temp < 41.0:
            print(f'Temperatura: {self.biezoca_temp}C (goraczka).')
        else:
            print(f'Temperatura: {self.biezoca_temp}C (Stan zagrożenia życia!!!).')
            
term = Termometr()
term.zmierz()
term.status()
        