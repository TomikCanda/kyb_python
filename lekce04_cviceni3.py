vstup = input("Zadej číslo: ")
cislo = int(vstup)

if cislo % 2 == 0:
    for i in range(0, cislo + 2, 2):
        print(i)
else:
    for i in range(0, cislo + 1, 2):
        print(i)

print(40*"=")

for i in range(cislo + 1):
    if i % 2 == 0:
        print(i)