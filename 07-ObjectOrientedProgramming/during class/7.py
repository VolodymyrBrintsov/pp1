class Student():
    nr_albomu = 100000;
    def __init__(self,imie, nazwisko,kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_albomu = Student.nr_albomu
        self.kerunek = kierunek
        Student.nr_albomu += 1
    def __str__(self):
        return f'{self.imie}, {self.nazwisko}, {self.nr_albomu}. {self.kerunek}'
    
student = Student('Vova', 'Brintsov', 'Informatyka')
print(student)
student = Student('Vova', 'Brintsov', 'Informatyka')
print(student)