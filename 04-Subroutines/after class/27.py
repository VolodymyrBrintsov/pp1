def czestosc():
    samogloski = ['a', 'e', 'i', 'y', 'o', 'u']
    text = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."
    import re
    samogloski_tekst = []
    for x in samogloski:
        samogloski_tekst = re.findall(x,text)
        print(f'Samogłoska: {x} występuje: {len(samogloski_tekst)} razy, częstość {len(samogloski_tekst)}/{len(text)}')    
czestosc()
        