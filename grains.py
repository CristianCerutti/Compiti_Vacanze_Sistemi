def contatore(num):
    if num > 64 and num < 0:
        print("numero non valido")
    else:
        cont = 1
        ris = 0
        for _ in range (64):
            ris += num ** cont
            cont += 1
        print(ris)
    return

def main():
    numero = int(input("Inserire un numero da 1 a 64: "))
    contatore(numero)

if __name__ == "__main__":
    main()