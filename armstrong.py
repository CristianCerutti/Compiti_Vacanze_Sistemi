def armstron_verificator(num):
  numSup = str(num)
  lunghezza = len(numSup)
  cont = 0
  for c in numSup:
    cont += int(c) ** lunghezza
    lunghezza -= 1
    print(cont)
  print(cont == num)
  if cont == num:
    ris = True
  else: 
    ris = False
  return ris

def main():
  num = input("inserire un numero: ")
  print(armstron_verificator(num))

if __name__ == "__main__":
  main()