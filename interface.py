# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 21:15:52 2023

@author: UTILISATEUR
"""

import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import *

import numpy as np
from Carte import Carte
from time import time

maCarte = Carte(5, 3)

def appui_bouton(a, b):
    a, b = str(a), str(b)
    print("Appui sur le bouton " + a + b)
    grille_btn(maCarte)
    
def val_case(carte, i, j):
    if carte.grille[i,j].is_rev == False and carte.grille[i,j].is_flag == False:
        return 'X'
    elif carte.grille[i,j].is_rev == True:
        valeur = str(carte.grille[i,j].contenu)
        return valeur
    elif carte.grille[i,j].is_flag == False:
        return 'D'
    

app = QApplication.instance() 
if not app: # sinon on crée une instance de QApplication
    app = QApplication(sys.argv)

# création d'une fenêtre avec QWidget dont on place la référence dans fen
fen = QWidget()

taille = 5

# Création de la grille de boutons
def grille_btn(carte):
    
    layoutH = QHBoxLayout()
    for i in range (taille):
        layoutV = QVBoxLayout()
        for j in range (taille):
            a, b = str(i), str(j)
            valeur = val_case(carte, i, j)
            bouton = QPushButton(a + b + " " + valeur)
            bouton.clicked.connect(lambda _, i=i, j=j: appui_bouton(i, j))
            layoutV.addWidget(bouton)   
        layoutH.addLayout(layoutV)
        
    # Ajout de la grille dans la fenetre
    fen.setLayout(layoutH)

grille_btn(maCarte)


 
# la fenêtre est rendue visible
fen.show()
# exécution de l'application, l'exécution permet de gérer les événements
app.exec_()