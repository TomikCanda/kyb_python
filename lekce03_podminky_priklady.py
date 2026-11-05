vstup = input("Zadejte svůj věk: ")
vek_uzivatele = int(vstup)
if vek_uzivatele < 0:
    print("Neexistujete.")
else:    
    if vek_uzivatele >= 18:
        print(f"Dotyčný je dospělý a je mu {vek_uzivatele} let.")
    else:
        if vek_uzivatele == 1:
            print(f"Dotyčný není dospělý a je mu {vek_uzivatele} rok")
        elif vek_uzivatele <= 4:
            print(f"Dotyčný není dospělý a jsou mu {vek_uzivatele} roky")
        else:
            print(f"Dotyčný není dospělý a je mu {vek_uzivatele} let")

    #print(f"Dotyčný není dospělý a je mu {vek_uzivatele} let")
    zbytek_do_dospelosti = 18 - vek_uzivatele
    if zbytek_do_dospelosti == 1:
        print(f"Do dospělosti mu zbývá {zbytek_do_dospelosti} rok")
    elif zbytek_do_dospelosti <= 4:
        print(f"Do dospělosti mu zbývají {zbytek_do_dospelosti} roky")
    else:
        print(f"Do dospělosti mu zbývá {zbytek_do_dospelosti} let")


# elif se spustí jenom, pokud podmínka nad ním selže
