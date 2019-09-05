from var import outEquation

def Cavalier(y, x, ny, nx, plate, piece):
    C = [(y + 2, x + 1, not plate[-ny][nx] in piece),
         (y + 2, x - 1, not plate[-ny][nx] in piece),
         (y - 2, x + 1, not plate[-ny][nx] in piece),
         (y - 2, x - 1, not plate[-ny][nx] in piece),
         (y + 1, x + 2, not plate[-ny][nx] in piece),
         (y - 1, x + 2, not plate[-ny][nx] in piece),
         (y + 1, x - 2, not plate[-ny][nx] in piece),
         (y - 1, x - 2, not plate[-ny][nx] in piece)]
    i = 0
    while not C[i] == (ny, nx, True):
        i += 1

def Tour(y, x, ny, nx, zy, zx):
    i = 0
    T = [(y + zy, x),
         (y, x + zx)]
    while not T[i] == (ny, nx):
        i += 1
    outEquation = i

def Fou(y, x, ny, nx, zy, zx):
    i = 0
    F = [(x + zx, y + zy, zy**2 == zx**2)]
    while not F[i] == (nx, ny, True):
        i += 1

def Dame(y, x, ny, nx, zy, zx):
    i = 0
    D = [(y + zy, x + zx, zy**2 == zx**2),
         (y + zy, x, True),
         (y, x + zx, True)]
    while not D[i] == (ny, nx, True):
        i += 1
    outEquation = i

def Roi(y, x, ny, nx, zy, zx, piece, plate):
    i = 0
    R = [(y + zy, x + zx, zy <= 1, zx <= 1, not plate[-ny][nx] in piece),
         (y + zy, x, zy <= 1, zx <= 1, not plate[-ny][nx] in piece),
         (y, x + zx, zy <= 1, zx <= 1, not plate[-ny][nx] in piece)]
    while not R[i] == (ny, nx, True, True, True):
        i += 1
    return R[i]

def Pion(turns, y, x, ny, nx, plate, pieceN, pieceB):
    i = 0
    P = [(turns == "Black", y - 1, x, True, not plate[-ny][nx] in pieceB, not plate[-ny][nx] in pieceN),
          (turns == "Black", y - 2, x, y == 7, not plate[-ny][nx] in pieceB, not plate[-ny][nx] in pieceN),
          (turns == "Black", y - 1, x + 1, True, plate[-ny][nx] in pieceB, True),
          (turns == "Black", y - 1, x - 1, True, plate[-ny][nx] in pieceB, True),

          (turns == "White", y + 1, x, True, not plate[-ny][nx] in pieceB, not plate[-ny][nx] in pieceN),
          (turns == "White", y + 2, x, y == 2, not plate[-ny][nx] in pieceB, not plate[-ny][nx] in pieceN),
          (turns == "White", y + 1, x + 1, True, plate[-ny][nx] in pieceN, True),
          (turns == "White", y + 1, x - 1, True, plate[-ny][nx] in pieceN, True)]
    while not P[i] == (True, ny, nx, True, True, True):
        i += 1
