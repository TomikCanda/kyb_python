vstup1 = input("Zadej číslo 1: ")
vstup2 = input("Zadej číslo 2: ")

vysledek_spatne = vstup1 + vstup2

cislo1 = float(vstup1)
cislo2 = float(vstup2)

vysledek = cislo1 + cislo2

print(vysledek)

#tyhle dva printy mají stejný output
print("Součet čísel je " +str(vysledek))
print(f"Součet čísel je {vysledek}")
#fstring je formátovaný string, sám zformátuje cokoliv na string

print("Součet čísel není " + str(vysledek_spatne))
