# víme dopředu, kolikrát chceme opakovat
# range(x) -> <0;x), pouze integery
# range(a,b) -> <a;b), pouze integery
# range(a,b,s) -> <a;b), pouze integery - krok s
for i in range(2, 15, 2):
    print(i)

print(40*"=")

for i in range(10, 2, -1):
    print(i)

print(40*"=")

for i in range(5):
    print("Ahoj")
# do argumentu 5 => 5krát ahoj