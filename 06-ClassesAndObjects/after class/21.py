import statistics

class Statystyka():
    def __init__(self, zbior_liczb):
        self.zbior_liczb = list(zbior_liczb)
        
    def wyswietl(self):
        print(*self.zbior_liczb)
        print(min(self.zbior_liczb))
        print(max(self.zbior_liczb))
        print(statistics.mean(self.zbior_liczb))
        print(statistics.median(self.zbior_liczb))
        
stat = Statystyka([12, 37, 6, 9, 17])
stat.wyswietl()

        