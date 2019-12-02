class TV():
    def __init__(self):
        self.is_on = False
        self.channel = 1
    
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False
        
    def set_channel(self, channel):
        self.channel = channel
    
    def show_status(self):
        if self.is_on == True:
            print(f'Telewizor jest załączony, kanal {self.channel}')
        else:
            print(f'Telewizor jest wyłączony')
TV = TV()
TV.on()
TV.show_status()
TV.set_channel(5)
TV.show_status()
TV.off()
TV.show_status()
