import random

"""caracteres = list("abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "~!@#$%^&*()_+")"""
caracteres = list("abcdefghijklmnopqrstuvwxyz")

def random_pass():
    largo = int(input("Ingresa el largo del password: "))
    random.shuffle(caracteres)

    password = []
    for i in range (largo):
        password.append(random.choice(caracteres))
    
    random.shuffle(password)

    print("".join(password))

    random_pass()