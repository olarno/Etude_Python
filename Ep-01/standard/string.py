# https://docs.python.org/3.5/library/stdtypes.html#text-sequence-type-str
#
# Method : les strings
#

hello = "     hello world!"

# liste des mots (séparé par un espace)
print(hello.split())
# supprimer les esapce blanc
print(hello.strip())
# mise en majuscule
print(hello.upper())
# mise en minuscule
print(hello.lower())
#mise en majuscule de la premiere lettre 
print(hello.capitalize())

# dynamiser une chaine de caractere
print("{character} a dit {quote}".format(character="Babar", quote="Bonjour"))
print("{} a dit {}".format("Babarounet", "Bonjour"))

