# Pythom 3.6

import random

print("-------------------------------------------------------")
print("-                                                     -")
print("-                                                     -")
print("-                      MAZMORRAS                      -")
print("-              By Daniel Castillo Guindos             -")
print("-                                                     -")
print("-                                                     -")
print("-------------------------------------------------------")

player = {"life": 50,"strong": 5, "money": 0, "potion": 0}

def entry():
	print("\n\nDesde El Reino de Khaos hasta El Monte Desdio se escucha")
	print("la leyenda de que una gran bestia guarda el tesoro mas")
	print("deseado por los Gnomos de Qwiuro en Deze's Castle.")
	print("\nEste objeto es capaz de cumplir cualquier deseo que se le")
	print("pida. Y tu, que tienes ganas de sentir el poder de la aventura")
	print("decides emprender viaje hacia")

	oEntry = input("\n¿Te atreves a entrar?( si | no)\n")

	if oEntry.lower() == "si":
		room1()
	elif oEntry.lower() == "no":
		exit()
	else:
		print("\" ", oEntry, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		entry()

def room1():
	print("¡Comencemos esta aventura!")
	print("Nada mas entrar en el castillo, las puertas se cierran")
	print("y por mucho que intentas comprobar si la puerta se abre")
	print("corroboras que esta cerrada a cal y canto. Quizas una llave")
	print("pueda abrirla pero tampoco te importa mucho por que lo unico")
	print("que esperas es que puedas obtener el gran tesoro.")
	print("Pones tu mirada en la salita y ves que tienes dos puertas.")
	print(" - Hacia el OESTE hay una puerta AZUL.")
	print(" - Hacia el ESTE hay una puerta ROJA.")


	oRoom1 = input("\n¿Hacia que direccion quieres ir?\n")

	if oRoom1.lower() == "este":
		room3()
	elif oRoom1.lower() == "oeste":
		room2()
	else:
		print("\" ", oRoom1, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		room1()

def room2():
	print("Abres la puerta y te introduces en ella")
	fight()
	print("Pones tu mirada en la salita y ves hay una puerta.")
	print(" - La puerta del NORTE es de color AMARILLA.")
	oRoom2 = input("\n¿Hacia que direccion quieres ir?\n")

	if oRoom2.lower() == "norte":
		room5()
	else:
		print("\" ", oRoom2, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		room2()

def room3():
	print("Abres la puerta y te introduces en ella")
	fight()
	print("Pones tu mirada en la salita y ves hay dos puertas.")
	print(" - La puerta del NORTE es de color AMARILLA.")
	print(" - La puerta del ESTE es de color AMARILLA.")
	oRoom3 = input("\n¿Hacia que direccion quieres ir?\n")

	if oRoom3.lower() == "norte":
		room7()
	elif oRoom3.lower() == "este":
		room4()
	else:
		print("\" ", oRoom3, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		room3()

def room4():
	print("Abres la puerta y te introduces en ella")
	treasure()
	print("Pones tu mirada en la salita y ves hay dos puertas.")
	print(" - La puerta del NORTE es de color .")
	oRoom4 = input("\n¿Hacia que direccion quieres ir?\n")

	if oRoom4.lower() == "norte":
		room8()
	else:
		print("\" ", oRoom4, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		room4()

def room5():
	print("Abres la puerta y te introduces en ella")
	treasure()
	print("Pones tu mirada en la salita y ves que hay dos puertas.")
	print(" - La puerta del NORTE es de color VERDE.")
	oRoom5 = input("\n¿Hacia que direccion quieres ir?\n")
	if oRoom5.lower() == "norte":
		room9()
	else:
		print("\" ", oRoom5, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		room5()

def room6():
	print("Abres la puerta y te introduces en ella")
	shop()
	print("Pones tu mirada en la salita y ves una puerta.")
	print(" - La puerta del NORTE es de color NEGRO.")
	oRoom6 = input("\n¿Hacia que direccion quieres ir?\n")
	if oRoom6.lower() == "norte":
		room10()
	else:
		print("\" ", oRoom6, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		room6()

def room7():
	print("Abres la puerta y te introduces en ella")
	treasure()
	print("Pones tu mirada en la salita y ves dos puerta.")
	print(" - La puerta del OESTE es de color VERDE.")
	print(" - La puerta del NORTE es de color VERDE.")
	oRoom7 = input("\n¿Hacia que direccion quieres ir?( oeste | norte )\n")
	if oRoom7.lower() == "norte":
		room10()
	elif oRoom7.lower() == "oeste":
		room6()
	else:
		print("\" ", oRoom7, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		room7()

def room8():
	print("Abres la puerta y te introduces en ella.")
	fight()
	print("Pones tu mirada en la salita y ves una puerta.")
	print(" - La puerta del NORTE es de color VERDE.")
	oRoom8 = input("\n¿Hacia que direccion quieres ir?\n")
	if oRoom8.lower() == "norte":
		room10()
	else:
		print("\" ", oRoom8, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		room8()

def room9():
	print("Abres la puerta y te introduces en ella.")
	shop()
	wichCry()
	print("Pones tu mirada en la salita y ves una puerta.")
	print(" - La puerta del OESTE es de color NEGRO.")
	oRoom9 = input("\n¿Hacia que direccion quieres ir?\n")
	if oRoom9.lower() == "oeste":
		roomBoss()
	else:
		print("\" ", oRoom9, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		room9()

def room10():
	print("Abres la puerta y te introduces en ella.")
	shop()
	wichCry()
	print("Pones tu mirada en la salita y ves una puerta.")
	print(" - La puerta del OESTE es de color NEGRO.")
	oRoom10 = input("\n¿Hacia que direccion quieres ir?\n")
	if oRoom10.lower() == "oeste":
		roomBoss()
	else:
		print("\" ", oRoom10, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		room10()

def roomBoss():
	print("Abres la puerta y te introduces en ella.")
	print("Todo se ve oscuro pero en seguida ves unas llamas...")
	print("que salen... de la boca de un... ¡DRAGON!")
	print("La leyenda era cierta. Detras del dragon se veia un")
	print("cofre que brilla mas que cualquier supernova en plena")
	print("juventud.")
	drawFinalBoss()
	fightFinalBoss()
	print("Con el dragon derrotado ves que el cofre ya no esta y")
	print("que en su lugar hay un hombre con tunica negra que no")
	print("te quita la vista de encima.")
	print("Esta levantando el brazo... sostiene algo que brilla")
	print("demasiado pero no sabes muy bien lo que es.")
	print("Acabas cegado y pierdes el conocimiento.")
	end()





def treasure():
	money = random.randint(2, 6)
	print("Encontraste un cofre.")
	treasure = input("\n¿Quieres abrirlo?(si | no)\n")
	if treasure.lower() == "si" :
		player["money"] += money
		print("¡Obtuviste", money, "monedas!")
		return
	elif treasure.lower == "no" :
		print("Decides pasar del cofre.")
		print("Ahora el cofre se siente solo.")
		return
	else:
		print("\" ", treasure, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		treasure()

def roomEmpty():
	print("Esta sala esta vacia.")
	return

def shop():
	print("--------------------------------")
	print("-      -                -      -")
	print("-     -                  -     -")
	print("-   ------------------------   -")
	print("-     -                  -     -")
	print("-     -   ---      ---   -     -")
	print("-     -                  -     -")
	print("-     -      ------      -     -")
	print("-   -- --              -- --   -")
	print("-  -     ---       ---      -  -")
	print("-           -------            -")
	print("-                              -")
	print("--------------------------------")
	print("Aparecio una bruja que decide venderte sus productos.")
	oShop = input("¿Quieres comprar algo?( si | no)\n")
	if oShop.lower() == "si":
		object()
	elif oShop.lower() == "no":
		wichCry()
	else:
		print("\" ", oShop, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		shop()

def wichCry():
	print("--------------------------------")
	print("-      -                -      -")
	print("-     -                  -     -")
	print("-   ------------------------   -")
	print("-     -                  -     -")
	print("-     -   ---      ---   -     -")
	print("-     -   | |      | |   -     -")
	print("-     -   | |------| |   -     -")
	print("-   -- -- | |      | | -- --   -")
	print("-  -     ---       ---      -  -")
	print("-           -------            -")
	print("-                              -")
	print("--------------------------------")
	print("Eras la única persona que esta brujita vio en meses")
	print("y llora por la alegria de verte. Te desea un buen")
	print("viaje.")

def object():
	print("---------- OBJETOS -----------")
	print("-                            -")
	print("-  5$ Pocion     +10 Vida en -")
	print("-                    combate -")
	print("-  10$ Espada    +10 Fuerza  -")
	print("-  10$ Armadura  +10 Vida    -")
	print("-                            -")
	print("------------------------------")
	print("Tienes", player["money"], "$.")
	oObject = input("¿Que quieres comprar?( Pocion | Espada | Armadura | Salir)\n")
	if oObject.lower() == "pocion":
		if player["money"] >= 5:
			player["money"] -= 5
			player["potion"] += 1
			print("Compraste una pocion.")
			print("Tienes", player["potion"], ".")
			print("La guardas para usarla en algun combate dificil.")
			object()
		else:
			print("No tienes dinero suficiente.")
			object()
	elif oObject.lower() == "espada":
		if player["money"] >= 10:
			player["money"] -= 10
			print("Compraste una espada.")
			player["strong"] += 10
			print("La equipas y ahora tienes", player["strong"], "de fuerza.")
			object()
		else:
			print("No tienes dinero suficiente.")
			object()
	elif oObject.lower() == "armadura":
		if player["money"] >= 10:
			player["money"] -= 10
			print("Compraste una armadura.")
			player["life"] += 10
			print("La equipas y ahora tienes", player["life"], "de vida.")
			object()
		else:
			print("No tienes dinero suficiente.")
			object()
	elif oObject.lower() == "salir":
		return
	else:
		print("\" ", oObject, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		object()

enemy1 = {"life": 5,"strong": 15, "money": 5}
def fight():
	print("¡Una bestia salvaje aparecio!")
	print("------------------------------")
	print("-                            -")
	print("-           -------          -")
	print("-        ---       ---       -")
	print("-     ---             ---    -")
	print("-     -    --     --    -    -")
	print("- ----                  ---- -")
	print("-     -      -----      -    -")
	print("-     ---             ---    -")
	print("-        ---       ---       -")
	print("-           -------          -")
	print("-                            -")
	print("-----------OPCIONES-----------")
	print("-                            -")
	print("-  atacar | convencer | huir  ")
	print("-                            -")
	print("------------------------------")
	status()
	oEnemy1 = input("\n¿Que quieres hacer?\n")
	if oEnemy1.lower() == "atacar":
		porcentaje = random.randint(1,10)
		if porcentaje <= 8:
			print("Vas con todo tu poder hacia la criatura.")
			enemy1["life"] -= player["strong"]
			if enemy1["life"] <= 0:
				player["money"] += enemy1["money"]
				print("¡Venciste!")
				print("Ganas", enemy1["money"], "de oro.")
				print("Ahora tienes", player["money"])
				status()
				enemy1["life"] = 5
				return
			elif enemy1["life"] >= 1: 
				print("La bestia solo queria jugar contigo...")
				print("Nada mas ver como la haces sufrir huye.")
			return
		else: 
			print("Vas con todo tu poder hacia la criatura.")
			print("Pero fallas... y ademas te ataca.")
			damage = random.randint(1, enemy1["strong"])
			print("Te quita", damage,"puntos de vida.")
			player["life"] -=  damage
			if player["life"] >= 1:
				print("Ahota tienes", player["life"], "puntos de vida")
				fight()
			elif player["life"] <= 0:
				print("Ahota tienes", player["life"], "puntos de vida")
				death()
	elif oEnemy1.lower() == "convencer":
		porcentaje = random.randint(1,10)
		if porcentaje <= 7:
			print("Convences a la criatura para que te deje pasar.")
			return
		else: 
			print("No eres capaz de convencerle y te ataca.")
			damage = random.randint(1, enemy1["strong"])
			print("Te quita", damage,"puntos de vida.")
			player["life"] -=  damage
			if player["life"] >= 1:
				print("Ahota tienes", player["life"], "puntos de vida")
				fight()
			elif player["life"] <= 0:
				print("Ahota tienes", player["life"], "puntos de vida")
				death()
	elif oEnemy1.lower() == "huir":
		porcentaje = random.randint(1,10)
		if porcentaje <= 5:
			print("Huir es de gallinas. Pero eres capaz de hacerlo.")
			return
		else: 
			print("No eres capaz de huir y te ataca.")
			damage = random.randint(1, enemy1["strong"])
			print("Te quita", damage,"puntos de vida.")
			player["life"] -=  damage
			if player["life"] >= 1:
				print("Ahota tienes", player["life"], "puntos de vida")
				fight()
			elif player["life"] <= 0:
				print("Ahota tienes", player["life"], "puntos de vida")
				death()
	else:
		print("\" ", oEnemy1, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		fight()

dragon = {"life": 100, "strong": 50}
def drawFinalBoss():
	print("@@@@@@@@@@@@@@@@@@@@@**^^\"\"~~~\"^@@^*@*@@**@@@@@@@@@")
	print("@@@@@@@@@@@@@*^^'\"~   , - ' '; ,@@b. '  -e@@@@@@@@@")
	print("@@@@@@@@*^\"~      . '     . ' ,@@@@(  e@*@@@@@@@@@@")
	print("@@@@@^~         .       .   ' @@@@@@, ~^@@@@@@@@@@@")
	print("@@@~ ,e**@@*e,  ,e**e, .    ' '@@@@@@e,  \"*@@@@@'^@")
	print("@',e@@@@@@@@@@ e@@@@@@       ' '*@@@@@@    @@@'   0")
	print("@@@@@@@@@@@@@@@@@@@@@',e,     ;  ~^*^'    ;^~   ' 0")
	print("@@@@@@@@@@@@@@@^\"\"^@@e@@@   .'           ,'   .'  @")
	print("@@@@@@@@@@@@@@'    '@@@@@ '         ,  ,e'  .    ;@")
	print("@@@@@@@@@@@@@' ,&&,  ^@*'     ,  .  i^\"@e, ,e@e  @@")
	print("@@@@@@@@@@@@' ,@@@@,          ;  ,& !,,@@@e@@@@ e@@")
	print("@@@@@,~*@@*' ,@@@@@@e,   ',   e^~^@,   ~'@@@@@@,@@@")
	print("@@@@@@, ~\" ,e@@@@@@@@@*e*@*  ,@e  @@\"\"@e,,@@@@@@@@@")
	print("@@@@@@@@ee@@@@@@@@@@@@@@@\" ,e@' ,e@' e@@@@@@@@@@@@@")
	print("@@@@@@@@@@@@@@@@@@@@@@@@\" ,@\" ,e@@e,,@@@@@@@@@@@@@@")
	print("@@@@@@@@@@@@@@@@@@@@@@@~ ,@@@,,0@@@@@@@@@@@@@@@@@@@")
	print("@@@@@@@@@@@@@@@@@@@@@@@@,,@@@@@@@@@@@@@@@@@@@@@@@@@")
	print("\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"")
	print("---------https://www.pinterest.es/mlrp1_98/--------")

def fightFinalBoss():
	print("----------------------OPCIONES---------------------")
	print("-                                                 -")
	print("-      atacar | ocultar | convencer | mochila     -")
	print("-                                                 -")
	print("---------------------------------------------------")
	oFinalBoss = input("\n¿Que quieres hacer?\n")
	if oFinalBoss.lower() == "atacar":
		porcentaje = random.randint(1,10)
		if porcentaje <= 8:
			print("Vas con todo tu poder hacia la criatura.")
			dragon["life"] -= player["strong"]
			if dragon["life"] <= 0:
				print("¡Venciste!")
				return
			elif dragon["life"] >= 1:
				print("El dragon esta a", dragon["life"], "puntos de vida.")
				fightFinalBoss()
		else: 
			print("Vas con todo tu poder hacia la criatura.")
			print("Pero fallas... y ademas te ataca.")
			damage = random.randint(1, dragon["strong"])
			print("Te quita", damage,"puntos de vida.")
			player["life"] -=  damage
			if player["life"] >= 1:
				print("Ahota tienes", player["life"], "puntos de vida")
				fightFinalBoss()
			elif player["life"] <= 0:
				print("Ahota tienes", player["life"], "puntos de vida")
				death()
	elif oFinalBoss.lower() == "ocultar":
		print("Te ocultas consiguiendo asi evitar el ataque.")
	elif oFinalBoss.lower() == "convencer":
		print("Este dragon no tiene pinta de querer dialogar.")
		fightFinalBoss()
	elif oFinalBoss.lower() == "mochila":
		bag()
		fightFinalBoss()
	else:
		print("\" ", oFinalBoss, "\" no es una opcion valida.")
		print("Por favor seleccione una opcion valida.")
		fightFinalBoss()
		
def bag():
	if player["potion"] <= 0:
		print("Tu mochilla esta vacia.")
	else:
		print("Miras a ver cuantas pociones tienes.")
		print("Tienes", player["potion"], ".")
		oPotion = input("¿Quieres usar una?( si | no)\n")
		if oPotion == "si":
			player["life"] += 10
			print("Te tomas la pocion. No te hace mas fuerte pero te sana un poco de vida.")
		elif oPotion == "no":
			return
		else:
			print("\" ", oPotion, "\" no es una opcion valida.")
			print("Por favor seleccione una opcion valida.")
			bag()

def status():
	print("---------- TU ESTADO -------------")
	print("-                               -")
	print("-  Vida:", player["life"],"  Daño:", player["strong"],"  Oro:", player["money"], " -")
	print("-                               -")
	print("---------------------------------")
	return

def death():
	print("-------------------------------------------------------")
	print("-                                                     -")
	print("-                                                     -")
	print("-                      GAME OVER                      -")
	print("-                                                     -")
	print("-                                                     -")
	print("-------------------------------------------------------")
	exit()

def end():
	print("-------------------------------------------------------")
	print("-                                                     -")
	print("-                                                     -")
	print("-                       THE END                       -")
	print("-                                                     -")
	print("-                                                     -")
	print("-------------------------------------------------------")
	exit()

entry()