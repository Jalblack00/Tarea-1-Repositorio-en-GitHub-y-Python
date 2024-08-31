a = float(input('Ingrese el tamaño del primer lado'))
b = float(input('Ingrese el tamaño del segundo lado'))
c = float(input('Ingrese el tamaño del tercer lado'))

if (a==b and b==c and c==a):
    print('Es equilatero')
elif(a==b or b==a or c==a):
    print('Es isoceles')
else:
    print('Es escaleno')
