"""
Ficher main.py
Ce programme permet de tester si un  nombre est premier ou pas et affiche
pour des nombres allant jusuq'à 100 ce qui sont premiers ou pas.
"""


def isprime(p):
    """
    Cette fonction permettra de vérifier si un nombre est premier ou pas
    en renoyant un boléen : 
    True si le nombre est premier.
    False dans le cas contraire.
    Args:
    p: entier positif.
    Returns:
    boolen: True si premier, false si non.

    Si le nombre est <=1, par définition le nombre n'est pas premier, le cas écheant
    False est donc renvoyé.
    """

    premier = True

    if p<=1:
        premier = False
    for i in range(2,p):
        if p%i==0:
            premier= False
    return premier

#### Fonction principale


def main():
    """
    Ici, on a la fonction principal d'appel à la fonction secondaire.
    On y envoie des paramètres et un boléen indiquant si le nombre est premier
    ou pas sera renvoyé.
    Par ailleurs le programme principal test aussi, pour des nombres de jsuqu'à 100
    lesquels sont premiers et les affiche.
    
    """

    # vos appels à la fonction secondaire ici
    print(isprime(7))
    print(isprime(1))

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
