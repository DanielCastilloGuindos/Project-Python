# Python 2.7

import pygame
from pygame.locals import * # importar para poder usar QUIT, keyUp, ...
import sys
import random
import time

pygame.init() # Para inicializar
fpsClock = pygame.time.Clock() # Para inicializar un reloj


sWidth = 1200
sHeight = 600
surface = pygame.display.set_mode((sWidth, sHeight)) # Para crear la ventana / superficie

azul_png = {"draw": pygame.image.load("./imagenes/azul.png"), "width": 600, "height": 600}

rosa_png = {"draw": pygame.image.load("./imagenes/rosa.png"), "width": 600, "height": 600}

linea_png = {"draw": pygame.image.load("./imagenes/linea.png"), "width": 5, "height": 600}

round_png = {"draw": pygame.image.load("./imagenes/round.png"), "width": 86, "height": 86}


piedra_png = {"draw": pygame.image.load("./imagenes/piedra.png"), "width": 86, "height": 86}

papel_png = {"draw": pygame.image.load("./imagenes/papel.png"), "width": 86, "height": 86}

tijera_png = {"draw": pygame.image.load("./imagenes/tijera.png"), "width": 86, "height": 86}




global oValueEnemy
oValueEnemy = 0
global aleatorio
aleatorio = 0
def numeroAleatorio():
	global aleatorio
	aleatorio = random.randint(1, 3)
	if aleatorio == 1:
		oValueEnemy = "piedra"
	elif aleatorio == 2:
		oValueEnemy = "papel"
	elif aleatorio == 3:
		oValueEnemy = "tijera"

def enemyPlay():
	if aleatorio == 1:
		oValueEnemy = "piedra"
		enemy_rect = surface.blit(piedra_png["draw"], (sWidth * 3/4 - piedra_png["width"]/1.95, sHeight/2 - piedra_png["height"] / 2))
	elif aleatorio == 2:
		oValueEnemy = "papel"
		enemy_rect = surface.blit(papel_png["draw"], (sWidth * 3/4 - papel_png["width"]/1.95, sHeight/2 - papel_png["height"] / 2))
	elif aleatorio == 3:
		oValueEnemy = "tijera"
		enemy_rect = surface.blit(tijera_png["draw"], (sWidth * 3/4 - tijera_png["width"]/1.95, sHeight/2 - tijera_png["height"] / 2))
	else:
		pygame.draw.circle(surface, (255, 255, 255), (898, 300), 43, 0)

global resultado
resultado = {"e": 0, "d": 0, "v": 0}

def comprobar():
	if oValueEnemy == "piedra":
		if oValuePlayer == "piedra":
			print "Empate"
			resultado["e"] += 1
		elif oValuePlayer == "papel":
			print "Derrota"
			resultado["d"] += 1
		elif oValuePlayer == "tijera":
			print "Victoria"
			resultado["v"] += 1
	elif oValueEnemy == "papel":
		if oValuePlayer == "piedra":
			print "Victoria"
			resultado["v"] += 1
		elif oValuePlayer == "papel":
			print "Empate"
			resultado["e"] += 1
		elif oValuePlayer == "tijera":
			print "Derrota"
			resultado["d"] += 1
	elif oValueEnemy == "tijera":
		if oValuePlayer == "piedra":
			print "Derrota"
			resultado["d"] += 1
		elif oValuePlayer == "papel":
			print "Victoria"
			resultado["v"] += 1
		elif oValuePlayer == "tijera":
			print "Empate"
			resultado["e"] += 1

def mostrar():
	if resultado["e"] >= resultado["v"] and resultado["e"] >= resultado["d"] :
		drawE()
	elif resultado["v"] >= resultado["d"] and resultado["v"] >= resultado["e"] :
		victory()
	elif resultado["d"] >= resultado["v"] and resultado["d"] >= resultado["e"] :
		defeat()

def victory():
	victory = {"draw": pygame.image.load("./imagenes/victory.png"), "width": 600, "height": 200}
	victory_rect = surface.blit(victory["draw"], (sWidth / 2 - victory["width"]/2, sHeight/2 - victory["height"] / 2))

def defeat():
	defeat = {"draw": pygame.image.load("./imagenes/defeat.png"), "width": 600, "height": 200}
	defeat_rect = surface.blit(defeat["draw"], (sWidth / 2 - defeat["width"]/2, sHeight/2 - defeat["height"] / 2))

def drawE():
	draw = {"draw": pygame.image.load("./imagenes/draw.png"), "width": 600, "height": 200}
	draw_rect = surface.blit(draw["draw"], (sWidth / 2 - draw["width"]/2, sHeight/2 - draw["height"] / 2))



pygame.font.init() # Para iniciar las fuentes
font = pygame.font.SysFont("Comic Sans MS", 32)
rCount = 3
while rCount > 0:
	# Por cada event en pygame.event.get()
	if rCount == 3:
		num = font.render("3", True, (0, 0, 0))
	elif rCount == 2:
		num = font.render("2", True, (0, 0, 0))
	elif rCount == 1:
		num = font.render("1", True, (0, 0, 0))
	elif rCount == 0:
		num = font.render("0", True, (0, 0, 0))
	surface.blit(rosa_png["draw"], (0, 0)) # coje la imagen rosa y lo pone en la pantalla
	surface.blit(azul_png["draw"], (sWidth/2, 0)) # coje la imagen azul y lo pone en la pantalla
	surface.blit(linea_png["draw"], (sWidth/2 - linea_png["width"] / 2, 0)) # coje la imagen linea y lo pone en la pantalla

	surface.blit(round_png["draw"], (sWidth/2 - round_png["width"]/2, 50 - round_png["height"] / 2)) # coje la imagen round y lo pone en la pantalla
	surface.blit(num, (sWidth/2 - 16 / 2,  85 - round_png["height"] / 2)) # coje el numero y lo pone en la pantalla

	piedra_rect = surface.blit(piedra_png["draw"], (sWidth/4 - piedra_png["width"] - piedra_png["width"]/1.8, sHeight/2 - piedra_png["height"] / 2)) # coje un elemento y lo pone en la pantalla
	papel_rect = surface.blit(papel_png["draw"], (sWidth/4 - papel_png["width"]/1.95, sHeight/2 - papel_png["height"] / 2)) # coje un elemento y lo pone en la pantalla
	tijera_rect = surface.blit(tijera_png["draw"], (sWidth/4 + tijera_png["width"]  / 2, sHeight/2 - tijera_png["height"] / 2)) # coje un elemento y lo pone en la pantalla
		
	enemyPlay()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x, y = event.pos
			print x, y
			if piedra_rect.collidepoint(x, y):
				oValuePlayer = "piedra"
				print "Player:", oValuePlayer
				numeroAleatorio()
				print "Enemy:", oValueEnemy
				comprobar()
				rCount -= 1
			elif papel_rect.collidepoint(x, y):
				oValuePlayer = "papel"
				print "Player:", oValuePlayer
				numeroAleatorio()
				print "Enemy:", oValueEnemy
				comprobar()
				rCount -= 1
			elif tijera_rect.collidepoint(x, y):
				oValuePlayer = "tijera"
				print "Player:", oValuePlayer
				numeroAleatorio()
				print "Enemy:", oValueEnemy
				comprobar()
				rCount -= 1
			else:
				oValuePlayer = ""
				print "Por favor, selecciona una de las opciones permitidas."
			print rCount

	pygame.display.update()
	fpsClock.tick(30) # Hacemos que se refresce 30 veces por segundo

while True:
	surface.fill((251, 94, 140))
	mostrar()
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(30) # Hacemos que se refresce 30 veces por segundo