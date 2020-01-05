import random
class matrix():

    @staticmethod
    def create(x,y):
        return [[0 for w in range(x)] for h in range(y)]

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
            
    def create_unit(x):
        m = matrix.create(x,x)
        indeks = 0
        for x in range(len(m)):
            m[indeks][indeks] = 1
            indeks += 1
        return m
    
    def fill_random(matrix,m,n):        
        index = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                random_int = random.randint(m,n)
                matrix[x][y] = random_int
        return matrix
    @staticmethod
    def transpozycja(matrix):
        matrix_transpozycja = []
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                matrix_transpozycja.append(matrix[y][x])
                
        return matrix_transpozycja
    
m = matrix.create(3,5)
mr = matrix.fill_random(m,1,9)
matrix.print(mr)
tr = matrix.transpozycja(mr)


matrix.print(tr)

