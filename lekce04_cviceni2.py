vstup = input("Zadej kladné celé číslo: ")
cislo = int(vstup)

for i in range(cislo, -1, -1):
    print(i)

#oba for loopy dělají to stejné
print(40*"=")

for i in range(cislo+1):
    print(cislo - i)