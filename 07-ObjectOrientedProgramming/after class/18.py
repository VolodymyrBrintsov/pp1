class Pojazdy():
    przebieg = 0
    def __init__(self, marka,nr_rejestracyjny):
        self.przebieg = Pojazdy.przebieg
        self.marka = marka
        self.nr_rejestracyjny = nr_rejestracyjny
        self.dostepnosc = "Wypozyczony"
        
        
    def __str__(self):
        return f'Marka pojazdu: {self.marka}, rejestracyjny numer: {self.nr_rejestracyjny}, przebieg {self.przebieg} km, dostepnosc: {self.dostepnosc}'
    
    def zmianaPrzebiegu(self, przebieg):
        self.przebieg = przebieg
        
    def zmianaStatusu_True(self):
         self.dostepnosc = "Dostepny"
        
    def zmianaStatusu_False(self):
        self.dostepnosc = "Wypozyczony"
        
p1 = Pojazdy('Roflianowa', 23134)
p2 = Pojazdy('Roflogleck',42124)
p3 = Pojazdy('Francua', 85431)
ListPojazow = [p1,p2,p3]

class wypozyczalnie():
    def __init__(self,ListPojazow,nazwa):
        self.list = ListPojazow
        self.nazwa = nazwa
        
    def wyswitl(self):
        for e in self.list:
            print(e)
        
    def dodacPojazd(self):
        pass
    
w = wypozyczalnie(ListPojazow)
w.wyswitl()




    
    
    
    
    
    
    
    
        