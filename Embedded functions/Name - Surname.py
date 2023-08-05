# Lists containing names and surnames
names = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
surnames = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

# Pair names and surnames and print them line by line
for name, surname in zip(names, surnames):
    print(name, surname)
