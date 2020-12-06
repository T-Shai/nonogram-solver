"""
    PROJET ALGORITHMIQUE 2

    author : T-Sai & Ethan

    fonction permettant le calcul 
    du temps d'une fonction
"""
from src.core.nonogram import Nonogram
from timeit import default_timer as timer
"""
    timeit permet de tenir compte du garbage collector
    des differents os
    il fournit aussi un chronometre par defaut qui est 
    l'horloge la plus precise disponible sur l'environnement tester

    LE LANCEMENT DE CES FONCTIONS DOIENT ETRE FAIT APRES LA SUPRESSION DE __PYCACHE__
"""
class Chronometre:

    def __init__(self, function):
        self.func = function
    
    def time(self, n: Nonogram) -> (float, Nonogram):
        start = timer()
        ok, cn = self.func(n)
        if ok == False:
            raise RuntimeError(f"Chronometre.time : Le nonogram {n.id} est pas coloriable !")
        return (timer() - start), ok, cn