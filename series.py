def main():
    string = input("inserire una stringa di 5 caratteri: ")
    if len(string) == 5:
        print(string[0:2], string[1:3], string[2:4], string[0:3], string[1:4], string[2:5], string[0:4], string[1:5])

if __name__ == "__main__":
    main()