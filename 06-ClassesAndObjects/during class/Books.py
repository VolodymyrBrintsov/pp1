class Book():
    def __init__(self,title,author,pages_num):
        self.title = title
        self.author = author
        self.pages_num = pages_num
        self.current_page = 0
        self.is_open = False
    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False
    def read(self):
        if self.is_open == True:
            print('Czytasz stronę', self.current_page)
    def next_page(self):
        if self.is_open == True:
            self.current_page +=1
    def previous_page(self):
        if self.is_open == True:
            self.current_page -=1
    
    def book_status(self):
        print(f'''
Nazwa:                   {self.title}
Autor:                   {self.author}
Ilosc stron              {self.pages_num}
Biezaca strona           {self.current_page}''')
