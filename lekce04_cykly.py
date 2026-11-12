x = 10
# příklad cyklu s podmínkou na začáku - podmínka je argument while
while x >= 5:
    print("Ahoj")
    x = x - 1
    
    if x == 7:
        continue # continue nedokončí zbytek současného loopu a spustí loop od začátku
    
    print(x)
    
    if x == 6:
        break # okamžitě navždycky ukončí loop a kód pokračuje dál


print("Konec")


# příklad podmínky s podmínkou na konci - while True a podmínka je na konci ve formě if ...

while True:
    print("Vyber si: a -> ahoj, q -> exit")
    vstup = input('Zadej volbu: ')
    if vstup == "a":
        print("ahoj")
    elif vstup == "q":
        break
    else:
        print("Neplatné, zkus to znovu!")