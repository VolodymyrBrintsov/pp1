class Student():
    def __init__(self, imie, nazwisko, nr_albumu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.album = nr_albumu
        
    def __str__(self):
        return f"Imie: {self.imie}, nazwisko: {self.nazwisko}, numer albumu: {self.album}"
    
    def __lt__(self, other):
        return self.album > other.album
    
s1 = Student("Michal","Janaszek",213455)
s2 = Student("Volodymyr","Brintsov",214825)
s3 = Student("Roflo","Kek",228337)
s4 = Student("Lol","Azaza",453452)
StudentList = [s1,s2,s3,s4]
    
StudentList.sort()
for e in StudentList:
    print(e)
    
        