#4 list 5ti, vypsat nejvyssi cislo ze seznamu
seznam = [2, 3, 5, 9, 8]
nejvyssi = 0
for i in seznam:
    if i > nejvyssi:
        nejvyssi = i

print(nejvyssi)

print(max(seznam))