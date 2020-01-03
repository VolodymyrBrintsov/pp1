import re
class ListaKontaktow():
    def __init__(self):
        self.nazwa = ['Maj Piotr', 'Vova Brintsov', 'Jan Kowalski']
        self.email = ['jh@mail.com', 'maj@google.com', 'lol@gmail.com']
        self.numer = ['555234000', '555234000', '555234000']
        
    def dodaj_kontakt(self):
        nazwa_nowego_kontaktu = 'nazwa_nowego_kontaktu'
        while nazwa_nowego_kontaktu != 'r':
            nazwa_nowego_kontaktu = input('Podaj nazwe nowego kontaktu: ')
            self.nazwa.append(nazwa_nowego_kontaktu)
            if nazwa_nowego_kontaktu == "":
                break
            
            email_nowego_kontaktu = input('Podaj email nowego kontaktu: ')
            self.email.append(email_nowego_kontaktu)
            
            numer_nowego_kontaktu = input('Podaj numer nowego kontaktu: ')
            self.numer.append(numer_nowego_kontaktu)
        
    def wyswietl(self):
        kek = 'Lista kontaktow: \n'
        for x in range(len(self.numer)):
            kek += f'{self.nazwa[x]}\t{self.email[x]}\t{self.numer[x]}\n'
        print(kek)
        
