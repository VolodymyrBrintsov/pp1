class Sala():
    def __init__(self, nazwa, liczba_miejsc):
        self.nazwa = nazwa
        self.liczba_miejsc = liczba_miejsc        

class Sale():
    sale = []
    id = 0
    def dodaj(self, sale):
        self.sale.append(sale)
        self.id += 1
        
    def print(self):
        print(self.sale[2].liczba_miejsc)
        
    
        
        
s1 = Sala("Nowa Aula", 50)
s2 = Sala("Hala Sportowa", 500)
s3 = Sala("Lab. komputerowa", 35)
s = Sale()        
s.dodaj(s1)
s.dodaj(s2)
s.dodaj(s3)
s.print()