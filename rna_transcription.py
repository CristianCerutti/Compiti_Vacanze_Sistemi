def traduzione(dna):
    rna = ""
    for x in dna:
        if x == "g" or x == "G":
            rna += "C"
        elif x == "c" or x == "C":
            rna += "G"
        elif x == "t" or x == "T":
            rna += "A"
        elif x == "a" or x == "A":
            rna += "U"
    return rna