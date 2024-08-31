n = int(input('Posicion de la sucesion\n'))

Suma1 = 0
Suma2 = 1
print(Suma1)

for i in range(n): 
    Suma3 = Suma1+Suma2
    Suma1=Suma2
    Suma2=Suma3
    print(Suma1)

