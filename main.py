import utils
'''
Creare un programma il quale prenderà determinate scelte per te

skill richieste:
	-python
	-random module
	-input() function
Skill avanzate (bonus):
	-Pandas (manipolazione tabelle tipo)
	-API'S (application programming interfaces)
		-> permette di interagire con softwares di altri
		-> utenti

Piccola introduzione teorica per affrontare il progetto
difficoltà base:
	fai una lista
	scegli un valore casuale e stampalo
'''

list = ["Super Mario", "Super smash bros", "Guilty gear strive",
				"Zelda"]
#mandatory
utils.do_for_me(list)

'''
advanced manipulation
potrebbe coinvolgere una lista con sotto liste le quali in base a dei parametri
potrebbero cercare un anime con statistiche che coinciderebbero
con il genere o robe del genere e non solo il nome della serie/film
'''
advanced_list = [
	["Super Mario", "Platformer", "Simple"],
	["Mario Kart 8 Deluxe", "Racing game", "Fast"],
	["Guilty gear strive", "Fighting game", "Frenetic"],
	["Zelda", "Action RPG", "Slow"]
]

try:
	critria = int(input("""What gameplay would you like in your game?\n
	i mean would like something:
	1) with simple gameplay
	2) fast gameplay
	3)frenetic gameplay
	4)slow gameplay\n"""))
except ValueError:
	print("You didn't put a correct number did you?")

try:
	print("The game for you would be: ", advanced_list[critria - 1][0])
except NameError:
	print("You didn't put a correct number did you?")
except IndexError:
	print("You put a number that wasn't in the")

test2 = input("tell me what's the genre you like ")
for genre in advanced_list:
	if (genre[1] == test2):
		print("you should play ", advanced_list[0])

