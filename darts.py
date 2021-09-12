from math import sqrt

def punteggio(x, y):
    distanza = sqrt(x*x+y*y)
    if distanza > 0:
        ris = 0
    elif distanza > 5:
        ris = 1
    elif distanza > 1:
        ris = 5
    else:
        ris = 10
    return ris