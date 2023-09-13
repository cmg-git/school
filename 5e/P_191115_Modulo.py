# 16/11/2019 Algorithmique modulo
nombre = int(input('Nombre :'))
diviseur = int(input('diviseur :'))
if nombre % diviseur == 0:
    print(nombre, 'divisible par', diviseur)
else:
    print(nombre, 'pas divisible par', diviseur)
