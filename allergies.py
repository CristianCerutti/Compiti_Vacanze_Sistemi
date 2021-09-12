def num_allergie(punteggio):
    ListaAllergie = {1: 'eggs', 2: 'peanuts', 4: 'shellfish',8: 'strawberries',16: 'tomatoes',32: 'chocolate',64: 'pollen', 128: 'cats'}
    allergie = []
    for e in num_allergie:
        if punteggio == e:
            allergie[e] = ListaAllergie[e]
    return allergie