#5 list 5ti, vypsat 2 nejvyzsi

seznam = [2, 9, 3, 5, 8, 7, 5, 11, 14, 6 ]

for i in seznam:
    if i < 99999999999999999999:
        nizko = i

nejvyssi1 = nizko
nejvyssi2 = nizko

for i in seznam:
    if i > nejvyssi1:
        nejvyssi1 = i

for i in seznam:
    if i > nejvyssi2 and i != nejvyssi1:
        nejvyssi2 = i

print(nejvyssi1)
print(nejvyssi2)