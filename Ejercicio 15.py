Monto = float(input('Precio de la compra'))
TasaIsr = float(input('Tasa del impuesto'))

Impuesto = Monto*(TasaIsr/100)

print('El precio total es:\n', Monto+Impuesto)