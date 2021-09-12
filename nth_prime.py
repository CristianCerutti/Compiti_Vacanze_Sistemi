def nPrimo(num):
    primi = [2]
    cont = 3
    while len(primi) < num:
        for n in primi:
            if cont % n == 0:
                break
            elif n * n > cont :
                primi.append(cont)
        cont = cont + 2
    return primi[-1]

def main():
    print(nPrimo(7))

if __name__ == "__main__":
    main()