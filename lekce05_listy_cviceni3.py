#3 likst 5ti, vytvorit aritmeticky prumer
seznam = [2, 3, 5, 8, 9]
soucet = 0
for i in range(len(seznam)):
    soucet = soucet + seznam[i]
    prumer = soucet/len(seznam)

print(prumer)

for i in range(5):
    print(i)