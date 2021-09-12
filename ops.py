def _append(n1, n2):
    return n1 + n2

def _lenght(lista):
    cont = 0
    for x in lista:
        cont += 1
    return cont

def _reverse(lista):
    lista2 = []
    for x in range(lista-1, -1, -1):
        lista2 += lista[x]
    return lista2

def _foldr(op, n1, n2):
    if op == "add" or op == "dif":
        ris = n1+n2
    elif op == "div":
        ris = n1/n2
    elif op == "mol":
        ris = n1*n2
    else: 
        ris = "error"

    return ris

def _map_clone(op, lista):
    lista2 = []
    for x in lista:
        lista2 +=[op(x)]
    return lista2
