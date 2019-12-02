class TV():
    def __init__(self):
        self.is_on = False
        self.channel = 1
        self.channels = 'Telewizor niezaprogramowany, brak dostępnych kanałów'
    
    def on(self):
        self.is_on = True
    
    def off(self):
        self.is_on = False
        
    def set_channel(self, channel):
        self.channel = channel
        
    def set_channels(self, channels_list):
        channels = ' '
        for x in channels_list:
            channels += x + ", "
        self.channels = channels
    
    def show_status(self):
        if self.is_on == True:
            print(f'Telewizor jest załączony, kanal {self.channel}')
            print(f'Istnieja taki kannaly :', self.channels)
        else:
            print(f'Telewizor jest wyłączony')
tv = TV()
tv.on()
tv.show_status()
tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox'])
tv.show_status()

