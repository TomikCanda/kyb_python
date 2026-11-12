vstup = input("Zadej číslo: ")
cislo = int(vstup)

for i in range(cislo+1):
    if i % 2 == 0:
        print(f"{i} - sudé")
    else:
        print(f"{i} - liché")