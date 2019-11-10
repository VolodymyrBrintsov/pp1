tab = [500,501,23,500,1,32,32]
nie_tab= []
def powtarzalkiLiczby():
    for x in tab:
        if tab.count(x) == 1:
            nie_tab.append(x)
    print(nie_tab)
powtarzalkiLiczby()