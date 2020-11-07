"""
    PROJET ALGORITHMIQUE 2

    author : T-Sai & Ethanlebg3

    Execution des instances 

"""

from core.util.parser import loadInstance
from core.nonogram import CASE
from core.resolveur import Resolveur

def test_chargement_coriage_affichage():
    """
        test :

        parser : loadInstance

        Nonogram : colorier, show_terminal
    """
    n = loadInstance(0)

    n.colorier(0, 0, CASE.NOIR)
    n.colorier(0, 1, CASE.NOIR)
    n.colorier(0, 2, CASE.NOIR)
    n.colorier(0, 3, CASE.BLANC)
    n.colorier(0, 4, CASE.BLANC)
    

    n.colorier(1, 0, CASE.BLANC)
    n.colorier(1, 1, CASE.BLANC)
    n.colorier(1, 2, CASE.BLANC)
    n.colorier(1, 3, CASE.BLANC)
    n.colorier(1, 4, CASE.BLANC)

    n.colorier(2, 0, CASE.NOIR)
    n.colorier(2, 1, CASE.BLANC)
    n.colorier(2, 2, CASE.NOIR)
    n.colorier(2, 3, CASE.BLANC)
    n.colorier(2, 4, CASE.NOIR)

    n.colorier(3, 0, CASE.BLANC)
    n.colorier(3, 1, CASE.BLANC)
    n.colorier(3, 2, CASE.NOIR)
    n.colorier(3, 3, CASE.NOIR)
    n.colorier(3, 4, CASE.NOIR)

    n.show_terminal()

def test_T():

    # cas l == 0
    s = []
    l = 0
    j = 21
    assert Resolveur.T(j, l, s) == True

    # cas j < sl-1
    s = [1, 1, 6]
    l = 3
    j = 4
    assert Resolveur.T(j, l, s) == False

    # cas j == sl et sl unique
    s = [4]
    l = 1
    j = 4
    assert Resolveur.T(j, l, s) == True

    # cas j == sl et sl non unique
    s = [20, 4]
    l = 2
    j = 4
    assert Resolveur.T(j, l, s) == False

    # j > sl-1 cas case (i,j) blanche impossible
    s = [20, 4]
    l = 2
    j = 25
    assert Resolveur.T(j, l, s) == True

    # j > sl-1 cas case (i,j) blanche et noir possible
    s = [20, 4]
    l = 2
    j = 26
    assert Resolveur.T(j, l, s) == True

    # j > sl-1 cas bloc antecedent trop grand
    s = [40, 4]
    l = 2
    j = 26
    assert Resolveur.T(j, l, s) == False

    # On test les 16 instances
    for i in range(17):
        print(f"######## instance {i} ########") # instance n°
        n = loadInstance(i) 
        for seqs in n.seqL: 
            s = seqs.split(" ") # on obtiens des strings
            s = [int(n) for n in s if n != ""] # on les convertis en int 
            l = len(s)  
            j = len(n.seqC) 

            print(f"Testing T({j}, {l}, {s}) ...")
            assert Resolveur.T(j, l, s) == True 
            print("Test passed successfully !")
            


if __name__ == "__main__":
    test_T()  