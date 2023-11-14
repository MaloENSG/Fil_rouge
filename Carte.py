# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:22:40 2023

@author: UTILISATEUR
"""
import numpy as np

from Case import Case

class Carte(object):
    
    def __init__(self, taille, nb_mine):
        self.taille = taille
        self. nb_mine = nb_mine
        
        case_mine = np.random.choice(taille**2, nb_mine, replace=False)
        
        c = 0
        grille = np.empty([taille, taille], dtype=object)
        # remplissage de la grille
        for i in range (taille):
            for j in range (taille):
                if c in case_mine:
                    grille[i,j]= Case(i,j, contenu = 99)
                else :
                    grille[i,j]= Case(i,j, contenu = 0)
                c += 1
        # Calcul du voisinage
        # Pour chaque case
        for i in range (taille):
            for j in range (taille):
                # Observation des cases voisines
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # Vérification des limites de la grille
                        if 0 <= x < taille and 0 <= y < taille and (x != i or y != j):
                            # Si la case voisine est une mine, le score de la case i, j augmente
                            if grille[i,j].contenu != 99: 
                                if grille[x,y].contenu == 99:
                                    grille[i,j].contenu += 1
                
        self.grille = grille
        print('Creation carte grille')
    
    
    def reveler(self, i, j):
        print('révéler case')
        rev = self.grille[i,j].reveler_case()
        
        if self.grille[i,j].contenu == 0 and rev == True:
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    # Vérification des limites de la grille
                    if 0 <= x < self.taille and 0 <= y < self.taille and (x != i or y != j):
                        self.reveler(x,y)
                        
    
        
    def aff_temps():
        print('temps')
        
        