# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:19:54 2023

@author: UTILISATEUR
"""
import numpy as np

class Case(object):
    
    def __init__(self, y, x, contenu):
        
        self.y = y
        self.x = x
        self.is_rev = False
        self.is_flag = False
        self.contenu = contenu
        
    def reveler_case(self):
        print('case revele')
        if self.is_rev == False and self.is_flag == False:
            self.is_rev = True
            return True
        elif self.is_rev == True:
            #print('Case déjà connue')
            return False
        elif self.is_rev == False and self.is_flag == True:
            #print('Case drapeau !')
            return False
            
    def placer_drapeau(self):
        print('drapeau en place')
        self.is_flag = True
        
        