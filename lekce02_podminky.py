vek = 17
print("Můj věk je: " + str(vek))
if vek >= 18:
    print("Jsem dospělý")
    print("Už můžu chlastat")
elif vek >= 15:
    print("Jsem mladistvý")
    print("A můžu chlastat jenom pokud vypadám na 18")
else:
    print("Jsem ještě dítě")
    print("Podle zákona ještě nesmím chlastat")
    if vek <= 13:
        print("67 six seveeen")

print("tečka")
print("#"*30)

muj_vek = 20

print("Můj věk je: " + str(muj_vek))

if muj_vek >= 18:
    print("Jsem dospělý, protože je mi " + str(muj_vek))

    if muj_vek >= 65:
        print("Krmím holuby")
    else:
        print("Jsem v produktivním věku")
else:
    print("Jsem ještě dítě")
    if muj_vek <= 13:
        print("67 six seveeen")