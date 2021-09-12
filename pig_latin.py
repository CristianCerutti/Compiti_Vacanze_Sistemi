import re
def traduci(parola):
    if re.match('^[xy][^aeiou]', parola):
        return parola + 'ay'
    return re.sub(r'^([^aeiouq]*(?:qu)?)([aeiou])(.*)', r'\2\3\1ay', parola)
def translate(frase):
    return ' '.join([traduci(parola) for parola in frase.split(' ')])

def main():
    print(traduci("hello, I'm a tuna"))

if __name__ == "__main__":
    main()