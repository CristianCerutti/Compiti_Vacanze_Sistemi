def main():
    string = input("inserire un nome: ")
    if(string == ""):
        print("One for you, one for me")
    else:
        print("one for " + string + ", one for me")

if __name__ == "__main__":
    main()