def bob(frase):
    frase = frase.replace(" ", "")  
    frase_out = "Whatever"
    if frase.isupper():
        if frase[-1] == "?":
            frase_out = "calm down, I know what I'm doing!"
        else: 
            frase_out = "whoa, chill out"
    elif frase == "":
        frase_out = "Fine, be that way!"
    elif frase[-1] == "?":
        frase_out = "sure"
    return frase_out

def main():
    print(bob("AO?"))
    
if __name__ == "__main__":
    main()