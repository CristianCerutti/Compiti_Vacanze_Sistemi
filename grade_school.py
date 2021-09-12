grade = [[],[],[]] #1, 2, 3


def grade_school(risposta):
    if risposta == "v" or risposta == "V":
        scelta = input("inserire il grado che si vuole visualizzare: ")
        if scelta == "1":
            print(f"gli studenti di primo grado sono: {grade[0]}")
        elif scelta == "2":
            print(f"gli studenti di secondo grado sono: {grade[1]}")
        elif scelta == "3":
            print(f"gli studenti di secondo grado sono: {grade[2]}")
        else:
            print("inserire un grado valido")
    elif risposta == "i" or risposta == "I":
        nome = input("inserire un nome: ")
        grado = str(input("inserire un grado: "))
        if grado != "1" and grado != "2" and grado != "3":
            print("Inserire un grado valido")
        else:
            if grado == "1":
                grade[0] += "studente " + nome + " di primo grado "
            elif grado == "2":
                grade[1] += "studente " + nome + " di secondo grado "
            elif grado == "3":
                grade[2] += "studente " + nome + " di terzo grado "
    return

def main():
    cont = 0
    risposta = input("inserire 0 per terminare, v per visualizzare, i per inserire: ")
    while risposta != "0" and (risposta == "0" or risposta == "i" or risposta == "v"):
        if cont == 0:
            cont += 1
            grade_school(risposta)
        else: 
            risposta = input("inserire 0 per terminare, v per visualizzare, i per inserire: ")
            grade_school(risposta)

if __name__ == "__main__":
    main()