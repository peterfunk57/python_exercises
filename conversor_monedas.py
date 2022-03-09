menu = """
Bienvenido al Conversor de monedas ❤🐱‍💻
Elige una opción porfavor

1 - Pesos Colombianos
2 - Pesos Mexicanos
3 - Pesos Argentinos

Elige una opnción:"""

opcion = int(input(menu))

if opcion == 1:
    pesos = input ("Teclea la cantidad de Pesos Colombianos: ")
    pesos = float(pesos)
    valor_dolar = 3875
    valor_dolar = float(valor_dolar)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")
elif opcion == 2:
    pesos = input ("Teclea la cantidad de Pesos Mexicanos: ")
    pesos = float(pesos)
    valor_dolar = 19.80
    valor_dolar = float(valor_dolar)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")
elif opcion == 3:
    pesos = input ("Teclea la cantidad de Pesos Argentinos: ")
    pesos = float(pesos)
    valor_dolar = 65
    valor_dolar = float(valor_dolar)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")
else:
    print("Elige una opcion valida")
    