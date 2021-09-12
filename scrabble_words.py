def scrabble_score(word):
    points = 0
    word.lower()
    for letter in word:
        print(points)
        print(letter)
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter =="u" or letter == "l" or letter == "n" or letter == "r" or letter == "s" or letter == "t":
            points = points + 1
        elif letter == "d" or letter == "g":
            points = points + 2
        elif letter == "b" or letter == "c" or letter == "m" or letter == "p":
            points = points + 3
        elif letter == "f" or letter == "h" or letter == "v" or letter == "w" or letter == "y":
            points = points + 4
        elif letter == "k":
            points = points + 5
        elif letter == "j" or letter == "x":
            points = points + 8
        elif letter == "q" or letter == "z":
            points = points + 10
    return points

def main():
    word = str(input("inserire una parola: "))
    print(scrabble_score(word))

if __name__ == "__main__":
    main()