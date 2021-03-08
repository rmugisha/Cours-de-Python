print("Hello world.")

import random
import math

# import test_import

a = random.randint(1, 1000)

# print(test_import.fibonacci(test_import.ma_variable))

while True:

    entree = input("Entrez un nombre entre 1 et 1000 puis entree, faites 'q' puis entree pour quitter: ")

    if entree == 'q':
        break

    elif not entree.isnumeric():
        print("Vous devez entrer un nombre entier.")
        continue

    elif int(entree) <= 0:
        print("Entrez un nombre plus grand ou egal a 1.")
        continue

    elif int(entree) > 1000:
        print("Entrez un nombre plus petit ou egal a 1000.")
        continue

    elif int(entree) < a:
        print("Plus grand.")
        continue

    elif int(entree) > a:
        print("Plus petit.")
        continue

    elif int(entree) == a:
        print("GAGNE !!!")
        break



