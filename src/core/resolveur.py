"""
    PROJET ALGORITHMIQUE 2

    author : T-Sai & Ethan

    classe resolvant le nonogramme

    dans les solutions implementees ici
    on va utilise une specificite de python
    qui evalue les operations de booleennes
    de facon "paresseuse".

    En effet, dans True or <a>
                   False and <b>

    Les expressions a et b ne seront pas evalué
    On utilisera donc ceci a notre avantage
    en essayant de mettre les appels recursives
    a droite
    Cela explique certains choix dans le code
    qui font defaut dans la clarte mais permettent
    un gain de vitesse
"""

from core.nonogram import Nonogram, CASE

from copy import deepcopy

class Resolveur:
    """
        classe intégrant les différents algorithmes permettant
        la resolution du nonogramme        
    """
    nT_ligne = 0
    ########################################################################################################################
    ##
    ##      1.1 Premiere Etape
    ##
    ########################################################################################################################

    @staticmethod
    def T(j : int, l : int, s: list) -> bool:
        """
            T(j : int, l : int, n : list) -> bool

            retourne vrai si il est possible de colorier les j+1
            premieres cases de la ligne li avec la sous-sequence
            des l premiers blocs de la ligne li
            
            s la liste des blocs de la ligne li
            
            hypothese l >= 0

            On utilise une fonction interne pour
            gerer la recursion et le tableau dynamique
        """
        dyna = dict()
        def loop(j: int, l: int, s: list) -> bool :
        
            if (j,l) in dyna:
                return dyna[j,l]

            # Cas de base :
            if l == 0: # 0 bloc 
                """
                    si l == 0 : il n'y a pas de bloc à prendre
                    en compte, donc les j+1 cases peuvent etre
                    colorie en blanc. On retourne donc vrai.
                """
                dyna[j,l] = True
                return dyna[j,l]
            
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
                    dyna[j,l] = False
                    return dyna[j,l]

                elif j == sl_moins_1:
                    """
                        nombre de case est égal au nombre
                        de case du bloc sl. il est vrai
                        si est seulement si sl est l'unique
                        bloc de la sequence
                    """
                    dyna[j,l] = len(s) == 1
                    return dyna[j,l]
                
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

                    dyna[j,l] = loop(j - s[l-1] -1, l-1, s) or loop(j-1, l, s)
                    return dyna[j,l]
        
        # Appelle à la fonction recursive interne implementant
        # la programmation dynamique
        return loop(j, l, s)
        
    ########################################################################################################################
    ##
    ##      1.2 Generalisation
    ##
    ########################################################################################################################

    @staticmethod
    def T_ligne (s : list, li : list) -> bool :
        """
            T_ligne(s : list, li : list) -> bool

            s  :    sequence de la ligne    : list[int]

            li :    ieme ligne              : list[int] 
            
            Etant donne une sequence (s1, . . . , sk) et une
            ligne li avec certaines cases deja coloriees en
            blanc ou en noir, il indique si une coloration
            de cette ligne est possible.

            Utilise une fonction interne.
        """

        dyna = dict()

        def loop(s : list, li : list) -> bool:
            """
                Fonction interne recursif permettant la
                programmation dynamique.
            """
            """
                En python, les list ne sont pas hashable
                et donc ne peuvent pas etre utilisees
                comme indice.
                On transforme donc la liste en str pour
                pouvoir l'implementer
            """
            # valeur permettant l'indexation
            # de l'etat de la fonction 
            hs = str(s)
            hli = str(li)
            if (hs, hli) in dyna :
                """
                    Si la case existe deja dans le tableau
                    dynamique, on retourne la valeur
                """
                return dyna[hs, hli]
            
            if len(s) == 0: # sequence vide
                """
                    Si il y a une case coloriee en noir
                    alors on ne peut pas colorier toute
                    la ligne en blanc donc

                    Si il y a une case noire dans la ligne
                    on retourne Faux sinon on retourne Vrai
                """
                dyna[hs, hli] = CASE.NOIR not in li
                return dyna[hs, hli]
            
            else :
                j = len(li)-1 # La longueur de la ligne
                sl = s[-1]  # le dernier bloc de la sequence
                k = len(s)
                if j < (sl -1):
                    """
                        nombre de case de la ligne a colorier
                        inferieur a la taille occupe par le 
                        dernier bloc de la sequence
                    """
                    dyna[hs, hli] = False
                    return dyna[hs, hli]
                
                elif j == (sl -1):
                    if k == 1:
                        """
                            Si c'est l'unique bloc on
                            verifie qu'il n' y a pas de
                            case blanche dans la ligne
                        """
                        dyna[hs, hli] = CASE.BLANC not in li
                        return dyna[hs, hli]
                        
                    else :
                        """
                            le dernier bloc n' est pas l'unique
                            bloc de la sequence donc on retourne
                            Faux
                        """
                        dyna[hs, hli] = False
                        return dyna[hs, hli]
                
                # j > sl - 1
                else :
                    """
                        3 cas possibles :

                            1) la case (i,j) est blanche
                            2) la case (i,j) est noire
                            3) la case (i,j) est vide    
                    """
                    if li[-1] == CASE.BLANC:
                        """
                            cas (i,j) blanc : on "enleve"
                            cette case et on cherche dans
                            la suite
                        """
                        dyna[hs, hli] = loop(s, li[:-1])
                        return dyna[hs, hli]
                    
                    elif li[-1] == CASE.NOIR:
                        """
                            cas (i, j) noir : 
                        """
                        """
                            Notons estColoriable
                            les sl derniers cases de la ligne
                            ne continnent pas de case blanc
                            et
                            Notons estUniqBloc
                            sl dernier bloc dans s
                            et
                            Notons estNonNoir
                            les lignes antecedents au sl dernier
                            cases de la ligne ne contienne pas de
                            case noir
                        """
                        estColoriable = CASE.BLANC not in li[j+1-sl:]
                        estUniqBloc = (k == 1)
                        estNonNoir = CASE.NOIR not in li[:j+1-sl]
                        # Si vrai alors on peut placer l'unique bloc
                        # sl à la fin de la ligne et colorier le reste
                        # en blanc
                        cas_1 = estColoriable and estUniqBloc and estNonNoir
                        """
                            Considérons la case precedent
                            les sl derniere cases si elle
                            est pas noir 
                            Alors on verifie les autres
                            sequences de la case
                        """
                        dyna[hs, hli] = cas_1 or (estColoriable and (li[j+1-sl-1] != CASE.NOIR) and loop(s[:-1], li[:j+1-sl-1])) # operation paresseuse
                        return dyna[hs, hli]
                    
                    # case (i,j) est vide
                    else :
                        """
                            La case (i,j) etant vide on peut avoir
                            les deux choix au dessus ainsi
                            on va faire un ou logique entre les 
                            deux
                        """
                        estColoriable = CASE.BLANC not in li[j+1-sl:]
                        estUniqBloc = (k == 1)
                        estNonNoir = CASE.NOIR not in li[:j+1-sl]
                        cas_1 = estColoriable and estUniqBloc and estNonNoir
                        #              |                      case (i,j) noir                               |   |  case (i,j) blanc               
                        dyna[hs, hli] = cas_1 or (estColoriable and (li[j+1 -sl -1] != CASE.NOIR) and loop(s[:-1], li[:j+1-sl-1])) or loop(s, li[:-1])
                        return dyna[hs, hli]
        
        # appelle recursive 
        return loop(s, li)


    
    ########################################################################################################################
    ##
    ##      1.3 Propagation
    ##
    ########################################################################################################################
    @staticmethod
    def ColoreLig(n: Nonogram, i: int) -> (bool, Nonogram):
        """
            Colorie par recurrence un maximum de cases de la ligne i de n
        """
        nouveaux = set()
        def loop(n: Nonogram, i: int, j: int) -> (bool, Nonogram):
            # print(f"T(n, {i}, {j}")
            # cas de base
            if j < 0:
                # print("j > n.M -1")
                return True, n
            """
                Si la case (i,j) est vide
            """
            if n.grille[i][j] == CASE.VIDE:
                # test blanc
                n.colorier(i, j, CASE.BLANC)
                test_blanc = Resolveur.T_ligne(n.sequenceL(i), n.grille[i])

                # test noir
                n.colorier(i, j, CASE.NOIR)
                test_noir = Resolveur.T_ligne(n.sequenceL(i), n.grille[i])

                # print(f"test_noir : {test_noir}")
                # print(f"test_blanc : {test_blanc}")
                if not test_blanc and not test_noir:
                    n.colorier(i, j, CASE.VIDE)
                    # print("not test :")
                    # print(i, j)
                    # n.affiche_grille()

                    return False, n # detection d'impossibilite


                elif test_blanc and not test_noir:
                    n.colorier(i, j, CASE.BLANC)
                    nouveaux.add(j)

                elif not test_blanc and test_noir:
                    n.colorier(i, j, CASE.NOIR)
                    nouveaux.add(j)

                else :
                    n.colorier(i, j, CASE.VIDE)
                
                # print(n.grille)
                return loop(n, i, j-1)
            
            else:
                return loop(n, i, j-1)
        
        ok, cn = loop(n, i, n.M -1)
        # print(cn.grille)
        # print(n.grille)
        return ok, cn, nouveaux

    @staticmethod
    def ColoreCol(n: Nonogram, j: int) -> (bool, Nonogram):
        """
        
            Colorie par recurrence un maximum de cases de la colonne j de n
        """
        nouveaux = set()
        def loop(n: Nonogram, j: int, i: int) -> (bool, Nonogram):
            # print("loop", n.grille)
            # cas de base
            if i < 0:
                # print("i > n.N-1")
                return True, n

            if n.grille[i][j] == CASE.VIDE:
                # test blanc
                n.colorier(i, j, CASE.BLANC)
                test_blanc = Resolveur.T_ligne(n.sequenceC(j), n.colonne(j)) 
                n.colorier(i, j, CASE.NOIR)
                test_noir = Resolveur.T_ligne(n.sequenceC(j), n.colonne(j))
                
                if not test_blanc and not test_noir:
                    n.colorier(i, j, CASE.VIDE)
                    # print("ColoreCol : not test :")
                    # print(i, j)
                    # print(n.sequenceC(j), n.colonne(j))
                    # n.affiche_grille()
                    return False, n


                elif test_blanc and not test_noir:
                    n.colorier(i, j, CASE.BLANC)
                    nouveaux.add(i)

                elif not test_blanc and test_noir:
                    n.colorier(i, j, CASE.NOIR)
                    nouveaux.add(i)
                
                else:
                    n.colorier(i, j, CASE.VIDE)
                
                return loop(n, j, i-1)
            
            else:
                return loop(n, j, i-1)
        
        ok, cn = loop(n, j, n.N-1)
        # print(n.grille)
        # print(cn.grille)
        return ok, cn, nouveaux

    @staticmethod
    def Coloration(n : Nonogram):
        """

            Copie et colorie un nonogramme si il est
            resolvable

        """
        """
            Copie du Nonogram
        """
        cn : Nonogram = deepcopy(n)
        """
            On recupere les lignes
            et les colonnes
        """
        LignesAVoir = set(range(cn.N))
        ColonnesAVoir = set(range(cn.M))

        while LignesAVoir != set() or ColonnesAVoir != set():

            for i in LignesAVoir:
                # print(i, "i1", cn.grille)
                ok, cn, nouveaux = Resolveur.ColoreLig(cn, i)
                # print(i, "i2", cn.grille, "\n")
                if not ok :
                    return False, n
                ColonnesAVoir |= nouveaux
                # En python, on ne peut pas
                # supprimer ou ajouter un element
                # tout en la parcourant donc on
                # vide la liste apres le parcours
            LignesAVoir = set()

            for j in ColonnesAVoir:
                # print(j, "j1", cn.grille)
                ok, cn, nouveaux = Resolveur.ColoreCol(cn, j)
                # print(j, "j2", cn.grille,"\n")
                if not ok :
                    return False, n
                LignesAVoir |= nouveaux
                # En python, on ne peut pas
                # supprimer ou ajouter un element
                # tout en la parcourant donc on
                # vide la liste apres le parcours
            ColonnesAVoir = set()
        
        if cn.estToutColorie():
            return True, cn

        return -1, cn # ne sait pas
    
    @staticmethod
    def ColorierEtPropager(n : Nonogram, li: int, ci: int, couleur: int):
        """

            Copie et colorie un nonogramme si il est
            resolvable

        """
        """
            Copie du Nonogram
        """
        cn : Nonogram = deepcopy(n)
        """
            On recupere les lignes
            et les colonnes
        """
        cn.colorier(li, ci, couleur)
        LignesAVoir = set([li])
        ColonnesAVoir = set([ci])

        while LignesAVoir != set() or ColonnesAVoir != set():

            for i in LignesAVoir:
                # print(i, "i1", cn.grille)
                ok, cn, nouveaux = Resolveur.ColoreLig(cn, i)
                # print(i, "i2", cn.grille, "\n")
                if not ok :
                    return False, n
                ColonnesAVoir |= nouveaux
                # En python, on ne peut pas
                # supprimer ou ajouter un element
                # tout en la parcourant donc on
                # vide la liste apres le parcours
            LignesAVoir = set()

            for j in ColonnesAVoir:
                # print(j, "j1", cn.grille)
                ok, cn, nouveaux = Resolveur.ColoreCol(cn, j)
                # print(j, "j2", cn.grille,"\n")
                if not ok :
                    return False, n
                LignesAVoir |= nouveaux
                # En python, on ne peut pas
                # supprimer ou ajouter un element
                # tout en la parcourant donc on
                # vide la liste apres le parcours
            ColonnesAVoir = set()
        
        if cn.estToutColorie():
            return True, cn

        return -1, cn # ne sait pas


    @staticmethod
    def Enum_rec(n: Nonogram, k: int, couleur: int):
        if k == n.M*n.N:
            return True
        i = int(k/n.M)
        j = k % n.M

        ok, cn = Resolveur.ColorierEtPropager(n, i, j, couleur)
        
        if ok != -1:
            if not ok:
                return False, n
            else:
                return True, cn
        
        k_p = n.M*n.N
        for indx in range(k+1, n.M*n.N+1):
            i = int(indx/n.M)
            j = indx % n.M
            if cn.grille[i][j] == CASE.VIDE:
                k_p = indx
                break
        
        return Resolveur.Enum_rec(cn, k_p, CASE.BLANC) or Resolveur.Enum_rec(cn, k_p, CASE.NOIR)

    @staticmethod
    def Enumeration(n : Nonogram):
        cn = deepcopy(n)
        ok, cn = Resolveur.Coloration(cn)
        if not ok:
            return False, n
        return Resolveur.Enum_rec(cn, 0, CASE.BLANC) or Resolveur.Enum_rec(cn, 0, CASE.NOIR)
    