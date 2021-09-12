def tringle_type(l1, l2, l3):
    type = ""
    if l1 + l2 <= l3 or l2 + l3 <= l1 or l1 + l3 <= l2 or l1 < 0 or l2 < 0 or l3 < 0:
        print("i lati del triangolo non sono validi")
    else:
        type = "isocele"
        if l1 != l2 and l1 != l3:
            type = "scaleno"
        elif l1 == l2 and l1 == l3:
            type = "equilatero"
    return type

def main():
    print(tringle_type(0, 2, 7))

if __name__ == "__main__":
    main()
    