class Ksiazki():
    def __init__(self, nazwa):
        self.nazwa = nazwa
        
    def __str__(self):
        return str(self.nazwa)
    
class e_book(Ksiazki):
    def __init__(self, nazwa_pliku, nazwa):
        super().__init__(nazwa)
        self.plik = nazwa_pliku
        
    def __str__(self):
        return f"Nazwa: {super().__str__()}, Nazwa pliku: {self.plik}"
    
class papiernicza(Ksiazki):
    def __init__(self,ilosc_stron, nazwa):
        super().__init__(nazwa)
        self.ilosc = ilosc_stron
        
    def __str__(self):
        return f"Nazwa: {super().__str__()}, Ilosc stron: {self.ilosc}"
        
e = e_book("HomeReading", "7 skills")
p = papiernicza("357", "7 skills")
print(e)
print(p)

        
    
        
        