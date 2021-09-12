def leap_year(anno):
    if anno % 4 == 0:
        if anno % 100 == 0:
            if anno % 400 == 0:
                ris = True
    else: 
        ris = False
    return ris