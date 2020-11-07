"""
    PROJET ALGORITHMIQUE 2

    author : T-Sai

    classe representant un nonogram 
"""
class CASE :
    """
        Different etat que peut prendre une Case

        VIDE    : -1
        BLANC   :  0
        NOIR    :  1
    """
    VIDE = -1
    BLANC = 0
    NOIR = 1


class Nonogram:
    """
        Classe representant un nonogramme
        
        le nonogramme est represente par
        
        id : int : le numero de l'instance

        seqL\seqC : list : representant
        respectivement la sequence des
        lignes et la sequence des 
        colonnes

        grille : list : matrice representant
        les differents cases du nonogramme
    """    
    def __init__(self,iden, l, c):
        self.id = iden
        self.seqL = l
        self.seqC = c
        self.grille = list()

        # initialisation de la grille à vide
        for _ in range(len(self.seqL)):
            li = list()
            for _ in range(len(self.seqC)):
                li.append(CASE.VIDE)
            self.grille.append(li)
    
    def colorier(self, li : int, ci : int, couleur : int):
        self.grille[li][ci]= couleur

    def show_terminal(self):
        print(f"Grille no {self.id} :\n")

        cpt = 0
        for ligne in self.grille:

            rep_l = "\t"
            if cpt == 0:
                for seq in self.seqC:
                    rep_l+= seq.replace(" ", "|")+"\t"
            
            rep_l += "\n"
            rep_l += self.seqL[cpt]+"\t"
            cpt += 1
            for i in ligne:
                if i == -1:
                    rep_l += "  \t"
                elif i == 1:
                    rep_l += "⬛\t"
                elif i == 0:
                    rep_l += "⬜\t"

            print(rep_l+"\n")
        