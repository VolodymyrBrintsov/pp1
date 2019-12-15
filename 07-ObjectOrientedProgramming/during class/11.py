class arrays():
    @staticmethod
    def print_in_col(array):
        gleck = ''
        for c in array:
            if c != array[-1]:
                gleck += str(c) + ","
            else:
                gleck+= str(c)
        print(gleck)

my_array = [4,1,8,7,2]
arrays.print_in_col(my_array)