class University():
    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        self.fullname = 'Uniwersytet ekonomiczny w Krakowie'
        
    def set_name(self, new_name):
        self.name = new_name

        
    # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
        
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self, new_name):
        self.fullname = new_name
Unik = University()
Unik.print_fullname()
Unik.set_fullname('Uniwersytet Stomatologii')
Unik.print_fullname()