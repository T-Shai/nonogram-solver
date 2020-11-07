"""
    PROJET ALGORITHMIQUE 2

    author : T-Sai

    Créer un/des nonogramme(s) à partir d'une ou plusieurs instances
"""
from core.nonogram import Nonogram

def loadInstance(n : int):
    """
        loadInstance(int) -> nonogram

        Prends en entrée le numero d'instance du fichier texte
        et retourne un nonogram si il existe sinon il genere
        une exception
    """
    # Chemin vers le fichier d'instance standard
    instancePath = "./instances/"
    fileName = str(n)+".txt"
    l = list()
    # ouverture du fichier est recuperation des sequences
    try:
        with open(instancePath + fileName, "r") as f:
            l = f.read().split("#")
    # attrape l'erreur si le fichier est introuvable
    except FileNotFoundError :
        print(f"\nLe fichier {instancePath + fileName} est introuvable :(\nIl a donc été ignoré ! Verifiez que le fichier d'instance est bien dans {instancePath}\n")
    
    m = tuple([seq.split("\n") for seq in l])
    if m == tuple():
        return None
    l, c = m
    return Nonogram(n, l[:len(l)-1],c[1:len(c)-1])
    