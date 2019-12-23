osoba = {
    "imie": "Marek",
    "nazwisko": "Banach",
    "wiek": 25,
    "hobby": ['programowanie',"wycieczki"],
    "student": True,
    "telefon": {"stacjonarny":"2233", "komorkowy":"7788"},
    }
osoba["hobby"].append('rower')
osoba['nazwisko'] = "Nowak"
osoba["student"] = False
osoba["plec"] = "Mezczyzna"
osoba['telefon']['sluzbowy'] = '3131'
print(osoba)
