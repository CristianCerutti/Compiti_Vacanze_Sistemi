def multipli(n, fattori):
    ris = []
    for x in range(1, n):
        for fattore in fattori:
            if fattore != 0 and x % fattore == 0:
                ris.append(x)
    print(ris)
    return

def main():
    multipli(30, [2, 5])

if __name__ == "__main__":
    main()