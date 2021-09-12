def verifier(isbn):
    isbn.replace("-","")
    contMol = 10
    ris = 0
    for _ in range(10):
        numeroMol = int(isbn) % 10
        isbn = int(isbn) // 10
        ris += contMol * numeroMol
        contMol -= 1
    print(ris)
    if ris%11 == 0:
        print("isbn valido")
    else:
        print("isbn non valido")

def main():
    isbn = input("Inserire un isbn-10: ")
    verifier(isbn)

if __name__ == "__main__":
    main()