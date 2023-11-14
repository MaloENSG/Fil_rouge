# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:29:47 2023

@author: UTILISATEUR
"""

import numpy as np
from Carte import Carte
from time import time

maCarte = Carte(5, 3)
print(maCarte.grille.shape)

def Affichage_console(carte):
    taille = carte.grille.shape[0]
    aff_carte = ''
    for i in range (taille):
        ligne = ''
        for j in range (taille):
            if carte.grille[i,j].is_rev == False and carte.grille[i,j].is_flag == False:
                ligne = ligne + 'X '
            elif carte.grille[i,j].is_rev == True:
                ligne = ligne + str(carte.grille[i,j].contenu) + ' ' 
                
            elif carte.grille[i,j].is_flag == False:
                ligne = ligne + 'D '
        ligne = ligne + '\n'
        aff_carte = aff_carte + ligne
    print(aff_carte)
    
def Affichage_console2(carte):
    taille = carte.grille.shape[0]
    aff_carte = ''
    for i in range (taille):
        ligne = ''
        for j in range (taille):
            if carte.grille[i,j].contenu == 99:
                ligne = ligne + 'M '
            else :
                ligne = ligne + str(carte.grille[i,j].contenu) + ' '
        ligne = ligne + '\n'
        aff_carte = aff_carte + ligne
    print(aff_carte)
    
Affichage_console(maCarte)
    
Affichage_console2(maCarte)


    
def afficher_options():
    print('________________________________')
    print('Placer ou enlever un drapeau : d')
    print('Révéler une case : r')
    print('Quitter le jeu : q')
    
def choix_case() :
    choix_ligne = input("Choisir la ligne : ")
    if not choix_ligne.isdigit():
        print('valeur non valide')
        return False
    else :
        choix_ligne  = int(choix_ligne)
    choix_colonne = input("Choisir la colonne : ")
    if not choix_colonne.isdigit():
        print('valeur non valide')
        return False
    else :
        choix_colonne = int(choix_colonne)
    return choix_ligne, choix_colonne


def lancer(carte):
    jeu = True
    
    while jeu:
        Affichage_console(carte)
        afficher_options()
        choix = input("Entrez l'option : ")
        if choix in ['d', 'r', 'q']:
            
            # Placer ou retirer un drapeau
            if choix == 'd':
                print('Drapeau')
                coord = choix_case()
                if coord == False:
                    print("pas d'action")
                else :
                    l, c = coord[0], coord[1]
                    carte.grille[l,c].placer_drapeau()
                    
            # Révéler une Case
            elif choix == 'r':
                print('Révéler')
                coord = choix_case()
                if coord == False:
                    print("pas d'action")
                else :
                    l, c = coord[0], coord[1]
                    carte.reveler(l,c)
                
            # Quitter la partie
            elif choix == 'q':
                jeu = False
        else :
            print('choix non valide \n')
            
            
                      
lancer(maCarte)            
            
            
            
            
            
            
            
            
        