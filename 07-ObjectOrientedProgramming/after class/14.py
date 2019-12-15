class Telefon():
    def __init__(self,developer, pamiec, suma):
        self.developer = developer
        self.pamiec = pamiec
        self.suma = suma
        
    def __str__(self):
        return f'{self.developer}, {self.pamiec}, {self.suma}'
    
OnePlus = Telefon('OnePlus',"64Gb","2000zl")
XiaOmi = Telefon('XiaOmi',"32Gb","1500zl")

print(OnePlus, XiaOmi)

        
    