names = ['Tim Benzinger', 'Colette Lohr', 'Brian Benzinger', 'Amanda Parille', 'Shawn Semmes', 'Katie Dunn', 'Max Retter', 'Molly Muranaka', 'Matt Wilson', 'Janelle Farabaugh']
print(names)

names_sorted = names.sort(key=lambda name: name.split(" ")[-1].lower())
print(names_sorted)
