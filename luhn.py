def luhn_algorithm(number):
    number.replace(" ", "")
    lista = []
    for x in number:
        lista.append(x)
    if len(lista) != 15:
        print("codice inserito non valido")
        pass
    cont1 = 1
    cont2 = 0
    for num in lista:
        num = int(num)
        if cont1 % 2 == 0:
            num = num * 2
            if num > 9:
                num -= 9
        cont1 +=1
        cont2 +=1
    totale = 0
    for num in lista:
        totale += num
    if totale % 10 == 0:
        print("il numero inserito e' valido")
    else:
        print("il numero inserito non e' valido")

def main():
    numero = input("Inserire un codice: ")
    luhn_algorithm(numero)

if __name__ == "__main__":
    main()
