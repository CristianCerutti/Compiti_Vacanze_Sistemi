def perfect_number(num):
    somma = 0
    for n in range(1, num):
        if num % n == 0:
            somma = somma +n

    if num == somma:
        ris = True
    else: 
        ris = False

    return ris