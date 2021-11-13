import random
MIN= 0
MAX= 0
while True:
    nivel=input("Seleccione un nivel entre fácil, medio, difícil o legendario: ")
    if nivel=="fácil":
        MIN= 0
        MAX= 99
        break
    if nivel=="medio":
        MIN= 0
        MAX= 999
        break
    if nivel=="difícil":
        MIN= 0
        MAX= 9999
        break
    if nivel=="legendario":
        MIN= 0
        MAX= 99999
        break
numero=random.randint(MIN,MAX)

def numero_elegido (invitación):
    while True:
        numero2= int(input("Por favor seleccione un número: "))
        if minimo<=numero2<=maximo:
            minimo=minimo + 1
            maximo=maximo - 1
    while numero != numero2:
        if numero < numero2:
            print("El número introducido es grande, vuelva a intentarlo.")
        if numero > numero2:
            print("El número introducido es pequeño, vuelva a intentarlo.")
        if numero == numero2:
            print("Ha ganado el juego.")