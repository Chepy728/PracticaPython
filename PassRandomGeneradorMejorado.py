import random

caractercase = list("abcdefghijklmnopqrstuvwxyz")
caracterupcase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
simbolos1 = list("!@#$%^&*()_+")

def random_pass():

        minusculas = int(input("Ingresa la cantidad de letras en minusculas: "))
        mayusculas = int(input("Ingresa la cantidad de letras en mayusculas: "))
        simbolos = int(input("Ingresa la cantidad de simbolos: "))

        random.shuffle(caractercase)
        random.shuffle(caracterupcase)
        random.shuffle(simbolos1)

        password = []

        for i in range (minusculas):
                password.append(random.choice(caractercase))
        for i in range (mayusculas):
                password.append(random.choice(caracterupcase))
        for i in range (simbolos):
                password.append(random.choice(simbolos1))

        
        random.shuffle(password)
        
        print("".join(password))
        
random_pass()
