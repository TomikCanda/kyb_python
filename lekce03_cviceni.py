print("Zadejte postupně jednotlivé délky stran trojúhelníku, u kterého potřebujete ověřit zkontruovatelnost")
a = int(input("První strana: "))
b = int(input("Druhá strana: "))
c = int(input("Třetí strana: "))

if (a+b) > c and (a+c) > b and (b+c) > a:
    print(f"Trojúhleník o stranách {a}, {b}, a {c} JE zkonstruovatelný.")
else:
    print(f"Trojúhleník o stranách {a}, {b}, a {c} NENÍ zkonstruovatelný.")

