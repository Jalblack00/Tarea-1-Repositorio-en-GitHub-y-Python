Mayor = 0 

Primervalor = int(input('Cual es su primer valor'))
SegundoValor =  int(input('Cual es su segunda valor'))

if Primervalor < 0:
    Mayor = Primervalor
else:
    Mayor = SegundoValor

print('El valor mayor es:', Mayor)