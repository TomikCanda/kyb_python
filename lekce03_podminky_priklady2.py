vstup = input("Číslo, u kterého chcete ověřit sudost nebo lichost: ")
cislo = int(vstup)

zbytek = cislo % 2
if zbytek == 1:
    print(f"Číslo {cislo} je liché")
else:
    print(f"Číslo {cislo} je sudé")