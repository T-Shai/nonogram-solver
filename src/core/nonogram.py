"""
    PROJET ALGORITHMIQUE 2

    author : T-Sai & Ethan

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
        self.id = iden  #instance
        self.seqL = l   #ligne
        self.seqC = c   #colonne
        self.grille = list() #la matrice representant le nonogram

        # initialisation de la grille à vide, toutes les cases a -1
        for _ in range(len(self.seqL)):
            li = list()
            for _ in range(len(self.seqC)):
                li.append(CASE.VIDE)
            self.grille.append(li)
    
    # On colorie la case a la couleur correspondante
    def colorier(self, li : int, ci : int, couleur : int):
        self.grille[li][ci]= couleur

    # afficher le nonogramme sur le terminal
    def show_terminal(self):
        print(f"Grille no {self.id} :\n") # n de l'instance

        cpt = 0 #compteur ligne 
        for ligne in self.grille:

            rep_l = "\t"    #rep_l = "  "
            if cpt == 0:    #1er cas 
                for seq in self.seqC:   #chaque colonne 
                    rep_l+= seq.replace(" ", "|")+"\t"  #rep_l =    |   |   |
            
            rep_l += "\n"   # rep_l =   |   |   |
            rep_l += self.seqL[cpt]+"\t"    #               rep_l =   |   |   |
                                            # seq de la 1er ligne  :   
                                            # seq de la ieme ligne  : 
            cpt += 1
            for i in ligne:
                if i == -1:
                    rep_l += "  \t"
                elif i == 1: 
                    rep_l += "⬛\t"
                elif i == 0:
                    rep_l += "⬜\t"

            print(rep_l+"\n")
            