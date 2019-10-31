import re
komunikat = 'To be, or not to be, that is the question'
kek = ()
cyfry = kek + tuple((re.findall('[aeiouyAEIOUY]', komunikat)))
print(len(cyfry))
