import os
from os import system, name
from time import sleep
from var import *
from verifpiece import *
from time import sleep
from verifmove import *
#from chess import *

def clear(): 
   os.system('cls' if os.name == 'nt' else 'clear')

def platePrint(plate):
   clear()
   # for i in range(8):
   #  print("|", 8 - i, "||", end=" ")
   #   for v in range(8):
   #      print(plate[i][v], end=" | ")
   #   print("")
   #   if not i == 7:
   #      print("--------------------------------------")
   # print("--------------------------------------")
   #print("| 0 || a | b | c | d | e | f | g | h |")

def PlateUpdate(chesspi, plate, alpha):
   holdPlate = []
   newPlate = []
   holdPlate = list(plate[8 - int(chesspi[0][1])])
   holdPlate[chesspi[0][0]] = "#"
   newPlate = list(plate[8 - int(chesspi[1][1])])
   newPlate[chesspi[1][0]] = chesspi[2]
   plate[8 - int(chesspi[0][1])] = holdPlate
   plate[8 - int(chesspi[1][1])] = newPlate
   platePrint(plate)
   return False

def getMove(turns):
   print("ex: a1,a3,T: move tower a1 to a3")
   if not error("get") == 0:
      print("Error : ", allError)
   print(turns)

def verif(chesspi, piece, pieceAdv, turns):
   chesspi.append(plate[-int(chesspi[0][1])][chesspi[0][0]])
   if not chesspi[2] in piece:
      if chesspi[2] in pieceAdv:
         error('pieceIsNotYour')
      else:
         error('pieceNotExist')
   if not plate[8 - (int(chesspi[0][1]))][chesspi[0][0]] in piece:
      error('pieceIsNotFind',)
   if not 1 <= int(chesspi[1][1]) <= 8 and 1 <= (chesspi[1][0]) <= 8:
      error('localisationNotInPlate')
   if error("get") == 0:
      pieceMove(chesspi, turns)

def error(errors):
   if errors == "get":
      return len(allError)
   elif errors == "clear":
      allError.clear()
   else:
      print(errors)
      allError.append(errors)
   

def pieceMove(chesspi, turns):
   y = int(chesspi[0][1])
   x = chesspi[0][0]
   ny = int(chesspi[1][1])
   nx = chesspi[1][0]
   zy = ny - y
   zx = nx - x
   piMo = chesspi[2]

   try:
      if piMo == "r"or piMo == "R":
         if turns == "Black":
            piece = pieceN
         elif turns == "White":
            piece = pieceB
         Roi(y, x, ny, nx, zy, zx, piece, plate)
   except IndexError:
      error('moveIsImpossible')

   try:
      if piMo == "p"or piMo == "P":
         Pion(turns, y, x, ny, nx, plate, pieceN, pieceB)
   except IndexError:
      error("moveIsImpossible")

   try:
      if piMo == "d"or piMo == "D":
         Dame(y, x, ny, nx, zy, zx)
   except IndexError:
      error('moveIsImpossible')

   try:
      if piMo == "f"or piMo == "F":
         Fou(y, x, ny, nx, zy, zx)
   except IndexError:
      error('moveIsImpossible')
      
   try:
      if piMo == "c"or piMo == "C":
         if turns == "Black":
            piece = pieceN
         elif turns == "White":
            piece = pieceB         
         Cavalier(y, x, ny, nx, plate, piece)
   except IndexError:
      error('moveIsImpossible')

   try:
      if piMo == "t"or piMo == "T":
         Tour(y, x, ny, nx, zy, zx)
   except IndexError:
      error('moveIsImpossible')
        
   if error("get") == 0:
      moveobs(piMo, zx, zy, x, y, nx, ny, plate, pieceB, pieceN, outEquation, chesspi, turns)

def moveobs(piMo, zx, zy, x, y, nx, ny, plate, pieceB, pieceN, outEquation, chesspi, turns):

   erreur = True

   if turns == "Black":
      piece = pieceN
      pieceAdv = pieceB
   elif turns == "White":
      piece = pieceB     
      pieceAdv = pieceN
      
   if piMo == "D" or piMo == "d":
      erreur = DameMoveVerif(zx, zy, x, y, nx, ny, plate, piece, pieceAdv, outEquation)

   if piMo == "T" or piMo == "t":
      erreur = TourMoveVerif(zx, zy, x, y, nx, ny, plate, piece, pieceAdv, outEquation)

   if piMo == "F" or piMo == "f":
      erreur = FouMoveVerif(zx, zy, x, y, nx, ny, plate, piece, pieceAdv)
      print(erreur)
   if erreur == False:
      error('CantMove(obstacle)')
   
   if error("get") == 0:
      PlateUpdate(chesspi, plate, alpha)

