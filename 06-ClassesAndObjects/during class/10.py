class TV():
    def __init__(self):
        self.is_on = False
    
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False
    
    def show_status(self):
        if self.is_on == True:
            print(f'Telewizor jest załączony')
        else:
            print(f'Telewizor jest wyłączony')
TV = TV()
TV.on()
TV.show_status()
TV.off()
TV.show_status()
    