class University():
    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        
    def set_name(self, new_name):
        self.name = new_name

        
    # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
    
Unik = University()
Unik.set_name('AGH')
Unik.print_name()