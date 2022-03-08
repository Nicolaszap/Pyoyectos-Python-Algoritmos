def conversor(tipo_peso, valor_dolar):
    pesos = input("cuantos pesos" + tipo_peso + "tienes ? :")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")


menu = """
Bienvenido al conversor de monedas 💸💸

1- Pesos Colombianos
2- Pesos Argentinos
3- Pesos mexicanos

Elige una opción:"""



opcion = int(input(menu))


if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("Argentino", 65)
elif opcion == 3:
    conversor("Mexicano", 24)
else:
    print("Ingresa una opción valida por favor")

