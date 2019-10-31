str = 'To be, or not to be, that is the question'
vowels ="a", "e", "i", "o", "u"
Samogloski = re.findall('\A{vowels}', str)
print(Samogloski)