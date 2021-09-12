def isograms(parola):
    parolaBase= parola.lower()
    lettereLette = []
    isIsogram = "e' un isogramma"
    for lettera in parolaBase:
            if lettera in lettereLette and lettera != " ":
                isIsogram = "non e' un isogramma"
            lettereLette.append(lettera)
    return(isIsogram)

def main():
    parola = input("inserire una frase o parola: ")
    print(isograms(parola))

if __name__ == "__main__":
    main()