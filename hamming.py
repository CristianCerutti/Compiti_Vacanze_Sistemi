def hamming(dna1, dna2):
    if len(dna1) != len(dna2):
        return "inserire due dna lunghi uguali"   
    lunghezza = len(dna1)
    errori = 0
    for x in range(lunghezza):
        if dna1[x] != dna2[x]:
            errori = errori+1
    print(f"il numero di errori e' di: {errori}")
    return 

def main():
    dna1 = input("Inserire il primo dna: ")
    dna2 = input("Inserire il secondo dna: ")
    hamming(dna1, dna2)

if __name__ == "__main__":
    main()