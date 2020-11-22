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
        
        self.colonnes = list()
        for _ in range(len(self.seqC)):
            ci = list()
            for _ in range(len(self.seqL)):
                ci.append(CASE.VIDE)
            self.colonnes.append(ci)

        self.N = len(self.grille)
        self.M = len(self.grille[0])

        ## opti
        # self.sequenceCs = dict()
        # self.sequenceLs = dict()
        self.sequenceCs = list()
        for ci in range(self.M):
            l = self.seqC[ci].split(" ")
            self.sequenceCs.append([int(i) for i in l if i != ''])
        
        self.sequenceLs = list()
        for li in range(self.N):
            l = self.seqL[li].split(" ")
            self.sequenceLs.append([int(i) for i in l if i != ''])
        
    # On colorie la case a la couleur correspondante
    def colorier(self, li : int, ci : int, couleur : int):
        self.grille[li][ci] = couleur
        self.colonnes[ci][li] = couleur

    def sequenceL(self, li : int) -> list:
        return self.sequenceLs[li]
        # if li in self.sequenceLs:
        #     return self.sequenceLs[li]
        # l = self.seqL[li].split(" ")
        # self.sequenceLs[li] = [int(i) for i in l if i != '']
        # return self.sequenceLs[li]
    
    def sequenceC(self, ci : int) -> list:
        return self.sequenceCs[ci]
        # if ci in self.sequenceCs:
        #     return self.sequenceCs[ci]
        # l = self.seqC[ci].split(" ")
        # self.sequenceCs[ci] = [int(i) for i in l if i != '']
        # return self.sequenceCs[ci]

    def colonne(self, j : int) -> list:
        return self.colonnes[j]
        # cols = list()
        # for ligne in self.grille:
        #     cols.append(ligne[j])
        # return cols
    
    def colorierColonne(self, j : int, l : list) -> list:
        for i in range(len(l)):
            self.colorier(i, j, l[i])
    
    def estToutColorie(self) -> bool:
        for ligne in self.grille:
            if CASE.VIDE in ligne:
                return False
        return True
    
    def affiche_grille(self):
        for i,ligne in enumerate(self.grille):
            print(ligne)

    
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
                if i == CASE.VIDE:
                    rep_l += "  \t"
                elif i == CASE.NOIR: 
                    rep_l += "⬛\t"
                elif i == CASE.BLANC:
                    rep_l += "⬜\t"

            print(rep_l+"\n")
            