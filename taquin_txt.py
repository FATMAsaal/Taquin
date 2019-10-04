#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: module

:author: FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_

:date: 2015, december

"""

from taquin import *


def lire_coup_a_jouer ():
    """
    lecture d'un coup

    :CU: Aucune.
    """
    liste=[cle for cle in COMMANDES]
    coup = input ('Votre coup ? ((H)aut, (B)as, (G)auche, (D)roit) ')
    coup=coup.upper()
    compteur = 1
    if coup in liste:
        print ('Nombre de coups joués :', compteur)
        return coup
        compteur+=1
    elif coup=='ABANDONNER':
        print('Vous avez abandonné !')
        sys.exit(1)
    else:
        while coup not in liste:
            coup = input ('Votre coup ? ((H)aut, (B)as, (G)auche, (D)roit) ')
            coup=coup.upper()
        return coup
   
def jouer (n):
    """
    procédure principale permettant de jouer au jeu du taquin.
    L'entier n détermine la taille nxn du taquin.
    
    :CU: pour des raisons de simplicité on impose à n d'être compris entre
         2 et 9 (bornes comprises)
    """
    taq = cree_taquin (n)
    melanger_taquin (taq)
    imprimer_taquin (taq)
    while not est_resolu (taq):
        coup = lire_coup_a_jouer ()
        COMMANDES[coup] (taq)
        imprimer_taquin (taq)
    print ('Taquin résolu.')
    
def usage ():
    print ('Usage : {:s} <n>'.format (sys.argv[0]))
    print ('\t<n> = taille du jeu (2 <= n <= 9)')
    exit (1)

if __name__ == '__main__':
    import sys

    # if len (sys.argv) == 1:
    #     n = 4
    # else:
    #     try:
    #         n = int (sys.argv[1])
    #     except (IndexError, ValueError):
    #         usage ()
    
    # jouer (n)
    # exit (0)

