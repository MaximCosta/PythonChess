from math import sqrt

def FouMoveVerif(zx, zy, x, y, nx, ny, plate, piece, pieceAdv):
    if zx < 0:
        tx = -1
    elif zx > 0:
        tx = 1
    if zy < 0:
        ty = -1
    elif zy > 0:
        ty = 1
    F = [(x + zx, y + zy, zy**2 == zx**2, plate[-y - ty][x - tx] == "#", not plate[-y - ty][x - tx] in pieceAdv or x + tx == nx and y + ty == ny)]
    for i in range(1, max(int(sqrt(zx**2)), int(sqrt(zy**2)))):
                
        if F[0] == (nx, ny, True, True, True):
            x += tx
            y += ty
            zy = ny - y
            zx = nx - x
        else:
            return False

def TourMoveVerif(zx, zy, x, y, nx, ny, plate, piece, pieceAdv, outEquation):
    if zx < 0:
        tx = -1
    elif zx > 0:
        tx = 1
    elif zx == 0:
        tx = 0
        
    if zy < 0:
        ty = -1
    elif zy == 0:
        ty = 0
    elif zy > 0:
        ty = 1
        
    T = [(y + zy, x, plate[-y - ty][x + tx] == "#", not plate[-y - ty][x - tx] in pieceAdv or x + tx == nx and y + ty == ny),
         (y, x + zx, plate[-y - ty][x + tx] == "#", not plate[-y - ty][x - tx] in pieceAdv or x + tx == nx and y + ty == ny)]
    for i in range(1, max(int(sqrt(zx**2)), int(sqrt(zy**2)))):
       
        if T[outEquation] == (nx, ny, True, True):
            x += tx
            y += ty
            zy = ny - y
            zx = nx - x              
        else:
            return False

def DameMoveVerif(zx, zy, x, y, nx, ny, plate, piece, pieceAdv, outEquation):
    if zx < 0:
        tx = -1
    elif zx > 0:
        tx = 1
    elif zx == 0:
        tx = 0
        
    if zy < 0:
        ty = -1
    elif zy == 0:
        ty = 0
    elif zy > 0:
        ty = 1
        
    D = [(x + zx, y + zy, zy**2 == zx**2, plate[-y - ty][x + tx] == "#", not plate[-y - ty][x - tx] in pieceAdv or x + tx == nx and y + ty == ny),
         (y + zy, x, True, plate[-y - ty][x + tx] == "#", not plate[-y - ty][x - tx] in pieceAdv or x + tx == nx and y + ty == ny),
         (y, x + zx, True, plate[-y - ty][x + tx] == "#", not plate[-y - ty][x - tx] in pieceAdv or x + tx == nx and y + ty == ny)]
    for i in range(1, max(int(sqrt(zx**2)), int(sqrt(zy**2)))):
              
        if D[outEquation] == (nx, ny, True, True, True):
            x += tx
            y += ty
            zy = ny - y
            zx = nx - x              
        else:
            return False
