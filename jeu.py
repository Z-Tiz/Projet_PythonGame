# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:00:39 2020

@author: dbz_z
"""

from Personnage import Personnage
import time


def chargement(t, p):
    for i in range(p):
        time.sleep(t)
        print('*')
    time.sleep(t)


if __name__ == '__main__':
    
    print('Bienvenu !')
    print('*********************************************')
    Nouveauperso = Personnage()
    print('Nouveau personnage créé')
    nom = input('Choissisez un nom de personnage:')
    chargement(1, 3)
    Nouveauperso.name = nom
    
    print('{}, welcome to THE GAME !'.format(Nouveauperso.name))
    niveau = Nouveauperso.niveau
    Pdv = Nouveauperso.pdv
    
    chargement(2, 2)
    
    print('Vous êtes prêt à jouer ?')
    Pret = input('OUI/NON')
    
    if Pret == 'NON':
        print('Au revoir !')
    if Pret == 'OUI':
        print('Lets go!')
    # fin du script pour le moment
