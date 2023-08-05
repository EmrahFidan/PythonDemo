# Read the file named "mailler.txt" containing emails and some other words
with open("Advanced data structure and objects/mails.txt", "r", encoding="utf-8") as file:
    # Read all lines from the file into a list
    file_content = file.readlines()

# Create an empty list to store valid emails
emails = []

# Iterate through each line and check if it is a valid email
for line in file_content:
    line = line.strip()  # Remove leading and trailing whitespace
    if line.endswith(".com") and "@" in line:
        emails.append(line)

# Print the valid emails to the console
for email in emails:
    print(email)


# 2. çözüm
"""
with open("mailler.txt","r",encoding= "utf-8") as file:
    mailler = file.readlines()
    mailler2 = list()

    for i in mailler:
        i = i.strip("\n")
        mailler2.append(i)


for i in mailler2:
    if (i.endswith(".com") and i.find("@") != -1):
        print(i)

"""