def leer_datos():
    edad = int(input("¿Cuál es tu edad? "))
    tarjeta = input("¿Tienes tarjeta de socio? (si/no): ")
    monto = int(input("¿Monto de compra? $"))
    return edad, tarjeta, monto


def calcular_descuento(edad, tarjeta, monto):
    califica =  monto > 10000 and (edad > 60 or tarjeta == "si")  
    if califica: 
        descuento = monto * 0.15
        final = monto - descuento  
        print(f"descuento 15% ${descuento}")
        print("total: {final}")
    else:
        print("no califica")
        print(f"total {monto}")






print(leer_datos())
print(calcular_descuento())