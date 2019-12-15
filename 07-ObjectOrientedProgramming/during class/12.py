import random
class arrays(): 
    def __init__(self,liczba_elementow,warotosc_elementow):
        self.liczba_elementow = liczba_elementow
        self.wartosc_elementow = warotosc_elementow
        self.tablica = []
    
    def Losowa_tablica(self,wartosc_od,wartosc_do):
        for x in range(self.liczba_elementow):
            r = random.randint(wartosc_od,wartosc_do)
            self.tablica.append(r)
        print(self.tablica)
           
    def Metoda(self,wartosc_od,wartosc_do):
        self.wartosci_z_przedzialu = []
        while wartosc_od != wartosc_do+1:
            self.wartosci_z_przedzialu.append(wartosc_od)
            wartosc_od += 1
        print(self.wartosci_z_przedzialu)          
    def Kek(self):
        ilosc = 0
        for x in self.tablica:
            for y in self.wartosci_z_przedzialu:
                if x == y:
                    ilosc += 1
                    
        print(ilosc)
a = arrays(20,20)
a.Losowa_tablica(-7,8)
a.Metoda(-1,1)
a.Kek()
        

    