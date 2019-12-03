from math import gcd
class Dzielenie():
    def __init__(self,licznik,mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
    def dzielenie_zwykle(self):
        print(self.licznik,'/',self.mianownik)
    def uprosczone(self):
        print(int((self.licznik/gcd(self.licznik,self.mianownik))),'/',int((self.mianownik/gcd(self.licznik,self.mianownik))))
div = Dzielenie(10,300)
div.uprosczone()
div.dzielenie_zwykle()