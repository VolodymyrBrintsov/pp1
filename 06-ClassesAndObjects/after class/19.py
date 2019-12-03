class Rachunek_bankowy():
    def __init__(self, nr):
        self.rachunek = str(nr)
        self.saldo = 0
        
    def wplacic(self, ilosc):
        self.saldo += ilosc
        
    def wyplac(self, ilosc):
        if self.saldo < ilosc:
            print('Niewystarczająca ilość środków na rachunku')
        else:
            self.saldo -= ilosc
        
    def status(self):
        if len(self.rachunek) == 26:
            print(self.rachunek[0:2] + " " + self.rachunek[2:6] + " " + self.rachunek[6:10] + " " + self.rachunek[10:14] + " " + self.rachunek[14:18] + " " + self.rachunek[18:22] + " " + self.rachunek[22:26])
            print(f'Saldo: {self.saldo} zl')
bank = Rachunek_bankowy(12345655559090111100007722)
bank.status()
bank.wplacic(25.30)
bank.status()
bank.wyplac(14)
bank.status()