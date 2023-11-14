# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 12:22:45 2023

@author: UTILISATEUR
"""

import numpy as np

class Niveau(object):
    
    def __init__(self, niveau):
        
        self.niveau = niveau
        
        if niveau in ['f','m','d']:
            if niveau == 'f':
                taille = 5
                mines = 3
            if niveau == 'm':
                taille = 10
                mines = 10
            if niveau == 'd':
                taille = 14
                mines = 14
        parametre = 