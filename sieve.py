def lista_primo(limite):
    multipli = set()
    primi = [2]
    for n in range(3, limite+1, 2):
        if not n in multipli:
            primi.append(n)
            multipli.update(range(n**2, limite, n))
    print(primi)
    return primi

def main():
    lista_primo(10)

if __name__ == "__main__":
    main()