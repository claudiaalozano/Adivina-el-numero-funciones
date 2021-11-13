# Adivina-el-numero-funciones
https://github.com/claudiaalozano/Adivina-el-numero-funciones.git
``import random
MIN= 0
MAX= 0
intentos= 0
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
def numero_elegido (invitacion):
    invitacion += "entre" + str(MIN) + "y" + str(MAX) + ":"
    numero2= int(invitacion)
    try:
        numero2= int(numero2)
    except:
        pass
    while True:
        numero2= int(input("Por favor seleccione un número: "))
        if MIN<=numero2<=MAX:
            break
    return
print("Comencemos:")
while True:
    oportunidad= numero_elegido("Adivine el número")
    if oportunidad < numero:
        intento= intento + 1
        print("El número es más grande.")
    if oportunidad > numero: 
        intento= intento + 1
        print("El número es más pequeño.")
    else:
        intento= intento + 1
        print("Enhorabuena, ha superado el juego con exito y con " + intento + "intentos")``
