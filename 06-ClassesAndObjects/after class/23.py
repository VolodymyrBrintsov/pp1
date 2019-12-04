from Lista import ListaKontaktow
class Kontakt(ListaKontaktow):
    
    def poszukKontaktu(self):
        self.jaki_kontakt = input('Podaj imie i nazwisko czlowieka ktorego szukasz: ')
        self.indeks_kontaktu = self.nazwa.index(self.jaki_kontakt)
        
    def wyswietlic(self):
        print(f'Imie i nazwisko czlowieka: {self.nazwa[self.indeks_kontaktu]}, Email: {self.email[self.indeks_kontaktu]}, Numer: {self.numer[self.indeks_kontaktu]}')
kont = Kontakt()
lista = ListaKontaktow()
lista.dodaj_kontakt()
lista.wyswietl()
kont.poszukKontaktu()
kont.wyswietlic()
    