#Auteur:Fatma Saal
#Objet: Projet taquin

from random import shuffle

def cree_taquin(n):
    """
    fonction permettant de créer les valeurs dans le tableau du taquin, ici on aura une liste de n listes de longueur n.
    CU: n doit être un entier compris entre 2 et 9 inclus.
    Exemple:
    >>> cree_taquin(2)
    [[1, 2], [3, 4]]
    """
    return [[k*n+(l+1)for l in range(n)]for k in range(n)]

def imprimer_taquin(taq):
    """
    fonction permettant d'imprimer le taquin.
    CU:n compris entre 2 et 9
    Exemple:
    >>> taq=cree_taquin(4)
    >>> imprimer_taquin(taq)
     ___ ___ ___ ____
    |  1|  2|  3|  4|
    |___|___|___|___|
    |  5|  6|  7|  8|
    |___|___|___|___|
    |  9| 10| 11| 12|
    |___|___|___|___|
    | 13| 14| 15| 16|
    |___|___|___|___|
    """
    n=len(taq)
    for decor in range(n):
        print(' ___',end="")
    print('_')

    for lignes in taq:
        for cases in lignes:
            if cases-10<0:
                print("| ",cases,end="")
            else:
                print("|",cases,end="")
        print("|")
        for decor in range(n):
            print('|___',end="")
        print('|',end='')

        print()

def haut(taq):
    """
    fonction qui deplace la case vide vers le haut.
    Exemple:
    >>> taq=cree_taquin(4)
    >>> haut(taq)
    >>> imprimer_taquin(taq)
     ___ ___ ___ ____
    |  1|  2|  3|  4|
    |___|___|___|___|
    |  5|  6|  7|  8|
    |___|___|___|___|
    |  9| 10| 11| 16|
    |___|___|___|___|
    | 13| 14| 15| 12|
    |___|___|___|___|
    """
    n=len(taq)
    case_vide=position_case_vide(taq)
    vide=case_vide
    if vide[1]>0:
        aux=taq[vide[1]-1][vide[0]]
        taq[vide[1]-1][vide[0]]=n**2
        taq[vide[1]][vide[0]]=aux
    else:
        None

def gauche(taq):
    """
    fonction qui deplace la case vide vers la gauche.
    Exemple:
    >>> taq=cree_taquin(4)
    >>> gauche(taq)
    >>> imprimer_taquin(taq)
     ___ ___ ___ ____
    |  1|  2|  3|  4|
    |___|___|___|___|
    |  5|  6|  7|  8|
    |___|___|___|___|
    |  9| 10| 11| 12|
    |___|___|___|___|
    | 13| 14| 16| 15|
    |___|___|___|___|
    """
    n=len(taq)
    case_vide=position_case_vide(taq)
    vide=case_vide
    if vide[0]>0:
        aux=taq[vide[1]][vide[0]-1]
        taq[vide[1]][vide[0]-1]=n**2
        taq[vide[1]][vide[0]]=aux
    else:
        None

def droite(taq):
    """
    fonction qui deplace la case vide vers la droite.
    Exemple:
    >>> taq=cree_taquin(4)
    >>> gauche(taq)
    >>> imprimer_taquin(taq)
     ___ ___ ___ ____
    |  1|  2|  3|  4|
    |___|___|___|___|
    |  5|  6|  7|  8|
    |___|___|___|___|
    |  9| 10| 11| 12|
    |___|___|___|___|
    | 13| 14| 16| 15|
    |___|___|___|___|
    >>> droite(taq)
    >>> imprimer_taquin(taq)
     ___ ___ ___ ____
    |  1|  2|  3|  4|
    |___|___|___|___|
    |  5|  6|  7|  8|
    |___|___|___|___|
    |  9| 10| 11| 12|
    |___|___|___|___|
    | 13| 14| 15| 16|
    |___|___|___|___|
    """
    n=len(taq)
    case_vide=position_case_vide(taq)
    vide=case_vide
    if vide[0]<n-1:
        aux=taq[vide[1]][vide[0]+1]
        taq[vide[1]][vide[0]+1]=n**2
        taq[vide[1]][vide[0]]=aux
    else:
        None

def bas(taq):
    """
    fonction qui deplace la case vide vers le bas.
    Exemple:
    >>> taq=cree_taquin(4)
    >>> haut(taq)
    >>> imprimer_taquin(taq)
     ___ ___ ___ ____
    |  1|  2|  3|  4|
    |___|___|___|___|
    |  5|  6|  7|  8|
    |___|___|___|___|
    |  9| 10| 11| 16|
    |___|___|___|___|
    | 13| 14| 15| 12|
    |___|___|___|___|
    >>> bas(taq)
    >>> imprimer_taquin(taq)
     ___ ___ ___ ____
    |  1|  2|  3|  4|
    |___|___|___|___|
    |  5|  6|  7|  8|
    |___|___|___|___|
    |  9| 10| 11| 12|
    |___|___|___|___|
    | 13| 14| 15| 16|
    |___|___|___|___|
    """
    n=len(taq)
    case_vide=position_case_vide(taq)
    vide=case_vide
    if vide[1]<n-1:
        aux=taq[vide[1]+1][vide[0]]
        taq[vide[1]+1][vide[0]]=n**2
        taq[vide[1]][vide[0]]=aux
    else:
        None

COMMANDES={'G':gauche,'D':droite,'H':haut,'B':bas}

def position_case_vide(taq):
    """
    fonction qui renvoie la position de la case vide, ici la case 16, sous forme d'un couple, d'aborde le numero de colonne puis celui de ligne.
    CU: aucune
    Exemple:
    >>> position_case_vide(cree_taquin(4))
    (3, 3)
    """
    n=len(taq)
    for i in range (0,len(taq),1):
        if n*n in taq [i]:
            ligne=i
    for e in range(0,len(taq),1):
        if taq[ligne][e]==n*n:
            colonne=e
    return (colonne,ligne)


def numero_piece(taq,x,y):
    """
    fonction qui renvoie le numero de la pièce dans le taquin, situé à la colonne x et à la ligne y.
    CU:x et y <= n, la dimension du taquin
    Exemple:
    >>> numero_piece(cree_taquin(4),0,2)
    9
    """
    return taq[y][x]

def echanger(taq,c1,c2):
    """
    fonction qui a pour effet de bord d'échanger les pièces aux coordonnées c1 et c2.
    CU:c1 et c2 sont des cases de coordonnées <=n.
    Exemple:
    >>> taq=cree_taquin(4)
    >>> echanger(taq,(2,3),(1,1))
    >>> imprimer_taquin(taq)
     ___ ___ ___ ____
    |  1|  2|  3|  4|
    |___|___|___|___|
    |  5| 15|  7|  8|
    |___|___|___|___|
    |  9| 10| 11| 12|
    |___|___|___|___|
    | 13| 14|  6| 16|
    |___|___|___|___|
    """
    piece1=numero_piece(taq,c1[0],c1[1])
    piece2=numero_piece(taq,c2[0],c2[1])
    aux=piece1
    taq[c1[1]][c1[0]]=piece2
    taq[c2[1]][c2[0]]=aux


def melanger_taquin(taq):
    """
    fonction permettant de mélanger les nombres des listes de manière à ce que le taquin puisse être résoluble.
    CU: la taquin doit être résoluble.
    >>> taq=cree_taquin(4)
    >>> taq2=cree_taquin(4)
    >>> melanger_taquin(taq2)
    >>> taq==taq2
    False
    """
    commande=[]
    for i in range (1,(len(taq)),1):
        commande=commande+[COMMANDES[k] for k in COMMANDES]
        shuffle(commande)
    indice=0
    while indice<=len(commande)-1:
        commande[indice](taq)
        indice+=1

def est_resolu(taq):
    """
    prédicat qui permet de savoir quand le taquin est résolu.
    CU:aucune
    Exemple:
     ___ ___ ___ ____
    |  1|  2|  3|  4|
    |___|___|___|___|
    |  5|  6|  7|  8|
    |___|___|___|___|
    |  9| 10| 11| 12|
    |___|___|___|___|
    | 13| 14| 16| 15|
    |___|___|___|___|
    Votre coup ? ((H)aut, (B)as, (G)auche, (D)roit) d
     ___ ___ ___ ____
    |  1|  2|  3|  4|
    |___|___|___|___|
    |  5|  6|  7|  8|
    |___|___|___|___|
    |  9| 10| 11| 12|
    |___|___|___|___|
    | 13| 14| 15| 16|
    |___|___|___|___|
    Taquin résolu.
    """
    n=len(taq)
    return taq==cree_taquin(n)







if __name__ == "__main__":
    import doctest
    doctest.testmod()
