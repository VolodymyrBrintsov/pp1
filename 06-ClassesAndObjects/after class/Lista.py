class ListaKontaktow():
    def __init__(self):
        self.nazwa = ['Maj Piotr', 'Vova Brintsov', 'Jan Kowalski']
        self.email = ['jh@mail.com', 'maj@google.com', 'lol@gmail.com']
        self.numer = ['555234000', '555234000', '555234000']
        
    def dodaj_kontakt(self):
        nazwa_nowego_kontaktu = 'nazwa_nowego_kontaktu'
        while nazwa_nowego_kontaktu != '':
            nazwa_nowego_kontaktu = input('Podaj nazwe nowego kontaktu: ')
            self.nazwa.append(nazwa_nowego_kontaktu)
            
            email_nowego_kontaktu = input('Podaj email nowego kontaktu: ')
            self.email.append(email_nowego_kontaktu)
            
            numer_nowego_kontaktu = input('Podaj numer nowego kontaktu: ')
            self.numer.append(numer_nowego_kontaktu)
        
    def wyswietl(self):
        print('Lista kontaktow: ')
        for x in range(0, len(self.nazwa)):
            print(f'{self.nazwa[x]}\t      {self.email[x]}\t          {self.numer[x]}')
        
lista = ListaKontaktow()