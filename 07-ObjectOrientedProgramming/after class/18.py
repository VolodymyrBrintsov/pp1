class Pojazdy():
    przebieg = 0
    def __init__(self, marka,nr_rejestracyjny):
        self.przebieg = Pojazdy.przebieg
        self.marka = marka
        self.nr_rejestracyjny = nr_rejestracyjny
        self.dostepnosc = "Wypozyczony"
        
    def __str__(self):
        return f'Marka pojazdu: {self.marka}, rejestracyjny numer: {self.nr_rejestracyjny}, przebieg {self.przebieg} km, dostepnosc: {self.dostepnosc}'

p1 = Pojazdy('Roflianowa', 23134)
print(p1)
        