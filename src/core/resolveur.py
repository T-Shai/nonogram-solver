"""
    PROJET ALGORITHMIQUE 2

    author : T-Sai & Ethanlebg3

    classe resolvant le nonogramme
"""

from core.nonogram import Nonogram

class Resolveur:
    """
        classe intégrant les différents algorithmes permettant
        la resolution du nonogramme
    """

    #####   Question 5  #####

    @staticmethod
    def T(j : int, l : int, s: list) -> bool:
        print(f"T({j}, {l}, {s}")
        """
            ## T(j : int, l : int, n : list) -> bool

            retourne vrai si il est possible de colorier les j+1
            premieres cases de la ligne li avec la sous-sequence
            des l premiers blocs de la ligne li
            
            s la liste des blocs de la ligne li
            
            #### hypothese l >= 0
        """
        # Cas de base :
        if l == 0: # 0 bloc 
            """
                si l == 0 : il n'y a pas de bloc à prendre
                en compte, donc les j+1 cases peuvent etre
                colorie en blanc. On retourne donc vrai.
            """
            return True
        
        # l >= 1
        else :
            sl_moins_1 = (s[l-1]-1)
            
            if j < sl_moins_1:
                """
                    j + 1 < sl

                    donc le nombre de case à colorier
                    est inférieur au nombre de case 
                    correspondant au bloc donc il est
                    impossible de colorier c'est donc
                    toujours faux
                """
                return False

            elif j == sl_moins_1:
                """
                    nombre de case est égal au nombre
                    de case du bloc sl. il est vrai
                    si est seulement si sl est l'unique
                    bloc de la sequence
                """
                return len(s) == 1
            
            # j > sl -1
            else :
                """
                    Le nombre de case est plus grand que
                    le nombre de bloc à colorier on peut
                    donc toujours le placer maintenant il
                    faut verifier les blocs antecedent

                    on a 2 cas possibles le cas ou la case
                    (i,j) est blanc et le cas ou cet case
                    est noir donc le bloc est place a la 
                    fin des j+1 cases
                """
                # Si (i, j) est blanc on décrémente j de 1
                # si (i, j) est noir on décrémente j du
                # nombre de case de sl et 1 case blanche
                # vu que les deux cas sont possibles
                # on veut le cas ou c'est possible
                return Resolveur.T(j - s[l-1] -1, l-1, s)  or Resolveur.T(j-1, l, s)
    
    @staticmethod
    def T_ligne (s : list, li : list) -> bool :
        """
            T_ligne(s : list, li : list) -> bool

            s  :    sequence de la ligne    : list[str]

            li :    ieme ligne              : list[int] 
            
            Etant donne une sequence (s1, . . . , sk) et une
            ligne li avec certaines cases deja coloriees en
            blanc ou en noir, il indique si une coloration
            de cette ligne est possible.
        """
        pass