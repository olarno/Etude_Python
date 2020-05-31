# 
# Methode : les liste
#

characters = ["Dark Vador", "Luke Skywalker", "Leila Skywalker", "Han solo", "Chewbaca"]

print(characters.index("Han solo"))


characters.append("Kylo ren")

print(characters)

characters.insert(2, "R2D2")

print(characters)

characters[0] = "Darkou"

print(characters)

# supprimer le dernier element de la liste 
characters.pop()

# supprimer un element ave cson index 
characters.remove("Han solo")
print(characters)