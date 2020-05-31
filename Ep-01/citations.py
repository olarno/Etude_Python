import random
# Listing of quotes & games
quotes = [
    "Le gateau est un mesonge.", 
    "La folie c'est refaire sans arret exactement la meme connerie qu'on repete sans arret, en esperant que ca change.",
    "La guerre, la guerre ne meurt jamais.",
    "Rien n'est vrai. Tout est permis.",
    "Je ne suis pas un heros, jamais je ne l'ai ete, jamais je ne le serai.",
    "C'est dangereux de sortir tout seul, tient, prend ceci!",
    "Avant j'etais un aventurieur comme toi. Et puis je me suis pris une fleche dans le genou.",
    "Objection !",
    "Et tu t'inquiete pas pour ton âme ?",
    "Mes couilles sur ton nez, t'auras l'air d'un dindon !",
    "Tu veux qu'on se tire l'oreille ?",
    "Hey cousin ! C'est ton cousin ! Allons faire du Bowling",
    "It's me Mario !",
    "Est-ce que tu pleures ? C'est seulement la pluie. Le diable ne pleure jamais !",
    "Merci Mario! Mais notre Princesse est dans un autre château !",
    "L'Homme choisit. L'esclave obeit.",
    "N'oubliez pas ... pas de Russe.",
    "Ah oui, les Moissonneurs ...",
    "Tout ce que nous avions à faire, c'etait suivre le foutu train CJ!",
    "All your base are belong to us.",
    "He, c'est moi, Imoen!",
    "Qu'est-ce qui ets le mieux ? Etre ne bon, ou depasser votre nature malfaisante au pris d'immenses efforts ? ",
    "Consider your bones olmd man. You're outmatched.",
    "Il y a des gens qui vous attaquent deliberement ??? ", 
    ]

games = [
    "Portal",
    "Far Cry 3",
    "Fallout",
    "assassion's Creed",
    "metal Gear Solid 4",
    "The Legend of Zelda",
    "Skyrim",
    "phoenix Wright",
    "GTA IV",
    "duke Nulen Foreever",
    "GTA IV",
    "Super Mario 64",
    "Devil May Cry 3",
    "Super Mario Bros",
    "bioshock",
    "Call of Duty : Modern Warfare II",
    "mass Effect 2",
    "GTA : San Andreas",
    "Zero Wings",
    "baldur's Gate",
    "Skyrim",
    "Final Fantasy XII",
    "Dragon Age : Origins",
    ]

# Show random quote 
def get_random_item(my_list):
    rand_numb = random.randint(0, len(my_list) - 1)
    item = my_list[rand_numb]
    return item

def capitalize(words):
    for word in words:
        word.capitalize()

def message(game, quote):
    capitalize(game)
    capitalize(quote)
    return "{} --> {}".format(quote, game)

# ask user for action
user_answer = input("Tapez entree pour connaitre une autre citation ou B pour quitter le programme : ")

# loop  
while user_answer != "B" :
    print(message(get_random_item(games), get_random_item(quotes)))
    user_answer = input("Tapez entree pour connaitre une autre citation ou B pour quitter le programme : ")






