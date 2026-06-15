def crear_matriz():
    matriz = []
    for i in range(3):
        fila = []
        print(f"Vendedor {i+1}:")
    for j in range(3):
        venta = int(input(f" Día {j+1}: $"))
        fila.append(venta)
        matriz.append(fila)
    return matriz

def calcular_totales(matriz):
    totales = []
    for fila in matriz:
        totales.append(sum(fila))
    return totales

def mejor_vendedor(matriz):
    if vendedor: 


print(crear_matriz)
print(calcular_totales)