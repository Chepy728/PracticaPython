import random

caracteres = list("abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "~!@#$%^&*()_+")


def random_pass():
        largo = int(input("Ingresa el largo del password: "))
        random.shuffle(caracteres)

        password = []
        if largo < 20:
            for i in range (largo):
                password.append(random.choice(caracteres))
        else:
            print("No se puede escribir un numero mayor a 20")
        random.shuffle(password)

        print("".join(password))

random_pass()

