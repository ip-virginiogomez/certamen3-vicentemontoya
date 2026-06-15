
def leer_velocidades():
    velocidades = []
    for i in range(5):
        velocidad = int(input(f"velocidad { i +1}"))
    return velocidad 

def promedio(velocidades):
    suma = 0
    for velocidad in velocidades:
        suma = suma + velocidad
        promedio = suma / len(velocidad) 
        print(f"el promedio de velocidad es {promedio}")
    return velocidad 

def velocidad_permitida(velocidades):
    for velocidad in velocidades:
        if velocidad > 60 or velocidad < 120:
            print("estas en lo permitido")
        elif velocidad < 20 or velocidad > 140:
            print("PELIGRO estas en exceso de velocida")

print(leer_velocidades())
print(promedio(velocidades))
velocidad_permitida(velocidades)