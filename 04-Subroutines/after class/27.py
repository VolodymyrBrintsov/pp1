def czestosc():
    samogloski = ('a', 'e', 'i', 'y', 'o', 'u')
    sylaby = []
    sylaba = ""
    slowo = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."
    for znak in slowo:
       if znak in samogloski:
           sylaba += znak
           sylaby.append(sylaba)
           sylaba = ""
       else:
           sylaba += znak
 
    if sylaba:
       sylaby.append(sylaba)
 
    print(sylaby)
czestosc()
        