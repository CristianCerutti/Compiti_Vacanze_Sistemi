def acronym(word):
    acronym = word[0]
    cont = 0
    #word.strip(" ")
    for letter in word:
        print(letter)
        if letter == " ":
            acronym += word[cont+1]
        cont += 1
    return acronym

def main():
    word = input("inserisci una parola: ")
    print(acronym(word))

if __name__ == "__main__":
    main()