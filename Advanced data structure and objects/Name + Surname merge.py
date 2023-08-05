# Two lists containing names and surnames
names = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
surnames = ["Yılmaz", "Öztürk", "Dağdeviren", "Atatürk", "Dikmen", "Kaya", "Polat"]

# Combine names and surnames into a list of tuples
name_surname_list = list(zip(names, surnames))

# Sort the list based on the names
name_surname_list.sort()

# Print the names and surnames in alphabetical order based on the names
for name, surname in name_surname_list:
    print(name, surname)
