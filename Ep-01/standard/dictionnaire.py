#
# Method : dictionnaire 
# accès via la clé pour obtenir une valeur
#

dico_en_fr = {'three':'trois', 'one':'un', 'two':'deux'}

print(dico_en_fr)

# mettre a jour // ajouter
dico_en_fr.update({"one":"Un", "two":"Deux"})

print(dico_en_fr)

# supprimer 
dico_en_fr.pop('one')

print(dico_en_fr)

# ajouter 
dico_en_fr.update({"one":"un"})
print(dico_en_fr)

dico_en_fr["one"]="Un"
print(dico_en_fr)