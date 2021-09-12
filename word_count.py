def count_words(frase):
    s = frase.lower()
    parole_contate = {}
    listaParole = [carattere.strip("'") for carattere in s.split()]
    for parola in set(listaParole):
        parole_contate.setdefault(parola, listaParole.count(parola)) #count conta quante volte è presente la parola nella lista, se trova una parola aumenta di uno il count
    return parole_contate

frase = "ciao mi chiamo gino ciao ciao"
print(count_words(frase))