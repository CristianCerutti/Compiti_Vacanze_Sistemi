def main():
    number = int(input("Inserire un numero: "))
    cont = 0
    while number > 1:
        cont += 1
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        print(number)
    print(f"ci sono voluti {cont} passaggi per arrivare a {number}")
if __name__ == "__main__":
    main()