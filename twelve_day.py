regali = dict()

regali[1] = "a Partridge in a Pear Tree"
regali[2] = "two Turtle Doves"
regali[3] = "three French Hens"
regali[4] = "four Calling Birds"
regali[5] = "five Gold Rings"
regali[6] = "six Geese-a-Laying"
regali[7] = "seven Swans-a-Swimming"
regali[8] = "eight Maids-a-Milking"
regali[9] = "nine Ladies Dancing"
regali[10] = "ten Lords-a-Leaping"
regali[11] = "eleven Pipers Piping"
regali[12] = "twelve Drummers Drumming"

giorni = ["zeroth", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

def main():
    testo = []
    cont = 0
    for giorno in range(12):
        if cont != 0:
            frase = f"On the {giorni[giorno]} day of Christmas my true love gave to me: "
            for regalo in range(giorno, 0, -1):  
                if regalo == 1 and giorno > 1:
                    frase = frase + "and "
                else: 
                    frase = frase + ""  
                frase = frase + regali[regalo]
                if regalo == 1:
                    frase = frase + "."
                else: 
                    frase = frase + ", "
            testo.append(frase)
        else:
            cont = cont + 1
    print(testo)

if __name__ == "__main__":
    main()