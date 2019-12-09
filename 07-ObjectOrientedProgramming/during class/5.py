class utworyMuzyczne():
    def __init__(self,wykonawca, tytul, album, rok):
        self.wykonawca = wykonawca
        self.tytul = tytul
        self.album = album
        self.rok = rok
        
    def __str__(self):
        return f'''
Wykonawca: {self.wykonawca}
Utwor:     {self.tytul}
Album:     {self.album}
Rok:       {self.rok}'''
    
utw = utworyMuzyczne('Dawid Podsiadlo', 'Nie ma fal', 'Mialomiasteczkowy', 2018)
print(utw)