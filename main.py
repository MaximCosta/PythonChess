
import pygame
from pygame.locals import *

pygame.init()

# Ouverture de la fenétre Pygame
fenetre = pygame.display.set_mode((240, 240))

#Chargement et collage du fond
fond = pygame.image.load("img/background.png").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("img/black_pawn.png").convert_alpha()
fenetre.blit(perso, (30, 30))
taille_sprite = 30
plate = [["T", "C", "F", "D", "R", "F", "C", "T"],
         ["P", "P", "P", "P", "P", "P", "P", "P"],
         ["#", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#"],
         ["#", "#", "#", "#", "#", "#", "#", "#"],
         ["p", "p", "p", "p", "p", "p", "p", "p"],
         ["t", "c", "f", "d", "r", "f", "c", "t"]]

def afficher(plate, fenetre):
    num_ligne = 0
    for ligne in plate:
        num_case = 0
        for sprite in ligne:
            x = num_case * taille_sprite
            y = num_ligne * taille_sprite
            if sprite == 'P':
                fenetre.blit(perso, (x, y))
            num_case += 1
        num_ligne +=1
afficher(plate, fenetre)
# Rafraichissement de l'écran
pygame.display.flip()


#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0