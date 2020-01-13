def obecnośćPliku(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print('Nie mogę znaleść tego pliku.')
            
obecnośćPliku("NoEducation.txt")