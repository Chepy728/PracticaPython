import random

while True:
    aleatorio = random.randrange(0,3)
    elijepc = ""
    print ("Piedra")
    print ("Papel")
    print ("Tijera")
    opcion = int(input("Elegi una opcion"))

    if opcion == 1:
        elijeusuario = "Piedra"
    elif opcion == 2:
        elijeusuario = "Papel"
    elif opcion == 3:
        elijeusuario = "Tijera"
    print("Elegiste: ", elijeusuario)   

    if aleatorio == 0:
        elijepc = "Piedra"
    if aleatorio == 1:
        elijepc = "Papel"
    if aleatorio == 2:
        elijepc = "Tijera" 
    print ("La PC eligio: ", elijepc)

    if elijepc == "Piedra" and elijeusuario == "Papel":
        print("Ganaste maraca, el papel vence a la piedra")
    elif elijepc == "Papel" and elijeusuario == "Tijera":
        print("Ganaste maraca, la tijera vence a la piedra")
    elif elijepc == "Tijera" and elijeusuario == "Piedra":
        print("Ganaste maraca, la piedra vence a la tijera")
    if elijepc == "Papel" and elijeusuario == "piedra":
        print("Perdiste maraca, el papel vence a la piedra")
    elif elijepc == "Tijera" and elijeusuario == "Papel":
        print("Perdiste maraca, la tijera vence a la piedra")
    elif elijepc == "Piedra" and elijeusuario == "Tijera":
        print("Perdiste maraca, la piedra vence a la tijera")
    elif elijepc == elijeusuario:
        print("Empate zoquete")

    