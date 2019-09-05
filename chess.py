########################START LIB#########################
import os
from os import system, name
from time import sleep
from verif import *
from var import *
import pygame
from pygame.locals import *



####################Script start######################################
# main()

######################################################################
pygame.init()

# Ouverture de la fenétre Pygame
fenetre = pygame.display.set_mode((240, 240))

#Chargement et collage du fond
fond = pygame.image.load("background.png").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
pawnW = pygame.image.load("white_pawn.png").convert_alpha()
rookW = pygame.image.load("white_rook.png").convert_alpha()
knightW = pygame.image.load("white_knight.png").convert_alpha()
bishopW = pygame.image.load("white_bishop.png").convert_alpha()
queenW = pygame.image.load("white_queen.png").convert_alpha()
kingW = pygame.image.load("white_king.png").convert_alpha()

pawnB = pygame.image.load("black_pawn.png").convert_alpha()
rookB = pygame.image.load("black_rook.png").convert_alpha()
knightB = pygame.image.load("black_knight.png").convert_alpha()
bishopB = pygame.image.load("black_bishop.png").convert_alpha()
queenB = pygame.image.load("black_queen.png").convert_alpha()
kingB = pygame.image.load("black_king.png").convert_alpha()

taille_sprite = 30

def afficher(plate, fenetre):
    num_ligne = 0
    for ligne in plate:
        num_case = 0
        for sprite in ligne:
            x = num_case * taille_sprite
            y = num_ligne * taille_sprite
            if sprite == 'P':
                fenetre.blit(pawnB, (x, y))
            elif sprite == 'T':
                fenetre.blit(rookB, (x, y))
            elif sprite == 'C':
                fenetre.blit(knightB, (x, y))
            elif sprite == 'F':
                fenetre.blit(bishopB, (x, y))
            elif sprite == 'D':
                fenetre.blit(queenB, (x, y))
            elif sprite == 'R':
                fenetre.blit(kingB, (x, y))
            elif sprite == 'p':
                fenetre.blit(pawnW, (x, y))
            elif sprite == 't':
                fenetre.blit(rookW, (x, y))
            elif sprite == 'c':
                fenetre.blit(knightW, (x, y))
            elif sprite == 'f':
                fenetre.blit(bishopW, (x, y))
            elif sprite == 'd':
                fenetre.blit(queenW, (x, y))
            elif sprite == 'r':
                fenetre.blit(kingW, (x, y))
            num_case += 1
        num_ligne +=1
afficher(plate, fenetre)
# Rafraichissement de l'écran
pygame.display.flip()

chessIsRun = 1

# BOUCLE INFINIE
while chessIsRun:
    continuer = 1
    reloop = False
    chessIsRun = True
    turns = "Black"
    while turns == "Black":
        chesspi = []
        platePrint(plate)
        loopget = 0
        continuer = 1
        getMove(turns)
        while continuer:
            for event in pygame.event.get():  # Attente des événements
                if event.type == QUIT:
                    continuer = 0
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and loopget == 0:
                    print((event.pos[0] // 30) + 1, 8 - (event.pos[1] // 30))
                    loopget += 1
                    chesspi.append(((event.pos[0] // 30), 8 - (event.pos[1] // 30)))
                if event.type == MOUSEBUTTONDOWN and event.button == 3 and loopget == 1:
                    print((event.pos[0] // 30) + 1, 8 - (event.pos[1] // 30))
                    chesspi.append(((event.pos[0] // 30), 8 - (event.pos[1] // 30)))
                    print(chesspi)
                    print("move",plate[-int(chesspi[0][1])][chesspi[0][0]],"in",chesspi[0],"to",chesspi[1])
                    continuer = 0
    
        #intp = getMove(turns)
        error("clear")
        verif(chesspi, pieceN, pieceB, turns)
        if error("get") == 0:
            turns = 'White'
        fenetre.blit(fond, (0, 0))
        afficher(plate, fenetre)
        # Rafraichissement de l'écran
        pygame.display.flip()    
    while turns == "White":
        chesspi = []
        platePrint(plate)
        loopget = 0
        continuer = 1
        getMove(turns)
        while continuer:
            for event in pygame.event.get():  # Attente des événements
                if event.type == QUIT:
                    continuer = 0
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and loopget == 0:
                    print((event.pos[0] // 30), 8 - (event.pos[1] // 30))
                    loopget += 1
                    chesspi.append(((event.pos[0] // 30), 8 - (event.pos[1] // 30)))
                if event.type == MOUSEBUTTONDOWN and event.button == 3 and loopget == 1:
                    print((event.pos[0] // 30), 8 - (event.pos[1] // 30))
                    chesspi.append(((event.pos[0] // 30), 8 - (event.pos[1] // 30)))
                    print(chesspi)
                    continuer = 0
        #intp = getMove(turns)
        error("clear")
        verif(chesspi, pieceB, pieceN, turns)
        if error("get") == 0:
            turns = 'Black'
        fenetre.blit(fond, (0, 0))
        afficher(plate, fenetre)
        # Rafraichissement de l'écran
        pygame.display.flip()

