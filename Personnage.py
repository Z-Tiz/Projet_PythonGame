# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:39:21 2020

@author: dbz_z
"""

import random


class Personnage(object):

    """
    Classe Personnage créée un personnage et lui attribue un niveau, le personnage commence au niveau 1 puis peut gagner
    des niveaux
    Lui attribue 150 points de vie au départ, ses points de vies augmentent avec le niveau
    de même pour ses dégâts d'attaque et de défense
    """
    
    def __init__(self):
        self._niveau = 1  # niveau de départ = 1, le niveau du personnage est un entier
        self._name = "Jean Neymar par défaut"
        self._pdv = 150  # Points de vies de départ = 150
        
    @property
    def niveau(self):
        print("niveau actuel: {}".format(self._niveau))
        return self._niveau

    @property    
    def name(self):
        if self._name == "Jean Neymar par défaut":
            raise ValueError("Vous devez choisir le nom de votre personnage")
        else:
            return self._name

    @property
    def pdv(self):
        print("vous avez {} points de vie".format(self._pdv))
        return self._pdv

    @niveau.setter
    def niveau(self, gainniv):
        if gainniv <= self._niveau:
            raise ValueError("Le niveau ne peut pas être inférieur au niveau actuel")
        print("Bravo ! Vous avez level up au niveau {}".format(gainniv))
        self._pdv += 10*(gainniv-self._niveau)
        self._niveau = gainniv
        
    @name.setter
    def name(self, nom):
        self._name = nom
    
    def attaque(self):
        jet = int(random.gauss(5, 2))
        jetfinal = int(10*(self._pdv/150)-((10-jet)/2)*(self._pdv/150))
        if jet == 0:
            print('Échec critique !')
            return jet
        elif jet == 10:
            print('Coup critique !')
            return jetfinal*2
        else:
            return jetfinal
            
    def defense(self):
        if self._niveau < 20:  # Pas de bouclier avant le niveau 20
            raise ValueError("Défense impossible pour le moment")
        jetdef = self._niveau//10
        return jetdef


class Monstre(object):

    def __init__(self):
        self._niveau = 1
        self._pdv = 50

    @property
    def niveau(self):
        print("Monstre de niveau {}".format(self._niveau))
        return self._niveau

    @property
    def pdv(self):
        print("Ce monstre a {} points de vie".format(self._pdv))
        return self._pdv

    #@niveau.setter