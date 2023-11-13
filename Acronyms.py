# Artificial Intelligence --> AI

term = input("Enter the term: ")
words = term.split()

acronym = ""
for item in words:
    acronym += item[0].upper()

print(acronym)



