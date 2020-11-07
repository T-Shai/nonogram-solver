"""
    PROJET ALGORITHMIQUE 2

    author : T-Sai & Ethanlebg3

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
    fileName = str(n)+".txt" # n° Instance.txt
    l = list()
    # ouverture du fichier et recuperation des sequences
    try:
        with open(instancePath + fileName, "r") as f:
            l = f.read().split("#") # lignes et colonnes separé par #

    # attrape l'erreur si le fichier est introuvable
    except FileNotFoundError :
        print(f"\nLe fichier {instancePath + fileName} est introuvable :(\nIl a donc été ignoré ! Verifiez que le fichier d'instance est bien dans {instancePath}\n")
    
    m = tuple([seq.split("\n") for seq in l]) # liste de liste (on separe les lignes et les colonnes)
    if m == tuple(): #liste vide 
        return None
    l, c = m # Ligne , colone 
    return Nonogram(n, l[:len(l)-1],c[1:len(c)-1]) # n° instance , lignes , colonnes 
    