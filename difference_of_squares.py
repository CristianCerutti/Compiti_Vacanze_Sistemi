def difference(n):
    s1 = 0
    s2 = 0
    for x in range(1, n+1):
        s1 += x
    s1 = s1 ** 2
    for a in range(1, n+1):
        s2 += a ** 2
    difference = s1 - s2
    print(s1, s2)
    return difference

def main():
    n = int(input("inserire un numero: "))
    print(difference(n))

if __name__ == "__main__":
    main()