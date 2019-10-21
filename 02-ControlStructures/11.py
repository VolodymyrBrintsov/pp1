login = 'marek'
haslo = 'm-123'
login_ = str(input("Podaj login: "))
haslo_ = str(input("Podaj haslo: "))
if haslo_ == haslo and login_ == login:
    print("Podane dane prawidlowe")
else:
    print("Podane dane nie sa prawidlowymi")