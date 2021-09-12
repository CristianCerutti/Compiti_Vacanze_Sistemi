def main():
    number = int(input("inserire un numero: "))
    string = str(number)
    if (number % 3 != 0 and number % 5 != 0 and number % 7 != 0):
        pass
    else:
        string = ""
        if (number % 3 == 0):
            string += "Pling"
        if (number % 5 == 0):
            string += "Plang"
        if (number % 7 == 0):
            string += "Plong"
    print(string)

if __name__ == "__main__":
    main()