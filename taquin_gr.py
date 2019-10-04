#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: module

:author: FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_
:completed by:

:date: 2015, december

Interface graphique pour jouer eu taquin
"""

from tkinter import *
import tkinter.filedialog as tkfdial

from taquin import *

# nbre de lignes et de pièces par lignes du taquin
DIM_TAQUIN = 4
# dimension en pixels de la taille de l'image du taquin
TAILLE_TAQUIN = 600
# taille d'une pièce carrée du taquin (en pixels)
TAILLE_PIECE = TAILLE_TAQUIN // DIM_TAQUIN
GEOMETRIE = '{:d}x{:d}'.format (30 + 2 * DIM_TAQUIN * TAILLE_PIECE,
                                52 + DIM_TAQUIN * TAILLE_PIECE)

image = None
image_decoupee = [None for k in range(DIM_TAQUIN * DIM_TAQUIN)]
taquin = None
fenetre = None
case_vide = None
puzzle = None
modele = None



def cases_voisines (c1, c2):
    """
    renvoie 
    - True si les cases c1 et c2 sont voisines
    - False sinon

    : CU: aucune

    :Exemples:
    >>> cases_voisines ((1,2), (1,3))
    True
    >>> cases_voisines ((1,2), (1,1))
    True
    >>> cases_voisines ((1,2), (0,2))
    True
    >>> cases_voisines ((1,2), (2,2))
    True
    >>> cases_voisines ((1,2), (2,1))
    False
    """
    numero1=c1[0]
    numero2=c1[1]
    numero3=c2[0]
    numero4=c2[1]
    if numero2+1==numero4 and numero1==numero3:
        return True
    elif numero2-1==numero4 and numero1==numero3:
        return True
    elif numero1-1==numero3 and numero2==numero4:
        return True
    elif numero1+1==numero3 and numero2==numero4:
        return True
    else:
        return False
        

def afficher_pieces ():
    """
    affiche les pièces du puzzle.
    """
    for l in range (DIM_TAQUIN):
        for c in range (DIM_TAQUIN):
            num_piece = numero_piece (taquin, c, l)
            if num_piece!=DIM_TAQUIN*DIM_TAQUIN:
                piece = image_decoupee [num_piece-1]
                puzzle.create_image (c * (TAILLE_PIECE + 1),
                                     l * (TAILLE_PIECE + 1),
                                     anchor = NW,
                                     image = piece)
            else:
                puzzle.create_image (c * (TAILLE_PIECE + 1),
                                     l * (TAILLE_PIECE + 1),
                                     anchor = NW,
                                     image = case_vide)
    
            


def melanger ():
    """
    mélange les pièces du taquin
    """
    if image != None:
       melanger_taquin(taquin)
       image_decoupee
       afficher_pieces()
           

def sous_image (src,xA,yA,xB,yB):
    """
    renvoie un morceau rectangulaire de l'image ``src``
    depuis le point supérieur gauche de coordonnées (xA,yA)
    au point inférieur droit de coordonnées (xB,yB).
    """
    pce = PhotoImage ()
    pce.tk.call (pce, 'copy', src,
                 '-from', xA, yA, xB, yB, '-to', 0, 0)
    return pce

def choix_image ():
    """
    permet de choisir via une boîte de dialogues un fichier contenant une image.

    Ce fichier doit être au format PNG ou GIF, et l'image qu'il contient doit 
    être au moins de taille 600x600.

    L'image choisie est découpée en morceaux.
    Les morceaux sont affichée à gauche, et l'image originale à droite.
    """
    global image, taquin
    taquin = cree_taquin (DIM_TAQUIN)
    imagename = tkfdial.askopenfilename (title = 'Choisir une image',
                                         filetypes = [('PNG','.png'),('GIF','.gif')])
    image = PhotoImage (file = imagename)
    for k in range (len(image_decoupee)):
        l = k // DIM_TAQUIN
        c = k % DIM_TAQUIN
        image_decoupee[k] = sous_image (image, c * TAILLE_PIECE, l * TAILLE_PIECE,
                                        (c+1) * TAILLE_PIECE, (l+1) * TAILLE_PIECE)
    afficher_pieces ()
    modele.create_image (0,0,anchor = NW, image = image)


def bouger_piece (event):
    """
    bouge la pièce désignée par le clic de souris (event),
    uniquement si cette pièce est voisine de la case vide.
    """
    c = event.x // (TAILLE_PIECE + 1)
    l = event.y // (TAILLE_PIECE + 1)
    if cases_voisines((c,l),position_case_vide(taquin)):
        echanger(taquin,position_case_vide(taquin),(c,l))
    afficher_pieces ()

def abandonner():
    """
    Fonction qui permet à l'utilisateur d'abandonner le jeu.
    CU:aucune
    """
    input("Vous avez abandonné !")
    
 

def main ():
    global fenetre, case_vide, puzzle, modele

    
    # La fenêtre principale
    fenetre = Tk ()
    fenetre.title ('Jeu du taquin')
    fenetre.geometry (GEOMETRIE)
    fenetre.resizable (width=False, height= False)

    # L'image représentant la case vide
    case_vide = sous_image(PhotoImage(file='images/case_vide_bleue.gif'),
                           0, 0,
                           TAILLE_PIECE-1, TAILLE_PIECE-1)

    # La zone gauche contenant le puzzle
    puzzle = Canvas (fenetre, width = TAILLE_PIECE * DIM_TAQUIN + DIM_TAQUIN - 1,
                     height = TAILLE_PIECE * DIM_TAQUIN +  DIM_TAQUIN - 1,
                     background = 'blue')
    puzzle.bind ('<Button-1>',bouger_piece)
    puzzle.grid (row=0, column=0, rowspan = DIM_TAQUIN, columnspan = DIM_TAQUIN,
                 padx = 6, pady = 8)

    # La zone droite contenant l'image modèle à reconstituer
    modele = Canvas (fenetre, width = TAILLE_PIECE * DIM_TAQUIN,
                     height = TAILLE_PIECE * DIM_TAQUIN,
                     background = 'black')
    modele.grid (row=0, column=DIM_TAQUIN, rowspan = DIM_TAQUIN,
                 columnspan = DIM_TAQUIN, padx=6, pady=8)

    # La zone du bas contenant les boutons
    Bouton_choix = Button (fenetre, text ='Choix image',
                           command = choix_image)
    Bouton_choix.grid (row = DIM_TAQUIN, column = 1, padx = 5, sticky = N)

    Bouton_melanger = Button (fenetre, text ='Mélanger',
                              command = melanger)
    Bouton_melanger.grid(row = DIM_TAQUIN, column = 2)

    Bouton_quitter = Button (fenetre, text ='Quitter',
                             command = fenetre.destroy)
    Bouton_quitter.grid(row = DIM_TAQUIN, column = 3)
    Bouton_abandonner= Button (fenetre, text ='Abandonner',
                              command = abandonner)
    Bouton_abandonner.grid(row = DIM_TAQUIN, column = 4)
    
    fenetre.mainloop ()

if __name__ == '__main__':
    import doctest
    doctest.testmod ()


    main ()
