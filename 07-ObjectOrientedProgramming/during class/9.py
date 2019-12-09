class Messege():
    def __init__(self, messege):
        self.messege = messege
        self.set_messege()
        
    def set_messege(self):
        self.messege = self.messege[0].upper() + self.messege[1:len(self.messege)].lower()
        
    def __str__(self):
        return self.messege + " BYE."
        
class SMS(Messege):
    def __init__(self, nr_tel, messege):
        self.nr_tel = nr_tel
        super().__init__(messege)

class Email(Messege):
    def __init__(self,adres_nadawcy,adres_odbircy,temat, messege):
        super().__init__(messege)
        self.adres_nadawcy = adres_nadawcy
        self.adres_odbircy = adres_odbircy
        self.temat = temat
    
    def __str__(self):
        return f'''
Od:      {self.adres_nadawcy}
Do:      {self.adres_odbircy}
Tema:    {self.temat}
Tresc:   {super().__str__()}'''

sms = SMS(481324, "GegGE")
email = Email('brints0v@gmail.com', 'nowak@gmail.com', 'Spotkanie', 'Informuję, że nasze czwartkowe spotkanie zostało \n odwołane.')
print(email)