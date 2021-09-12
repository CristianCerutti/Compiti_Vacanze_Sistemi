def highScores(lista):
    p1max = -1
    p2max = -1
    p3max = -1
    for n in lista:
        lastPoint = n
        if n > p1max:
            p2max = p1max
            p1max = n
        elif n > p2max:
            p3max = p2max
            p2max = n
        elif n > p3max:
            p3max = n
    return "il punteggio massimo ottenuto è: " + p1max + ", i tre punteggi migliori sono: "+ p1max + ", " + p2max + ", " + p3max + ", mentre l'ultimo punteggio aggiunto è " +lastPoint
    
    