import math
class Obliczenie():
    @staticmethod
    def Obliczenie_o_promeniu(promien = None):
        return math.pi*promien**2
    @staticmethod
    def ObliczenieProstokata(a = None, b = None):
        return a*b
    
    @staticmethod
    def Obliczenie_trojkata(strona = None, wysokosc = None):
        return strona*wysokosc*0.5
obliczenie = Obliczenie()
print(obliczenie.Obliczenie_o_promeniu(3))
print(obliczenie.ObliczenieProstokata(4,7))
print(obliczenie.Obliczenie_trojkata(6,2))